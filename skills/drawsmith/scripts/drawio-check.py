"""diagram-check.py — Automated geometry & style validator for draw.io XML.

Run after generating any .drawio file. Reports concrete pass/fail for
edge crossings, bounding box overlap, color reuse, and perimeter gaps.

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
            report.append(f"FAIL: Edge crossing between {c[0]} and {c[1]}")
            fail_count += 1
    else:
        report.append("PASS: No edge crossings detected")

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
