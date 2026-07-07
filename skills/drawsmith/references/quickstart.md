# Drawsmith Quickstart

Read this FIRST for any diagram request. This file is self-contained —
it has everything needed for 80% of diagrams. Only reach for the full
reference files (`drawio-guide.md`, `drawio-layouts.md`, `style-guide.md`)
when you need a niche template or detailed rationale.

---

## Step 0: Which Engine?

| User wants | Engine | Output |
|------------|--------|--------|
| Architecture, flowchart, pipeline, topology, UML, ERD, state machine | **draw.io** | `.drawio` |
| Bar, line, scatter, heatmap, ROC, violin, pie — anything with X/Y axes | **matplotlib** | `.py` → `.png` + `.pdf` |

---

## Step 1: Pick a Layout (draw.io)

| Description | Template § | Canvas |
|-------------|-----------|--------|
| System/platform/tool architecture, core + side panels | **§22 System Architecture** | 1100×850 |
| Vertical layers, protocol stacks | §1 Vertical Stack | 600×750 |
| Horizontal stages, CI/CD, data pipeline | §2 Horizontal Pipeline | 1100×300 |
| Central hub + satellites, star topology | §3 Center Hub | 750×600 |
| Before/after, method A vs B | §4 Side-by-Side | 900×650 |
| Process flow, decision tree | §6 Flowchart | 650×800 |
| DB schema, table relationships | §7 ERD | 800×600 |
| OOP design, inheritance | §8 UML Class | 800×700 |
| State transitions | §10 State Machine | 800×650 |

For multi-column architecture (the most common request), jump to §22.
For everything else, find the matching § in `references/drawio-layouts.md`.

---

## Step 2: Copy the XML Skeleton

Replace IDs, labels, coordinates from the template. Keep the structure.

```xml
<mxfile host="app.diagrams.net">
  <diagram name="Figure" id="fig">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="900" pageHeight="700"
                  jumpStyle="arc" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- YOUR NODES + EDGES HERE -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Step 3: Node & Edge Patterns

### Node (rounded rect, blue fill)

```xml
<mxCell id="my_node" value="&lt;b&gt;Title&lt;/b&gt;&lt;br&gt;Subtitle"
  style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle"
  vertex="1" parent="1">
  <mxGeometry x="400" y="160" width="280" height="60" as="geometry"/>
</mxCell>
```

### Edge (solid forward arrow)

```xml
<mxCell id="e1"
  style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5"
  edge="1" parent="1" source="node_a" target="node_b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Container (dashed grey box around related nodes)

```xml
<mxCell id="zone" value=""
  style="rounded=1;arcSize=6;container=1;pointerEvents=0;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4"
  vertex="1" parent="1">
  <mxGeometry x="30" y="80" width="300" height="250" as="geometry"/>
</mxCell>
<!-- Label INSIDE container at top-left, verticalAlign=top (the ONE exception) -->
<mxCell id="zone_lbl" value="Section Name"
  style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top"
  vertex="1" parent="zone">
  <mxGeometry x="10" y="6" width="200" height="16" as="geometry"/>
</mxCell>
<!-- Child nodes use parent="zone" with RELATIVE coordinates -->
```

---

## Step 4: XML Escape Cheat Sheet

The #1 cause of malformed XML. Inside `value="..."` with `html=1`:

| You want | Write in XML | Renders as |
|----------|-------------|------------|
| `&` (ampersand) | `&amp;amp;` | `&` |
| `<b>Bold</b>` | `&amp;lt;b&amp;gt;Bold&amp;lt;/b&amp;gt;` | **Bold** |
| line break | `&amp;#xa;` or `&lt;br&gt;` | newline |
| non-breaking space | `&amp;nbsp;` | ` ` (nbsp) |
| `"` (quote) | `&quot;` | `"` |

**Short version:** `&` → `&amp;amp;`, `<` → `&amp;lt;`, `>` → `&amp;gt;`, newline → `&lt;br&gt;`.

---

## Step 5: Grid Formula

```
x = col * 180 + 40    (col 0=40, 1=220, 2=400...)
y = row * 120 + 60    (row 0=60, 1=180, 2=300...)
Standard node: 140×60. Decision diamond: 140×80. Ellipse: 60×60.
```

For multi-column layouts (system architecture), partition the canvas:
```
zone_gap = 70px between columns  (40px is too tight — edges collide)
col_w = (pageWidth - 2*margin - (n_cols-1)*zone_gap) / n_cols
col_x[i] = margin + i * (col_w + zone_gap)
```
Example for 1100px, 3 cols, margin=30, gap=70:
```
Left:   x=30,  w=280  (right edge 310)
Center: x=380, w=340  (right edge 720)
Right:  x=790, w=280  (right edge 1070)
```
Bottom output nodes fan OUT wider than the processing node above them
(span 1.3×–1.5× the spine width).

