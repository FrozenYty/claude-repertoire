# Diagram Layout Templates

Read this file when generating any conceptual diagram with draw.io.
Pick the closest layout pattern, adapt labels to the user's spec,
and keep the coordinate math as-is.

All templates follow the Flow Direction and No-Overlap rules from
`drawio-guide.md`. For visual style (colors, fonts, line weights),
see `style-guide.md`.

## Index

### Specific architectures (full XML)

| Architecture | When to use | Section |
|---|---|---|
| Transformer encoder-decoder | Translation, summarization, LLM architectures | §20 |
| Diffusion forward/reverse | DDPM/DDIM, score-based, flow-matching | §21 |
| RAG pipeline | Retrieval-augmented LLM systems | §22 |
| Multi-stage training | Pretrain -> SFT -> RLHF, foundation models | §23 |

### Layout patterns

| Pattern | When to use | Section |
|---|---|---|
| Vertical stack (TB) | Protocol stacks, layered architectures, dependency chains | §1 |
| Horizontal pipeline (LR) | Data processing pipelines, CI/CD, multi-stage workflows | §2 |
| Center hub + satellites | CPU/system overviews, IoT gateways, star-topology networks | §3 |
| Side-by-side comparison | Before/after, method A vs B, paired-element comparison | §4 |
| Grid / table layout | Feature matrices, parameter tables, ablation grids | §5 |

### Classic diagram types

| Type | When to use | Section |
|---|---|---|
| Flowchart | Decision trees, process flows, algorithm logic | §6 ⚠️ |
| Entity-Relationship Diagram (ERD) | Database schemas, data models, table relationships | §7 |
| UML Class Diagram | OOP design, architecture modeling, inheritance hierarchies | §8 ⚠️ |
| Sequence Diagram | Protocol interactions, API call flows, message passing | §9 ⚠️ |
| State Machine Diagram | State transitions, formal methods, protocol specifications | §10 ⚠️ |
| Data Flow Diagram (DFD) | Software engineering, system data flows, process modeling | §11 |
| Swimlane Diagram | Cross-functional process flows, RACI charts | §17 ⚠️ |
| Wireframe / Mockup | App screens, website layouts, UI prototypes | §18 |
| Cross-Functional Table | Actor × Phase process grid, two-axis flowcharts | §19 |

⚠️ = quality may degrade for hand-written XML; keep diagrams simple or split across pages

If the user's request doesn't match any of these, fall back to the
general workflow in `prompts/drawio.md` and apply the Flow Direction
rule manually. Don't force-fit a non-matching diagram onto a template.

---

## §1 Vertical stack (TB)

**When to use:** Protocol stacks, layered architectures, dependency chains,
hierarchies — any figure where nodes are logically stacked top-to-bottom
in a single column. Not specifically ML; use the Flow Direction rule to
decide which end is "input" and which is "output."

**Canvas:** 600×750 portrait. Single column centered.

**Layout conventions:**
- All nodes share the same `x` and `w`, vertically centered in the canvas
  (`x = (pageWidth - w) / 2`).
- Equal vertical gap between adjacent nodes (24–30px).
- Arrows between adjacent nodes only. No diagonal or long cross-arrows.
- Flow direction: decide which way data flows. If bottom-to-top (ML
  convention), place input at the largest y and ensure `source.y > target.y`
  for every forward edge. If top-to-bottom (protocol stack convention,
  e.g. OSI), place the topmost layer at the smallest y and arrows go DOWN.
  **Disclose the convention in the first comment of the XML.**

**Node table** (6-node example, bottom-up data flow):

```
id      | label        | x   | y   | w   | h
n6_out  | Output       | 140 | 40  | 320 | 50
n5      | Layer 5      | 140 | 120 | 320 | 50
n4      | Layer 4      | 140 | 200 | 320 | 50
n3      | Layer 3      | 140 | 280 | 320 | 50
n2      | Layer 2      | 140 | 360 | 320 | 50
n1_in   | Input        | 140 | 440 | 320 | 50
```

Edge chain: n1_in → n2 → n3 → n4 → n5 → n6_out. All vertical, no
waypoints. Every edge satisfies `source.y > target.y` (arrows go UP).

**To adapt:** change node count, labels, and the flow direction comment.
Shift all `y` values by the same offset to move the stack up or down.

**Golden XML example (6-layer stack, bottom-up data flow):**



**Key patterns:** same x/w (centered column), y=row*80+140, bottom-to-top flow.



## §2 Horizontal pipeline (LR)

**When to use:** Data processing pipelines, CI/CD, multi-stage workflows
— anything where stages are sequential and flow left to right.

**Canvas:** 1100×300 landscape. Single row centered vertically.

**Layout conventions:**
- All stage nodes share the same `y` and `h`, spaced equally along X.
- Arrows between adjacent stages, going RIGHT (`source.x < target.x`).
- Labels above or below each stage naming the input/output of that stage.
  Small data-source boxes can hang below stages (e.g., dataset names).
- Use vertical arrows from data-source boxes UP into the pipeline stage.

**Node table** (5-stage example with 3 data-source boxes):

```
id      | label              | x   | y   | w   | h
s1      | Stage 1: Ingest   | 30  | 100 | 170 | 60
s2      | Stage 2: Process  | 240 | 100 | 170 | 60
s3      | Stage 3: Validate | 450 | 100 | 170 | 60
s4      | Stage 4: Export   | 660 | 100 | 170 | 60
s5      | Stage 5: Archive  | 870 | 100 | 170 | 60
d1      | Raw Data (S3)     | 30  | 200 | 170 | 40
d3      | Schema V2         | 450 | 200 | 170 | 40
d5      | Parquet / Iceberg | 870 | 200 | 170 | 40
```

Edge chain: s1 → s2 → s3 → s4 → s5 (all LR, `source.x < target.x`).
Data-source → stage edges: d1 → s1 (↑), d3 → s3 (↑), d5 → s5 (↑).

**To adapt:** add/remove stages, rename labels, change data-source box
labels to match your pipeline's artifacts. Keep `x` spacing uniform:
`gap = (pageWidth - n * w) / (n + 1)` for n equally-

**Golden XML example (5-stage pipeline, left-to-right flow):**

```xml
<mxGraphModel dx="1200" dy="500" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="300" math="0" shadow="0">
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <mxCell id="s1" value="Stage 1 &lt;br&gt;&lt;b&gt;Ingest&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="30" y="100" width="170" height="60" as="geometry"/></mxCell>
    <mxCell id="e12" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="s1" target="s2"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="s2" value="Stage 2 &lt;br&gt;&lt;b&gt;Process&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="240" y="100" width="170" height="60" as="geometry"/></mxCell>
    <mxCell id="e23" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="s2" target="s3"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="s3" value="Stage 3 &lt;br&gt;&lt;b&gt;Validate&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="450" y="100" width="170" height="60" as="geometry"/></mxCell>
    <mxCell id="e34" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="s3" target="s4"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="s4" value="Stage 4 &lt;br&gt;&lt;b&gt;Export&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="660" y="100" width="170" height="60" as="geometry"/></mxCell>
    <mxCell id="e45" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="s4" target="s5"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="s5" value="Stage 5 &lt;br&gt;&lt;b&gt;Archive&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="870" y="100" width="170" height="60" as="geometry"/></mxCell>
  </root>
</mxGraphModel>
```

**Key patterns:** same y/h per stage, x=col*210+30, left-to-right flow.

spaced stages.



---

## §3 Center hub + satellites

**When to use:** System overviews, CPU/SoC block diagrams, IoT gateway
topologies, any star-topology or hub-and-spoke figure.

**Canvas:** 750×600.

**Layout conventions:**
- One central component (the "hub") placed at the canvas center.
- 2–6 satellite nodes placed around it: left, right, above, below, and
  optionally at the four corners.
- Radial connecting arrows from hub to each satellite (or bidirectional).
- Satellites may connect to each other with dashed side edges.
- **Flow direction is not TB or LR.** The hub pattern is inherently radial.
  Edges exit the hub at the side closest to each satellite. Direct edges,
  no waypoints unless satellites are at the same angle from the hub.
- Hub uses a distinct fill color or heavier stroke to stand out.

**Node table** (4-satellite example):

```
id      | label                 | x   | y   | w   | h
hub     | System Core (Hub)     | 255 | 230 | 240 | 100
top     | Satellite A (Input)   | 255 | 60  | 240 | 60
right   | Satellite B (Output)  | 560 | 250 | 150 | 60
bottom  | Satellite C (Storage) | 255 | 460 | 240 | 60
left    | Satellite D (Control) | 40  | 250 | 150 | 60
```

Edges:
- top → hub (↓, enters hub top)
- hub → right (→, exits hub right)
- hub → bottom (↓, exits hub bottom)
- left → hub (→, exits left right, enters hub left)

All edges are direct `exitX=0.5;exitY=1` or `exitX=1;exitY=0.5` etc.
No waypoints needed because satellites are axis-aligned with the hub.

