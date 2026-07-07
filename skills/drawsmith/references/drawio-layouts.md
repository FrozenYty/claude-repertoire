# Diagram Layout Templates

Read this file when generating any conceptual diagram with draw.io.
Pick the closest layout pattern, adapt labels to the user's spec,
and keep the coordinate math as-is.

All templates follow the Flow Direction and No-Overlap rules from
`drawio-guide.md`. For visual style (colors, fonts, line weights),
see `style-guide.md`.

## Index

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
| Flowchart | Decision trees, process flows, algorithm logic | §6 |
| Entity-Relationship Diagram (ERD) | Database schemas, data models, table relationships | §7 |
| UML Class Diagram | OOP design, architecture modeling, inheritance hierarchies | §8 |
| Sequence Diagram | Protocol interactions, API call flows, message passing | §9 |
| State Machine Diagram | State transitions, formal methods, protocol specifications | §10 |
| Data Flow Diagram (DFD) | Software engineering, system data flows, process modeling | §11 |
| Network Topology | LAN/WAN, router/switch, subnet boundaries | §12 |
| Org Chart / Mind Map | Hierarchies, file trees, concept maps | §13 |
| Timeline / Gantt Chart | Project roadmaps, milestone overviews | §14 |
| Venn Diagram / Set Relations | Set intersection, overlapping categories | §15 |
| Conceptual Coordinate | 2x2 matrix, BCG, maturity curves | §16 |
| Swimlane Diagram | Cross-functional process flows, RACI charts | §17 |
| Wireframe / Mockup | App screens, website layouts, UI prototypes | §18 |
| Cross-Functional Table | Actor x Phase process grid, two-axis flowcharts | §19 |
| Cloud Architecture | AWS/Azure/GCP 3-tier, VPC/subnet, IaaS | §20 |
| BPMN Process | Cross-functional business process with lanes | §21 |
| System Architecture Overview | CLI/infra/tool architecture, core + side panels | §22 |

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

```xml
<mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="600" pageHeight="750" math="0" shadow="0">
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <mxCell id="layer_in" value="Input Data" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="620" width="320" height="50" as="geometry"/></mxCell>
    <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="layer_in" target="layer_1"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="layer_1" value="Layer 1: Physical" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="540" width="320" height="50" as="geometry"/></mxCell>
    <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="layer_1" target="layer_2"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="layer_2" value="Layer 2: Data Link" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="460" width="320" height="50" as="geometry"/></mxCell>
    <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="layer_2" target="layer_3"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="layer_3" value="Layer 3: Network" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="380" width="320" height="50" as="geometry"/></mxCell>
    <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="layer_3" target="layer_4"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="layer_4" value="Layer 4: Transport" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="300" width="320" height="50" as="geometry"/></mxCell>
    <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="layer_4" target="layer_5"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="layer_5" value="Layer 5: Session" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="220" width="320" height="50" as="geometry"/></mxCell>
    <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="layer_5" target="layer_out"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="layer_out" value="Output / Application" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="140" y="140" width="320" height="50" as="geometry"/></mxCell>
  </root>
</mxGraphModel>
```

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

**To adapt:** change hub and satellite labels, add corner satellites at (40, 60), (560, 60), (560, 460), (40, 460) for an 8-node star.

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
    <mxCell id="sep" style="endArrow=none;dashed=1;dashPattern=12 6;strokeColor=#AAAAAA;strokeWidth=1;verticalAlign=middle" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="450" y="80" as="sourcePoint"/><mxPoint x="450" y="600" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="a1" value="Element A-1 &lt;br&gt;Description" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="120" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b1" value="Element B-1 &lt;br&gt;Description" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="120" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m1" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1;verticalAlign=middle" edge="1" parent="1" source="a1" target="b1"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="a2" value="Element A-2" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="230" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b2" value="Element B-2" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="230" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m2" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1;verticalAlign=middle" edge="1" parent="1" source="a2" target="b2"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="a3" value="Element A-3" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="340" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b3" value="Element B-3" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="340" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m3" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1;verticalAlign=middle" edge="1" parent="1" source="a3" target="b3"><mxGeometry relative="1" as="geometry"/></mxCell>
    <mxCell id="a4" value="Element A-4" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="40" y="450" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="b4" value="Element B-4" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1"><mxGeometry x="540" y="450" width="320" height="70" as="geometry"/></mxCell>
    <mxCell id="m4" style="endArrow=none;dashed=1;dashPattern=8 4;strokeColor=#AAAAAA;strokeWidth=1;verticalAlign=middle" edge="1" parent="1" source="a4" target="b4"><mxGeometry relative="1" as="geometry"/></mxCell>
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

**When to use:** Protocol interactions, API call flows, message passing
between actors – any interaction where time flows top-to-bottom with
participant lifelines.

**Canvas:** 900x700. LR layout – actors placed horizontally.

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| Lifeline header | `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;fillColor=#DAE8FC;strokeColor=#6C8EBF;size=40;fontFamily=Times New Roman;fontStyle=1;fontSize=12` |
| Activation box | `rounded=0;fillColor=#E8EAF6;strokeColor=#6C8EBF;strokeWidth=1` (w=20 inside lifeline) |
| Request (sync) | `endArrow=block;endFill=1;strokeColor=#333333` |
| Response (return) | `endArrow=open;dashed=1;strokeColor=#999999` |

**Layout conventions:**
- 3-4 lifelines, evenly spaced (e.g., x=40, 280, 520 – 240px gaps)
- Messages ordered top-to-bottom, y increments ~50-60px per message
- Activation box y = message arrival y, height = duration
- **Bidirectional message pairs**: offset exitY (request=0.25, response=0.75)
  to avoid overlap on the same lifeline segment
- Request=block arrow rightward, Response=open dashed arrow leftward

**Golden XML example (OAuth 2.0 flow, 3 participants):**

