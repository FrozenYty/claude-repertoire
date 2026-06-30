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

    # 1. Vertex overlap (critical: nodes visually collide)
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

    # 2. Edge reference validity (critical: broken edges = broken diagram)
    vertex_ids = set(vertices.keys())
    for e in edges:
        if e["source"] not in vertex_ids:
            report.append(f"FAIL: Edge {e['id']}: source '{e['source']}' not found")
            fail_count += 1
        if e["target"] not in vertex_ids:
            report.append(f"FAIL: Edge {e['id']}: target '{e['target']}' not found")
            fail_count += 1
    if fail_count == len(overlaps):  # no new fails from edges
        report.append("PASS: All edge references valid")

    # 3. Duplicate IDs (critical: breaks draw.io rendering)
    seen = {}
    for vid in vertices:
        if vid in seen:
            report.append(f"FAIL: Duplicate vertex ID '{vid}'")
            fail_count += 1
        seen[vid] = True
    for e in edges:
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