**To adapt:** change hub and satellite labels, add corner satellites
at (40, 60), (560, 60), (560

**Golden XML example (hub + 4 satellites, star topology):**

```xml
<mxGraphModel dx="1000" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="750" pageHeight="600" math="0" shadow="0">
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <mxCell id="hub" value="&lt;b&gt;System Core&lt;/b&gt;&lt;br&gt;Orchestrator" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=2;fontFamily=Times New Roman;fontStyle=0;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="255" y="230" width="240" height="100" as="geometry"/></mxCell>
    <mxCell id="sat_input" value="&lt;b&gt;Input Adapter&lt;/b&gt;&lt;br&gt;Data Ingestion" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="255" y="60" width="240" height="60" as="geometry"/></mxCell>
    <mxCell id="e_in" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="sat_input" target="hub"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="sat_output" value="&lt;b&gt;Output&lt;/b&gt;&lt;br&gt;API Gateway" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="560" y="250" width="150" height="60" as="geometry"/></mxCell>
    <mxCell id="e_out" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="hub" target="sat_output"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="sat_storage" value="&lt;b&gt;Storage&lt;/b&gt;&lt;br&gt;Persistent Layer" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="255" y="460" width="240" height="60" as="geometry"/></mxCell>
    <mxCell id="e_sto" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="hub" target="sat_storage"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="sat_control" value="&lt;b&gt;Control&lt;/b&gt;&lt;br&gt;Management API" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="250" width="150" height="60" as="geometry"/></mxCell>
    <mxCell id="e_ctrl" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="sat_control" target="hub"><mxGeometry relative="1" as="geometry"/></mxCell>
  </root>
</mxGraphModel>
```

**Key patterns:** hub centered with strokeWidth=2, 4 axis-aligned satellites, no waypoints.

, 460), (40, 460) for an 8-node star.



---

## §4 Side-by-side comparison

**When to use:** Before/after comparisons, Method A vs Method B, paired
element mapping between two systems.

**Canvas:** 900×650. Two vertical columns side by side.

**Layout conventions:**
- Left and right columns share the same module count, heights, and Y
  positions so paired elements sit at the same visual row.
- A vertical separator line (dashed, gray, no arrowheads) runs down the
  middle gap.
- Dashed thin mapping lines (no arrowheads) connect corresponding
  elements between columns.
- Column labels sit ABOVE each column (or at the top of each column as a
  colored header bar).

**Node table** (4-pair example):

```
id         | label            | x   | y   | w   | h
a1         | Element A1       | 40  | 120 | 320 | 70
a2         | Element A2       | 40  | 230 | 320 | 70
a3         | Element A3       | 40  | 340 | 320 | 70
a4         | Element A4       | 40  | 450 | 320 | 70
b1         | Element B1       | 540 | 120 | 320 | 70
b2         | Element B2       | 540 | 230 | 320 | 70
b3         | Element B3       | 540 | 340 | 320 | 70
b4         | Element B4       | 540 | 450 | 320 | 70
```

Mapping edges: a1 → b1, a2 → b2, a3 → b3, a4 → b4 — all dashed gray,
`endArrow=none`, `entryX=0;entryY=0.5;exitX=1;exitY=0.5`. Direct
horizontal lines because Y positions are matched. No waypoints.

Separator: a vertical edge at x=450 from y=90 to y=540, `endArrow=none`,
`dashed=1;dashPattern=12 6;strokeColor=#AAAAAA;strokeWidth=1`.

**To adapt:** change element count (add/remove pairs with corresponding
Y shifts), rename labels, op

**Golden XML example (4-element comparison, Method A vs B):**

```xml
<mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="650" math="0" shadow="0">
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <mxCell id="hdr_a" value="&lt;b&gt;Method A&lt;/b&gt;" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="40" width="320" height="40" as="geometry"/></mxCell>
    <mxCell id="hdr_b" value="&lt;b&gt;Method B&lt;/b&gt;" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="40" width="320" height="40" as="geometry"/></mxCell>
    <mxCell id="sep" style="endArrow=none;dashed=1;dashPattern=12 6;strokeColor=#AAAAAA;strokeWidth=1" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="450" y="80" as="sourcePoint"/><mxPoint x="450" y="600" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="a1" value="Element A-1 &lt;br&gt;Description" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="120" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b1" value="Element B-1 &lt;br&gt;Description" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="120" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m1" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1" edge="1" parent="1" source="a1" target="b1"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="a2" value="Element A-2" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="230" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b2" value="Element B-2" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="230" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m2" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1" edge="1" parent="1" source="a2" target="b2"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="a3" value="Element A-3" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="340" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b3" value="Element B-3" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="340" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m3" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1" edge="1" parent="1" source="a3" target="b3"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="a4" value="Element A-4" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="450" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b4" value="Element B-4" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="450" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m4" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1" edge="1" parent="1" source="a4" target="b4"><mxGeometry relative="1" as="geometry"/></mxCell>
  </root>
</mxGraphModel>
```

**Key patterns:** paired elements share y-position, mapping edges (no arrowhead), separator line down middle.

tionally use different fill colors for
column A vs column B.



---

## §5 Grid / table layout

**When to use:** Feature comparison matrices, parameter tables,
ablation-configuration matrices — anything that's essentially a labeled
grid with cells.

**Canvas:** 800×550. Row×column grid with headers.

**Layout conventions:**
- Top row = column headers (dark fill, white text, bold).
- Leftmost column = row headers (lighter header fill).
- Body cells = uniform fill, light border.
- Equal cell sizes: `cell_w = (pageWidth - rowHeader_w) / n_cols`,
  `cell_h = (pageHeight - colHeader_h) / n_rows`.
- No edges between cells — adjacent rectangles with thin borders imply
  the grid structure.

**Node table** (3×4 example with 3 columns + row header, 4 data rows):

```
id      | label         | x   | y   | w   | h   | style
h_r1    |               | 30  | 60  | 110 | 44  | (top-left corner, empty or "Metric")
h_c1    | Method A      | 140 | 60  | 200 | 44  | (column header)
h_c2    | Method B      | 340 | 60  | 200 | 44  | (column header)
h_c3    | Ours          | 540 | 60  | 200 | 44  | (column header)
r1_l    | Accuracy (%)  | 30  | 104 | 110 | 40  | (row header)
c11-c13 | 78.2/80.4/83.7| 140 | 104 | 200 | 40  | (body cells)
r2_l    | F1 Score      | 30  | 144 | 110 | 40  | (row header)
c21-c23 | 75.1/78.3/81.9| 140 | 144 | 200 | 40  |
r3_l    | Latency (ms)  | 30  | 184 | 110 | 40  | (row header)
c31-c33 | 12/15/10      | 140 | 184 | 200 | 40  |
r4_l    | Params (M)    | 30  | 224 | 110 | 40  | (row header)
c41-c43 | 85/120/78     | 140 | 224 | 200 | 40  |
```

Body cell style: `rounded=0;fillColor=#FFFFFF;strokeColor=#DDDDDD;
strokeWidth=0.5;html=1;align=center;verticalAlign=middle;
fontFamily=Times New Roman;fontSize=11;fontColor=#333333`.

Header style: `rounded=0;fillColor=#37474F;strokeColor=#333333;
strokeWidth=0.5;html=1;fontFamily=Times New Roman;fontSize=11;
fontStyle=1;fontColor=#FFFFFF;align=center;verticalAlign=middle`.

Row header style: `rounded=0;fillColor=#ECEFF1;strokeColor=#DDDDDD;
strokeWidth=0.5;html=1;fontFamily=Times New Roman;fontSize=11;
fontStyle=1;fontColor=#333333;align=left;verticalAlign=middle`.

"Houdini" cell (ours, best value): `fillColor=#E8F5E9;fontStyle=3` to
highlight the winning entry.

**To adapt:** change n_rows and n_cols, recalculate `cell_w` and `cell_h`,
replace labels and values. The header row and body cell styles stay
constant.



---

## §6 Flowchart

> **Quality note:** Hand-written XML for this diagram type can produce
> arrow spaghetti with complex topologies. The check-refine loop helps but
> has a hard 3-iteration cap. Keep the diagram as simple as possible —
> split complex cases across multiple pages.

**When to use:** Decision trees, algorithm logic, process flows, approval
workflows — any step-by-step branching logic.

**Canvas:** 650×800 portrait. TB flow, decisions branch LR then rejoin.

**Shape vocabulary (each a distinct semantic role):**

| Element | Style keywords | Example |
|---|---|---|
| Start / End | `ellipse;fillColor=#D5E8D4;strokeColor=#82B366` | Green oval |
| Process | `rounded=0;fillColor=#DAE8FC;strokeColor=#6C8EBF` | Blue rect |
| Decision | `rhombus;fillColor=#FFF2CC;strokeColor=#D6B656` | Yellow diamond |
| I/O | `shape=parallelogram;perimeter=parallelogramPerimeter;fillColor=#FFE6CC;strokeColor=#D79B00` | Orange |
| Subprocess | `rounded=1;fillColor=#E1D5E7;strokeColor=#9673A6` | Purple |

**All nodes:** `whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontSize=12;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle`

**Layout conventions:**
- Start node at top-center, end node at bottom-center.
- Process and I/O nodes form the vertical spine (center aligned).
- Decision nodes branch left/right, then rejoin below.
- **Always label decision branches** `"Yes"` / `"No"` (or specific
  conditions) on the outgoing edges.
- Vertical gap 150px, horizontal gap 200px between decision branches.
- Use orthogonal routing for all edges — `exitX=0.5;exitY=1` on process
  nodes, `exitX=0;exitY=0.5` and `exitX=1;exitY=0.5` on decision nodes.