```xml
<mxGraphModel dx="1001" dy="690" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="800" pageHeight="650" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="ll_client" parent="1" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;fillColor=#DAE8FC;strokeColor=#6C8EBF;size=40;fontFamily=Times New Roman;fontStyle=1;fontSize=12;verticalAlign=middle" value="User Client" vertex="1">
          <mxGeometry height="40" width="100" x="40" y="40" as="geometry" />
        </mxCell>
        <mxCell id="ll_auth" parent="1" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;fillColor=#DAE8FC;strokeColor=#6C8EBF;size=40;fontFamily=Times New Roman;fontStyle=1;fontSize=12;verticalAlign=middle" value="Auth Server" vertex="1">
          <mxGeometry height="40" width="100" x="280" y="40" as="geometry" />
        </mxCell>
        <mxCell id="ll_res" parent="1" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;fillColor=#DAE8FC;strokeColor=#6C8EBF;size=40;fontFamily=Times New Roman;fontStyle=1;fontSize=12;verticalAlign=middle" value="Resource Server" vertex="1">
          <mxGeometry height="40" width="100" x="520" y="40" as="geometry" />
        </mxCell>
        <mxCell id="act_c1" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="120" width="16" x="82" y="110" as="geometry" />
        </mxCell>
        <mxCell id="act_a1" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="120" width="16" x="322" y="110" as="geometry" />
        </mxCell>
        <mxCell id="act_c2" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="220" width="16" x="82" y="250" as="geometry" />
        </mxCell>
        <mxCell id="msg1" edge="1" parent="1" source="act_c1" style="endArrow=block;endFill=1;strokeColor=#333333;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.25;exitDx=0;exitDy=0;" target="act_a1" value="GET /authorize">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="56" y="140" as="sourcePoint" />
            <mxPoint x="279.9959999999999" y="140.00000000000003" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="msg2" edge="1" parent="1" source="act_a1" style="endArrow=open;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;exitX=0;exitY=0.75;exitDx=0;exitDy=0;entryX=1;entryY=0.75;entryDx=0;entryDy=0;" target="act_c1" value="302 redirect  code">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="260" y="220" as="sourcePoint" />
            <mxPoint x="120" y="220" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="msg3" edge="1" parent="1" style="endArrow=block;endFill=1;strokeColor=#333333;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;entryX=0;entryY=0.25;entryDx=0;entryDy=0;" target="act_r1" value="GET /resource?code=xxx">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="100" y="270" as="sourcePoint" />
            <mxPoint x="562" y="270.0000000000001" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="msg4" edge="1" parent="1" source="act_r1" style="endArrow=block;endFill=1;strokeColor=#333333;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=-0.105;exitY=0.858;exitDx=0;exitDy=0;exitPerimeter=0;" target="act_a2" value="Validate token">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="550" y="320" as="sourcePoint" />
            <mxPoint x="410" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="msg5" edge="1" parent="1" source="act_a2" style="endArrow=open;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;entryX=0.039;entryY=0.138;entryDx=0;entryDy=0;entryPerimeter=0;exitX=1.085;exitY=0.906;exitDx=0;exitDy=0;exitPerimeter=0;" target="act_r2" value="Token valid">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="380" y="390" as="sourcePoint" />
            <mxPoint x="520" y="390" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="msg6" edge="1" parent="1" source="act_r2" style="endArrow=open;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;entryX=1;entryY=0.75;entryDx=0;entryDy=0;exitX=-0.076;exitY=0.589;exitDx=0;exitDy=0;exitPerimeter=0;" target="act_c2" value="Data response">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="560" y="450" as="sourcePoint" />
            <mxPoint x="180" y="450" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="legend_box" parent="1" style="rounded=1;arcSize=6;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1;html=1;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="90" width="190" x="590" y="540" as="geometry" />
        </mxCell>
        <mxCell id="legend_title" parent="1" style="text;html=1;strokeColor=none;fontFamily=Times New Roman;fontSize=9;fontStyle=1;fontColor=#333333;align=left;verticalAlign=top" value="Legend" vertex="1">
          <mxGeometry height="14" width="50" x="600" y="544" as="geometry" />
        </mxCell>
        <mxCell id="leg_req" edge="1" parent="1" style="endArrow=block;endFill=1;strokeColor=#333333;strokeWidth=1.5;html=1;verticalAlign=middle" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="600" y="570" as="sourcePoint" />
            <mxPoint x="640" y="570" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_req_lbl" parent="1" style="text;html=1;strokeColor=none;fontFamily=Times New Roman;fontSize=9;fontStyle=0;fontColor=#333333;align=left;verticalAlign=middle" value="Request" vertex="1">
          <mxGeometry height="14" width="60" x="646" y="564" as="geometry" />
        </mxCell>
        <mxCell id="leg_res" edge="1" parent="1" style="endArrow=open;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;verticalAlign=middle" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="600" y="590" as="sourcePoint" />
            <mxPoint x="640" y="590" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_res_lbl" parent="1" style="text;html=1;strokeColor=none;fontFamily=Times New Roman;fontSize=9;fontStyle=0;fontColor=#333333;align=left;verticalAlign=middle" value="Response" vertex="1">
          <mxGeometry height="14" width="60" x="646" y="584" as="geometry" />
        </mxCell>
        <mxCell id="leg_box" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="10" width="16" x="600" y="608" as="geometry" />
        </mxCell>
        <mxCell id="leg_box_lbl" parent="1" style="text;html=1;strokeColor=none;fontFamily=Times New Roman;fontSize=9;fontStyle=0;fontColor=#333333;align=left;verticalAlign=middle" value="Activation" vertex="1">
          <mxGeometry height="14" width="100" x="622" y="606" as="geometry" />
        </mxCell>
        <mxCell id="J75T59nXUttIiPp1htpR-2" edge="1" parent="1" style="endArrow=none;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;endFill=0;" target="ll_client" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="90" y="520" as="sourcePoint" />
            <mxPoint x="300" y="590" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="J75T59nXUttIiPp1htpR-3" edge="1" parent="1" source="act_a2" style="endArrow=none;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;endFill=0;" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="329.65999999999997" y="560" as="sourcePoint" />
            <mxPoint x="329.65999999999997" y="80" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="J75T59nXUttIiPp1htpR-4" edge="1" parent="1" source="act_r1" style="endArrow=none;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;endFill=0;" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="577.31" y="560" as="sourcePoint" />
            <mxPoint x="577.31" y="80" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="J75T59nXUttIiPp1htpR-5" edge="1" parent="1" source="act_r2" style="endArrow=none;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;endFill=0;" target="act_r1" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points" />
            <mxPoint x="577.31" y="560" as="sourcePoint" />
            <mxPoint x="577.31" y="80" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="act_r1" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="80" width="16" x="570" y="250" as="geometry" />
        </mxCell>
        <mxCell id="J75T59nXUttIiPp1htpR-7" edge="1" parent="1" style="endArrow=none;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;endFill=0;" target="act_a2" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="330" y="520" as="sourcePoint" />
            <mxPoint x="329.65999999999997" y="80" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="act_a2" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="80" width="16" x="322" y="300" as="geometry" />
        </mxCell>
        <mxCell id="J75T59nXUttIiPp1htpR-8" edge="1" parent="1" style="endArrow=none;dashed=1;strokeColor=#999999;strokeWidth=1.5;html=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;align=center;verticalAlign=bottom;endFill=0;" target="act_r2" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="577" y="480" />
            </Array>
            <mxPoint x="577" y="520" as="sourcePoint" />
            <mxPoint x="578" y="330" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="act_r2" parent="1" style="rounded=0;fillColor=#F5F5F5;strokeColor=#999999;strokeWidth=0.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="100" width="16" x="570" y="360" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
```

**Key patterns:**
- 3 lifelines at x=40/280/520
- Request/response pairs use exitY 0.25/0.75 offset
- Activation boxes show processing time on each lifeline
- Legend at bottom explains arrow types
- All edges: 0 waypoints (exitX/exitY only)

**To adapt:** change participant names, message labels, add/remove lifelines.
Keep 240px spacing between lifelines, 50-60px vertical message spacing.
## §10 State Machine Diagram

**When to use:** State transition specifications, protocol state machines,
embedded system modes – any transition-based model.

**Canvas:** 800x650. Variable layout – states arranged in natural order.

**Shape vocabulary:**

| Element | Style keywords |
|---|---|
| State | `rounded=1;arcSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle` |
| Initial (●) | `ellipse;fillColor=#333333;strokeColor=#333333` (20x20) |
| Final (◎) | double ellipse: outer `fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=2.5` (30x30), inner `fillColor=#333333` (16x16) |
| Transition | `edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5` |
| Self-loop | `curved=1;exitX=1;exitY=0.25;entryX=1;entryY=0.5` + 3 waypoints for right-side box |
| Emergency | `dashed=1;strokeColor=#B85450;strokeWidth=1.5` |

**Layout conventions:**
- 4-6 states in natural reading order
- Initial black circle connects to first state
- Final double circle reached from terminal transitions
- Spacing: 250-300px between states
- **Self-loop**: exits RIGHT, arcs UP and LEFT in a box above the node,
  comes back down to entry. 3 waypoints. NOT left-side arc.
- **Bidirectional**: offset exitY for opposite directions (0.035/0.119)
- **Emergency edges**: direct, dashed, right-side exit – no waypoints
- **Return edges**: dashed, left-side exit with 2 waypoints

**Golden XML example (Elevator controller, 5 states):**

