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

## Step 4: XML Escape — Just 3 Rules

The #1 cause of malformed XML. Inside `value="..."` with `html=1`:

| Goal | Write in XML | Why |
|------|-------------|-----|
| **Bold text** `<b>X</b>` | `&amp;lt;b&amp;gt;X&amp;lt;/b&amp;gt;` | `&lt;` → XML decodes to `<` → HTML renders bold |
| **Line break** | `&lt;br&gt;` | `&lt;br&gt;` → XML decodes to `<br>` → HTML newline |
| **`&` character** | `&amp;amp;` | `&amp;` → `&`, then `amp;` → HTML renders `&` |
| Non-breaking space | `&amp;nbsp;` | → `&nbsp;` → HTML renders ` ` |
| `"` (double quote) | `&quot;` | Standard XML escape |

**Pattern:** Every `&` in the final rendered text → `&amp;` in XML. Every `<` in HTML → `&lt;` in XML. That's it.

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

### Industry Architecture (AWS/Azure/GCP cloud & enterprise infra)

Source: [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/), [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/).

| Layer | Fill | Stroke |
|-------|------|--------|
| Compute / Services | `#ED7100` | `#D05C17` |
| Storage / Database | `#7AA116` | `#5A8A0E` |
| Networking / CDN | `#8C4FFF` | `#6A30C0` |
| Security / IAM | `#C7131F` | `#A0101A` |
| Analytics / ML | `#116D5B` | `#0D5546` |
| Integration / Messaging | `#BC1356` | `#960F44` |
| External / Users | `#232F3E` | `#1A2430` |

**Palette router:** ML model → IEEE. Software system → System Arch. Cloud infra → Industry.

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

After generating, run: `python scripts/drawio-check.py <file.drawio>` (sanity check — review warnings, use judgment).

### Before Delivering: 5 Must-Checks

These catch the failure modes that cause 90% of rework. Check BEFORE showing the user:

1. **Column/zone gaps ≥ 60px.** At 40px, edge labels collide with adjacent containers.
   Measure `rightZone.x − (leftZone.x + leftZone.w)`. If < 60, widen the canvas or
   reduce column widths.

2. **Two bottom-row nodes have ≥ 50px horizontal gap between them.** When a processing
   layer funnels into two outputs (store + search, FS + git), fan them OUT — span should
   be 1.3× to 1.5× the parent node's width. They shouldn't hug each other.

3. **Stacked nodes have ≥ 30px vertical gap.** At < 30px, arrow shafts become invisible.
   Check: `lowerNode.y − (upperNode.y + upperNode.h) ≥ 30`.

4. **Legend present if > 2 colors or > 1 edge style used.** No legend = reader can't
   decode the diagram. Always include both edge types AND color swatches in the legend.

5. **No container right edge overlaps with adjacent column's left edge.** Scan each
   container: `container.x + container.w` must be < next column's `x` minus 10px.

---

## Matplotlib Quickstart

### Chart Type Decision Tree

| Data scenario | Chart type | Template § |
|---------------|-----------|------------|
| Compare values across categories | Grouped / Horizontal bar | §I-1, §I-2 |
| Show trend over time or sequence | Line + confidence band | §II-6 |
| Binary classifier performance | ROC / PR curve | §III-9, §III-10 |
| Correlation matrix or intensity grid | Heatmap | §IV-11 |
| Distribution of a single variable | Box / Violin | §V-15, §V-14 |
| Parts of a whole (few categories) | Donut / Pie | §V-17 |
| Two different Y-axis scales | Dual Y-axis | §V-18 |
| Multi-variable comparison across groups | Faceted grid | §VI-19 |
| Show top-N + cumulative (Pareto) | Pareto front | §I-4 |
| Multi-dimensional profile | Radar | §I-5 |

Read `references/matplotlib-templates.md` for all 19 types with runnable code.

### rcParams Block (copy-paste to EVERY script)

```python
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif', 'font.serif': ['Times New Roman'],
    'font.size': 11, 'axes.titlesize': 12, 'axes.labelsize': 11,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'figure.dpi': 150, 'savefig.dpi': 600, 'savefig.bbox': 'tight',
    'axes.spines.top': False, 'axes.spines.right': False,
})
```

### Color Palette (default: Nature 2025)

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| `#433764` | `#E48566` | `#A05179` | `#C66571` | `#C6C687` | `#668441` |

```python
nature_pal = ["#433764", "#E48566", "#A05179", "#C66571", "#C6C687", "#668441"]
```

For IEEE, Science, Cell, or other palettes, see `references/style-guide.md` §1.
**Forbidden regardless of use case:** `jet`, `rainbow`, matplotlib defaults.

### Non-Negotiable Rules

1. **rcParams block at top of every script.** Not optional — it sets fonts, DPI, font embedding.
2. **Nature/IEEE/Science palette** — never matplotlib defaults or `jet`/`rainbow`.
3. **Always add a title** — `fig.suptitle("...", fontweight="bold")` makes the chart self-documenting.
4. **Remove top + right spines.** `spines[['top','right']].set_visible(False)` on EVERY chart.
5. **`frameon=False` on legends.** Frame around legend looks amateurish.
6. **Error bars/bands MUST state what they represent** in output text (±1 SD, 95% CI, N runs).
7. **Extend both axes** a few percent beyond data range — breathing room, not empty space.
8. **Save as BOTH `.png` (≥600 dpi) and `.pdf` (vector).** PNG for quick view, PDF for publication.

### Common Patterns

```python
# Bar chart — the most common request
fig, ax = plt.subplots(figsize=(3.5, 2.6))
ax.bar(x, values, color=nature_pal[:len(values)], edgecolor='black', linewidth=0.5)
ax.spines[['top', 'right']].set_visible(False)
ax.set_title("Result Comparison", fontweight="bold")
fig.savefig('output.png', dpi=600)
fig.savefig('output.pdf')
```

```python
# Line chart with confidence band
fig, ax = plt.subplots(figsize=(4.5, 2.8))
ax.plot(x, mean, color=nature_pal[0], linewidth=1.5, label='Ours')
ax.fill_between(x, mean-std, mean+std, color=nature_pal[0], alpha=0.15)
ax.spines[['top', 'right']].set_visible(False)
ax.legend(frameon=False)
fig.savefig('output.png', dpi=600)
```

### Common Pitfalls (real failures)

1. **Type-3 fonts in PDF.** Symptom: ACM/IEEE submission rejected. Fix: `'pdf.fonttype': 42` in rcParams.
2. **Chinese text as tofu squares.** Symptom: `□□□□` instead of Chinese. Fix: set CJK font chain (see `style-guide.md` §11).
3. **Legend covers data.** Symptom: legend box on top of data points. Fix: `bbox_to_anchor=(1.02, 1)` or place outside.
4. **Bars clipped at axis edge.** Symptom: tallest bar hits the top. Fix: `ax.set_ylim(0, max_val * 1.12)`.
5. **`jet` colormap used.** Symptom: chart looks like a weather radar. Fix: use `viridis`, `cividis`, or journal palette.

### Before Delivering: 4 Must-Checks

1. **`pdf.fonttype = 42` in rcParams.** If missing, PDF fails journal submission.
2. **Spines removed.** `top` and `right` spines hidden. Left + bottom only.
3. **Error disclosure.** If error bars/bands present, output text states what they represent.
4. **Color palette declared.** State which palette was used (Nature, IEEE, etc.) in output.

After generating, run: `python scripts/matplotlib-check.py <script.py>` (sanity check — review warnings, use judgment).