**Edge style:**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5
```


**Golden XML example (3-step with decision, Yes/No branches):**

```xml
<mxGraphModel dx="900" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="650" pageHeight="1000" math="0" shadow="0">
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <!-- Start -->
    <mxCell id="start" value="Start" style="ellipse;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;perimeter=ellipsePerimeter;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="225" y="30" width="200" height="60" as="geometry"/></mxCell>
    <mxCell id="e_start_p1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="start" target="p1"><mxGeometry relative="1" as="geometry"/></mxCell>
    <!-- Process: Read Input -->
    <mxCell id="p1" value="Read Input" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="225" y="170" width="200" height="60" as="geometry"/></mxCell>
    <mxCell id="e_p1_dec" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="p1" target="dec"><mxGeometry relative="1" as="geometry"/></mxCell>
    <!-- Decision: Valid? -->
    <mxCell id="dec" value="Valid?" style="rhombus;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;perimeter=rhombusPerimeter;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="250" y="300" width="150" height="80" as="geometry"/></mxCell>
    <!-- Yes branch (right side) — waypoints through mid-column corridor -->
    <mxCell id="e_dec_yes" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=1;exitY=0.5;entryX=0;entryY=0.5" edge="1" parent="1" source="dec" target="p2" value="Yes">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="440" y="340"/>
          <mxPoint x="440" y="490"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <!-- No branch (left side) — waypoints through mid-column corridor -->
    <mxCell id="e_dec_no" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=0;exitY=0.5;entryX=0.5;entryY=0" edge="1" parent="1" source="dec" target="p3" value="No">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="210" y="340"/>
          <mxPoint x="210" y="490"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <!-- Process: Process Data (Yes path) -->
    <mxCell id="p2" value="Process Data" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="460" y="460" width="200" height="60" as="geometry"/></mxCell>
    <!-- Process: Fix & Retry (No path) -->
    <mxCell id="p3" value="Fix &amp; Retry" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="50" y="460" width="200" height="60" as="geometry"/></mxCell>
    <!-- Rejoin to Output -->
    <mxCell id="e_p2_out" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="p2" target="out"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="e_p3_out" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="p3" target="out"><mxGeometry relative="1" as="geometry"/></mxCell>
    <!-- Output Result -->
    <mxCell id="out" value="Output Result" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="225" y="600" width="200" height="60" as="geometry"/></mxCell>
    <mxCell id="e_out_end" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="out" target="end"><mxGeometry relative="1" as="geometry"/></mxCell>
    <!-- End -->
    <mxCell id="end" value="End" style="ellipse;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;perimeter=ellipsePerimeter;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="275" y="720" width="100" height="50" as="geometry"/></mxCell>
  </root>
</mxGraphModel>
```

**Key patterns to copy:**
- Spine nodes (start/p1/dec/out/end) centered at x=225-275
- Decision rhombus at center, Yes branch goes RIGHT, No branch goes LEFT
- Both branches rejoin at the output node
- **Branch edges MUST use waypoints** through mid-column corridors, NOT direct diagonals.
  Use `exitX=1;exitY=0.5` + waypoints for right branches, `exitX=0;exitY=0.5` for left.
  Waypoint x = (spine_x + branch_x) / 2, creating a clean orthogonal route.
- Simple same-region edges (no column crossing) use exitX/exitY only, no waypoints needed
- Edge labels "Yes"/"No" set via `value` attribute on edge
- `perimeter=rhombusPerimeter` and `perimeter=ellipsePerimeter` required for non-rect shapes


**Example node table** (3-step process with one decision):

```
id     | label             | x   | y   | w   | h   | style
start  | Start             | 225 | 30  | 200 | 60  | ellipse green
p1     | Read Input        | 225 | 200 | 200 | 60  | process blue
dec    | Valid?            | 250 | 360 | 150 | 80  | decision yellow
p2     | Process Data      | 100 | 510 | 200 | 60  | process blue (left branch)
p3     | Fix & Retry       | 350 | 510 | 200 | 60  | process blue (right branch)
out    | Output Result     | 225 | 680 | 200 | 60  | process blue
end    | End               | 275 | 810 | 100 | 50  | ellipse green
```

**Edges:** start→p1→dec. dec→p2 ("Yes", exitX=0;exitY=0.5),
dec→p3 ("No", exitX=1;exitY=0.5). p2→out (exitX=1;exitY=0.5, bends
back center). p3→out (exitX=0;exitY=0.5, bends back center). out→end.



---

## §7 Entity-Relationship Diagram (ERD)

**When to use:** Database schemas, data models, table relationships,
SQL schema documentation.

**Canvas:** 800×600. TB layout. Tables stacked vertically with FK
relationship lines between them.

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Table container | `shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;strokeColor=#6C8EBF;fillColor=#DAE8FC` |
| Table row (column) | `shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontSize=12` — parent = table container ID |
| PK column | `fontStyle=1` (bold) on the row. Prefix label with `PK` or a key icon. |

**Layout conventions:**
- 3–7 tables, vertically stacked or arranged in 2 columns.
- Table width ~220px, row height ~26px.
- Gap between tables: 300px horizontal, 150px vertical.
- Entity relationships drawn as edges between table containers.
- FK → PK: `endArrow=ERmandOne;startArrow=ERmandOne;` with
  `exitX=0;exitY=0.5;entryX=1;entryY=0.5` or the reverse.
- For cardinality annotations, add a small label on the edge:
  `value="1"` at one end, `value="*"` at the other.

**Edge style (ER):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=ERmandOne;startArrow=ERmandOne;strokeColor=#333333;strokeWidth=1.5
```



---

## §8 UML Class Diagram

**When to use:** Object-oriented design papers, architecture
modeling, inheritance/interface hierarchies.


**Canvas:** 800×700. TB layout. Classes as swimlane boxes with 3
compartments (name / attributes / methods).

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Class box | `swimlane;startSize=26;fontStyle=1;align=center;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Times New Roman` |
| Separator line | `line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest` — placed between sections |
| Inheritance (→) | `endArrow=block;endFill=0` — hollow triangle |
| Composition (◆─) | `endArrow=diamondThin;endFill=1` — filled diamond |
| Aggregation (◇─) | `endArrow=diamondThin;endFill=0` — hollow diamond |
| Realization (dashed →) | `endArrow=block;endFill=0;dashed=1` — dashed hollow triangle |

**Layout conventions:**
- 4–8 classes vertically stacked or arranged in a column.
- Class width ~250px, height auto-fits content (~120-200px for 3-4
  attributes + 3-4 methods).
- Gap between classes: 200px TB, 280px LR.
- Superclasses above subclasses (inheritance arrows point UP).
- **Off-center subclasses use mid-column waypoints** for clean routing
  (e.g., WeChatPay at x=560, Payment at x=300 -> waypoint at x=410 midway).
  Same corridor principle as flowchart and org chart.
- Composition/aggregation edges connect the containing class to the
  contained class with the diamond at the container end.

**Edge style base:**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#333333;strokeWidth=1.5
```



---

## §9 Sequence Diagram

**When to use:** Protocol handshakes, API call chains, message-passing
between actors/objects — any interaction where time flows top-to-bottom
and participants are shown as vertical lifelines.


**Canvas:** 900×700. LR layout (actors placed horizontally).

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Actor/Object header | `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;fillColor=#DAE8FC;strokeColor=#6C8EBF;size=40;fontFamily=Times New Roman;fontStyle=1;fontSize=12` |
| Activation box | `rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5` — narrow (w=16) rectangles placed on the lifeline |
| Sync message (→) | `endArrow=block;endFill=1` — solid filled arrow |
| Async message (→>) | `endArrow=open;dashed=1` — dashed open arrow |
| Return/Reply (<--) | `endArrow=open;dashed=1;strokeColor=#999999` — grey dashed |
| Self-call | `endArrow=block;curved=1` — loops back to same lifeline |

**Layout conventions:**
- 3-6 lifelines, evenly spaced at x=80, x=280, x=480, x=680, ...
- Lifelines start at y=80 with the actor header box.
- Vertical dashed lines extend from the header down to the last message
  (these are auto-rendered by the `umlLifeline` shape).
- **Time flows top-to-bottom** — the first message is at y=120, the next
  at y=180, etc., incrementing by ~60px per message.
- Activation boxes (w=16) are placed on the lifeline starting at the
  message entry y, ending at the reply y.
- Message labels sit above the arrow line.

**Edge style (sync message):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor=#333333;strokeWidth=1.5
```

**Edge style (return):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;dashed=1;strokeColor=#999999;strokeWidth=1.5
```

**Minimal X positions for 4 participants:**
```
Participant  | x    | w   | h
Client       | 40   | 60  | 40 (header), then lifeline auto-extends
API Gateway  | 240  | 60  | 40
Service      | 440  | 60  | 40
DB           | 640  | 60  | 40
```



---

## §10 State Machine Diagram

**When to use:** State transition specifications, protocol state
machines, embedded system modes, formal-method visualizations.


**Canvas:** 800×650. Variable layout — states can be arranged
horizontally (LR) or in a circle depending on transition count.

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| State | `rounded=1;arcSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle` — rounded rect, blue |
| Initial state (●) | `ellipse;fillColor=#333333;strokeColor=#333333` — filled black circle, w=20 h=20 |
| Final state (◎) | `ellipse;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=2.5` — double circle: outer ellipse w=30 h=30 filled white, inner filled black ellipse w=16 h=16 |
| Transition | Edge with `edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=classic` |
| Self-transition | `curved=1;exitX=0;exitY=0.5;entryX=0;entryY=0.8` — loops from state left side back to itself |
| Choice/Junction (●) | `rhombus;fillColor=#FFF2CC;strokeColor=#D6B656` — yellow diamond |

**Edge label:** `value="event / action"` on the transition edge
(e.g., "e_acc_on / init()").