```xml
<mxGraphModel dx="1716" dy="1783" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="800" pageHeight="600" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="initial" parent="1" style="ellipse;fillColor=#333333;strokeColor=#333333;strokeWidth=1.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="20" width="20" x="600" y="-340" as="geometry" />
        </mxCell>
        <mxCell id="e_init_idle" edge="1" parent="1" source="initial" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" target="idle">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="idle" parent="1" style="rounded=1;arcSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;Idle&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="160" x="530" y="-278" as="geometry" />
        </mxCell>
        <mxCell id="door_open" parent="1" style="rounded=1;arcSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;Door Open&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="160" x="530" y="-116" as="geometry" />
        </mxCell>
        <mxCell id="moving_up" parent="1" style="rounded=1;arcSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;Moving Up&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="160" x="530" y="45" as="geometry" />
        </mxCell>
        <mxCell id="moving_down" parent="1" style="rounded=1;arcSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;Moving Down&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="160" x="530" y="205" as="geometry" />
        </mxCell>
        <mxCell id="emergency" parent="1" style="rounded=1;arcSize=12;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=2.5;whiteSpace=wrap;html=1;fontFamily=Times New Roman;fontStyle=1;fontSize=13;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;Emergency&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="160" x="960" y="-40" as="geometry" />
        </mxCell>
        <mxCell id="e_idle_up" edge="1" parent="1" source="idle" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=1;exitY=0.75;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="moving_up" value="up_request">
          <mxGeometry relative="1" x="-0.1656" as="geometry">
            <mxPoint as="offset" />
            <Array as="points">
              <mxPoint x="770" y="-233" />
              <mxPoint x="770" y="60" />
            </Array>
            <mxPoint x="830" y="-184" as="sourcePoint" />
            <mxPoint x="718" y="25" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_up_idle" edge="1" parent="1" source="moving_down" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;dashed=1;exitX=0;exitY=0.5;entryX=-0.006;entryY=0.372;entryDx=0;entryDy=0;entryPerimeter=0;exitDx=0;exitDy=0;" target="idle" value="arrived">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="440" y="235" />
              <mxPoint x="440" y="-256" />
            </Array>
            <mxPoint x="200" y="5" as="sourcePoint" />
            <mxPoint x="240" y="-234" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_idle_down" edge="1" parent="1" source="idle" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=1;exitY=0.25;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="moving_down" value="down_request">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="820" y="-263" />
              <mxPoint x="820" y="220" />
            </Array>
            <mxPoint x="910" y="-210" as="sourcePoint" />
            <mxPoint x="870" y="60.000000000000114" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_down_idle" edge="1" parent="1" source="moving_up" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;dashed=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=0;exitY=0.5;entryX=0;entryY=0.75;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="idle" value="arrived">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="490" y="75" />
              <mxPoint x="490" y="-233" />
            </Array>
            <mxPoint x="400" y="191" as="sourcePoint" />
            <mxPoint x="440" y="-169" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_idle_door" edge="1" parent="1" source="idle" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=0.424;exitY=1.02;entryX=0.428;entryY=-0.004;entryDx=0;entryDy=0;entryPerimeter=0;exitDx=0;exitDy=0;exitPerimeter=0;" target="door_open" value="door_open">
          <mxGeometry relative="1" x="-0.352" y="1" as="geometry">
            <mxPoint as="offset" />
            <mxPoint x="550" y="-204" as="sourcePoint" />
            <mxPoint x="550" y="-135" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_door_idle" edge="1" parent="1" source="door_open" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;entryX=0.56;entryY=1.011;entryDx=0;entryDy=0;entryPerimeter=0;exitX=0.563;exitY=-0.022;exitDx=0;exitDy=0;exitPerimeter=0;" target="idle" value="close">
          <mxGeometry relative="1" x="-0.4692" as="geometry">
            <mxPoint as="offset" />
            <mxPoint x="620" y="-135" as="sourcePoint" />
            <mxPoint x="620" y="-204" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_up_door" edge="1" parent="1" source="moving_up" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=0.5;exitY=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="door_open" value="open">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="490" y="83" as="sourcePoint" />
            <mxPoint x="490" y="3" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_down_door" edge="1" parent="1" source="moving_down" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=0.414;exitY=0.035;entryX=0.414;entryY=0.97;entryDx=0;entryDy=0;entryPerimeter=0;exitDx=0;exitDy=0;exitPerimeter=0;" target="moving_up" value="open">
          <mxGeometry relative="1" x="0.3686" as="geometry">
            <mxPoint as="offset" />
            <mxPoint x="430" y="150" as="sourcePoint" />
            <mxPoint x="470" y="-105" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_door_self" edge="1" parent="1" source="door_open" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;curved=1;exitX=1;exitY=0.25;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitDx=0;exitDy=0;entryX=0.75;entryY=0;entryDx=0;entryDy=0;" target="door_open" value="obstacle / reopen">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="730" y="-101" />
              <mxPoint x="730" y="-164" />
              <mxPoint x="650" y="-164" />
            </Array>
            <mxPoint x="850" y="-164" as="sourcePoint" />
            <mxPoint x="750" y="-184" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_up_down" edge="1" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;entryX=0.5;entryY=0;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryDx=0;entryDy=0;" value="reverse">
          <mxGeometry relative="1" x="0.42" as="geometry">
            <mxPoint as="offset" />
            <mxPoint x="620" y="105" as="sourcePoint" />
            <mxPoint x="620" y="205" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_down_up" edge="1" parent="1" source="moving_down" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;dashed=1;exitX=-0.006;exitY=0.119;entryX=0;entryY=0.75;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;entryDx=0;entryDy=0;exitDx=0;exitDy=0;exitPerimeter=0;" target="moving_up" value="reverse">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="490" y="212" />
              <mxPoint x="490" y="90" />
            </Array>
            <mxPoint x="160" y="290" as="sourcePoint" />
            <mxPoint x="320" y="157" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_idle_emer" edge="1" parent="1" source="moving_down" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#B85450;strokeWidth=1.5;dashed=1;dashPattern=8 4;exitX=1;exitY=0.75;entryX=0.539;entryY=1.026;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;entryDx=0;entryDy=0;entryPerimeter=0;exitDx=0;exitDy=0;" target="emergency" value="emergency">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="700" y="307.78" as="sourcePoint" />
            <mxPoint x="1079.2799999999997" y="86" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_door_emer" edge="1" parent="1" source="door_open" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#B85450;strokeWidth=1.5;dashed=1;dashPattern=8 4;exitX=1;exitY=0.5;entryX=0.25;entryY=0;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;exitDx=0;exitDy=0;entryDx=0;entryDy=0;" target="emergency" value="emergency">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="880" y="356" as="sourcePoint" />
            <mxPoint x="1220" y="415" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_up_emer" edge="1" parent="1" source="moving_up" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#B85450;strokeWidth=1.5;dashed=1;dashPattern=8 4;exitX=1;exitY=0.75;entryX=0.25;entryY=1;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="emergency" value="emergency">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="730" y="805" as="sourcePoint" />
            <mxPoint x="1070" y="706" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_down_emer" edge="1" parent="1" source="idle" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#B85450;strokeWidth=1.5;dashed=1;dashPattern=8 4;exitX=0.75;exitY=0;entryX=0.5;entryY=0;fontFamily=Times New Roman;fontSize=10;fontColor=#333333;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="emergency" value="emergency">
          <mxGeometry relative="1" x="-0.3413" y="-4" as="geometry">
            <mxPoint as="offset" />
            <mxPoint x="570" y="743" as="sourcePoint" />
            <mxPoint x="910" y="526" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="legend_box" parent="1" style="rounded=1;arcSize=6;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1;html=1;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="110" width="180" x="1115" y="132" as="geometry" />
        </mxCell>
        <mxCell id="legend_title" parent="1" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=left;verticalAlign=top" value="&lt;b&gt;Legend&lt;/b&gt;" vertex="1">
          <mxGeometry height="16" width="60" x="1125" y="137" as="geometry" />
        </mxCell>
        <mxCell id="leg_solid" edge="1" parent="1" style="endArrow=classic;strokeColor=#333333;strokeWidth=1.5;html=1;verticalAlign=middle">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1130" y="162" as="sourcePoint" />
            <mxPoint x="1160" y="162" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_solid_t" parent="1" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;verticalAlign=middle" value="Normal transition" vertex="1">
          <mxGeometry height="16" width="120" x="1170" y="154" as="geometry" />
        </mxCell>
        <mxCell id="leg_dash" edge="1" parent="1" style="endArrow=classic;strokeColor=#333333;strokeWidth=1.5;dashed=1;html=1;verticalAlign=middle">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1130" y="182" as="sourcePoint" />
            <mxPoint x="1160" y="182" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_dash_t" parent="1" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;verticalAlign=middle" value="Return / reverse" vertex="1">
          <mxGeometry height="16" width="120" x="1170" y="174" as="geometry" />
        </mxCell>
        <mxCell id="leg_emer" edge="1" parent="1" style="endArrow=classic;strokeColor=#B85450;strokeWidth=1.5;dashed=1;dashPattern=8 4;html=1;verticalAlign=middle">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1130" y="202" as="sourcePoint" />
            <mxPoint x="1160" y="202" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_emer_t" parent="1" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;verticalAlign=middle" value="Emergency stop" vertex="1">
          <mxGeometry height="16" width="120" x="1170" y="194" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
```

**Key patterns:**
- Self-loop: 3 waypoints (730,-101)→(730,-164)→(650,-164), exitX=1,exitY=0.25
- 15 of 19 edges use exitX/exitY only (NO waypoints)
- Only 4 edges have waypoints: self-loop(3) + 2 idle-branch(2) + 2 return(2)
- Emergency: all dashed, direct, right-side exitX=1
- Bidirectional: moving_up↔moving_down use exitY 0.035/0.119

**To adapt:** change state labels, add states, adjust transition labels.
Keep the self-loop box pattern and exitY offset convention.
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
  Processes at same y share same height for clean horizontal alignment. Data flows IN from entities, is transformed by processes, and flows OUT to stores or entities.
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

**Golden XML example:**

