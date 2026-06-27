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
| Flowchart | Decision trees, process flows, algorithm logic | §6 ⚠️ |
| Entity-Relationship Diagram (ERD) | Database schemas, data models, table relationships | §7 |
| UML Class Diagram | OOP design, architecture modeling, inheritance hierarchies | §8 ⚠️ |
| Sequence Diagram | Protocol interactions, API call flows, message passing | §9 ⚠️ |
| State Machine Diagram | State transitions, formal methods, protocol specifications | §10 ⚠️ |
| Data Flow Diagram (DFD) | Software engineering, system data flows, process modeling | §11 |
| Swimlane Diagram | Cross-functional process flows, RACI charts | §17 ⚠️ |
| Wireframe / Mockup | App screens, website layouts, UI prototypes | §18 |

⚠️ = moderate quality degradation risk for hand-written XML
⚠️ = high risk (consider using draw.io Mermaid import instead)

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



---

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
`gap = (pageWidth - n * w) / (n + 1)` for n equally-spaced stages.



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
at (40, 60), (560, 60), (560, 460), (40, 460) for an 8-node star.



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
Y shifts), rename labels, optionally use different fill colors for
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
- Processes form the central hub — data flows IN from entities,
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

**To adapt:** change labels, add/remove levels, switch TB to LR by
swapping x/y logic.

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
> check-refine loop helps but has a hard 3-iteration cap. For production
> swimlane diagrams, consider using draw.io's built-in **Arrange → Insert
> → Advanced → Mermaid** import instead, which auto-layouts perfectly.

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
| Lane |  | One per actor |
| Start |  | Leftmost in first lane |
| End |  | One per terminal |
| Process |  | White fill, stroke=owning lane color |
| Decision |  | 1 input, 2 outputs |

### Lane color palette (official draw.io pastels)

| Role | Lane fill | Lane stroke | Node stroke |
|------|-----------|-------------|-------------|
| Customer/Client |  |  |  |
| Internal system |  |  |  |
| Payment/Finance |  |  |  |
| Warehouse/Ops |  |  |  |
| External partner |  |  |  |
| Generic |  |  |  |

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