**Layout conventions:**
- 4–8 states arranged in a natural reading order (LR or TB).
- Initial state (small black circle) connects to the first state via
  an arrow with no label.
- Final state (bullseye) is reached from terminal transitions.
- Distribute states with 250-300px spacing for readability.
- Self-transitions use `curved=1` with exit/entry both on the same
  side of the state (left side, y=0.5 and y=0.8).

**Edge style (transition):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333
```


**Golden self-loop example (visible with waypoints):**

```xml
<mxCell id="e_tick" value="tick / update()"
  style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;curved=1;exitX=0;exitY=0.5;entryX=0;entryY=0.75"
  edge="1" parent="1" source="running" target="running">
  <mxGeometry relative="1" x="0.2" y="-15" as="geometry">
    <Array as="points">
      <mxPoint x="350" y="215"/>
      <mxPoint x="350" y="235"/>
    </Array>
  </mxGeometry>
</mxCell>
```

**Key pattern:** waypoints pull the loop OUT from the node.
For a node at (nx, ny, nw, nh), two patterns work:
- Left-side: exit left, arc down and back (wp1=nx-40,ny-10; wp2=nx-40,ny+nh+10)
- Right-side box: exit right, go up, go left above node, curve back
  (wp1=nx+nw-56,ny-60; wp2=nx+nw+24,ny-60; wp3=nx+nw+24,ny-120; wp4=nx-93,ny-120)
Without waypoints, `curved=1` alone produces an invisible node-hugging arc.

**Edge style (self-loop):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;curved=1;exitX=0;exitY=0.5;entryX=0;entryY=0.2
```



---

## §11 Data Flow Diagram (DFD)

**When to use:** Software engineering papers, system analysis — showing
how data moves through processes and stores. Distinct from a flowchart:
DFD shows **data movement**, not control flow.

**Canvas:** 800×600. Variable layout — processes form the center, external
entities on the edges, data stores at the bottom.

**Shape vocabulary:**

| Element | Style keywords | Visual |
|---|---|---|
| Process | `ellipse;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5` | Blue circle/ellipse |
| External Entity | `rounded=1;arcSize=8;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5` | Red rounded rect (source/sink of data) |
| Data Store | `shape=partialRectangle;whiteSpace=wrap;html=1;fillColor=#FFF9C4;strokeColor=#F9A825;bottom=0;right=0;top=0;left=0;strokeWidth=1.5` or `rounded=0;fillColor=#FFF9C4;strokeColor=#F9A825;strokeWidth=1.5` + two parallel horizontal lines | Yellow open-ended box |
| Data Flow | Edge with `endArrow=classic` | Solid arrow with data label |

**All element styles** include: `fontFamily=Times New Roman;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle`

**Layout conventions:**
- Processes numbered (P1, P2, P3) with a brief verb-noun label.
- External entities placed around the edges (top-left, top-right,
  bottom corners).
- Data stores at the bottom center.
- Data flow edges are labeled with the data being moved
  (e.g. `value="Customer Data"`, `value="Validation Result"`).
- Processes form the central hub — position them evenly across the canvas.
  Off-center external entities or stores should balance the layout.
  Processes at same y share same height for clean horizontal alignment. — data flows IN from entities,
  is transformed by processes, and flows OUT to stores or entities.
- Spacing: 200-300px between processes.

**Edge style (data flow):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333
```

**4-process example layout:**

```
id     | label               | x   | y   | w   | h   | shape
ent1   | Customer            | 40  | 80  | 120 | 60  | entity (red rounded)
ent2   | Warehouse           | 640 | 80  | 120 | 60  | entity
p1     | 1. Validate Order   | 280 | 100 | 150 | 70  | process (blue ellipse)
p2     | 2. Check Inventory  | 280 | 240 | 150 | 70  | process
p3     | 3. Ship Order       | 280 | 380 | 150 | 70  | process
store1 | Orders DB           | 160 | 480 | 120 | 50  | data store (yellow)
store2 | Inventory DB        | 520 | 480 | 120 | 50  | data store
```

Edges: ent1→p1 ("Order"), p1→p2 ("Validated Order"), p2→p3
("Available Qty"), p3→ent2 ("Shipping Label"). p1↔store1
("Order Record"), p2↔store2 ("Stock Level").


---

## §12 Network Topology

**When to use:** Network architecture diagrams — LAN/WAN layouts, router/switch
hierarchies, cloud infrastructure, subnet boundaries.

**Canvas:** 900×650. Central routers/switches with connected subnets.

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Router | `rounded=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2` |
| Switch | `rounded=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2` |
| Firewall | `rounded=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=2` |
| Subnet/VLAN container | `rounded=1;dashed=1;dashPattern=10 4;fillColor=#F5F5F5;strokeColor=#BDBDBD` |
| Server | `rounded=1;fillColor=#D5E8D4;strokeColor=#82B366` |
| Workstation | `rounded=1;fillColor=#E3F2FD;strokeColor=#64B5F6` |
| WAN/Internet cloud | `shape=cloud;fillColor=#ECEFF1;strokeColor=#90A4AE` |

**Layout conventions:**
- WAN cloud at top, core routers below it, then distribution switches,
  then access switches, then endpoints
- Each subnet inside a dashed container with a label
- Backbone links: `strokeWidth=2.5;strokeColor=#333333`
- Access links: `strokeWidth=1;strokeColor=#666666`
- Vertical gap between tiers: 100-120px

**To adapt:** change device labels, subnet names, and connection counts.

**Routing pattern:** off-center switch->subnet connections use a horizontal bus
at `y = (switch.bottom + subnet.top) / 2`. Same corridor pattern as org chart.
Example: switch at x=450, web at x=600 -> bus at y=380, waypoints (450,380)->(600,380).
Add/remove firewall, load balancer, or IDS/IPS blocks as needed.

---

## §13 Org Chart / Mind Map

**When to use:** Organization hierarchies, file-system trees, concept
mind maps — any tree structure where one root has children at multiple
levels.

**Canvas:** 900×700. TB tree (root at top) or LR tree (root at left).

**Layout conventions:**
- Root node at top-center (TB) or left-center (LR)
- Each level at a consistent y (TB) or x (LR)
- Children spaced evenly under/next to their parent
- Connecting lines: orthogonal, one line from parent center to a
  horizontal bar, then branches down/right to each child

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Root node | `rounded=1;fillColor=#37474F;strokeColor=#333333;fontColor=#FFFFFF;fontStyle=1;strokeWidth=2` |
| Branch node | `rounded=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5` |
| Leaf node | `rounded=1;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1` |

**Edge style:**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;
jettySize=auto;html=1;endArrow=none;strokeColor=#999999;strokeWidth=1.5
```

Vertical gap between levels: 120px. Horizontal spread: children spaced
240px apart center-to-center.

**Routing pattern:** off-center parent→child edges use a HORIZONTAL BUS at
`y = (parent.bottom + child.top) / 2`. Center-positioned child uses direct
vertical (no waypoints). This prevents diagonal lines crossing other nodes.
Example: CEO at x=450, VP Eng at x=140 → bus at y=140, waypoints (450,140)→(140,140).

**To adapt:** change labels, add/remove levels, switch TB to LR by
swapping x/y logic.

**Golden XML example (3-level org chart, top-down tree):**

```xml
<mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="700" math="0" shadow="0">
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <!-- Root (level 0) -->
    <mxCell id="root" value="&lt;b&gt;CEO&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#37474F;strokeColor=#333333;fontColor=#FFFFFF;fontStyle=1;strokeWidth=2;fontFamily=Times New Roman;fontSize=13;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="330" y="40" width="240" height="60" as="geometry"/></mxCell>
    <!-- Level 1: VPs -->
    <mxCell id="vp1" value="&lt;b&gt;VP Engineering&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="50" y="180" width="200" height="60" as="geometry"/></mxCell>
    <mxCell id="e_r_vp1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#999999;strokeWidth=1.5" edge="1" parent="1" source="root" target="vp1"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="vp2" value="&lt;b&gt;VP Product&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="350" y="180" width="200" height="60" as="geometry"/></mxCell>
    <mxCell id="e_r_vp2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#999999;strokeWidth=1.5" edge="1" parent="1" source="root" target="vp2"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="vp3" value="&lt;b&gt;VP Sales&lt;/b&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="650" y="180" width="200" height="60" as="geometry"/></mxCell>
    <mxCell id="e_r_vp3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#999999;strokeWidth=1.5" edge="1" parent="1" source="root" target="vp3"><mxGeometry relative="1" as="geometry"/></mxCell>
    <!-- Level 2: Directors under VP Eng -->
    <mxCell id="dir1" value="Director&lt;br&gt;Frontend" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="10" y="330" width="130" height="50" as="geometry"/></mxCell>
    <mxCell id="e_vp1_dir1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#999999;strokeWidth=1.5" edge="1" parent="1" source="vp1" target="dir1"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="dir2" value="Director&lt;br&gt;Backend" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="170" y="330" width="130" height="50" as="geometry"/></mxCell>
    <mxCell id="e_vp1_dir2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#999999;strokeWidth=1.5" edge="1" parent="1" source="vp1" target="dir2"><mxGeometry relative="1" as="geometry"/></mxCell>
  </root>