```xml
<mxGraphModel dx="828" dy="571" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="700" pageHeight="600" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" parent="1" style="ellipse;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2;opacity=35;html=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="320" width="320" x="130" y="80" as="geometry" />
        </mxCell>
        <mxCell id="3" parent="1" style="ellipse;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=2;opacity=35;html=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="320" width="320" x="260" y="80" as="geometry" />
        </mxCell>
        <mxCell id="4" parent="1" style="ellipse;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=2;opacity=35;html=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="320" width="320" x="190" y="219" as="geometry" />
        </mxCell>
        <mxCell id="5" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="Frontend-Only" vertex="1">
          <mxGeometry height="20" width="100" x="130" y="190" as="geometry" />
        </mxCell>
        <mxCell id="6" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="Backend-Only" vertex="1">
          <mxGeometry height="20" width="100" x="480" y="190" as="geometry" />
        </mxCell>
        <mxCell id="7" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="DevOps-Only" vertex="1">
          <mxGeometry height="20" width="100" x="300" y="490" as="geometry" />
        </mxCell>
        <mxCell id="8" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="Full-Stack" vertex="1">
          <mxGeometry height="20" width="80" x="310" y="150" as="geometry" />
        </mxCell>
        <mxCell id="9" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="DevEx" vertex="1">
          <mxGeometry height="20" width="60" x="220" y="330" as="geometry" />
        </mxCell>
        <mxCell id="10" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="Infrastructure" vertex="1">
          <mxGeometry height="20" width="120" x="390" y="340" as="geometry" />
        </mxCell>
        <mxCell id="11" parent="1" style="text;html=1;fontSize=11;fontFamily=Times New Roman;fontColor=#333333;align=center;;verticalAlign=middle" value="Platform Engineering" vertex="1">
          <mxGeometry height="20" width="160" x="270" y="270" as="geometry" />
        </mxCell>
        <mxCell id="12" parent="1" style="text;html=1;fontSize=14;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;;verticalAlign=middle" value="Frontend" vertex="1">
          <mxGeometry height="20" width="100" x="240" y="40" as="geometry" />
        </mxCell>
        <mxCell id="13" parent="1" style="text;html=1;fontSize=14;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;;verticalAlign=middle" value="Backend" vertex="1">
          <mxGeometry height="20" width="80" x="380" y="40" as="geometry" />
        </mxCell>
        <mxCell id="14" parent="1" style="text;html=1;fontSize=14;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=center;;verticalAlign=middle" value="DevOps" vertex="1">
          <mxGeometry height="20" width="80" x="310" y="550" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
```



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

**Golden XML example:**

```xml
<mxGraphModel dx="1740" dy="679" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="750" pageHeight="650" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#D5E8D4;opacity=15;strokeColor=none;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="260" width="335" x="375" y="50" as="geometry" />
        </mxCell>
        <mxCell id="3" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;opacity=15;strokeColor=none;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="260" width="335" x="40" y="50" as="geometry" />
        </mxCell>
        <mxCell id="4" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;opacity=15;strokeColor=none;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="260" width="335" x="375" y="310" as="geometry" />
        </mxCell>
        <mxCell id="5" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F8CECC;opacity=15;strokeColor=none;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="260" width="335" x="40" y="310" as="geometry" />
        </mxCell>
        <mxCell id="6" edge="1" parent="1" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=2;startArrow=none;verticalAlign=middle" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="375" y="570" as="sourcePoint" />
            <mxPoint x="375" y="50" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7" edge="1" parent="1" style="endArrow=classic;html=1;strokeColor=#333333;strokeWidth=2;startArrow=none;verticalAlign=middle" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="40" y="310" as="sourcePoint" />
            <mxPoint x="710" y="310" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="8" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=14;fontColor=#333333" value="High" vertex="1">
          <mxGeometry height="20" width="40" x="380" y="50" as="geometry" />
        </mxCell>
        <mxCell id="9" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=14;fontColor=#333333" value="Low" vertex="1">
          <mxGeometry height="20" width="40" x="335" y="550" as="geometry" />
        </mxCell>
        <mxCell id="10" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=14;fontColor=#333333" value="Low" vertex="1">
          <mxGeometry height="20" width="40" x="50" y="320" as="geometry" />
        </mxCell>
        <mxCell id="11" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=14;fontColor=#333333" value="High" vertex="1">
          <mxGeometry height="20" width="40" x="660" y="315" as="geometry" />
        </mxCell>
        <mxCell id="12" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=16;fontColor=#333333;rotation=-90;horizontal=1;" value="Market Growth" vertex="1">
          <mxGeometry height="160" width="30" x="-20" y="230" as="geometry" />
        </mxCell>
        <mxCell id="13" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=16;fontColor=#333333" value="Market Share" vertex="1">
          <mxGeometry height="30" width="120" x="340" y="600" as="geometry" />
        </mxCell>
        <mxCell id="14" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=28;fontColor=#999999;opacity=30" value="Stars" vertex="1">
          <mxGeometry height="30" width="100" x="490" y="145" as="geometry" />
        </mxCell>
        <mxCell id="15" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=28;fontColor=#999999;opacity=30" value="Question Marks" vertex="1">
          <mxGeometry height="30" width="140" x="130" y="145" as="geometry" />
        </mxCell>
        <mxCell id="16" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=28;fontColor=#999999;opacity=30" value="Cash Cows" vertex="1">
          <mxGeometry height="30" width="130" x="480" y="435" as="geometry" />
        </mxCell>
        <mxCell id="17" parent="1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Times New Roman;fontSize=28;fontColor=#999999;opacity=30" value="Dogs" vertex="1">
          <mxGeometry height="30" width="80" x="160" y="435" as="geometry" />
        </mxCell>
        <mxCell id="18" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=12;align=center;verticalAlign=middle" value="Product A&lt;br&gt;&lt;b&gt;Star&lt;/b&gt;" vertex="1">
          <mxGeometry height="40" width="100" x="492.5" y="200" as="geometry" />
        </mxCell>
        <mxCell id="19" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=12;align=center;verticalAlign=middle" value="Product B&lt;br&gt;&lt;b&gt;Question Mark&lt;/b&gt;" vertex="1">
          <mxGeometry height="40" width="100" x="157.5" y="210" as="geometry" />
        </mxCell>
        <mxCell id="20" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=12;align=center;verticalAlign=middle" value="Product C&lt;br&gt;&lt;b&gt;Cash Cow&lt;/b&gt;" vertex="1">
          <mxGeometry height="40" width="100" x="490" y="380" as="geometry" />
        </mxCell>
        <mxCell id="21" parent="1" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=12;align=center;verticalAlign=middle" value="Product D&lt;br&gt;&lt;b&gt;Dog&lt;/b&gt;" vertex="1">
          <mxGeometry height="40" width="100" x="150" y="380" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
```



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
`



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

## §18 Wireframe / Mockup

**Golden XML example:**

```xml
<mxGraphModel dx="2002" dy="1380" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="750" pageHeight="1000" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" parent="1" style="rounded=1;arcSize=12;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=2.5;container=1;pointerEvents=0;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="900" width="600" x="75" y="50" as="geometry" />
        </mxCell>
        <mxCell id="3" parent="2" style="rounded=0;fillColor=#37474F;strokeColor=#333333;strokeWidth=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="60" width="600" as="geometry" />
        </mxCell>
        <mxCell id="4" parent="2" style="text;html=1;fontFamily=Arial;fontSize=14;fontColor=#FFFFFF;align=center;verticalAlign=middle;" value="&lt;b&gt;Dashboard&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="600" as="geometry" />
        </mxCell>
        <mxCell id="5" parent="2" style="rounded=0;fillColor=#ECEFF1;strokeColor=#E0E0E0;strokeWidth=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="800" width="160" y="60" as="geometry" />
        </mxCell>
        <mxCell id="6" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;fontStyle=1;;verticalAlign=middle" value="Overview" vertex="1">
          <mxGeometry height="20" width="120" x="20" y="80" as="geometry" />
        </mxCell>
        <mxCell id="7" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="Analytics" vertex="1">
          <mxGeometry height="20" width="120" x="20" y="120" as="geometry" />
        </mxCell>
        <mxCell id="8" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="Users" vertex="1">
          <mxGeometry height="20" width="120" x="20" y="160" as="geometry" />
        </mxCell>
        <mxCell id="9" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="Settings" vertex="1">
          <mxGeometry height="20" width="120" x="20" y="200" as="geometry" />
        </mxCell>
        <mxCell id="10" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="Reports" vertex="1">
          <mxGeometry height="20" width="120" x="20" y="240" as="geometry" />
        </mxCell>
        <mxCell id="11" parent="2" style="rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;shadow=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="80" width="190" x="180" y="80" as="geometry" />
        </mxCell>
        <mxCell id="12" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="&lt;b&gt;Total Users&lt;/b&gt;" vertex="1">
          <mxGeometry height="20" width="170" x="190" y="90" as="geometry" />
        </mxCell>
        <mxCell id="13" parent="2" style="text;html=1;fontFamily=Arial;fontSize=20;fontColor=#333333;align=left;;verticalAlign=middle" value="12,847" vertex="1">
          <mxGeometry height="30" width="170" x="190" y="115" as="geometry" />
        </mxCell>
        <mxCell id="14" parent="2" style="rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;shadow=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="80" width="190" x="390" y="80" as="geometry" />
        </mxCell>
        <mxCell id="15" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="&lt;b&gt;Revenue&lt;/b&gt;" vertex="1">
          <mxGeometry height="20" width="170" x="400" y="90" as="geometry" />
        </mxCell>
        <mxCell id="16" parent="2" style="text;html=1;fontFamily=Arial;fontSize=20;fontColor=#333333;align=left;;verticalAlign=middle" value="$48,290" vertex="1">
          <mxGeometry height="30" width="170" x="400" y="115" as="geometry" />
        </mxCell>
        <mxCell id="17" parent="2" style="rounded=1;arcSize=4;fillColor=#F5F5F5;strokeColor=#E0E0E0;strokeWidth=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="250" width="400" x="180" y="180" as="geometry" />
        </mxCell>
        <mxCell id="18" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="&lt;b&gt;Revenue Over Time&lt;/b&gt;" vertex="1">
          <mxGeometry height="20" width="200" x="190" y="185" as="geometry" />
        </mxCell>
        <mxCell id="19" parent="2" style="rounded=0;fillColor=#BDBDBD;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="100" width="40" x="220" y="330" as="geometry" />
        </mxCell>
        <mxCell id="20" parent="2" style="rounded=0;fillColor=#BDBDBD;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="140" width="40" x="280" y="290" as="geometry" />
        </mxCell>
        <mxCell id="21" parent="2" style="rounded=0;fillColor=#BDBDBD;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="90" width="40" x="340" y="340" as="geometry" />
        </mxCell>
        <mxCell id="22" parent="2" style="rounded=0;fillColor=#BDBDBD;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="160" width="40" x="400" y="270" as="geometry" />
        </mxCell>
        <mxCell id="23" parent="2" style="rounded=0;fillColor=#BDBDBD;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="120" width="40" x="460" y="310" as="geometry" />
        </mxCell>
        <mxCell id="24" parent="2" style="rounded=0;fillColor=#BDBDBD;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="80" width="40" x="520" y="350" as="geometry" />
        </mxCell>
        <mxCell id="25" parent="2" style="rounded=1;arcSize=4;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="200" width="400" x="180" y="450" as="geometry" />
        </mxCell>
        <mxCell id="26" parent="2" style="text;html=1;fontFamily=Arial;fontSize=11;fontColor=#333333;align=left;;verticalAlign=middle" value="&lt;b&gt;Recent Orders&lt;/b&gt;" vertex="1">
          <mxGeometry height="20" width="120" x="190" y="455" as="geometry" />
        </mxCell>
        <mxCell id="27" parent="2" style="rounded=0;fillColor=#F5F5F5;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="24" width="400" x="180" y="480" as="geometry" />
        </mxCell>
        <mxCell id="28" parent="2" style="text;html=1;fontFamily=Arial;fontSize=10;fontColor=#333333;align=center;;verticalAlign=middle" value="Order ID" vertex="1">
          <mxGeometry height="20" width="70" x="190" y="482" as="geometry" />
        </mxCell>
        <mxCell id="29" parent="2" style="text;html=1;fontFamily=Arial;fontSize=10;fontColor=#333333;align=center;;verticalAlign=middle" value="Customer" vertex="1">
          <mxGeometry height="20" width="80" x="270" y="482" as="geometry" />
        </mxCell>
        <mxCell id="30" parent="2" style="text;html=1;fontFamily=Arial;fontSize=10;fontColor=#333333;align=center;;verticalAlign=middle" value="Status" vertex="1">
          <mxGeometry height="20" width="70" x="360" y="482" as="geometry" />
        </mxCell>
        <mxCell id="31" parent="2" style="text;html=1;fontFamily=Arial;fontSize=10;fontColor=#333333;align=center;;verticalAlign=middle" value="Amount" vertex="1">
          <mxGeometry height="20" width="80" x="440" y="482" as="geometry" />
        </mxCell>
        <mxCell id="32" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="1" width="400" x="180" y="504" as="geometry" />
        </mxCell>
        <mxCell id="33" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="60" x="190" y="510" as="geometry" />
        </mxCell>
        <mxCell id="34" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="70" x="270" y="510" as="geometry" />
        </mxCell>
        <mxCell id="35" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="50" x="360" y="510" as="geometry" />
        </mxCell>
        <mxCell id="36" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="70" x="440" y="510" as="geometry" />
        </mxCell>
        <mxCell id="37" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="1" width="400" x="180" y="528" as="geometry" />
        </mxCell>
        <mxCell id="38" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="60" x="190" y="534" as="geometry" />
        </mxCell>
        <mxCell id="39" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="70" x="270" y="534" as="geometry" />
        </mxCell>
        <mxCell id="40" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="50" x="360" y="534" as="geometry" />
        </mxCell>
        <mxCell id="41" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="70" x="440" y="534" as="geometry" />
        </mxCell>
        <mxCell id="42" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="1" width="400" x="180" y="552" as="geometry" />
        </mxCell>
        <mxCell id="43" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="60" x="190" y="558" as="geometry" />
        </mxCell>
        <mxCell id="44" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="70" x="270" y="558" as="geometry" />
        </mxCell>
        <mxCell id="45" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="50" x="360" y="558" as="geometry" />
        </mxCell>
        <mxCell id="46" parent="2" style="rounded=0;fillColor=#E0E0E0;strokeColor=none;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="6" width="70" x="440" y="558" as="geometry" />
        </mxCell>
        <mxCell id="47" parent="2" style="rounded=0;fillColor=#37474F;strokeColor=#333333;strokeWidth=1;;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="40" width="600" y="860" as="geometry" />
        </mxCell>
        <mxCell id="48" parent="2" style="text;html=1;fontFamily=Arial;fontSize=9;fontColor=#FFFFFF;align=center;verticalAlign=middle;" value="&amp;copy; 2026 Company Name. All rights reserved." vertex="1">
          <mxGeometry height="40" width="600" y="860" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