---

## Step 6: Color Palettes

### IEEE Semantic (ML diagrams — default for ML papers)

| Role | Fill | Stroke |
|------|------|--------|
| Attention / Key method | `#E1D5E7` | `#9673A6` |
| Convolution / Primary processing | `#DAE8FC` | `#6C8EBF` |
| Pooling / Downsample | `#D5E8D4` | `#82B366` |
| Normalization | `#F5F5F5` | `#999999` |
| FC / Linear / Projection | `#FFE6CC` | `#D79B00` |
| Input / Embedding | `#F8CECC` | `#B85450` |
| Output / Loss | `#FFF2CC` | `#D6B656` |
| Element-wise ops | `#FFFFFF` | `#666666` |

### System Architecture (general system/tool/infra diagrams)

| Role | Fill | Stroke |
|------|------|--------|
| Core Engine / Orchestrator | `#DAE8FC` | `#6C8EBF` |
| Instruction / Config Layer | `#E1D5E7` | `#9673A6` |
| Tool / Processing Layer | `#D5E8D4` | `#82B366` |
| I/O Boundary (User, FS, DB) | `#F8CECC` | `#B85450` |
| External API / Service | `#FFF2CC` | `#D6B656` |
| Extension / Plugin System | `#FFE6CC` | `#D79B00` |
| Section Container (dashed box) | `#F5F5F5` | `#BDBDBD` |

---

## Step 7: Non-Negotiable Rules

1. `verticalAlign=middle` on EVERY content node (container labels: `verticalAlign=top`).
2. Coords MUST be multiples of 10.
3. Node gap ≥ 30px between vertically stacked nodes.
4. Column gap ≥ 40px for multi-column layouts.
5. `fontFamily=Times New Roman` everywhere.
6. Legend required when >2 colors or line styles used.
7. Every edge: `<mxGeometry relative="1" as="geometry"/>`. Never self-closing.
8. Every vertex: `<mxGeometry x y w h as="geometry"/>`. Always explicit.
9. `jumpStyle=arc` on `<mxGraphModel>` — crossings get visible arc jumps.
10. `html=1` on every content node — enables `<b>`, `<br>`, HTML formatting.

---

## Step 8: Edge Routing Quick Patterns

- **Simple down/right**: source + target only, no waypoints.
- **Bidirectional pair**: offset exitY — forward 0.35, reverse 0.65.
- **Self-loop**: exitX=1, exitY=0.25, 3 waypoints pulling loop outside node.
- **Cross-panel**: 2 waypoints through the inter-column corridor.
- **Multi-connection (3+ edges same side)**: distribute exitY evenly (0.2, 0.5, 0.8).

---

## Step 9: Self-Check (before delivering)

```
 1. No XML comments (<!-- -->) anywhere:             pass/fail
 2. id="0" and id="1" present as first cells:        pass/fail
 3. Every vertex has <mxGeometry as="geometry"/>:    pass/fail
 4. Every edge has <mxGeometry relative="1">:         pass/fail
 5. verticalAlign=middle on all content nodes:        pass/fail
 6. Coords are multiples of 10:                       pass/fail
 7. No overlapping bounding boxes:                    pass/fail
 8. Edge source/target IDs exist:                     pass/fail
 9. All IDs unique:                                   pass/fail
10. jumpStyle=arc on mxGraphModel:                    pass/fail
```

After generating, run: `python scripts/drawio-check.py <file.drawio>`

---

## Matplotlib Quickstart

### rcParams Block (copy-paste to every script)

```python
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif', 'font.serif': ['Times New Roman'],
    'font.size': 11, 'axes.titlesize': 12, 'axes.labelsize': 11,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'figure.dpi': 150, 'savefig.dpi': 600, 'savefig.bbox': 'tight',
})
```

### Non-Negotiable Rules

1. IEEE/Nature palette — never matplotlib defaults or `jet`/`rainbow`.
2. Always add a title — it makes the chart self-documenting.
3. `frameon=False` on legends. `spines[['top','right']].set_visible(False)`.
4. Error bars/bands MUST state what they represent in output text.
5. Extend BOTH axes a few percent beyond data range.

### Common Patterns

```python
fig, ax = plt.subplots(figsize=(3.5, 2.6))
ax.bar(x, values, color=palette, edgecolor='black', linewidth=0.5)
ax.spines[['top', 'right']].set_visible(False)
fig.savefig('output.png', dpi=600)
fig.savefig('output.pdf')
```

### Top Templates

- **§I-1** Grouped bar (SOTA comparison)
- **§II-6** Line + confidence band (training curves)
- **§III-9** ROC curve
- **§V-15** Box plot

Read `references/matplotlib-templates.md` for all 19 types.

After generating, run: `python scripts/matplotlib-check.py <script.py>`