</mxGraphModel>
```

**Key patterns to copy:**
- Root node: dark fill + white text + strokeWidth=2 for visual dominance
- Level 1 (branch): IEEE blue fill, level 2 (leaf): white fill with grey border
- Children under a parent: x = parent_x + offset_from_parent_center
- Vertical gap: 140px between levels
- Edge style: `endArrow=none` for hierarchy lines (not data flow)




---

## §14 Timeline / Gantt Chart

**When to use:** Project roadmaps, historical sequences, process phases,
milestone overviews — any time-ordered sequence of events.

**Canvas:** 1000×400. LR flow with time markers.

**Layout conventions:**
- Horizontal time axis at the top, marked with dates/phases
- Events as rounded boxes below the axis, centered on their time position
- Milestones as diamond markers on the axis
- Dependency arrows between events (optional)
- "Today" marker as a vertical dashed line (optional)

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Time axis | Horizontal line: `endArrow=none;strokeColor=#333333;strokeWidth=1.5` |
| Event / Phase box | `rounded=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5` |
| Milestone | `rhombus;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5` |
| Today marker | Vertical dashed: `dashed=1;dashPattern=8 4;strokeColor=#E53935` |
| Dependency arrow | `endArrow=classic;strokeColor=#999;strokeWidth=1;dashed=1` |

Stagger y positions to avoid label collisions for overlapping phases.
- **Spacing**: events spaced 180-220px apart horizontally (not tightly packed).
  Wider spacing prevents label overlap and improves readability.

**To adapt:** change time span, event labels, and y staggering pattern.

---

## §15 Venn Diagram / Set Relations

**When to use:** Set intersection/union, overlapping categories, shared
properties between groups — classic 2-4 circle Venn diagrams.

**Canvas:** 700×600. Circles centered for optimal overlap.

**Layout conventions:**
- 2 circles: centers spaced ~40% of radius apart
- 3 circles: equilateral triangle of centers
- 4 circles: use elliptical shapes for all-region visibility, or Euler
  diagram (only show existing intersections)
- Labels in the non-overlapping regions and intersection centers
- Circle fill with high transparency (`opacity=30-40`)

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Circle | `ellipse;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2;opacity=35` |
| Region label | `text;html=1;fontSize=11;fontFamily=Times New Roman;align=center` |
| Set title | `text;html=1;fontSize=14;fontFamily=Times New Roman;fontStyle=1;align=center` |

Region labels placed at geometric centers of each intersection zone.

**To adapt:** change set labels, circle sizes, colors. Use 2 or 3 circles
for readability. For 4+ sets, use Euler approximation.

---

## §16 Conceptual Coordinate Framework

**When to use:** 2×2 matrices, technology maturity curves, BCG matrices,
hype cycles, positioning maps — any diagram using a coordinate space
(two axes) to position conceptual entities (NOT data points).

Distinct from a matplotlib scatter plot: these frameworks use labeled
zones ("Stars", "Cash Cows", "Question Marks", "Dogs") rather than
numerical data. The diagram shows *categories* positioned conceptually,
not data points plotted from measurements.

**Canvas:** 750×650. Two perpendicular axes forming four quadrants.

**Layout conventions:**
- Horizontal axis (e.g., "Market Share" — low to high)
- Vertical axis (e.g., "Market Growth" — low to high)
- Axes intersect at center. Labels at both ends of each axis.
- Quadrants labeled at the center of each zone
- Entities placed as labeled circles at their conceptual positions
- Optional: quadrant background colors to distinguish zones

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Axis line | `endArrow=classic;strokeColor=#333333;strokeWidth=2` |
| Axis label | `text;fontSize=12;fontStyle=1` |
| Quadrant zone | `rounded=0;fillColor=...;opacity=15;strokeColor=none` (behind axes) |
| Entity | `ellipse;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1.5` with text label |
| Zone label | `text;fontSize=14;fontStyle=1;fontColor=#666666` |

**To adapt:** change axis labels, quadrant labels, entity names and
positions. For a technology maturity curve, use a single S-curve line
instead of four quadrants.

---

## §17 Swimlane Diagram

> **Capability note:** Hand-written draw.io XML for swimlanes is inherently
> error-prone — parent-child nesting, cross-lane edge routing, and lane
> responsibility logic often produce spaghetti on first attempt. The
> check-refine loop helps but has a hard 3-iteration cap. Keep diagrams
> simple — split complex cases across multiple pages.

**When to use:** Cross-functional process flows, responsibility matrices,
RACI charts — any process where tasks execute across multiple actors,
departments, or systems. Each lane represents one actor.

**Canvas:** 1100×650 landscape. Lanes run horizontally; flow is
left-to-right within lanes, top-to-bottom between lanes.

### Critical: use native swimlane shapes, NOT rectangles

draw.io has a built-in swimlane container shape. Use it. Do NOT draw
swimlanes as colored rectangles with absolute-positioned child nodes.



Key points:
- Lane: , absolute x/y on the root canvas.
- Child nodes: , coordinates RELATIVE to the lane
  top-left corner (x=0,y=0 is inside the lane).
- Connectors between lanes:  (root level), orthogonal routing.
- Moving/deleting a lane moves/deletes all its children automatically.

### Shape vocabulary

| Element | Style | When |
|---|---|---|
| Lane | `swimlane;startSize=30;horizontal=0;container=1;pointerEvents=0;fillColor=#F5F5F5;strokeColor=#999999;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1` | One per actor |
| Start | `ellipse;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;perimeter=ellipsePerimeter` | Leftmost in first lane |
| End | `ellipse;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;perimeter=ellipsePerimeter` | One per terminal |
| Process | `rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1` | White fill, stroke=owning lane color |
| Decision | `rhombus;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;perimeter=rhombusPerimeter` | 1 input, 2 outputs |

### Lane color palette (official draw.io pastels)

| Role | Lane fill | Lane stroke | Node stroke |
|------|-----------|-------------|-------------|
| Customer/Client | `#FCE4EC` | `#B85450` | `#B85450` |
| Internal system | `#E3F2FD` | `#6C8EBF` | `#6C8EBF` |
| Payment/Finance | `#F3E5F5` | `#9673A6` | `#9673A6` |
| Warehouse/Ops | `#E8F5E9` | `#82B366` | `#82B366` |
| External partner | `#FFF3E0` | `#D79B00` | `#D79B00` |
| Generic | `#F5F5F5` | `#999999` | `#999999` |

### Flow direction rules

1. **Default: top-to-bottom between lanes.** Lane 1 at smallest y, Lane N at
   largest y. Responsibility flows downward.
2. **Within a lane: left-to-right.** Nodes ordered by time — earliest at
   smallest x. Every forward edge: .
3. **Decision: 1 input, 2 outputs.** "Yes" branch goes RIGHT and down to
   the next lane. "No" branch goes RIGHT to a terminal in the same lane
   or arcs down to a cancel node in the responsible system lane.
4. **Terminals: no outgoing edges.** Start has 0 inputs. End/Cancel has
   0 outputs.

### Color continuity

After a decision, every edge on the "Yes" branch stays green ()
until terminal. Every edge on the "No" branch stays orange ()
until cancel. Do not revert to black mid-branch.

### Lane responsibility

Nodes belong in the lane of the performer:
- "Order Cancelled" = Order System lane, NOT Customer lane.
- Payment decision "Success?" = Payment Gateway lane.

### Business logic validation (Phase 1)

Before writing XML:
1. List all nodes in time order. Correct sequence?
2. Trace each branch to a terminal. Dead ends?
3. After "Cancelled", are there more steps? (There should not be.)
4. "Confirm" must follow payment success, not precede it.
5. Each node in the right performer lane?

### Layout conventions

- Lane height: **equal for all lanes** (130-160px). The lane with the
  decision diamond determines the height for all.
- Within-lane x-spacing: 100-150px between process nodes.
- Node y-position within lane: centered vertically. For a 160px lane,
  process nodes (h=50) go at y=55-60.
- Connectors: , .

**To adapt:** change lane labels, node text, decision logic. Keep the
swimlane shape, parent-child nesting, and flow direction rules intact.
## §18 Wireframe / Mockup

**When to use:** App screens, website layouts, dashboard designs, UI
prototypes — any user-facing interface mockup before development.

**Canvas:** 600×900 portrait (mobile) or 1024×768 landscape (desktop).

**Layout conventions:**
- Outer frame = device/screen boundary
- Top bar: navigation / header (h=50-60px)
- Content area: main body, can be subdivided
- Bottom bar: tab bar / footer (h=50-60px)
- Sidebar (desktop): left column w=200-250px
- Placeholder rectangles for images, text blocks, buttons

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Screen frame | `rounded=1;arcSize=12;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=2.5` |
| Header bar | `rounded=0;fillColor=#37474F;strokeColor=#333333;strokeWidth=1` — dark bar |
| Content area | `rounded=1;arcSize=4;fillColor=#F5F5F5;strokeColor=#E0E0E0;strokeWidth=1` |
| Button | `rounded=1;arcSize=20;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF` |
| Image placeholder | `rounded=1;arcSize=6;fillColor=#E0E0E0;strokeColor=#BDBDBD;strokeWidth=1;dashed=1` — with "×" or "img" label |
| Text block | `rounded=0;fillColor=#E0E0E0;strokeColor=none` — thin horizontal bars of varying widths |
| Tab bar | `rounded=0;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1` — bottom strip with icon placeholders |
| Card | `rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;shadow=1` |

**Layout conventions:**
- Screen frame centered on canvas
- Internal elements use parent-child containment (relative coords)
- All text in sans-serif (Arial/Helvetica), 10-14px
- Use grey rectangles of varying widths to simulate text lines
- Images: dashed-border rectangles with centered "img" label

**To adapt:** change screen dimensions, add/remove UI elements, adjust
layout for mobile vs desktop.

---