``
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
<mxCell id="tbl" style="shape=table;childLayout=tableLayout;startSize=0;collapsible=0;fillColor=none;;verticalAlign=middle" vertex="1" parent="1">
  <mxGeometry x="0" y="0" width="900" height="320" as="geometry"/>
</mxCell>
<mxCell id="r0" style="shape=tableRow;horizontal=0;startSize=0;collapsible=0;;verticalAlign=middle" vertex="1" parent="tbl">
  <mxGeometry width="900" height="40" as="geometry"/>
</mxCell>
<mxCell id="h0" style="text;html=1;;verticalAlign=middle" vertex="1" parent="r0">
  <mxGeometry width="140" height="40" as="geometry"/>
</mxCell>
<mxCell id="h1" value="Order" style="text;align=center;fontStyle=1;fillColor=#e8e8e8;;verticalAlign=middle" vertex="1" parent="r0">
  <mxGeometry x="140" width="380" height="40" as="geometry"/>
</mxCell>
<mxCell id="h2" value="Fulfill" style="text;align=center;fontStyle=1;fillColor=#e8e8e8;;verticalAlign=middle" vertex="1" parent="r0">
  <mxGeometry x="520" width="380" height="40" as="geometry"/>
</mxCell>
<mxCell id="r1" style="shape=tableRow;horizontal=0;startSize=0;collapsible=0;;verticalAlign=middle" vertex="1" parent="tbl">
  <mxGeometry y="40" width="900" height="140" as="geometry"/>
</mxCell>
<mxCell id="a1" value="Customer" style="fillColor=#dae8fc;fontStyle=1;;verticalAlign=middle" vertex="1" parent="r1">
  <mxGeometry width="140" height="140" as="geometry"/>
</mxCell>
<mxCell id="c11" style="fillColor=none;;verticalAlign=middle" vertex="1" parent="r1">
  <mxGeometry x="140" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="n_place" value="Place Order" style="rounded=1;whiteSpace=wrap;html=1;;verticalAlign=middle" vertex="1" parent="c11">
  <mxGeometry x="120" y="40" width="140" height="60" as="geometry"/>
</mxCell>
<mxCell id="c12" style="fillColor=none;;verticalAlign=middle" vertex="1" parent="r1">
  <mxGeometry x="520" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="r2" style="shape=tableRow;horizontal=0;startSize=0;collapsible=0;;verticalAlign=middle" vertex="1" parent="tbl">
  <mxGeometry y="180" width="900" height="140" as="geometry"/>
</mxCell>
<mxCell id="a2" value="System" style="fillColor=#d5e8d4;fontStyle=1;;verticalAlign=middle" vertex="1" parent="r2">
  <mxGeometry width="140" height="140" as="geometry"/>
</mxCell>
<mxCell id="c21" style="fillColor=none;;verticalAlign=middle" vertex="1" parent="r2">
  <mxGeometry x="140" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="n_validate" value="Validate" style="rounded=1;whiteSpace=wrap;html=1;;verticalAlign=middle" vertex="1" parent="c21">
  <mxGeometry x="120" y="40" width="140" height="60" as="geometry"/>
</mxCell>
<mxCell id="c22" style="fillColor=none;;verticalAlign=middle" vertex="1" parent="r2">
  <mxGeometry x="520" width="380" height="140" as="geometry"/>
