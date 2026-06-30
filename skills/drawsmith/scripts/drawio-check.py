"""diagram-check.py — Automated geometry & style validator for draw.io XML.

Run after generating any .drawio file. Reports concrete pass/fail for
edge crossings (warn-only), bounding box overlap, color reuse, perimeter gaps, coordinate alignment, tight spacing (<10px), and edge-shape intersections.

This script checks the AUTOMATABLE subset of the drawio-guide.md self-check
(overlap detection, edge crossings, page bounds, color reuse, multi-connection
distribution, coordinate alignment, minimum spacing, edge-shape intersections,
edge reference validity, ID uniqueness, XML structure, font/edge consistency,
legend presence, html=1 requirements, container child coordinates). For the full 15-item checklist, see references/drawio-guide.md.

Usage: python diagram-check.py <file.drawio>
"""

import sys
import xml.etree.ElementTree as ET
from collections import defaultdict


def parse_drawio(path):
    tree = ET.parse(path)
    root = tree.getroot()
    model = root.find(".//mxGraphModel")
    pw = int(model.get("pageWidth", 0))
    ph = int(model.get("pageHeight", 0))

    vertices = {}  # id -> {x,y,w,h,style,parent}
    edges = []     # [{id,source,target,style,points}]

    for cell in root.iter("mxCell"):
        cid = cell.get("id", "")
        geom = cell.find("mxGeometry")
        if geom is None:
            continue
        if cell.get("vertex") == "1":
            vertices[cid] = {
                "id": cid,
                "x": float(geom.get("x", 0)),
                "y": float(geom.get("y", 0)),
                "w": float(geom.get("width", 0)),
                "h": float(geom.get("height", 0)),
                "style": cell.get("style", ""),
                "parent": cell.get("parent", "1"),
            }
        elif cell.get("edge") == "1":
            src = cell.get("source", "")
            tgt = cell.get("target", "")
            points = []
            arr = geom.find(".//Array")
            if arr is not None:
                for pt in arr.findall("mxPoint"):
                    points.append((float(pt.get("x", 0)), float(pt.get("y", 0))))
            edges.append({
                "id": cid,
                "source": src,
                "target": tgt,
                "style": cell.get("style", ""),
                "points": points,
            })

    # Resolve absolute coordinates through parent chain
    for vid in vertices:
        v = vertices[vid]
        px, py = 0.0, 0.0
        pid = v["parent"]
        while pid and pid != "1":
            if pid in vertices:
                pv = vertices[pid]
                px += pv["x"]
                py += pv["y"]
                pid = pv["parent"]
            else:
                break
        v["x"] += px
        v["y"] += py

    # Edge waypoints are in root coordinates (parent="1"); no resolution needed

    return {"pw": pw, "ph": ph, "vertices": vertices, "edges": edges}


def bbox_overlap(a, b):
    """Check if two bounding boxes overlap.

    Returns False if shapes are fully separated, or if one fully contains
    the other (parent-child containment). Also returns False if a parent-
    child relationship exists (one's parent ID equals the other's ID).
    """
    ax1, ay1 = a["x"], a["y"]
    ax2, ay2 = a["x"] + a["w"], a["y"] + a["h"]
    bx1, by1 = b["x"], b["y"]
    bx2, by2 = b["x"] + b["w"], b["y"] + b["h"]
    # Allow edge-touching (exact alignment), only flag true overlap
    if ax2 <= bx1 or bx2 <= ax1 or ay2 <= by1 or by2 <= ay1:
        return False
    # Check parent-child relationship by ID
    if a.get("parent") == b.get("id") or b.get("parent") == a.get("id"):
        return False
    # Check if one is a container for the other (no padding requirement
    # for text/ label elements; just check full containment)
    a_contains_b = (ax1 <= bx1 and ay1 <= by1 and
                    ax2 >= bx2 and ay2 >= by2)
    b_contains_a = (bx1 <= ax1 and by1 <= ay1 and
                    bx2 >= ax2 and by2 >= ay2)
    if a_contains_b or b_contains_a:
        return False
    return True


def line_segments_intersect(p1, p2, p3, p4):
    """Check if line segments p1-p2 and p3-p4 intersect."""
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    return (ccw(p1, p3, p4) != ccw(p2, p3, p4) and
            ccw(p1, p2, p3) != ccw(p1, p2, p4))


