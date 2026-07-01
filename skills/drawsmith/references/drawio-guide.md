# Draw.io Diagram Reference

## Index

- [Workflow](#workflow-mandatory) — Phase 1-3 planning loop
- [XML Skeleton](#xml-skeleton) — bare minimum mxfile structure
- [Flow Direction](#flow-direction-read-first----most-common-failure-mode) — bottom-to-top rule (most common failure mode)
- [Cross-Stack Y-Alignment](#cross-stack-y-alignment) — encoder-decoder horizontal edge alignment
- [Design Philosophy](#design-philosophy) — Concise, Clear, Consistent (Three Cs)
- [Shape type conventions](#shape-type-conventions) — built-in shapes, never approximate
- [Hard Rules](#hard-rules-always-enforced) — 22 hard rules
- [Section Container Layout](#section-container-layout) — labels inside containers, no overlap
- [XML Escapes](#xml-escapes) — `&amp;`, `&lt;`, `&#xa;`, etc.
- [Layout Rules](#layout-rules) — spacing, margins, line limits
- [Arrow Routing](#arrow-routing) — self-loops, bidirectional, cross-panel waypoints
- [Visual Style Guide](#visual-style-guide) — references `style-guide.md` for colors/fonts/weights
- [Common Pitfalls](#common-pitfalls-real-failures-from-past-generations) — 14 real failures and their fixes
- [Self-Check](#self-check-output-passfail-for-each) — 15-item output checklist

---

## Reasoning Budget (READ FIRST)

Your job is to declare the LOGICAL STRUCTURE of the diagram -- what nodes
exist, what edges connect them, what labels they carry.

- Identify diagram type + actors/stages (1-2 sentences)
- Place nodes on the grid: x = col * 180 + 40, y = row * 120 + 40
- For simple edges (1-to-1, clear path): declare source/target only
- For self-loops, bidirectional pairs, cross-panel edges: ADD waypoints
  (see Arrow Routing section for exact patterns)
- Go straight to XML. Do NOT compute coordinates in prose

## Design Philosophy

Every diagram must be Concise, Clear, and Consistent (draw.io official).

- Concise: Only what is necessary. One abstraction level per diagram —
  high-level overview OR detailed drill-down, never both. 7 nodes max for overview.
- Clear: Understandable in 30 seconds by a new reader. Every color, shape,
  and line style must be defined in a legend.
- Consistent: Same shape for same element type. Same color for same meaning
  throughout the diagram.

## Shape type conventions

Use draw.io built-in shape styles — do not approximate with rectangles.

| Concept | Style | When |
|---------|-------|------|
| Process / action | `rounded=1;arcSize=8` | Normal step |
| Decision / branch | `rhombus;perimeter=rhombusPerimeter` | Yes/No split — perimeter is REQUIRED |
| Start | `ellipse;fillColor=#D5E8D4;perimeter=ellipsePerimeter` | One per diagram |
| End / terminal | `ellipse;fillColor=#F8CECC;perimeter=ellipsePerimeter` | One per path |
| Swimlane | `swimlane;startSize=30` | Cross-functional lanes |
| Database | `shape=cylinder3` | Persistent storage |
| Document | `shape=document` | Report, invoice |
| I/O | `shape=parallelogram;perimeter=parallelogramPerimeter` | External data |

## Style Properties

| Property | Values | Use for |
|----------|--------|---------|
| `rounded=1` | 0 or 1 | Rounded corners |
| `whiteSpace=wrap` | wrap | Text wrapping |
| `fillColor=#dae8fc` | Hex color | Background color |
| `strokeColor=#6c8ebf` | Hex color | Border color |
| `fontColor=#333333` | Hex color | Text color |
| `fontStyle=0` | bitmask: 0=normal, 1=bold, 2=italic, 4=underline | Font style; combine via OR (3=bold+italic) |
| `html=1` | 0 or 1 | Enable HTML rendering in labels (`<b>`, `<br>`, etc.) |
| `shape=cylinder3` | shape name | Database cylinders |
| `ellipse` | style keyword | Circles/ovals |
| `rhombus` | style keyword | Diamonds |
| `edgeStyle=orthogonalEdgeStyle` | style keyword | Right-angle connectors |
| `dashed=1` | 0 or 1 | Dashed lines |
| `swimlane` | style keyword | Swimlane containers |
| `group` | style keyword | Invisible container |
| `container=1` | 0 or 1 | Make any shape a container |
| `pointerEvents=0` | 0 or 1 | Prevent container from capturing child connections |
| `perimeter=ellipsePerimeter` | perimeter name | Edge attachment to shape boundary (not bbox) |
| `light-dark(#ABC,#DEF)` | CSS function | Explicit dark mode color |

**Dark mode:** Set `adaptiveColors="auto"` on `<mxGraphModel>`. Colors
auto-invert. Use `light-dark(lightColor,darkColor)` only when the automatic
inverse is unsatisfactory.


## Workflow (MANDATORY)

### Phase 1 — Plan (output these before any XML)

**1. Figure purpose** (one sentence)

**2. Figure type** — `pipeline` | `architecture` | `comparison` | `flowchart` | `taxonomy`

**3. Canvas** — `pageWidth` × `pageHeight` (A4: 827×1169; wider: scale up)

**4. Layout zones**
```
Zone A: x=... y=... w=... h=...   (what goes here)
Zone B: x=... y=... w=... h=...   (what goes here)
```

**5. Node table**
```
id | label | x | y | w | h | role
```

**6. Edge table**
```
id | source | target | style (solid/dashed)
```

Proceed to Phase 2 only after layout is confirmed.

### Phase 2 — Generate XML

Follow the rules below. Generate ALL vertex cells first, then ALL edge cells.

### Phase 3 — Self-check

Run the checklist and report each item `pass/fail`.

---

## XML Skeleton

```xml
<mxfile host="app.diagrams.net">
  <diagram name="Figure" id="fig">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="1200" pageHeight="800" jumpStyle="arc"
                  math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Orthogonal edge routing (base style for ALL edges):**

Use `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;`
as the base style. Add `endArrow=classic` for forward edges, `endArrow=none` for
hierarchy lines. The built-in router produces STRAIGHT or simple right-angle paths
with NO obstacle avoidance. For visible, clean routing, add waypoints in these cases:
self-loops, bidirectional pairs, and cross-panel edges (see Arrow Routing section).

```xml
<!-- Standard forward edge -->
<mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="node_a" target="node_b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Simple same-region edges need only `source`/`target`. Use `exitX`/`exitY` when
2+ connections leave the same node side. Add `dashed=1` for skip/residual edges,
`curved=1` for self-loops.

### Edge style variants

| Style | When |
|-------|------|
| `edgeStyle=orthogonalEdgeStyle` | Default for all diagrams |
| `edgeStyle=entityRelationEdgeStyle` | ER diagrams - perpendicular stubs |

## Grid Coordinate System

Use this rigid grid to eliminate position guessing. Every node at standard
coordinates prevents overlap structurally.

| Node type | Width | Height | Notes |
|-----------|-------|--------|-------|
| Standard process | 140 | 60 | Rounded rect |
| Wide process | 200 | 60 | For longer labels |
| Decision (rhombus) | 140 | 80 | Add perimeter=rhombusPerimeter |
| Start/End ellipse | 60 | 60 | Circle, perimeter=ellipsePerimeter |
| Database cylinder | 120 | 80 | shape=cylinder3 |

Column formula: x = col_index * 180 + 40 (col 0=40, 1=220, 2=400...)
Row formula: y = row_index * 120 + 40 (row 0=40, 1=160, 2=280...)

For layered diagrams, each tier = one row. For pipelines, each stage = one column.
For swimlanes, nodes within a lane share y and increment x.

## Flow Direction (READ FIRST — most common failure mode)

**ML architecture diagrams flow BOTTOM-TO-TOP by convention.** This is the
single most common thing models get wrong. The Vaswani 2017 Transformer figure,
ResNet figures, every textbook RNN diagram — input at the bottom, output at the
top, arrows pointing UP.

**The rule, mechanically:**

1. The FIRST computation in a stack (input embedding, layer 1) gets the
   LARGEST y-coordinate (bottom of the section).
2. The LAST computation (final projection / softmax / output) gets the
   SMALLEST y-coordinate (top of the section).
3. Every forward arrow points UP: `source.y > target.y`.
4. When you write the Phase 1 node table, list rows in DATA-FLOW ORDER
   (input first, output last), then assign y values in DECREASING order.

**Why this trips models up:** Reading order is top-to-bottom, so the natural
instinct is to put "layer 1" at the top of your text plan and the small y
values. That puts the encoder upside-down. Resist it.

**Concrete example for Transformer encoder (encoder section spans y=300..580):**

```
data-flow order               y assignment (decreasing)
1. Input Embedding             y = 870  (BELOW the section)
2. Encoder MHA                 y = 540
3. Add & Norm 1                y = 470
4. Feed Forward                y = 400
5. Add & Norm 2                y = 330  (TOP of stack)
```
Input at largest y, output at smallest y. Every forward arrow: source.y > target.y.

The encoder OUTPUT (Add & Norm 2) is at the TOP and feeds K,V to the decoder
cross-attention. The encoder INPUT enters at the BOTTOM. Source tokens and
embeddings sit BELOW the encoder section, with arrows pointing UP into it.

The output stack (Linear → Softmax → Output Probabilities) sits ABOVE the
decoder, ordered the same way: Linear at the bottom (closest to decoder),
Output Probabilities at the top.

**Quick self-test** — before writing XML, scan your node table:
- For every adjacent pair `A → B` in your data-flow order, check `A.y > B.y`.
- If any pair fails, your stack is inverted. Fix it before generating XML.

**When NOT to use bottom-up:** Pipeline / system / data-flow diagrams (not ML
architectures) typically flow LEFT-TO-RIGHT. Use the same logic with x instead
of y: source on the left, target on the right, every forward arrow has
`source.x < target.x`. Don't mix LR and TB in one figure.

**Quick self-test** — before writing XML, scan your node table:
- For every adjacent pair A -> B in data-flow order, check A.y > B.y (TB) or A.x < B.x (LR).
- If any pair fails, the stack is inverted. Fix before generating XML.

**When NOT to use bottom-up:** Pipeline / system / data-flow diagrams (not ML
architectures) typically flow LEFT-TO-RIGHT. Use the same logic with x instead
of y: source on the left, target on the right, every forward arrow has
`source.x < target.x`. Don't mix LR and TB in one figure.

## Cross-Stack Y-Alignment

For encoder-decoder diagrams, align the Y-coordinates of layers connected by
horizontal arrows so the connection is a clean horizontal line, not a diagonal
or a multi-waypoint detour.

**The K,V cross-attention case** — encoder output (Add & Norm at the top of
the encoder stack) feeds into decoder cross-attention. Set:

```
enc_an_top.y == dec_cross_attn.y   (same Y center, different X)
```

A direct edge with `exitX=1;exitY=0.5;entryX=0;entryY=0.5` then renders as a
straight horizontal arrow with no waypoints needed. If the Y values can't
match exactly (different module heights), pad with vertical whitespace inside
the decoder so the cross-attention center lines up with the encoder output
center.

**The encoder-output → linear case** — when both the decoder top and the
output stack are visible, position the output stack so its bottom (Linear)
aligns with the decoder top (Add & Norm). Same trick: direct edge, no
waypoints.

If alignment is genuinely impossible (e.g. asymmetric stacks), use ONE
waypoint at the midline x between stacks, never multiple waypoints chasing
a node center.

## Hard Rules (always enforced)

1. `id="0"` and `id="1"` always present as first two cells
2. Every vertex HAS `<mxGeometry x y width height as="geometry"/>`
3. Every edge HAS `<mxGeometry relative="1" as="geometry"/>` — self-closing edges are INVALID
4. Edge `source`/`target` must reference existing vertex IDs
5. IDs unique, semantic, lowercase_underscore — no random strings
6. Use the rigid grid for placement: column x = col_index * 180 + 40,
   row y = row_index * 120 + 40. All coordinates MUST be multiples of 10.
   Node sizes: rectangles 140x60, diamonds 140x80, circles 60x60, documents
   120x80, cylinders 120x80. Exact grid placement prevents overlap by construction.
7. All elements within page bounds (x+w ≤ pageWidth, y+h ≤ pageHeight)
8. Uncompressed XML only (no `compressed="true"`)
9. No `--` in XML comments
10. **Flow direction consistent** — every forward edge satisfies `source.y > target.y` for TB diagrams or `source.x < target.x` for LR diagrams. If not, the stack is inverted.
11. **Use native shape types** — process: `rounded=1`, decision: `rhombus`,
    start/end: `ellipse`, DB: `shape=cylinder3`. Never approximate semantic
    shapes with plain rectangles.
12. **Parent-child for containers** — when a shape belongs inside another
    (swimlane lane, section group), set `parent="container_id"`. Child
    coordinates are RELATIVE to container top-left. Moving the container
    moves all children automatically.
13. **Cross-container edges at root** — edges between nodes in different
    containers use `parent="1"` (root level). Otherwise connectors are
    clipped to the source container bounding box.
22. **Single abstraction level** — a diagram is EITHER high-level overview
    (7 nodes max) OR detailed drill-down, never both mixed. Use sub-pages
    for detail layers.
22. **No-Overlap** — no two vertex bounding boxes may intersect, with one allowed exception: a *section container* may contain modules whose bbox is FULLY INSIDE the container's bbox (with ≥10px padding on all four sides). Edges (arrows) are exempt from this rule. See § Section Container Layout for the exact pattern.
22. **I/O direction consistent** — every component uses fixed entry/exit
    sides. Pick one convention per diagram: top-in-bottom-out (default for
    layered architectures), left-in-right-out (pipelines). Never mix entry
    directions on the same component.
22. **One color = one link type** — each color encodes exactly one semantic role. Never reuse the same color for unrelated link types. If two things are different concepts, use different colors. Max 6 distinct colors per diagram.
22. **Allocate space by edge density** — widen the vertical gap where edges are densest. A tier with 10+ crossing edges needs 2× the gap of a tier with 2 edges. Never give blank space to a low-density region while edges pile up in a narrow corridor.
22. **Grid is a user preference** — default to `grid=1` with `gridSize=10` (visible, helpful for editing). If the user requests grid-off, set `grid=0`. The grid is an alignment tool that many users find useful during review. Do not force it off unless asked.
22. **Uniform line weight** — all edges in the same diagram use the same `strokeWidth` (default 1.5). Differentiate link types by color and dash pattern, not by thickness. Exception: emphasis arrows (e.g., primary data flow) may use `strokeWidth=2.5`.
22. **No decorative containers** — every dashed box or container must be defined in the legend. If a box has no semantic meaning, remove it. Containers exist to group related components or mark a boundary — not for visual decoration.
22. **Jump-over on crossings** — add `jumpStyle=arc` to the `<mxGraphModel>` element to enable automatic arc jumps where edges cross. draw.io renders a small arch so the crossing lines are visually distinct. Without this, every crossing looks like a junction.

## Section Container Layout

Section containers (the dashed gray boxes around encoder/decoder/etc.) are
the most common source of card overlap. Past failures placed section labels
ABOVE their containers, where they intrude on the container of the section
above. Use this pattern instead:

**1. Label INSIDE the container, top-left corner.** Not above. Pattern:

```xml
<mxCell id="enc_sec" value="" style="rounded=1;arcSize=6;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
  <mxGeometry x="40" y="200" width="320" height="260" as="geometry"/>
</mxCell>
<mxCell id="enc_lbl" value="Encoder  × N" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="1">
  <mxGeometry x="50" y="206" width="200" height="16" as="geometry"/>
</mxCell>
```

Label `x` = container.x + 10, `y` = container.y + 6, `align=left`,
`verticalAlign=top`, height 16-18px. Label is fully inside container. Container labels are the ONE exception to `verticalAlign=middle` — they use `verticalAlign=top` for top-left placement. All content nodes use `verticalAlign=middle`.

**2. Container padding ≥10px on all sides.** First module's `y` =
container.y + 10 (or +28 if a top-left label takes the first 18px row).
Last module's `y + h` = container.y + container.h − 10. Modules' `x`
≥ container.x + 10 and `x + w` ≤ container.x + container.w − 10.

**3. Section gap ≥30px between adjacent containers.** For two stacked
sections A (above) and B (below), require `B.y − (A.y + A.h) ≥ 30`. Same
horizontally for side-by-side sections.

**4. Drop containers for 2-3 module groups.** Output stack
(Linear/Softmax/Output Probabilities) and input stack (Token/Embedding/
PosEnc) are usually only 3 modules. Skip the dashed container — just float
the modules. Color coding (input red, output yellow) already conveys their
role. This eliminates a whole class of overlap bugs.

**5. When you DO use a container, only for repeated blocks.** Encoder ×N
and decoder ×N benefit from containers because the `× N` annotation lives
in the section label. Single-use groups don't.

## Parent-Child Containment (alternative to absolute coordinates)

For diagrams where modules are logically INSIDE a container (encoder
modules inside the encoder section, services inside a swimlane, etc.),
use drawio's native parent-child nesting. This is cleaner than absolute
coordinates because:

- Children use coordinates **relative to the container's top-left corner**
  (e.g., `x="20" y="40"` means "20px inside from the container's left,
  40px down from its top").
- Moving the container automatically moves all children.
- Overlap is structurally impossible — the parent IS the bounding box.
- Section labels can sit inside at `parent="containerId"` with
  `x="10" y="6"`.

**Required attributes for the container:**

```
container=1;pointerEvents=0;
```

`container=1` makes the shape accept children. `pointerEvents=0`
prevents the container from intercepting clicks/connections meant for
child nodes.

```xml
<!-- Container (parent="1" — top-level) -->
<mxCell id="enc_sec" value="" style="rounded=1;arcSize=6;container=1;pointerEvents=0;fillColor=#F5F5F5;strokeColor=#BDBDBD;strokeWidth=1.5;html=1;dashed=1;dashPattern=10 4" vertex="1" parent="1">
  <mxGeometry x="40" y="390" width="320" height="260" as="geometry"/>
</mxCell>

<!-- Label INSIDE the container (parent="enc_sec", relative coords) -->
<mxCell id="enc_lbl" value="Encoder  × N" style="text;html=1;strokeColor=none;fontSize=11;fontFamily=Times New Roman;fontStyle=2;fontColor=#666666;align=left;verticalAlign=top" vertex="1" parent="enc_sec">
  <mxGeometry x="10" y="6" width="200" height="16" as="geometry"/>
</mxCell>

<!-- Module INSIDE the container (parent="enc_sec", relative coords) -->
<mxCell id="enc_mha" value="Multi-Head Self-Attention" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.5;fontFamily=Times New Roman;fontStyle=1;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle" vertex="1" parent="enc_sec">
  <mxGeometry x="20" y="200" width="280" height="50" as="geometry"/>
</mxCell>
```

**Conversion rule:** relative_x = absolute_x - container.x. The resulting
layout is identical to the absolute-coordinate approach, but moving the
container to a different canvas position only requires changing the
container's `x`/`y`.

**When to use parent-child:** the general layout and classic diagram
templates (§5–§15) use this. The specific architecture templates (§1–§4)
use absolute coordinates — both are valid; parent-child is recommended
for new diagrams.

## Layers

Layers control visibility and z-order. Useful for diagrams with distinct
conceptual groupings that viewers may want to toggle independently.

- A layer is an `mxCell` with `parent="0"` and no `vertex`/`edge` attribute
- Assign shapes to a layer by setting `parent` to the layer's id
- Later layers render on TOP of earlier layers (higher z-order)
- Add `visible="0"` on the layer cell to hide it by default

```xml
<mxCell id="2" value="Annotations" parent="0"/>
<mxCell id="10" value="Server" style="rounded=1;html=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="20" value="Note" style="text;" vertex="1" parent="2">
  <mxGeometry x="100" y="170" width="120" height="30" as="geometry"/>
</mxCell>
```

## Tags

Tags enable cross-cutting visibility filters - unlike layers, one element can
have multiple tags. Tags require wrapping `mxCell` in an `<object>` element with
the `tags` attribute (space-separated):

```xml
<object id="2" label="Auth Service" tags="critical v2">
  <mxCell style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
    <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
  </mxCell>
</object>
```

- The `label` attribute on `<object>` replaces `value` on `mxCell`
- Viewers filter by tag in the draw.io UI (Edit > Tags)

## Metadata & Placeholders

Metadata attaches custom key-value properties to shapes via the `<object>`
wrapper. Combined with placeholders (`%key%` in labels), this enables
data-driven labels (status, owner, IP, version). Set `placeholders="1"` on
`<object>` to enable substitution:

```xml
<object id="2" label="&lt;b&gt;%component%&lt;/b&gt;&lt;br&gt;Owner: %owner%"
        placeholders="1" component="Auth Service" owner="Team Backend">
  <mxCell style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
    <mxGeometry x="100" y="100" width="160" height="80" as="geometry"/>
  </mxCell>
</object>
```

Predefined placeholders (no custom properties needed): `%id%`, `%date%`,
`%time%`, `%page%`, `%pagenumber%`, `%filename%`.

## XML Escapes

| Char | Write as |
|------|----------|
| `&` | `&amp;` |
| `<` | `&amp;#60;` (or `&amp;lt;`) | Use numeric ref for safety inside `html=1` |
| `>` | `&amp;#62;` (or `&amp;gt;`) | Numeric ref avoids being parsed as HTML tag |
| `"` | `&quot;` |
| newline | `&#xa;` |

HTML tags in `value` supported with `html=1`, must be XML-escaped:
`&lt;b&gt;Bold&lt;/b&gt;` `&lt;br&gt;` `&lt;sub&gt;x&lt;/sub&gt;`

## Layout Rules

**Spacing scales with diagram complexity.** Don't use the same gap for a
5-node stack and a 30-node pipeline.

| Nodes | X gap (LR) | Y gap (TB) | Notes |
|---|---|---|---|
| ≤5 | 200px | 150px | Tight stacks, adjacent arrows are short |
| 6–10 | 280px | 200px | Standard paper figure |
| >10 | 350px | 250px | Needs routing corridors between rows |

**Routing corridors:** between densely-packed rows, leave ~80px of clear
vertical/horizontal space where edges can route without crossing shapes.
Don't place small nodes in corridors.

- Content 65-80% of canvas, 20-35% whitespace
- External margin ≥40px, zone gap 40-80px
- **Vertical gap between stacked modules: 24-30px** — shorter than 20px makes arrow shafts invisible
- Same-tier nodes share Y (LR flow) or X (TB flow), equal size
- Main flow direction consistent — don't mix LR and TB in one figure
- No arrow passes through a shape (orthogonal routing helps with this)
- Max 2 line crossings per edge (use jump-over for unavoidable crosses)
- 3 lines max per node, 25 chars/line English

## Professional Layout Principles

These rules prevent the most common failures observed in hand-written
diagrams: edge spaghetti, unbalanced spacing, and invisible semantics.

### Bus-style routing for parallel edges

When 3+ edges travel the same direction between two tiers, merge them
into a single "bus" channel rather than drawing N independent zigzag
lines. The bus is a horizontal or vertical corridor through which all
parallel edges run, branching off only near the source/target component.

Pattern: source nodes → short vertical stub → horizontal bus channel →
short vertical stub → target nodes. The bus channel sits in the routing
corridor between tiers, keeping the dense edge region clean.

```xml
<!-- 4 services each produce to Kafka: all route through a shared bus at y=240 -->
<mxCell id="e_us_p" style="...exitX=0.5;exitY=1;entryX=0.08;entryY=0" ...>
  <mxGeometry relative="1" as="geometry">
    <Array as="points"><mxPoint x="170" y="240"/><mxPoint x="110" y="240"/></Array>
  </mxGeometry>
</mxCell>
```

### Space allocation by density

| Zone | Guidance |
|------|----------|
| 10+ edges crossing | gap ≥ 160px |
| 5-10 edges | gap ≥ 100px |
| 1-4 edges | gap ≥ 60px |
| No edges | gap = 30-40px |

Measure the gap, count the edges that cross it, apply the table. Never
give blank space to a low-density tier while high-density tiers choke.

### I/O direction convention

Every component in a layered diagram uses the SAME entry and exit sides.
For layered (top-down) diagrams: entry at top, exit at bottom. This lets
readers identify data flow direction from the arrow-entry side alone.

```
Good (uniform):                    Bad (chaotic):
All services take input from top    Service A: input from top
All services send output to bottom  Service B: input from left
                                    Service C: output to right
```

### Component alignment

All components in the same tier share the SAME height and vertical
center. Horizontal spacing is uniform — use the draw.io Arrange →
Distribute Horizontally function (or compute `gap = (pageW - N*w)/(N+1)`).

### Tier labels

Add a small grey italic label to the left of each tier (e.g., "Entry",
"Services", "Infrastructure", "Storage"). This gives the reader a mental
map before they inspect individual components.

## Arrow Routing

**CRITICAL: draw.io's built-in router is unreliable.** It produces:
- Invisible arrows (gap < 30px between nodes)
- Overlapping bidirectional edges (same exitY)
- Self-loops that hug the node (invisible)
- Straight lines cutting through shapes

You MUST hand-route edges in these cases. Follow the patterns below,
verified through real production use.

### Edge style (always choose one, consistent per diagram):

| Style | Syntax | Best for |
|-------|--------|---------|
| Orthogonal | `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;` | Default for most diagrams |
| Straight | no `edgeStyle` key | UML class/sequence, direct connections |
| Entity Relation | `edgeStyle=entityRelationEdgeStyle` | ER diagrams |

### Self-loops (CRITICAL — must be visible)

Self-loops with `curved=1` alone produce invisible, node-hugging arcs.
ALWAYS add TWO waypoints to pull the loop OUT from the node:

```xml
<mxCell id="e_self" value="tick / update()"
  style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5;curved=1;exitX=0;exitY=0.5;entryX=0;entryY=0.75"
  edge="1" parent="1" source="running" target="running">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="350" y="215"/>
      <mxPoint x="350" y="235"/>
    </Array>
  </mxGeometry>
</mxCell>
```

Waypoint formula for a node at (nx, ny, nw, nh):
- wp1: x = nx - 40, y = ny - 10   (above-left of node)
- wp2: x = nx - 40, y = ny + nh + 10  (below-left of node)
- exitX=0, exitY=0.5, entryX=0, entryY=0.75

### Bidirectional Pairs (must be offset)

When A->B and B->A both exist, offset exitY so they run as parallel tracks:

```
Forward:  exitX=1; exitY=0.35; entryX=0; entryY=0.35
Reverse:  exitX=0; exitY=0.65; entryX=1; entryY=0.65; dashed=1
```

### Cross-panel Routing (avoid obstacles)

When an edge must cross the diagram (e.g., error->idle reset), use waypoints
to route through clear space. Keep waypoints outside all node bounding boxes:

```xml
<mxCell id="e_cross" style="...exitX=0;exitY=0.5;entryX=0;entryY=0.5"
  edge="1" parent="1" source="src" target="tgt">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="387" y="471"/>
      <mxPoint x="190" y="471"/>
    </Array>
  </mxGeometry>
</mxCell>
```

### Minimum Arrow Length

Node-to-node gap MUST be >= 30px. At < 30px the arrow shaft is invisible.
Use this spacing: nodes with h=50-80 → gap >= 50px; nodes with h=30 → gap >= 35px.

### Multi-Connection Nodes

When 3+ edges connect to the same side of a node, distribute exitY values
evenly across [0,1]. Same exitY on the same side = invisible overlap:
```
N=2: 0.3, 0.7
N=3: 0.2, 0.5, 0.8
N=4: 0.15, 0.4, 0.6, 0.85
```

Edge labels: short (1-3 words). Set `value` directly on the edge cell.

## Visual Style Guide

For typography, stroke weights, color palettes, and resolution standards,
see `references/style-guide.md`. The style guide is the single source of
truth shared across draw.io diagrams and matplotlib charts.

draw.io-specific style notes:
- `fontStyle` bitmask: 0=normal, 1=bold, 2=italic, 4=underline; 3=bold+italic
- Use Unicode symbols (📐 ⚡ 🧪 ✗ ✓ ▲) as visual tags
- Legend required when colors/lines encode meaning

## Common Pitfalls (real failures from past generations)

These are the failure modes most often seen in generated diagrams. Scan for
them before writing XML and re-check after.

**1. Inverted stack** — first sub-layer placed at the smallest y, arrows
point downward through the stack. Symptom: in a Transformer encoder you have
`enc_mha (y=310) → enc_an1 (y=380) → enc_ff (y=440) → enc_an2 (y=510)` and
the encoder INPUT is below at y=730 with an arrow going UP into MHA at the
top. This is wrong. Reason: data flows bottom-to-top, so `enc_mha` (first
sub-layer) belongs at the LARGEST y inside the encoder, `enc_an2` at the
smallest. See Flow Direction at the top of this file.

**2. Output stack ordered by reading order, not data flow** — Linear at top
y, Softmax middle, "Output Probabilities" at bottom y, with arrows going
DOWN. Wrong: Output Probabilities is the FINAL output and belongs at the
SMALLEST y (top of canvas). Order from bottom to top should be: decoder
top → Linear → Softmax → Output Probabilities.

**3. e_out connects to wrong source** — the edge from decoder to Linear is
sourced from the FIRST decoder sub-layer (e.g. `dec_mmha`) instead of the
LAST one (the topmost Add & Norm). Symptom: a long edge with 3+ waypoints
wrapping around the diagram. Fix: the edge source is the node with the
SMALLEST y inside the decoder stack (the "top" of the stack = the last
computation in data-flow order).

**4. Input section internally inverted** — Source Tokens at smaller y
than Input Embedding, with arrow tokens→embedding going DOWN. Wrong:
embedding processes tokens, so embedding is the next step and belongs ABOVE
tokens (smaller y). Same rule applies to (token → embedding → positional
encoding) — list in data-flow order, assign decreasing y.

**5. Cross-stack Y misalignment** — encoder output at y=510, decoder
cross-attention at y=440. The K,V edge between them needs waypoints to
route the 70px height difference, producing a visible jog. Fix: make
`enc_an_top.y == dec_cross_attn.y` (set the same y center), then a direct
horizontal edge with `exitX=1;entryX=0` renders cleanly with no waypoints.

**6. Section header collision with neighbor section** — older diagrams
placed section labels ABOVE their container (e.g. label y = container.y −
22), which intruded into the section above when sections were stacked
close together. Wrong. Place labels INSIDE the container at top-left
(label x = container.x + 10, y = container.y + 6, with `align=left;
verticalAlign=top`). See § Section Container Layout for the full pattern.

**7. Double-escaped HTML in `value`** — writing `Add &amp;amp; Norm` when
you only meant one level of escape. Inside `value="..."` with `html=1`,
write `&amp;` for a literal `&` (XML-level escape). Drawio renders that
as `&`. Writing `&amp;amp;` displays as `&amp;` — the literal HTML entity
text shown to the reader. Use `&amp;` once, not twice.

**8. Arrow overlap at multi-connection nodes** — when 3+ edges connect to
the same side of a node (common in pipeline hubs, git workflows, system
overviews), all edges route to the center and overlap visually. Fix:
distribute `exitY` values evenly across the [0,1] range for each edge —
see § Arrow Routing → Multi-Connection Nodes for the distribution table.
Scan for nodes with degree >= 3 on any side; verify each edge has a
distinct exit/entry coordinate.

**9. Bidirectional edge pairs collide** — when two nodes have both a forward
(A→B) and reverse (B→A) edge (e.g., push/pull, request/response), both
edges route through the same centerline and overlap. Fix: offset the two
edges vertically so they run as parallel tracks (`exitY=0.35` for forward,
`exitY=0.65` for reverse). See § Arrow Routing → Bidirectional Edge Pairs
for the exact pattern.

**10. Edges take scenic detours** (legacy concern — automatic routing via libavoid/ELK eliminates this). Edges route around the outside of the
diagram with 3-4 unnecessary waypoints when a short direct connection
exists. Symptom: a produce arrow from a service to a component directly
below it takes a path that goes up to the tier above, then horizontal,
then back down — tripling the line length. Fix: every edge should be the
shortest orthogonal path. If the source and target are vertically aligned,
route straight down. Only add waypoints to avoid obstacles or distribute
connections on the same side.

**11. Color reused for unrelated link types** — the same color appears on
two semantically different connections (e.g., yellow used for both Redis
cache and database access). Symptom: in a dense region, the reader cannot
tell whether a yellow line is cache or storage. Fix: assign each link type
its own color. If you run out of colors, reduce the number of link types
shown rather than reusing colors.

**12. Space allocated inversely to edge density** — the tier with the most
crossing edges gets the narrowest gap, while a tier with zero edges gets
generous whitespace. Symptom: 16 edges packed into a 60px corridor while
140px of blank space sits unused below. Fix: measure edge count per gap,
apply the density table from § Professional Layout Principles.

**13. Decorative containers with no legend entry** — dashed boxes or
colored outlines appear around groups of nodes without any label or legend
explanation. Symptom: a purple dashed frame overlaps with purple Kafka
arrows, causing color confusion and adding zero semantic value. Fix: every
container must have a label and a legend entry, or be removed.

**14. HTML double-escaping in node values** — writing `&amp;amp;` when
you only meant `&amp;`. Symptom: nodes display raw HTML like
`&lt;b&gt;Place Order&lt;/b&gt;` or show `&amp;` as literal text. Fix: inside
`value=\"...\"` with `html=1` in the style, write HTML entities once:
`&lt;b&gt;Label&lt;/b&gt;`, `&amp;`. Never double-escape. Validating with an
XML parser catches this but the fix is to write the entity correctly.

## Self-Check (output pass/fail for each)

```
 1. No `<!-- -->` XML comments anywhere:              pass/fail
 2. `<mxGraphModel>` + `<root>` wrappers present:     pass/fail
 3. Cell `id="0"` and `id="1"` exist:                pass/fail
 4. Every vertex has `<mxGeometry ... as="geometry"/>`: pass/fail
 5. Every edge has `<mxGeometry relative="1" as="geometry"/>`: pass/fail
 6. Edge `source`/`target` reference existing IDs:    pass/fail
 7. All IDs unique:                                   pass/fail
 8. `&lt;`, `&gt;`, `&amp;` escaped in values:             pass/fail
 9. No double-escaped `&amp;amp;` in values:            pass/fail
10. All x/y coords multiples of 10:                   pass/fail
11. Flow direction consistent (TB: source.y > target.y; LR: source.x < target.x): pass/fail
12. Container children use `parent="containerId"` with relative coords: pass/fail
13. Cross-container edges use `parent="1"`:            pass/fail
14. Multi-connection nodes have distinct exitY values:  pass/fail
15. One color per link type (no semantic reuse):       pass/fail
```

## Official Shape Libraries

draw.io ships with extensive built-in shape libraries. Access via
**+More Shapes** in the draw.io UI. When generating diagrams, mention
which official library the user should enable for best results.

### Key Libraries by Category

| Category | Library | Shapes |
|----------|---------|--------|
| **Cloud** | AWS, AWS 3D, Azure, GCP, IBM Cloud, Alibaba Cloud | Infrastructure components |
| **Networking** | Network 2025, Network 2018, Cisco | Routers, switches, firewalls, topologies |
| **Standards** | BPMN 2.0, UML 2.5, ERD, EPC | Business process, software design |
| **Enterprise** | SAP, Citrix, VMWare, Oracle | Enterprise architecture |
| **UI/UX** | Mockups, Wireframes, Bootstrap | App/website layouts |
| **Engineering** | Electrical, Fluid Power, HVAC, P&ID | Engineering schematics |

### Community Libraries (GitHub)

Official draw.io libraries repo: [github.com/jgraph/drawio-libs](https://github.com/jgraph/drawio-libs)

Notable community contributions:
- **Font Awesome** — web icons for mockups
- **DevSecOps** (djschleen/aquasecurity) — pipeline shapes + security logos
- **Threat Modeling** (Michael Henrikson) — integrated into draw.io
- **HashiCorp** — Terraform, Vault, Consul logos
- **IBCS** — standards-compliant business charts
- **VOWL** — OWL ontology visualization

### Custom Shape Libraries

Custom libraries are XML files. Create one:
1. Build shapes on canvas
2. Drag to Scratchpad
3. Click pencil icon → Export as `.xml`
4. Share the file or load via **File → Open Library**

Format reference: [drawio.com/docs/reference/format-custom-shape-library](https://www.drawio.com/docs/reference/format-custom-shape-library)

### When to Recommend Shape Libraries

- Network diagram → suggest **Network 2025** or **Cisco**
- Cloud architecture → suggest **AWS** / **Azure** / **GCP**
- UI mockup → suggest **Mockups** or **Bootstrap**
- Business process → suggest **BPMN 2.0**
- DB schema → suggest **ERD** (built-in)