</mxCell>
<mxCell id="n_ship" value="Ship" style="rounded=1;whiteSpace=wrap;html=1;;verticalAlign=middle" vertex="1" parent="c22">
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





---

---



---

---





---

---





---


---

## §20 Cloud Architecture (3-Tier)

**When to use:** AWS/Azure/GCP infrastructure diagrams - VPC, subnets,
load balancers, compute instances, managed databases.

**Canvas:** 1000x700. Nested containers: VPC > Subnet > Resources.

**Layout conventions:**
- VPC: outermost dashed container (strokeWidth=2)
- Subnets: nested dashed containers inside VPC, distinct fill colors
- Public subnet (green tint): ALB, NAT Gateway
- Private subnet (yellow tint): EC2, containers
- Data subnet (red tint): RDS, ElastiCache
- Users/Internet box outside VPC at top
- Legend: thick line = internet, thin dashed = internal

**Golden XML example (AWS 3-tier, VPC + 3 subnets):**

```xml
<mxGraphModel dx="1413" dy="974" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1000" pageHeight="700" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="vpc" parent="1" style="rounded=1;arcSize=6;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=2;html=1;dashed=1;dashPattern=10 4;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="580" width="920" x="40" y="80" as="geometry" />
        </mxCell>
        <mxCell id="vpc_lbl" parent="1" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" value="VPC (10.0.0.0/16)" vertex="1">
          <mxGeometry height="16" width="200" x="50" y="86" as="geometry" />
        </mxCell>
        <mxCell id="pub_sub" parent="1" style="rounded=1;arcSize=4;fillColor=#E8F5E9;strokeColor=#82B366;strokeWidth=1.5;html=1;dashed=1;dashPattern=6 3;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="160" width="860" x="70" y="130" as="geometry" />
        </mxCell>
        <mxCell id="pub_lbl" parent="1" style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666;align=left;verticalAlign=top" value="Public Subnet (10.0.1.0/24)" vertex="1">
          <mxGeometry height="14" width="180" x="80" y="136" as="geometry" />
        </mxCell>
        <mxCell id="alb" parent="1" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;ALB&lt;/b&gt;&lt;br&gt;Application Load Balancer" vertex="1">
          <mxGeometry height="70" width="200" x="400" y="170" as="geometry" />
        </mxCell>
        <mxCell id="priv_sub" parent="1" style="rounded=1;arcSize=4;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;html=1;dashed=1;dashPattern=6 3;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="160" width="860" x="70" y="320" as="geometry" />
        </mxCell>
        <mxCell id="priv_lbl" parent="1" style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666;align=left;verticalAlign=top" value="Private Subnet (10.0.2.0/24)" vertex="1">
          <mxGeometry height="14" width="180" x="80" y="326" as="geometry" />
        </mxCell>
        <mxCell id="ec2_1" parent="1" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;EC2&lt;/b&gt;&lt;br&gt;Web Server 1" vertex="1">
          <mxGeometry height="80" width="160" x="180" y="360" as="geometry" />
        </mxCell>
        <mxCell id="ec2_2" parent="1" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;EC2&lt;/b&gt;&lt;br&gt;Web Server 2" vertex="1">
          <mxGeometry height="80" width="160" x="420" y="360" as="geometry" />
        </mxCell>
        <mxCell id="ec2_3" parent="1" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;EC2&lt;/b&gt;&lt;br&gt;App Server" vertex="1">
          <mxGeometry height="80" width="160" x="660" y="360" as="geometry" />
        </mxCell>
        <mxCell id="e_alb_1" edge="1" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#666666;strokeWidth=1.5;exitX=0.5;exitY=0.25;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="ec2_1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="400" y="199.97" as="sourcePoint" />
            <mxPoint x="240" y="429.97000000000014" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_alb_2" edge="1" parent="1" source="alb" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#666666;strokeWidth=1.5;exitX=0.5;exitY=1;entryX=0.5;entryY=0;exitDx=0;exitDy=0;entryDx=0;entryDy=0;" target="ec2_2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="490" y="252" as="sourcePoint" />
            <mxPoint x="430" y="447.0000000000001" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_alb_3" edge="1" parent="1" source="alb" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#666666;strokeWidth=1.5;exitX=1;exitY=0.5;entryX=0.5;entryY=0;exitDx=0;exitDy=0;entryDx=0;entryDy=0;" target="ec2_3">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="620" y="199.97" as="sourcePoint" />
            <mxPoint x="860" y="359.97000000000014" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="data_sub" parent="1" style="rounded=1;arcSize=4;fillColor=#FCE4EC;strokeColor=#B85450;strokeWidth=1.5;html=1;dashed=1;dashPattern=6 3;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="130" width="860" x="70" y="510" as="geometry" />
        </mxCell>
        <mxCell id="data_lbl" parent="1" style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666;align=left;verticalAlign=top" value="Data Subnet (10.0.3.0/24)" vertex="1">
          <mxGeometry height="14" width="180" x="80" y="516" as="geometry" />
        </mxCell>
        <mxCell id="rds" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;RDS&lt;/b&gt;&lt;br&gt;Primary" vertex="1">
          <mxGeometry height="70" width="120" x="200" y="545" as="geometry" />
        </mxCell>
        <mxCell id="rds_ro" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="&lt;b&gt;RDS&lt;/b&gt;&lt;br&gt;Read Replica" vertex="1">
          <mxGeometry height="70" width="120" x="440" y="545" as="geometry" />
        </mxCell>
        <mxCell id="e_ec2_rds" edge="1" parent="1" source="ec2_1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#666666;strokeWidth=1.5;dashed=1" target="rds">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="users" parent="1" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#666666;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="Users" vertex="1">
          <mxGeometry height="40" width="160" x="420" y="10" as="geometry" />
        </mxCell>
        <mxCell id="e_users_alb" edge="1" parent="1" source="users" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=2" target="alb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="leg" parent="1" style="rounded=1;arcSize=6;fillColor=#FFFFFF;strokeColor=#999;strokeWidth=1;html=1;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="60" width="180" x="780" y="10" as="geometry" />
        </mxCell>
        <mxCell id="leg_t" parent="1" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;align=left;verticalAlign=middle" value="&lt;b&gt;Legend&lt;/b&gt;" vertex="1">
          <mxGeometry height="14" width="50" x="790" y="12" as="geometry" />
        </mxCell>
        <mxCell id="leg_l1" edge="1" parent="1" style="endArrow=classic;strokeColor=#333333;strokeWidth=2;html=1;verticalAlign=middle" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="795" y="35" as="sourcePoint" />
            <mxPoint x="825" y="35" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_l1t" parent="1" style="text;html=1;strokeColor=none;fontSize=8;fontFamily=Times New Roman;verticalAlign=middle" value="Internet" vertex="1">
          <mxGeometry height="14" width="50" x="830" y="28" as="geometry" />
        </mxCell>
        <mxCell id="leg_l2" edge="1" parent="1" style="endArrow=classic;strokeColor=#666666;strokeWidth=1.5;dashed=1;html=1;verticalAlign=middle" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="795" y="50" as="sourcePoint" />
            <mxPoint x="825" y="50" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_l2t" parent="1" style="text;html=1;strokeColor=none;fontSize=8;fontFamily=Times New Roman;verticalAlign=middle" value="Internal" vertex="1">
          <mxGeometry height="14" width="50" x="830" y="43" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
```

**Key patterns:**
- VPC outermost at x=40, 920px wide
- Subnets: 160px height, 40px gaps
- ALB->EC2 multi-connection: exitY 0.25/0.5/0.75
- Internet=thick solid, internal=thin dashed

**To adapt:** change subnet CIDRs, EC2/RDS count, add NAT/ElastiCache.


---

## §21 BPMN Process (Swimlane)

**When to use:** Cross-functional business process flows - purchase approvals,
hiring pipelines, order fulfillment. Multi-actor workflows with gateways.

**Canvas:** 1200x550. Lanes run horizontally; flow left-to-right within lanes,
top-to-bottom between lanes.

**Layout conventions:**
- Each lane = one actor. Equal height (150px).
- Nodes within lane: x = 120 + col*180, y = 45-55
- Cross-lane edges: parent="1", orthogonal routing
- Gateway at x after last task in deciding lane
- Yes branch goes down to next lane. No branch stays in same lane

**Golden XML example (Purchase Order Approval, 3 lanes):**