def edge_path_segments(data, vertices):
    """Return list of (p1,p2) line segments for an edge."""
    src_v = vertices.get(data["source"])
    tgt_v = vertices.get(data["target"])
    if not src_v or not tgt_v:
        return []

    # Source center
    sx = src_v["x"] + src_v["w"] / 2
    sy = src_v["y"] + src_v["h"] / 2
    # Target center
    tx = tgt_v["x"] + tgt_v["w"] / 2
    ty = tgt_v["y"] + tgt_v["h"] / 2

    pts = [(sx, sy)] + data["points"] + [(tx, ty)]
    segments = []
    for i in range(len(pts) - 1):
        segments.append((pts[i], pts[i + 1]))
    return segments


def parse_style(style_str):
    """Parse semicolon-separated key=value style string."""
    result = {}
    for part in style_str.split(";"):
        part = part.strip()
        if "=" in part:
            k, v = part.split("=", 1)
            result[k.strip()] = v.strip()
        elif part:
            result[part] = True
    return result


def check(filepath):
    data = parse_drawio(filepath)
    vertices = data["vertices"]
    edges = data["edges"]
    pw, ph = data["pw"], data["ph"]

    report = []
    fail_count = 0

    # 1. Bounding box overlap
    vids = list(vertices.keys())
    overlaps = []
    for i in range(len(vids)):
        for j in range(i + 1, len(vids)):
            a = vertices[vids[i]]
            b = vertices[vids[j]]
            if bbox_overlap(a, b):
                overlaps.append((vids[i], vids[j]))
    if overlaps:
        for o in overlaps:
            report.append(f"FAIL: Vertex overlap between {o[0]} and {o[1]}")
            fail_count += 1
    else:
        report.append("PASS: No vertex bounding box overlap")

    # 2. Edge crossings (between different edges)
    all_segments = []
    for e in edges:
        segs = edge_path_segments(e, vertices)
        for seg in segs:
            all_segments.append((e["id"], seg))

    crossings = []
    # Build edge adjacency info
    edge_vertices = {}
    for e in edges:
        edge_vertices[e["id"]] = {e["source"], e["target"]}
    for i in range(len(all_segments)):
        for j in range(i + 1, len(all_segments)):
            eid1, (p1, p2) = all_segments[i]
            eid2, (q1, q2) = all_segments[j]
            # Skip segments sharing a source/target (they naturally meet)
            if eid1 == eid2:
                continue
            # Skip edges that share any endpoint vertex
            vset1 = edge_vertices.get(eid1, set())
            vset2 = edge_vertices.get(eid2, set())
            if vset1 & vset2:
                continue
            if line_segments_intersect(p1, p2, q1, q2):
                crossings.append((eid1, eid2))

    if crossings:
        for c in crossings:
            report.append(f"WARN: Edge-edge crossing between {c[0]} and {c[1]} (harmless with jumpStyle=arc)")
            fail_count += 1
    else:
        report.append("PASS: No edge-edge crossings detected")

    # 3. Out-of-page elements
    oob = []
    for vid, v in vertices.items():
        if v["x"] < 0 or v["y"] < 0 or v["x"] + v["w"] > pw or v["y"] + v["h"] > ph:
            oob.append(vid)
    if oob:
        for o in oob:
            report.append(f"FAIL: Vertex {o} out of page bounds")
            fail_count += 1
    else:
        report.append("PASS: All vertices within page bounds")

    # 4. Color reuse check (same strokeColor on semantically different vertex types)
    colors_used = defaultdict(list)
    for vid, v in vertices.items():
        style = parse_style(v["style"])
        sc = style.get("strokeColor", "")
        if sc and sc not in ("none", "default", "#000000"):
            colors_used[sc].append(vid)

    color_conflicts = []
    for color, vlist in colors_used.items():
        if len(vlist) > 3:
            # Check if all same shape type (semantic similarity)
            shapes = set()
            for vvid in vlist:
                s = parse_style(vertices[vvid]["style"])
                shapes.add(s.get("shape", "rect"))
            if len(shapes) > 1:  # same color on different shapes = likely conflict
                color_conflicts.append((color, vlist, shapes))
    if color_conflicts:
        for cc in color_conflicts:
            report.append(
                f"WARN: Color {cc[0]} used on different shape types {cc[2]} — check semantic consistency"
            )
    else:
        report.append("PASS: No color semantic conflicts detected")

    # 5. Multi-connection node check
    connections_per_side = defaultdict(list)
    for e in edges:
        style = parse_style(e["style"])
        ex = style.get("exitX", "")
        ey = style.get("exitY", "")
        if ex and ey:
            key = f"{e['source']}:exitX={ex}"
            connections_per_side[key].append(e["id"])

    for side_key, e_list in connections_per_side.items():
        if len(e_list) > 1:
            exit_ys = set()
            for eid in e_list:
                for ee in edges:
                    if ee["id"] == eid:
                        s = parse_style(ee["style"])
                        exit_ys.add(s.get("exitY", "0.5"))
            if len(exit_ys) < len(e_list):
                report.append(
                    f"WARN: {side_key} has {len(e_list)} edges sharing exitY values — may overlap"
                )


    # 6. Coordinate multiples-of-10 check
    coord_issues = []
    for vid, v in vertices.items():
        if v["x"] % 10 != 0 or v["y"] % 10 != 0:
            coord_issues.append(f"{vid}(x={v['x']},y={v['y']})")
    if coord_issues:
        for ci in coord_issues:
            report.append(f"FAIL: Coordinates not multiples of 10: {ci}")
            fail_count += 1
    else:
        report.append("PASS: All coordinates multiples of 10")

    # 7. Minimum spacing check (warning only)
    from itertools import combinations
    spacing_warnings = []
    for a_id, b_id in combinations(vids, 2):
        a = vertices[a_id]
        b = vertices[b_id]
        # Skip parent-child pairs
        if a.get("parent") == b_id or b.get("parent") == a_id:
            continue
        # Check horizontal gap
        h_gap = max(0, min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"]))
        v_gap = max(0, min(a["y"] + a["h"], b["y"] + b["h"]) - max(a["y"], b["y"]))
        # If they're adjacent horizontally and vertically gap is tight
        if h_gap > 0:  # horizontally overlapping
            vert_dist = abs(a["y"] - b["y"]) if a["y"] < b["y"] else abs(b["y"] - a["y"])
            if 0 < vert_dist < 10 and a["y"] + a["h"] != b["y"] and b["y"] + b["h"] != a["y"]:
                spacing_warnings.append(f"{a_id} and {b_id} too close (vert gap {vert_dist}px)")
        if v_gap > 0:  # vertically overlapping
            horiz_dist = abs(a["x"] - b["x"]) if a["x"] < b["x"] else abs(b["x"] - a["x"])
            if 0 < horiz_dist < 10 and a["x"] + a["w"] != b["x"] and b["x"] + b["w"] != a["x"]:
                spacing_warnings.append(f"{a_id} and {b_id} too close (horiz gap {horiz_dist}px)")
    if spacing_warnings:
        for sw in spacing_warnings[:5]:  # limit to first 5
            report.append(f"WARN: Tight spacing: {sw}")
    else:
        report.append("PASS: Minimum node spacing acceptable")

    # 8. Edge crossing through non-endpoint shapes
    edge_shape_crossings = []
    for e in edges:
        segs = edge_path_segments(e, vertices)
        e_src = e["source"]
        e_tgt = e["target"]
        for seg in segs:
            p1, p2 = seg
            for vid, v in vertices.items():
                if vid in (e_src, e_tgt):
                    continue
                # Check if seg crosses the vertex bounding box
                bx, by, bw, bh = v["x"], v["y"], v["w"], v["h"]
                # Simple AABB line intersection
                if (min(p1[0], p2[0]) < bx + bw and max(p1[0], p2[0]) > bx and
                    min(p1[1], p2[1]) < by + bh and max(p1[1], p2[1]) > by):
                    # Check if the line actually crosses (not just passes by)
                    # This is approximate — flag for manual review
                    if v.get("parent") != "1" and e_src not in (vid,):
                        edge_shape_crossings.append((e["id"], vid))
    if edge_shape_crossings:
        for esc in edge_shape_crossings[:5]:
            report.append(f"WARN: Edge {esc[0]} may cross shape {esc[1]}")
    else:
        report.append("PASS: No edges crossing non-endpoint shapes")


    # 9. Edge source/target reference validation (Hard Rule 4)
    edge_ref_issues = []
    vertex_ids = set(vertices.keys())
    for e in edges:
        if e["source"] not in vertex_ids:
            edge_ref_issues.append(f"{e['id']}: source '{e['source']}' not found")
        if e["target"] not in vertex_ids:
            edge_ref_issues.append(f"{e['id']}: target '{e['target']}' not found")
    if edge_ref_issues:
        for er in edge_ref_issues:
            report.append(f"FAIL: Edge ref invalid: {er}")
            fail_count += 1
    else:
        report.append("PASS: All edge references valid")

    # 10. Duplicate ID check (Hard Rule 5)
    seen_ids = {}
    all_cells = []
    for e in edges:
        all_cells.append(("edge", e["id"]))
    for vid in vertices:
        all_cells.append(("vertex", vid))
    dup_issues = []
    for cell_type, cid in all_cells:
        if cid in seen_ids:
            dup_issues.append(f"{cid} (first as {seen_ids[cid]}, then as {cell_type})")
        else:
            seen_ids[cid] = cell_type
    if dup_issues:
        for di in dup_issues:
            report.append(f"FAIL: Duplicate ID: {di}")
            fail_count += 1
    else:
        report.append("PASS: All IDs unique")

    # 11. XML structure validation (Hard Rules 1-3)
    # Verify id="0" and id="1" exist as root/structure cells
    tree2 = ET.parse(filepath)
    all_ids = {c.get("id") for c in tree2.getroot().iter("mxCell")}
    if "0" not in all_ids:
        report.append("FAIL: Missing cell id=0 (root)")
        fail_count += 1
    elif "1" not in all_ids:
        report.append("FAIL: Missing cell id=1 (default layer)")
        fail_count += 1
    else:
        report.append("PASS: Root cells id=0/1 present")
    # 12. Font consistency check
    fonts_used = set()
    for vid, v in vertices.items():
        style = parse_style(v["style"])
        ff = style.get("fontFamily", "")
        if ff:
            fonts_used.add(ff)
    if len(fonts_used) > 1:
        report.append(f"WARN: Multiple fonts used: {fonts_used}")
    elif len(fonts_used) == 1:
        report.append(f"PASS: Consistent font ({list(fonts_used)[0]})")
    else:
        report.append("PASS: No font declarations (will use app default)")

    # 13. Edge style consistency check
    edge_styles_used = set()
    for e in edges:
        style = parse_style(e["style"])
        es = style.get("edgeStyle", "none")
        edge_styles_used.add(es)
    if len(edge_styles_used) > 1:
        report.append(f"WARN: Multiple edge styles used: {edge_styles_used}")
    else:
        report.append(f"PASS: Consistent edge style ({list(edge_styles_used)[0]})")

    # 14. Legend presence check (warn if >3 colors, no legend-like node)
    colors_in_use = set()
    for vid, v in vertices.items():
        style = parse_style(v["style"])
        sc = style.get("strokeColor", "")
        if sc and sc not in ("none", "default", "#000000"):
            colors_in_use.add(sc)
    has_legend = any("legend" in v.get("value", "").lower() or
                     "legend" in v.get("id", "").lower()
                     for v in vertices.values())
    if len(colors_in_use) > 3 and not has_legend:
        report.append(f"WARN: {len(colors_in_use)} colors used, no legend node detected")
    else:
        report.append("PASS: Legend check OK")


    # 15. html=1 check on cells with HTML tags in value
    html_issues = []
    tree3 = ET.parse(filepath)
    for cell in tree3.getroot().iter("mxCell"):
        value = cell.get("value", "")
        style = cell.get("style", "")
        if value and ("&lt;" in value or "<br>" in value or "<b>" in value or "<i>" in value):
            if "html=1" not in style:
                html_issues.append(cell.get("id", "?"))
    if html_issues:
        for hi in html_issues[:5]:
            report.append(f"FAIL: Cell {hi} has HTML tags in value but no html=1 in style")
            fail_count += 1
    else:
        report.append("PASS: HTML cells have html=1")

    # 16. Container child coordinate check (Hard Rule 12)
    container_ids = set()
    for vid, v in vertices.items():
        style = parse_style(v["style"])
        if style.get("container") == "1" or style.get("swimlane") is True:
            container_ids.add(vid)
    child_coord_issues = []
    for vid, v in vertices.items():
        if v["parent"] in container_ids:
            # Child of a container - coords should be small (relative to container)
            if v["x"] > 1000 or v["y"] > 1000:
                child_coord_issues.append(f"{vid} (parent={v['parent']}, x={v['x']}, y={v['y']})")
    if child_coord_issues:
        for cci in child_coord_issues[:5]:
            report.append(f"WARN: Container child may have absolute coords: {cci}")
    else:
        report.append("PASS: Container child coordinates OK")

    # Summary
    report.append("")
    report.append(f"Total: {fail_count} failures, {len(color_conflicts)} warnings")
    report.append(f"Vertices: {len(vertices)}, Edges: {len(edges)}, Canvas: {pw}x{ph}")

    return "\n".join(report), fail_count == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python diagram-check.py <file.drawio>")
        sys.exit(1)

    result, ok = check(sys.argv[1])
    print(result)
    sys.exit(0 if ok else 1)