## §19 Cross-Functional Table (Actor × Phase Grid)

**When to use:** Cross-functional flowcharts showing process steps across
TWO axes - actors (rows) and phases (columns). Distinct from swimlanes
(one axis only).

**Canvas:** 900x320 per ~3 rows. Scale width for more phases.

**Layout conventions:**
- Outer container uses `shape=table;childLayout=tableLayout`
- Rows: `shape=tableRow` children of the table
- Cells: children of rows - one per (actor, phase) intersection
- First row = phase headers; first cell of data rows = actor label
- Process nodes go INSIDE cells at relative coords
- Cross-cell edges use `parent="1"`

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Table | `shape=table;childLayout=tableLayout;startSize=0;collapsible=0;fillColor=none;` |
| Row | `shape=tableRow;horizontal=0;startSize=0;collapsible=0;` |
| Header cell | `text;align=center;fontStyle=1;fillColor=#e8e8e8;` |
| Actor label | `fillColor=#dae8fc;fontStyle=1;` |
| Body cell | `fillColor=none;` (transparent, just a container) |
| Process node | `rounded=1;whiteSpace=wrap;html=1;` |

**Example (2 actors x 2 phases):**

```xml
<mxCell id="tbl" style="shape=table;childLayout=tableLayout;startSize=0;collapsible=0;fillColor=none;" vertex="1" parent="1">
  <mxGeometry x="0" y="0" width="900" height="320" as="geometry"/>
</mxCell>
<mxCell id="r0" style="shape=tableRow;horizontal=0;startSize=0;collapsible=0;" vertex="1" parent="tbl">
  <mxGeometry width="900" height="40" as="geometry"/>
</mxCell>
<mxCell id="h0" style="text;html=1;" vertex="1" parent="r0">
  <mxGeometry width="140" height="40" as="geometry"/>
</mxCell>
<mxCell id="h1" value="Order" style="text;align=center;fontStyle=1;fillColor=#e8e8e8;" vertex="1" parent="r0">
  <mxGeometry x="140" width="380" height="40" as="geometry"/>
</mxCell>
<mxCell id="h2" value="Fulfill" style="text;align=center;fontStyle=1;fillColor=#e8e8e8;" vertex="1" parent="r0">
  <mxGeometry x="520" width="380" height="40" as="geometry"/>
</mxCell>
<mxCell id="r1" style="shape=tableRow;horizontal=0;startSize=0;collapsible=0;" vertex="1" parent="tbl">
  <mxGeometry y="40" width="900" height="140" as="geometry"/>
</mxCell>
<mxCell id="a1" value="Customer" style="fillColor=#dae8fc;fontStyle=1;" vertex="1" parent="r1">
  <mxGeometry width="140" height="140" as="geometry"/>
</mxCell>
<mxCell id="c11" style="fillColor=none;" vertex="1" parent="r1">
  <mxGeometry x="140" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="n_place" value="Place Order" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="c11">
  <mxGeometry x="120" y="40" width="140" height="60" as="geometry"/>
</mxCell>
<mxCell id="c12" style="fillColor=none;" vertex="1" parent="r1">
  <mxGeometry x="520" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="r2" style="shape=tableRow;horizontal=0;startSize=0;collapsible=0;" vertex="1" parent="tbl">
  <mxGeometry y="180" width="900" height="140" as="geometry"/>
</mxCell>
<mxCell id="a2" value="System" style="fillColor=#d5e8d4;fontStyle=1;" vertex="1" parent="r2">
  <mxGeometry width="140" height="140" as="geometry"/>
</mxCell>
<mxCell id="c21" style="fillColor=none;" vertex="1" parent="r2">
  <mxGeometry x="140" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="n_validate" value="Validate" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="c21">
  <mxGeometry x="120" y="40" width="140" height="60" as="geometry"/>
</mxCell>
<mxCell id="c22" style="fillColor=none;" vertex="1" parent="r2">
  <mxGeometry x="520" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="n_ship" value="Ship" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="c22">
  <mxGeometry x="120" y="40" width="140" height="60" as="geometry"/>
</mxCell>
<mxCell id="e1" edge="1" parent="1" source="n_place" target="n_validate" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="e2" edge="1" parent="1" source="n_validate" target="n_ship" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

**To adapt:** change actor labels, phase names, process node text. Keep the
table/row/cell structure intact.


---

## §20 Transformer encoder-decoder (Vaswani 2017)

**Canvas:** 920×870, portrait. Encoder on the left, decoder on the right,
output stack above the decoder, source input below the encoder, target input
below the decoder.

**Edge convention:** All edges use the orthogonal routing base from
`drawio-reference.md` — `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic`.
Residuals add `dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1`.
K,V cross-attention adds `exitX=1;entryX=0;strokeColor=#9673A6`.

**Layout choices that prevent overlap:**

1. Output stack and input groups (3 modules each) have NO dashed container —
   they're floating with color-coding doing the grouping work.
2. Encoder and decoder containers exist (because of `× N` annotation), with
   labels placed INSIDE the container at top-left, not above.
3. Encoder bottom (y=650) is LOWER than decoder bottom (y=590) because the
   encoder is shorter but its TOP aligns with decoder cross-attention. This
   makes K,V cross-attention a clean straight horizontal line and is
   Vaswani's actual layout choice.
4. ≥30px clear gap between every section: linear → decoder (32), encoder →
   source-input (30), decoder → target-input (30).

**Self-check** (before writing):
1. All forward edges: `source.y > target.y` ✓
2. enc_an2 center y (435) == dec_ca center y (435) → K,V straight horizontal ✓
3. Encoder modules inside enc_sec with ≥10px padding. Same for decoder ✓
4. Section gaps: linear→dec(32), enc→src(30), dec→tgt(30) — all ≥30 ✓
5. All coords x/y/w multiples of 10; heights use 30/32/38/42/50 ✓

**Node table** (data-flow order; y decreases as you go up the stack):

```
SECTION       | id          | label                          | x   | y   | w   | h
output        | outp        | Output Probabilities           | 540 | 20  | 340 | 42
output        | softmax     | Softmax                        | 600 | 80  | 220 | 38
output        | linear      | Linear                         | 600 | 140 | 220 | 38
DECODER       | dec_sec     | (container)                    | 520 | 210 | 380 | 380
DECODER       | dec_lbl     | "Decoder × N" (inside top-left)| 530 | 216 | 200 | 16
DECODER       | dec_an3     | Add & Norm                     | 540 | 240 | 340 | 30
DECODER       | dec_ff      | Feed Forward                   | 540 | 290 | 340 | 50
DECODER       | dec_an2     | Add & Norm                     | 540 | 360 | 340 | 30
DECODER       | dec_ca      | Multi-Head Cross-Attention     | 540 | 410 | 340 | 50  ← center y=435
DECODER       | dec_an1     | Add & Norm                     | 540 | 480 | 340 | 30
DECODER       | dec_mmha    | Masked Multi-Head Self-Attn    | 540 | 530 | 340 | 50
ENCODER       | enc_sec     | (container)                    | 40  | 390 | 320 | 260
ENCODER       | enc_lbl     | "Encoder × N" (inside top-left)| 50  | 396 | 200 | 16
ENCODER       | enc_an2     | Add & Norm                     | 60  | 420 | 280 | 30  ← center y=435
ENCODER       | enc_ff      | Feed Forward                   | 60  | 470 | 280 | 50
ENCODER       | enc_an1     | Add & Norm                     | 60  | 540 | 280 | 30
ENCODER       | enc_mha     | Multi-Head Self-Attention      | 60  | 590 | 280 | 50
src_input     | src_pos     | Positional Encoding            | 60  | 680 | 280 | 32
src_input     | src_emb     | Input Embedding                | 60  | 730 | 280 | 38
src_input     | src_tk      | Source Tokens                  | 60  | 790 | 280 | 42
tgt_input     | tgt_pos     | Positional Encoding            | 540 | 620 | 340 | 32
tgt_input     | tgt_emb     | Output Embedding               | 540 | 670 | 340 | 38
tgt_input     | tgt_tk      | Target Tokens (shifted right)  | 540 | 730 | 340 | 42
KV label      | kv_lbl      | "K, V"                         | 420 | 412 | 40  | 16
```

**Edge table** (every forward edge satisfies `source.y > target.y`):

```
id          | source     | target     | style                                   | notes
e_tk_emb_s  | src_tk     | src_emb    | solid black                             | input flow ↑
e_emb_pos_s | src_emb    | src_pos    | solid black                             |
e_pos_enc   | src_pos    | enc_mha    | solid black                             | enters encoder bottom
e_e_mha_an1 | enc_mha    | enc_an1    | solid black                             | encoder stack ↑
e_e_an1_ff  | enc_an1    | enc_ff     | solid black                             |
e_e_ff_an2  | enc_ff     | enc_an2    | solid black                             |
e_kv        | enc_an2    | dec_ca     | colored, exitX=1;exitY=0.5;entryX=0;entryY=0.5 | straight horizontal (centers both 435)
e_tk_emb_t  | tgt_tk     | tgt_emb    | solid black                             | target input ↑
e_emb_pos_t | tgt_emb    | tgt_pos    | solid black                             |
e_pos_dec   | tgt_pos    | dec_mmha   | solid black                             | enters decoder bottom
e_d_mha_an1 | dec_mmha   | dec_an1    | solid black                             | decoder stack ↑
e_d_an1_ca  | dec_an1    | dec_ca     | solid black                             |
e_d_ca_an2  | dec_ca     | dec_an2    | solid black                             |
e_d_an2_ff  | dec_an2    | dec_ff     | solid black                             |
e_d_ff_an3  | dec_ff     | dec_an3    | solid black                             |
e_dec_lin   | dec_an3    | linear     | solid black                             | decoder → output
e_lin_sm    | linear     | softmax    | solid black                             | output stack ↑
e_sm_outp   | softmax    | outp       | solid black                             |
```