```xml
<mxGraphModel dx="1848" dy="1274" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="550" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="lane_emp" parent="1" style="swimlane;startSize=30;horizontal=0;container=1;pointerEvents=0;fillColor=#FCE4EC;strokeColor=#B85450;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;verticalAlign=middle" value="Employee" vertex="1">
          <mxGeometry height="150" width="1200" as="geometry" />
        </mxCell>
        <mxCell id="start" parent="lane_emp" style="ellipse;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1.5;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="36" width="36" x="119" y="57" as="geometry" />
        </mxCell>
        <mxCell id="t1" parent="lane_emp" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="Submit Purchase&lt;br&gt;Request" vertex="1">
          <mxGeometry height="60" width="140" x="210" y="45" as="geometry" />
        </mxCell>
        <mxCell id="e_start_t1" edge="1" parent="1" source="start" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" target="t1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lane_mgr" parent="1" style="swimlane;startSize=30;horizontal=0;container=1;pointerEvents=0;fillColor=#E3F2FD;strokeColor=#6C8EBF;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;verticalAlign=middle" value="Manager" vertex="1">
          <mxGeometry height="150" width="1200" y="150" as="geometry" />
        </mxCell>
        <mxCell id="t2" parent="lane_mgr" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="Review Request" vertex="1">
          <mxGeometry height="60" width="140" x="400" y="45" as="geometry" />
        </mxCell>
        <mxCell id="gw1" parent="lane_mgr" style="rhombus;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.5;perimeter=rhombusPerimeter;html=1;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="50" width="50" x="590" y="50" as="geometry" />
        </mxCell>
        <mxCell id="t4" parent="lane_mgr" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="Notify Employee" vertex="1">
          <mxGeometry height="60" width="140" x="719" y="45" as="geometry" />
        </mxCell>
        <mxCell id="end_no" parent="lane_mgr" style="ellipse;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=2;perimeter=ellipsePerimeter;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="36" width="36" x="920" y="57" as="geometry" />
        </mxCell>
        <mxCell id="e_gw1_no" edge="1" parent="lane_mgr" source="gw1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#B85450;strokeWidth=1.5;exitX=1;exitY=0.5;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="t4" value="Rejected">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="300" y="234.50000000000023" as="sourcePoint" />
            <mxPoint x="445" y="214.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e_t1_t2" edge="1" parent="1" source="t1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" target="t2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_t2_gw1" edge="1" parent="1" source="t2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" target="gw1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lane_fin" parent="1" style="swimlane;startSize=30;horizontal=0;container=1;pointerEvents=0;fillColor=#E8F5E9;strokeColor=#82B366;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;whiteSpace=wrap;html=1;verticalAlign=middle" value="Finance" vertex="1">
          <mxGeometry height="150" width="1200" y="300" as="geometry" />
        </mxCell>
        <mxCell id="t3" parent="lane_fin" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#82B366;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" value="Process Payment" vertex="1">
          <mxGeometry height="60" width="140" x="720" y="45" as="geometry" />
        </mxCell>
        <mxCell id="end_ok" parent="lane_fin" style="ellipse;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=2;perimeter=ellipsePerimeter;verticalAlign=middle" value="" vertex="1">
          <mxGeometry height="36" width="36" x="920" y="57" as="geometry" />
        </mxCell>
        <mxCell id="e_t3_end" edge="1" parent="1" source="t3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" target="end_ok">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_t4_end" edge="1" parent="1" source="t4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#B85450;strokeWidth=1.5" target="end_no">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_gw1_yes" edge="1" parent="1" source="gw1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=0.5;exitY=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitDx=0;exitDy=0;" target="t3" value="Approved">
          <mxGeometry relative="1" x="-0.7391" as="geometry">
            <mxPoint as="offset" />
            <mxPoint x="520" y="370.0000000000001" as="sourcePoint" />
            <mxPoint x="670" y="490" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
```

**Key patterns:**
- Lanes at y=0, 150, 300, equal height
- Lane colors from style-guide §10 (Customer/Internal/Finance)
- Tasks: white fill + lane-specific stroke
- Gateway "Approved" = exitX=1 downward, "Rejected" = exitY=1 rightward
- All edges parent="1" (cross-lane)
- End events: filled red ellipse with perimeter

**To adapt:** change lane names, task labels, decision logic.



---

## §22 System Architecture Overview

**When to use:** System architecture diagrams, infrastructure overviews,
tool/platform architecture, CLI/infrastructure architecture — any
multi-component system with a core engine, supporting side panels, and
layered data flow. This is the most commonly needed template for
general-purpose software architecture diagrams.

**Canvas:** 1100×850. Three-column layout with a main spine plus left
and right side panels.

**Layout conventions:**
- Three zones with clear gaps: Left (supporting context), Center (main
  data flow spine), Right (external systems + extensions).
- Flow direction: top-to-bottom for the main spine. Side panels connect
  horizontally via dashed arrows (context loading / extension).
- All column widths are pre-computed — do NOT adjust ad-hoc. If you need
  more room, scale the entire canvas proportionally.
- Use parent-child containment for section containers. Children use
  coordinates relative to the container's top-left corner.
- Row spacing for spine nodes: 160px between centers. For h=60 nodes,
  this leaves 100px gaps — plenty for arrows and labels.

**Zone partitioning (1100px canvas):**

```
Left:   x=30,  w=300   (Instruction / Config / Input panels)
Center: x=370, w=360   (Main data flow: User → Core → Tools → Storage)
Right:  x=770, w=300   (External APIs, Skills, Extensions)
Gap between columns: 40px
```

**Row grid (main spine nodes, center column):**

```
Row 0: y=40   (User / Entry point)
Row 1: y=200  (Core engine / Orchestrator)
Row 2: y=360  (Processing / Tool layer)
Row 3: y=520  (Storage / Output)
```

**Node sizing:**

| Role | Width | Height |
|------|-------|--------|
| Main spine node (entry, core) | 280 | 56–60 |
| Wide description node (tool system) | 280 | 100–120 |
| Bottom pair (FS, DB, Git) | 130–150 each | 50–56 |
| Side panel container | 280–300 | varies |
| Side panel content node | fill − 30 | 40–50 |

**Color mapping (System Architecture palette):**

| Component | Fill | Stroke |
|-----------|------|--------|
| Core Engine / Orchestrator | `#DAE8FC` | `#6C8EBF` |
| Instruction / Config Layer | `#E1D5E7` | `#9673A6` |
| Tool / Processing Layer | `#D5E8D4` | `#82B366` |
| I/O Boundary (User, FS, DB) | `#F8CECC` | `#B85450` |
| External API / Service | `#FFF2CC` | `#D6B656` |
| Extension / Plugin System | `#FFE6CC` | `#D79B00` |
| Section Container (dashed) | `#F5F5F5` | `#BDBDBD` |

**Edge conventions:**
- Main spine vertical edges: exitX=0.5, exitY=1 → entryX=0.5, entryY=0.
  Solid black, 1.5px.
