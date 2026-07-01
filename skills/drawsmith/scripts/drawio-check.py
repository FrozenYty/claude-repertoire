"""drawio-check.py — Automated critical-defect validator for draw.io XML.

Run after generating any .drawio file. Reports concrete pass/fail for
defects that would render the diagram broken or visually unreadable:
vertex overlap, broken edge refs, duplicate IDs, out-of-page elements,
html=1 missing, bidirectional overlap, duplicate edges, invisible arrows,
exit-point collisions, and edge-through-shape warnings.

For the full 15-item checklist, see references/drawio-guide.md.

Usage: python drawio-check.py <file.drawio>
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

    # Filter: exclude coordinate-based edges (axis lines, separators) from edge checks
    noded_edges = [e for e in edges if e["source"] and e["target"]]
    coord_edges = [e for e in edges if not e["source"] or not e["target"]]

    # 1. Vertex overlap (skip Venn circles, text labels inside Venn regions)
    vids = list(vertices.keys())
    overlaps = []
    for i in range(len(vids)):
        for j in range(i + 1, len(vids)):
            a = vertices[vids[i]]
            b = vertices[vids[j]]
            if bbox_overlap(a, b):
                # Skip Venn-style overlaps: both are ellipses with opacity <= 50
                sa = parse_style(a.get("style", ""))
                sb = parse_style(b.get("style", ""))
                both_ellipse = (sa.get("ellipse") or sa.get("ellipse") is True) and (sb.get("ellipse") or sb.get("ellipse") is True)
                if both_ellipse:
                    op_a = float(sa.get("opacity", 100))
                    op_b = float(sb.get("opacity", 100))
                    if op_a <= 50 and op_b <= 50:
                        continue
                # Skip text labels (annotations can overlap with shapes)
                if sa.get("text") is True or sb.get("text") is True:
                    continue
                # Skip small markers on timeline axis (<=20px) next to text
                if min(a.get("w",0) + a.get("h",0), b.get("w",0) + b.get("h",0)) <= 40:
                    continue
                overlaps.append((vids[i], vids[j]))
    if overlaps:
        for o in overlaps:
            report.append(f"FAIL: Vertex overlap between {o[0]} and {o[1]}")
            fail_count += 1
    else:
        report.append("PASS: No vertex bounding box overlap")

    # 2. Edge reference validity (critical: broken edges = broken diagram)
    vertex_ids = set(vertices.keys())
    for e in noded_edges:
        # Skip coordinate-based edges (sourcePoint/targetPoint) — used for axis lines
        if not e["source"] and not e["target"]:
            continue
        if e["source"] and e["source"] not in vertex_ids:
            report.append(f"FAIL: Edge {e['id']}: source '{e['source']}' not found")
            fail_count += 1
        if e["target"] and e["target"] not in vertex_ids:
            report.append(f"FAIL: Edge {e['id']}: target '{e['target']}' not found")
            fail_count += 1
    if fail_count == len(overlaps):
        report.append("PASS: All edge references valid")

    # 3. Duplicate IDs (critical: breaks draw.io rendering)
    seen = {}
    for vid in vertices:
        if vid in seen:
            report.append(f"FAIL: Duplicate vertex ID '{vid}'")
            fail_count += 1
        seen[vid] = True
    for e in noded_edges:
        if e["id"] in seen:
            report.append(f"FAIL: Duplicate edge ID '{e['id']}'")
            fail_count += 1
        seen[e["id"]] = True
    if fail_count == len(overlaps):  # no new fails
        report.append("PASS: All IDs unique")

    # 4. Out-of-page elements (critical: invisible in editor)
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

    # 5. html=1 missing on HTML labels (critical: renders &lt;br&gt; as raw text)
    tree = ET.parse(filepath)
    for cell in tree.getroot().iter("mxCell"):
        value = cell.get("value", "")
        style = cell.get("style", "")
        if value and ("&lt;" in value or "<br>" in value or "<b>" in value):
            if "html=1" not in style:
                report.append(f"FAIL: Cell {cell.get('id','?')} has HTML but no html=1")
                fail_count += 1

    # 6. Bidirectional edge overlap (critical: arrows drawn on top of each other)
    from collections import defaultdict as dd
    pairs = dd(list)
    for e in noded_edges:
        key = tuple(sorted([e["source"], e["target"]]))
        pairs[key].append(e)
    for key, elist in pairs.items():
        if len(elist) >= 2:
            styles = [parse_style(e["style"]) for e in elist]
            # Only flag if edges exit/enter on the SAME side (both exitX or both exitY match)
            positions = [(s.get("exitX", "0.5"), s.get("exitY", "0.5")) for s in styles]
            if len(set(positions)) < len(positions):
                report.append(f"FAIL: Bidirectional edges {key[0]}<->{key[1]} overlap at same exit point")
                fail_count += 1


    # 7. Duplicate edges (same source->target AND same exit side = visual overlap)
    from collections import defaultdict as dd2
    edge_pairs = dd2(list)
    for e in noded_edges:
        style = parse_style(e["style"])
        exit_side = f'{style.get("exitX","0.5")}-{style.get("exitY","0.5")}'
        key = (e["source"], e["target"], exit_side)
        edge_pairs[key].append(e["id"])
    for (src, tgt, side), eids in edge_pairs.items():
        if len(eids) > 1:
            report.append(f"FAIL: Overlapping edges {src}->{tgt} at exit {side}: {eids}")
            fail_count += 1

    # 8. Invisible / extremely short edges (gap < 10px between connected nodes)
    short_count = 0
    for e in noded_edges:
        src_v = vertices.get(e["source"])
        tgt_v = vertices.get(e["target"])
        if src_v and tgt_v:
            # Calculate the gap between the two nodes (center to center distance minus radii)
            scx, scy = src_v["x"] + src_v["w"]/2, src_v["y"] + src_v["h"]/2
            tcx, tcy = tgt_v["x"] + tgt_v["w"]/2, tgt_v["y"] + tgt_v["h"]/2
            dist = ((tcx - scx)**2 + (tcy - scy)**2)**0.5
            if src == tgt:
                continue  # self-loops use curved=1, distance is irrelevant
            if dist < 30:  # center-to-center < 30px = arrow nearly invisible
                short_count += 1
                report.append(f"WARN: Very short edge {e['id']} ({src}->{tgt}, center distance {dist:.0f}px)")
    if short_count == 0:
        report.append("PASS: All edge lengths acceptable")

    # 9. Same-exit-point collision (edges from same source sharing same exitX+exitY)
    from collections import defaultdict as dd3
    exit_map = dd3(list)
    for e in noded_edges:
        style = parse_style(e["style"])
        ex = style.get("exitX", "0.5")
        ey = style.get("exitY", "0.5")
        key = (e["source"], ex, ey)
        exit_map[key].append(e["id"])
    exit_collisions = 0
    for key, eids in exit_map.items():
        if len(eids) > 1:
            exit_collisions += 1
            report.append(f"FAIL: Edges from {key[0]} share exit point ({key[1]},{key[2]}): {eids}")
            fail_count += 1
    if exit_collisions == 0:
        report.append("PASS: No exit-point collisions")

    # 10. Edge passing through non-endpoint shape (warn: layout issue)
    edge_shape_warns = 0
    for e in noded_edges:
        src_id, tgt_id = e["source"], e["target"]
        segs = edge_path_segments(e, vertices)
        for (p1, p2) in segs:
            for vid, v in vertices.items():
                if vid in (src_id, tgt_id):
                    continue
                # Skip swimlane containers (edges naturally pass through lanes)
                vstyle = parse_style(v.get("style", ""))
                if vstyle.get("swimlane") is True:
                    continue
                # Skip Venn circles (intentional overlap)
                if vstyle.get("ellipse") is True:
                    op = float(vstyle.get("opacity", 100))
                    if op <= 50:
                        continue
                bx, by, bw, bh = v["x"], v["y"], v["w"], v["h"]
                if (min(p1[0], p2[0]) < bx + bw and max(p1[0], p2[0]) > bx and
                    min(p1[1], p2[1]) < by + bh and max(p1[1], p2[1]) > by):
                    edge_shape_warns += 1
                    report.append(f"WARN: Edge {e['id']} ({src_id}->{tgt_id}) passes through {vid}")
                    break
            else:
                continue
            break
    if edge_shape_warns == 0:
        report.append("PASS: No edges crossing through shapes")


    # Summary
    report.append("")
    report.append(f"Total: {fail_count} failures")
    report.append(f"Vertices: {len(vertices)}, Edges: {len(edges)}, Canvas: {pw}x{ph}")

    return chr(10).join(report), fail_count == 0

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