Residuals: dashed thin gray, `exitX=0;exitY=0.5;entryX=0;entryY=0.5` for
encoder (waypoints at x=45, inside container left edge), and
`exitX=1;exitY=0.5;entryX=1;entryY=0.5` for decoder (waypoints at x=895,
inside container right edge). One residual per (sub-layer → its Add&Norm).

**Self-check after instantiating:**
1. For every adjacent pair in the data-flow order, verify `source.y > target.y`.
2. Encoder modules `bbox` fully inside `enc_sec` bbox with ≥10px padding on
   all sides. Same for decoder.
3. Section labels (`enc_lbl`, `dec_lbl`) inside their container, not above.
4. Output stack bottom (linear y+h = 178) and decoder top (210) have ≥30px
   gap. Same for encoder bottom / source input top, decoder bottom / target
   input top.
5. enc_an2 center y == dec_ca center y (both 435) so K,V is horizontal.

**XML skeleton** — copy this and adjust names/counts:

```xml
<mxfile host="app.diagrams.net">
  <diagram name="Transformer" id="transformer">
    <mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="920" pageHeight="870" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- ===== Output stack (top, no container) ===== -->
        <mxCell id="outp" value="Output Probabilities" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="20" width="340" height="42" as="geometry"/>
        </mxCell>
        <mxCell id="softmax" value="Softmax" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="600" y="80" width="220" height="38" as="geometry"/>
        </mxCell>
        <mxCell id="linear" value="Linear" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="600" y="140" width="220" height="38" as="geometry"/>
        </mxCell>

        <!-- ===== Decoder section (container y=210..590, label INSIDE top-left) ===== -->
        <mxCell id="dec_sec" value="" style="rounded=1;arcSize=6;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
          <mxGeometry x="520" y="210" width="380" height="380" as="geometry"/>
        </mxCell>
        <mxCell id="dec_lbl" value="Decoder  × N" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="1">
          <mxGeometry x="530" y="216" width="200" height="16" as="geometry"/>
        </mxCell>

        <!-- Decoder modules: top → bottom; data flows ↑ (smaller y is later in flow) -->
        <mxCell id="dec_an3" value="Add &amp; Norm" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=1;fontSize=11;fontFamily=Times New Roman;fontColor=#666666;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="240" width="340" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="dec_ff" value="Feed Forward" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="290" width="340" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="dec_an2" value="Add &amp; Norm" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=1;fontSize=11;fontFamily=Times New Roman;fontColor=#666666;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="360" width="340" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="dec_ca" value="Multi-Head Cross-Attention" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="410" width="340" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="dec_an1" value="Add &amp; Norm" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=1;fontSize=11;fontFamily=Times New Roman;fontColor=#666666;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="480" width="340" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="dec_mmha" value="Masked Multi-Head Self-Attention" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="530" width="340" height="50" as="geometry"/>
        </mxCell>

        <!-- ===== Encoder section (container y=390..650, enc_an2 center y=435 = dec_ca center y=435) ===== -->
        <mxCell id="enc_sec" value="" style="rounded=1;arcSize=6;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
          <mxGeometry x="40" y="390" width="320" height="260" as="geometry"/>
        </mxCell>
        <mxCell id="enc_lbl" value="Encoder  × N" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="1">
          <mxGeometry x="50" y="396" width="200" height="16" as="geometry"/>
        </mxCell>

        <mxCell id="enc_an2" value="Add &amp; Norm" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=1;fontSize=11;fontFamily=Times New Roman;fontColor=#666666;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="420" width="280" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="enc_ff" value="Feed Forward" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="470" width="280" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="enc_an1" value="Add &amp; Norm" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=1;fontSize=11;fontFamily=Times New Roman;fontColor=#666666;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="540" width="280" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="enc_mha" value="Multi-Head Self-Attention" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="590" width="280" height="50" as="geometry"/>
        </mxCell>

        <!-- ===== Source input (no container, BELOW encoder, ≥30px gap) ===== -->
        <mxCell id="src_pos" value="Positional Encoding" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="680" width="280" height="32" as="geometry"/>
        </mxCell>
        <mxCell id="src_emb" value="Input Embedding" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="730" width="280" height="38" as="geometry"/>
        </mxCell>
        <mxCell id="src_tk" value="Source Tokens (x&lt;sub&gt;1&lt;/sub&gt;, …, x&lt;sub&gt;n&lt;/sub&gt;)" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="60" y="790" width="280" height="42" as="geometry"/>
        </mxCell>

        <!-- ===== Target input (no container, BELOW decoder, ≥30px gap) ===== -->
        <mxCell id="tgt_pos" value="Positional Encoding" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="620" width="340" height="32" as="geometry"/>
        </mxCell>
        <mxCell id="tgt_emb" value="Output Embedding" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="670" width="340" height="38" as="geometry"/>
        </mxCell>
        <mxCell id="tgt_tk" value="Target Tokens (shifted right)" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1.5;fontSize=12;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="540" y="730" width="340" height="42" as="geometry"/>
        </mxCell>

        <!-- ===== EDGES — every forward edge has source.y > target.y ===== -->
        <mxCell id="e_stk_emb" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="src_tk" target="src_emb"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_semb_pos" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="src_emb" target="src_pos"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_spos_enc" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="src_pos" target="enc_mha"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_emha_an1" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="enc_mha" target="enc_an1"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ean1_ff" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="enc_an1" target="enc_ff"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_eff_an2" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="enc_ff" target="enc_an2"><mxGeometry relative="1" as="geometry"/></mxCell>
        <!-- K,V cross-attention: enc_an2 center y=435 = dec_ca center y=435, straight horizontal -->
        <mxCell id="e_kv" style="endArrow=classic;html=1;strokeColor=#9673A6;strokeWidth=1.5;exitX=1;exitY=0.5;entryX=0;entryY=0.5" edge="1" parent="1" source="enc_an2" target="dec_ca"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="kv_lbl" value="K, V" style="text;html=1;fontSize=10;fontFamily=Times New Roman;fontColor=#9673A6;fontStyle=2;align=center" vertex="1" parent="1">
          <mxGeometry x="420" y="412" width="40" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="e_ttk_emb" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="tgt_tk" target="tgt_emb"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_temb_pos" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="tgt_emb" target="tgt_pos"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_tpos_dec" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="tgt_pos" target="dec_mmha"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_dmha_an1" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="dec_mmha" target="dec_an1"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_dan1_ca" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="dec_an1" target="dec_ca"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_dca_an2" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="dec_ca" target="dec_an2"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_dan2_ff" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="dec_an2" target="dec_ff"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_dff_an3" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="dec_ff" target="dec_an3"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_dec_lin" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="dec_an3" target="linear"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_lin_sm" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="linear" target="softmax"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_sm_outp" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="softmax" target="outp"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Encoder residuals (left side, dashed thin, x=45 inside enc_sec) -->
        <mxCell id="e_ers1" style="endArrow=classic;html=1;dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1;exitX=0;exitY=0.5;entryX=0;entryY=0.5" edge="1" parent="1" source="enc_mha" target="enc_an1">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="45" y="615"/><mxPoint x="45" y="555"/></Array></mxGeometry>
        </mxCell>
        <mxCell id="e_ers2" style="endArrow=classic;html=1;dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1;exitX=0;exitY=0.5;entryX=0;entryY=0.5" edge="1" parent="1" source="enc_ff" target="enc_an2">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="45" y="495"/><mxPoint x="45" y="435"/></Array></mxGeometry>
        </mxCell>

        <!-- Decoder residuals (right side, dashed thin, x=895 inside dec_sec) -->
        <mxCell id="e_drs1" style="endArrow=classic;html=1;dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1;exitX=1;exitY=0.5;entryX=1;entryY=0.5" edge="1" parent="1" source="dec_mmha" target="dec_an1">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="895" y="555"/><mxPoint x="895" y="495"/></Array></mxGeometry>
        </mxCell>
        <mxCell id="e_drs2" style="endArrow=classic;html=1;dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1;exitX=1;exitY=0.5;entryX=1;entryY=0.5" edge="1" parent="1" source="dec_ca" target="dec_an2">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="895" y="435"/><mxPoint x="895" y="375"/></Array></mxGeometry>
        </mxCell>
        <mxCell id="e_drs3" style="endArrow=classic;html=1;dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1;exitX=1;exitY=0.5;entryX=1;entryY=0.5" edge="1" parent="1" source="dec_ff" target="dec_an3">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="895" y="315"/><mxPoint x="895" y="255"/></Array></mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```



---

---

## §21 Diffusion (forward + reverse process)

**When to use:** DDPM/DDIM/score-based/flow-matching figures showing the
two-direction Markov chain. Canonical Ho et al. 2020 Figure 2 layout.

**Canvas:** 1100×440. Two parallel chains stacked vertically — forward on
top (q, →), reverse on bottom (p_θ, ←). Nodes are square placeholders for
sample images (h=80, w=100-120).