- Core ↔ API bidirectional: forward solid, reverse dashed. Different
  exitY (0.3 / 0.7). Gold (#D6B656) to match API color.
- Side panel → spine (context/extension): dashed, 1.5px, color matches
  panel theme (purple for instruction, orange for extension).
- Spine → bottom pair: split exitX (0.3 left child, 0.65 right child).

**Golden XML example (CLI tool architecture, 3-column, 11 nodes):**

```xml
<mxfile host="app.diagrams.net">
  <diagram name="System Architecture" id="arch">
    <mxGraphModel dx="1400" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" jumpStyle="arc" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- ===== LEFT: Side Panel Container ===== -->
        <mxCell id="left_panel" value="" style="rounded=1;arcSize=6;container=1;pointerEvents=0;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
          <mxGeometry x="30" y="50" width="300" height="250" as="geometry"/>
        </mxCell>
        <mxCell id="left_lbl" value="Side Panel Title" style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="left_panel">
          <mxGeometry x="10" y="6" width="200" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="left_item1" value="Item A" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="left_panel">
          <mxGeometry x="15" y="36" width="125" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="left_item2" value="Item B" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="left_panel">
          <mxGeometry x="155" y="36" width="130" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="left_item3" value="Item C" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="left_panel">
          <mxGeometry x="15" y="94" width="270" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="left_note" value="Description of this panel&amp;#39;s role" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontStyle=0;fontColor=#888888;align=left;verticalAlign=middle" vertex="1" parent="left_panel">
          <mxGeometry x="15" y="150" width="270" height="30" as="geometry"/>
        </mxCell>

        <!-- ===== CENTER: Main Spine ===== -->
        <mxCell id="spine_entry" value="&lt;b&gt;Entry Point&lt;/b&gt;&lt;br&gt;User / CLI / API Gateway" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=2;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="410" y="40" width="280" height="56" as="geometry"/>
        </mxCell>

        <mxCell id="spine_core" value="&lt;b&gt;Core Engine&lt;/b&gt;&lt;br&gt;Orchestrator · Coordinator" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="410" y="200" width="280" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="spine_processing" value="&lt;b&gt;Processing Layer&lt;/b&gt;&lt;br&gt;Tool A · Tool B · Tool C · Tool D&lt;br&gt;&lt;span style=&quot;font-size:9px;color:#666666&quot;&gt;Description of what this layer does&lt;/span&gt;" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=2;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="410" y="360" width="280" height="110" as="geometry"/>
        </mxCell>

        <mxCell id="spine_output_a" value="&lt;b&gt;Output A&lt;/b&gt;&lt;br&gt;Storage / File" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="410" y="540" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="spine_output_b" value="&lt;b&gt;Output B&lt;/b&gt;&lt;br&gt;External / History" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="560" y="540" width="130" height="50" as="geometry"/>
        </mxCell>

        <!-- ===== RIGHT: External Systems ===== -->
        <mxCell id="right_api" value="&lt;b&gt;External API&lt;/b&gt;&lt;br&gt;Remote Service / Backend" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="770" y="200" width="300" height="56" as="geometry"/>
        </mxCell>

        <mxCell id="right_ext_panel" value="" style="rounded=1;arcSize=6;container=1;pointerEvents=0;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
          <mxGeometry x="770" y="310" width="300" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="right_ext_lbl" value="Extension System" style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="right_ext_panel">
          <mxGeometry x="10" y="6" width="200" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="right_ext_items" value="Plugin A · Plugin B · Plugin C&lt;br&gt;On-demand loaded modules" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="right_ext_panel">
          <mxGeometry x="15" y="36" width="270" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="right_ext_note" value="Location / trigger mechanism&lt;br&gt;How extensions are discovered" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontStyle=0;fontColor=#888888;align=left;verticalAlign=middle" vertex="1" parent="right_ext_panel">
          <mxGeometry x="15" y="96" width="270" height="30" as="geometry"/>
        </mxCell>

        <mxCell id="right_ext2_panel" value="" style="rounded=1;arcSize=6;container=1;pointerEvents=0;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
          <mxGeometry x="770" y="500" width="300" height="100" as="geometry"/>
        </mxCell>
        <mxCell id="right_ext2_lbl" value="External Integration" style="text;html=1;strokeColor=none;fontSize=10;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="right_ext2_panel">
          <mxGeometry x="10" y="6" width="200" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="right_ext2_items" value="Protocol A · Protocol B&lt;br&gt;External Tools &amp;amp; Data Sources" style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=0;fontSize=11;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="right_ext2_panel">
          <mxGeometry x="15" y="30" width="270" height="50" as="geometry"/>
        </mxCell>

        <!-- ===== LEGEND ===== -->
        <mxCell id="legend_box" value="" style="rounded=1;arcSize=6;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=1;html=1;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="30" y="660" width="520" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="legend_title" value="&lt;b&gt;Legend&lt;/b&gt;" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=1;fontColor=#333333;align=left;verticalAlign=top" vertex="1" parent="1">
          <mxGeometry x="42" y="667" width="60" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="leg_solid" style="endArrow=classic;strokeColor=#333333;strokeWidth=1.5;html=1;verticalAlign=middle" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="45" y="698" as="sourcePoint"/><mxPoint x="95" y="698" as="targetPoint"/></mxGeometry>
        </mxCell>
        <mxCell id="leg_solid_t" value="Data / Control Flow" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="105" y="690" width="120" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="leg_api" style="endArrow=classic;strokeColor=#D6B656;strokeWidth=2;html=1;verticalAlign=middle" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="45" y="722" as="sourcePoint"/><mxPoint x="95" y="722" as="targetPoint"/></mxGeometry>
        </mxCell>
        <mxCell id="leg_api_t" value="API Call / Response" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="105" y="714" width="130" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="leg_purple" style="endArrow=classic;strokeColor=#9673A6;strokeWidth=1.5;dashed=1;html=1;verticalAlign=middle" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="255" y="698" as="sourcePoint"/><mxPoint x="305" y="698" as="targetPoint"/></mxGeometry>
        </mxCell>
        <mxCell id="leg_purple_t" value="Context / Config" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="315" y="690" width="110" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="leg_orange" style="endArrow=classic;strokeColor=#D79B00;strokeWidth=1.5;dashed=1;html=1;verticalAlign=middle" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="255" y="722" as="sourcePoint"/><mxPoint x="305" y="722" as="targetPoint"/></mxGeometry>
        </mxCell>
        <mxCell id="leg_orange_t" value="Extension / Plugin" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="315" y="714" width="130" height="16" as="geometry"/>
        </mxCell>

        <!-- Legend color swatches -->
        <mxCell id="c_blue" value="" style="rounded=1;arcSize=3;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1;html=1" vertex="1" parent="1">
          <mxGeometry x="45" y="756" width="16" height="12" as="geometry"/>
        </mxCell>
        <mxCell id="c_blue_t" value="Core Engine" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="67" y="754" width="80" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="c_red" value="" style="rounded=1;arcSize=3;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1;html=1" vertex="1" parent="1">
          <mxGeometry x="155" y="756" width="16" height="12" as="geometry"/>
        </mxCell>
        <mxCell id="c_red_t" value="I/O Boundary" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="177" y="754" width="90" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="c_green" value="" style="rounded=1;arcSize=3;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1;html=1" vertex="1" parent="1">
          <mxGeometry x="275" y="756" width="16" height="12" as="geometry"/>
        </mxCell>
        <mxCell id="c_green_t" value="Tool Layer" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="297" y="754" width="80" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="c_yellow" value="" style="rounded=1;arcSize=3;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1;html=1" vertex="1" parent="1">
          <mxGeometry x="385" y="756" width="16" height="12" as="geometry"/>
        </mxCell>
        <mxCell id="c_yellow_t" value="External API" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="407" y="754" width="90" height="16" as="geometry"/>
        </mxCell>
        <mxCell id="c_orange" value="" style="rounded=1;arcSize=3;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1;html=1" vertex="1" parent="1">
          <mxGeometry x="45" y="780" width="16" height="12" as="geometry"/>
        </mxCell>
        <mxCell id="c_orange_t" value="Extension System" style="text;html=1;strokeColor=none;fontSize=9;fontFamily=Times New Roman;fontColor=#333333;align=left;verticalAlign=middle" vertex="1" parent="1">
          <mxGeometry x="67" y="778" width="110" height="16" as="geometry"/>
        </mxCell>

        <!-- ===== EDGES ===== -->
        <mxCell id="e_entry_core" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=0.5;exitY=1;entryX=0.5;entryY=0" edge="1" parent="1" source="spine_entry" target="spine_core">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e_core_api_out" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#D6B656;strokeWidth=2;exitX=1;exitY=0.3;entryX=0;entryY=0.5" edge="1" parent="1" source="spine_core" target="right_api" value="Request">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e_api_core_back" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#D6B656;strokeWidth=2;exitX=0;exitY=0.7;entryX=1;entryY=0.6;dashed=1" edge="1" parent="1" source="right_api" target="spine_core" value="Response">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e_core_proc" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=0.5;exitY=1;entryX=0.5;entryY=0" edge="1" parent="1" source="spine_core" target="spine_processing">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e_proc_outa" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=0.25;exitY=1;entryX=0.5;entryY=0" edge="1" parent="1" source="spine_processing" target="spine_output_a">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e_proc_outb" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;exitX=0.65;exitY=1;entryX=0.5;entryY=0" edge="1" parent="1" source="spine_processing" target="spine_output_b">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e_left_core" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#9673A6;strokeWidth=1.5;dashed=1;exitX=1;exitY=0.5;entryX=0;entryY=0.25" edge="1" parent="1" source="left_panel" target="spine_core" value="Context">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e_ext_core" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#D79B00;strokeWidth=1.5;dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.8" edge="1" parent="1" source="right_ext_panel" target="spine_core" value="Extends">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e_ext2_proc" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#D79B00;strokeWidth=1.5;dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.7" edge="1" parent="1" source="right_ext2_panel" target="spine_processing" value="Extends">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Key patterns to copy:**
- Three-column zone partitioning with pre-computed widths.
- Main spine: 4 rows at y=40, 200, 360, 540 (160px row spacing).
- Left panel connects to Core with dashed purple → "Context".
- Right API connects to Core with bidirectional gold arrows.
- Extension panels connect via dashed orange → "Extends".
- Tool/processing layer is a single wide node (keep high-level; 7 nodes max).
- Bottom outputs split from processing layer using exitX=0.25/0.65.
- Legend with both edge types and color swatches.
- All container children use relative coordinates with `parent="containerId"`.

**To adapt:**
1. Rename all labels to match your system.
2. Adjust row positions up/down by adding the same offset to all y values.
3. Add/remove side panel items — keep within the panel container's bounds.
4. If you need a 4th row, add `y = (previous_row_y) + 160`.
5. If you need wider columns, scale canvas and recalculate zone widths:
   `col_w = (new_pageWidth - 2*30 - 2*40) / 3`.
6. For systems with no external API, remove the right_api node and its edges.
7. For systems with more side panels, add containers in the right column
   stacked vertically with 40px gaps.