**Edge convention:** All edges use the orthogonal routing base from
`drawio-reference.md`. Forward edges (blue): `endArrow=classic;strokeColor=#1976D2`. Reverse edges (orange): `endArrow=classic;strokeColor=#E65100` (these have `source.x > target.x` because the reverse process flows right-to-left — this is a documented exception per-chain per `drawio-reference.md`). Dashed edges across the "…" gaps: `dashed=1;dashPattern=6 3`.

**Layout choices:**
- The reverse chain renders edges with `source.x > target.x` because the
  process flows right-to-left. This is allowed: the rule "every forward
  edge has source.x < target.x for LR" applies per-flow within a single
  chain. Treat the reverse chain as its own LR flow with its own positive
  direction (right-to-left here).
- Five visible nodes per chain: x_0, x_1, x_{t-1}, x_t, x_T, with text "..."
  fillers between x_1↔x_{t-1} and x_t↔x_T to indicate omitted steps.
- Color: x_0 light green (data), x_T light red (noise), intermediates white.
- Forward arrows blue, reverse arrows orange (or any two distinguishable
  colors with a legend).

**Node table:**

```
SECTION  | id           | label                              | x   | y   | w   | h
title    | t_fwd        | Forward Process: q(x_t | x_{t-1})  | 280 | 30  | 540 | 24
forward  | f_x0         | x_0  (data)                        | 80  | 80  | 100 | 80
forward  | f_x1         | x_1                                | 240 | 80  | 100 | 80
forward  | f_dots1      | …                                  | 380 | 110 | 80  | 20
forward  | f_xtm1       | x_{t-1}                            | 480 | 80  | 120 | 80
forward  | f_xt         | x_t                                | 640 | 80  | 120 | 80
forward  | f_dots2      | …                                  | 800 | 110 | 80  | 20
forward  | f_xT         | x_T  (noise)                       | 900 | 80  | 100 | 80
title    | t_rev        | Reverse Process: p_θ(x_{t-1} | x_t)| 280 | 240 | 540 | 24
reverse  | r_xT         | x_T                                | 900 | 290 | 100 | 80
reverse  | r_dots2      | …                                  | 800 | 320 | 80  | 20
reverse  | r_xt         | x_t                                | 640 | 290 | 120 | 80
reverse  | r_xtm1       | x_{t-1}                            | 480 | 290 | 120 | 80
reverse  | r_dots1      | …                                  | 380 | 320 | 80  | 20
reverse  | r_x1         | x_1                                | 240 | 290 | 100 | 80
reverse  | r_x0         | x_0                                | 80  | 290 | 100 | 80
```

**Edge table:**

```
id    | source   | target   | style
e_f01 | f_x0     | f_x1     | →, blue, label "q"
e_f12 | f_x1     | f_xtm1   | →, blue, dashed (over the dots)
e_f23 | f_xtm1   | f_xt     | →, blue, label "q(x_t | x_{t-1})"
e_f34 | f_xt     | f_xT     | →, blue, dashed
e_r10 | r_x1     | r_x0     | ←, orange, label "p_θ"
e_r21 | r_xtm1   | r_x1     | ←, orange, dashed
e_r32 | r_xt     | r_xtm1   | ←, orange, label "p_θ(x_{t-1} | x_t)"
e_r43 | r_xT     | r_xt     | ←, orange, dashed
```

**Style hint** for sample-image placeholder nodes:
`rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor=#666666;strokeWidth=1.5;
fontFamily=Times New Roman;fontSize=14;fontStyle=2;align=center;verticalAlign=middle`

If you want to embed actual sample images, replace each square's `value=""`
with `<img src="data:image/png;base64,...">` HTML or use drawio's image
shape (`shape=image;image=...`).

**Self-check:**
1. Forward chain: all edges `source.x < target.x`
2. Reverse chain: all edges `source.x > target.x` (documented exception)
3. Row gap: forward bottom (160) to reverse top (290) = 130px, no overlap
4. Canvas 1100x440: all nodes within bounds

---

---

## §22 RAG pipeline

**When to use:** Retrieval-augmented LLM system figures. Common in 2024+
LLM application papers.

**Edge convention:** All edges use the orthogonal routing base from `drawio-reference.md`.
LR pipeline edges: `endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=1;entryX=0`.
Vertical edges (DB→retriever, LLM→answer): `exitX=0.5` with bend waypoints.

**Canvas:** 1180×360. Single LR pipeline. The vector DB hangs below the
retriever as a cylinder (the canonical "external knowledge" symbol).

**Node table:**

```
SECTION  | id          | label                               | x    | y   | w   | h
input    | q           | User Query                          | 30   | 140 | 130 | 60
process  | enc         | Query Encoder (e.g., BGE)           | 200  | 140 | 150 | 60
process  | retr        | Retriever (top-k similarity)        | 390  | 140 | 160 | 60
data     | docs        | Top-k Documents                     | 590  | 140 | 150 | 60
process  | rerank      | Reranker (cross-encoder)            | 780  | 140 | 150 | 60
process  | llm         | LLM Generator                       | 970  | 140 | 130 | 60
output   | ans         | Answer                              | 970  | 260 | 130 | 60
storage  | kb          | Vector DB (knowledge base)          | 390  | 260 | 160 | 60
```

The Vector DB cylinder uses `shape=cylinder3;fillColor=#E1F5FE;strokeColor=#0288D1`.

**Edge table:**

```
id      | source | target | style
e_q_e   | q      | enc    | → solid black
e_e_r   | enc    | retr   | → solid black
e_r_d   | retr   | docs   | → solid black
e_d_rr  | docs   | rerank | → solid black
e_rr_l  | rerank | llm    | → solid black
e_l_a   | llm    | ans    | ↓ solid black (LLM down to Answer)
e_kb_r  | kb     | retr   | ↑ dashed gray, label "embeddings + index"
```

**Layout choices:**
- LR primary flow at y=140. Vector DB and Answer sit at y=260, BELOW the
  pipeline, with vertical arrows feeding/exiting. Source and target are
  always y_source > y_target for upward arrows (e.g., kb → retr, since
  data flows from DB up into retriever).
- llm → ans is a downward arrow (data exits the pipeline toward the user).
  Treat this as a "pipeline outlet" not a forward flow edge.
- Use Operators palette colors: process boxes light blue (`#DAE8FC`/
  `#6C8EBF`), data boxes light orange (`#FFE6CC`/`#D79B00`), input red
  (`#F8CECC`/`#B85450`), output yellow (`#FFF2CC`/`#D6B656`), DB cyan.

**Optional extensions:**
- Add a "Prompt Template" box between rerank and llm if showing prompt
  construction explicitly.
- Add a "Citation extractor" between llm and ans for citation-grounded
  RAG.



---

---

## §23 Multi-stage training pipeline

**When to use:** Foundation-model recipe figures: Pretrain → SFT → RLHF
→ Eval, or analogous multi-stage workflows. Common in LLM/VLM/codegen
papers since 2023.

**Edge convention:** All edges use the orthogonal routing base from `drawio-reference.md`.
Stage→stage edges: `strokeWidth=2.5` (bold, parameter inheritance).
Data source→stage edges: `strokeWidth=1;strokeColor=#999` (↑ thin gray).

**Canvas:** 1180×360. LR pipeline of 4-5 stage boxes; below each stage,
a small "data" box names the dataset / objective / size.

**Node table:**

```
SECTION  | id          | label                            | x    | y   | w   | h
stage    | s1          | Stage 1: Pretrain                | 60   | 100 | 220 | 70
data     | d1          | C4 + Common Crawl (1.5T tokens)  | 60   | 200 | 220 | 50
stage    | s2          | Stage 2: SFT                     | 320  | 100 | 220 | 70
data     | d2          | 50K instruction pairs            | 320  | 200 | 220 | 50
stage    | s3          | Stage 3: RLHF (PPO)              | 580  | 100 | 220 | 70
data     | d3          | 100K preference pairs            | 580  | 200 | 220 | 50
stage    | s4          | Stage 4: Eval                    | 840  | 100 | 220 | 70
data     | d4          | MMLU + HumanEval + ARC           | 840  | 200 | 220 | 50
output   | model       | Final Model                      | 1080 | 100 | 70  | 70
```

**Edge table:**

```
id      | source | target | style
e_s1_s2 | s1     | s2     | → bold, label "θ₀"
e_s2_s3 | s2     | s3     | → bold, label "θ_SFT"
e_s3_s4 | s3     | s4     | → bold, label "θ_RLHF"
e_s4_m  | s4     | model  | → bold
e_d1_s1 | d1     | s1     | ↑ thin gray, "trains"
e_d2_s2 | d2     | s2     | ↑ thin gray
e_d3_s3 | d3     | s3     | ↑ thin gray
e_d4_s4 | d4     | s4     | ↑ thin gray, "evaluates"
```

**Layout choices:**
- Stages aligned at y=100, data tags aligned at y=200. Both rows form
  parallel bands.
- Stage boxes use a stronger fill (`#DAE8FC`/`#6C8EBF` blue), data tags
  use a lighter fill or just a white background with thin border.
- Stage→stage edges are bold (`strokeWidth=2.5`) with the running
  parameter label (θ₀, θ_SFT, etc.) above the arrow. This shows
  parameter inheritance, which is the figure's main point.
- Data→stage edges thin gray (`strokeWidth=1`, `strokeColor=#999`).

**Variants:**
- Add a "Reward Model" subbox during Stage 3 if the RLHF figure needs to
  show RM training separately.
- For DPO instead of PPO, change the Stage 3 label and skip the reward
  model subbox.
- For continual pretraining, add a feedback loop from Stage 4 back to
  Stage 1 with a dashed curve.



---
