# Draw.io Diagram Reference

## Index

- [Workflow](#workflow-mandatory) — Phase 1-3 planning loop
- [XML Skeleton](#xml-skeleton) — bare minimum mxfile structure
- [Flow Direction](#flow-direction-read-first----most-common-failure-mode) — bottom-to-top rule (most common failure mode)
- [Cross-Stack Y-Alignment](#cross-stack-y-alignment) — encoder-decoder horizontal edge alignment
- [Hard Rules](#hard-rules-always-enforced) — 11 non-negotiable rules
- [Section Container Layout](#section-container-layout) — labels inside containers, no overlap
- [XML Escapes](#xml-escapes) — `&amp;`, `&lt;`, `&#xa;`, etc.
- [Layout Rules](#layout-rules) — spacing, margins, line limits
- [Arrow Routing](#arrow-routing-critical----most-common-source-of-errors) — waypoints, diagonals, residuals
- [Visual Style Guide](#visual-style-guide) — references `style-guide.md` for colors/fonts/weights
- [Common Pitfalls](#common-pitfalls-real-failures-from-past-generations) — 9 real failures and their fixes
- [Self-Check](#self-check-output-passfail-for-each) — 15-item output checklist

---

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
                  pageScale="1" pageWidth="1200" pageHeight="800"
                  math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Orthogonal edge routing (new default, applies to all edges):**

Use `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;`
as the base style for ALL edges. These four keywords enable drawio's
built-in smart routing: automatic 90° bends that avoid shape overlaps.
Combined with the No-Overlap rule, this eliminates most waypoint
hand-coding.

```xml
<!-- Standard edge with orthogonal routing -->
<mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5" edge="1" parent="1" source="node_a" target="node_b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Add explicit `exitX`/`exitY`/`entryX`/`entryY` only when a node has 2+
connections on the same side — distribute them across the shape
perimeter. Add `dashed=1` for skip/residual connections. Add `curved=1`
for feedback loops.

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
6. All x/y coordinates multiples of 10; widths multiples of 10; heights may use 2-multiples (30, 32, 38, 42, 50) when needed to encode visual hierarchy
7. All elements within page bounds (x+w ≤ pageWidth, y+h ≤ pageHeight)
8. Uncompressed XML only (no `compressed="true"`)
9. No `--` in XML comments
10. **Flow direction consistent** — every forward edge satisfies `source.y > target.y` for TB diagrams or `source.x < target.x` for LR diagrams. If not, the stack is inverted.
11. **No-Overlap** — no two vertex bounding boxes may intersect, with one allowed exception: a *section container* may contain modules whose bbox is FULLY INSIDE the container's bbox (with ≥10px padding on all four sides). Edges (arrows) are exempt from this rule. See § Section Container Layout for the exact pattern.
12. **I/O direction consistent** — every component uses fixed entry/exit sides. Pick one convention per diagram: top-in-bottom-out (default for layered architectures), left-in-right-out (pipelines). Never mix entry directions on the same component.
13. **One color = one link type** — each color encodes exactly one semantic role. Never reuse the same color for unrelated link types. If two things are different concepts, use different colors. Max 6 distinct colors per diagram.
14. **Allocate space by edge density** — widen the vertical gap where edges are densest. A tier with 10+ crossing edges needs 2× the gap of a tier with 2 edges. Never give blank space to a low-density region while edges pile up in a narrow corridor.
15. **Grid off for export** — set `grid=0` on `<mxGraphModel>` or set `gridSize=1` with grid color `#f5f5f5`. The grid is an alignment tool, not a visual element. Exported diagrams must not show visible grid lines.
16. **Uniform line weight** — all edges in the same diagram use the same `strokeWidth` (default 1.5). Differentiate link types by color and dash pattern, not by thickness. Exception: emphasis arrows (e.g., primary data flow) may use `strokeWidth=2.5`.
17. **No decorative containers** — every dashed box or container must be defined in the legend. If a box has no semantic meaning, remove it. Containers exist to group related components or mark a boundary — not for visual decoration.
18. **Jump-over on crossings** — add `jumpStyle=arc` to the `<mxGraphModel>` element to enable automatic arc jumps where edges cross. draw.io renders a small arch so the crossing lines are visually distinct. Without this, every crossing looks like a junction.

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
`verticalAlign=top`, height 16-18px. Label is fully inside container.

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

## Arrow Routing (critical — most common source of errors)

**Golden rule: design the layout so arrows are short and direct.** If you find
yourself adding 3+ waypoints to route around obstacles, the layout is wrong.
Redesign it.

**Tight vertical stacks (preferred):** Place all nodes for one stack
(Encoder/Decoder) in a single vertical column with 24-30px gaps. Integrate
input tokens and embeddings directly into the stack — don't put them in a
separate section far below. This makes ALL arrows short vertical connections
between adjacent nodes that route automatically.

Remember the Flow Direction rule: input at the BOTTOM (largest y), output at
the TOP (smallest y), arrows point UP. The Good column below shows correct
data flow — `Tokens` is at the bottom (largest y) and arrows point upward
through Embed → LSTM 1 → LSTM 2 → Output.

```
Correct (bottom-up data flow):  tokens (y=600) → embed → LSTM1 → LSTM2 → output (y=100)
              arrows point UP, every adjacent pair has source.y > target.y

Wrong (top-down):               decoder (y=100) → ... → input (y=540)
              arrows point DOWN or diagonally across long gaps
```

**Horizontal cross-arrows (between left/right stacks):** When two nodes are at
different Y levels, a direct source→target connection will produce an ugly
diagonal. Force right-angle routing with a waypoint in the gap between stacks:

```xml
<mxCell id="e_cross" style="...exitX=1;exitY=0.5;entryX=0;entryY=0.5" ... source="enc_node" target="dec_node">
  <mxGeometry relative="1" as="geometry">
    <Array as="points"><mxPoint x="390" y="484"/><mxPoint x="390" y="324"/></Array>
  </mxGeometry>
</mxCell>
```

The first waypoint starts the horizontal exit at the source's Y, the second
aligns with the target's Y. Use `x` in the gap between the two stacks (e.g.
halfway between encoder and decoder containers).

**Residual / skip connections:** Use dashed lines on the LEFT side of a stack,
exiting/entering at `exitX=0;exitY=0.5` with waypoints. Follow the same pattern
as the vertical main stack — short segments between adjacent layers.

```xml
<mxCell id="e_skip" style="endArrow=classic;html=1;dashed=1;dashPattern=6 3;strokeColor=#666666;strokeWidth=1;exitX=0;exitY=0.5;entryX=0;entryY=0.5" edge="1" parent="1" source="enc_mha" target="enc_an1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points"><mxPoint x="55" y="334"/><mxPoint x="55" y="398"/></Array>
  </mxGeometry>
</mxCell>
```

**Feedback loops:** Route on the outside of the diagram using `curved=1` or
waypoints that stay outside the main structure. Label feedback arrows briefly
(e.g. `s<sub>t-1</sub>`).

**Forbidden:** Never use diagonal arrows crossing through shapes. Never route
arrows "around the outside" of the entire diagram to connect distant nodes —
fix the layout instead. Never use multiple short edge segments pretending to
be one arrow — a single edge with waypoints is always cleaner.

### Multi-Connection Nodes

When a single node has 3+ edges on the same side, distributing exit/entry
points across the shape perimeter is critical. Without explicit distribution,
all edges will route to the center of that side and overlap visually.

**The rule:** for N edges on the same side of a node, distribute `exitY`
values evenly across the [0, 1] range, avoiding 0.5 (the center) when N >= 2.

```
N=2 edges (right side):   exitY=0.3, exitY=0.7
N=3 edges (right side):   exitY=0.2, exitY=0.5, exitY=0.8
N=4 edges (right side):   exitY=0.15, exitY=0.4, exitY=0.6, exitY=0.85
N=5 edges (right side):   exitY=0.1, exitY=0.3, exitY=0.5, exitY=0.7, exitY=0.9
```

Same pattern for `exitX` on top/bottom sides. For left side, use `exitX=0`
with varying `exitY`. For entry points on the target node, mirror the
distribution so edges don't converge at the center.

**Example — 4 edges exiting right side of a node:**

```xml
<!-- Edge 1: top -->
<mxCell id="e1" style="...exitX=1;exitY=0.15;entryX=0;entryY=0.5" ...>
<!-- Edge 2: upper-mid -->
<mxCell id="e2" style="...exitX=1;exitY=0.4;entryX=0;entryY=0.5" ...>
<!-- Edge 3: lower-mid -->
<mxCell id="e3" style="...exitX=1;exitY=0.6;entryX=0;entryY=0.5" ...>
<!-- Edge 4: bottom -->
<mxCell id="e4" style="...exitX=1;exitY=0.85;entryX=0;entryY=0.5" ...>
```

**Self-check for multi-connection nodes:** scan every node with degree >= 3
on a single side. Verify each has a distinct `exitY` or `exitX` value.

### Bidirectional Edge Pairs

When two nodes have both a forward edge (A→B) and a reverse edge (B→A),
the two edges will overlap if they both use the center of the same side.

**Rule:** offset the two edges vertically so they run as parallel tracks.

Use different `exitY` values on the source node and matching `entryY`
values on the target, so the two edges run as parallel tracks:

```xml
<!-- Forward (top track) -->
<mxCell id="e_push" style="...exitX=1;exitY=0.35;entryX=0;entryY=0.35" ... source="A" target="B">
<!-- Reverse (bottom track, dashed) -->
<mxCell id="e_pull" style="...exitX=0;exitY=0.65;entryX=1;entryY=0.65;dashed=1" ... source="B" target="A">
```

Edge labels should sit on the OUTSIDE of their respective track (forward
label above, reverse label below) to avoid label collision.

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

**10. Edges take scenic detours** — edges route around the outside of the
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

## Self-Check (output pass/fail for each)

```
 1.  XML well-formed:                           pass/fail
 2.  Wrappers present:                          pass/fail
 3.  IDs unique:                                pass/fail
 4.  Edge refs valid:                           pass/fail
 5.  All vertices have geometry:                pass/fail
 6.  All edges have mxGeometry:                 pass/fail
 7.  No out-of-page elements:                   pass/fail
 8.  No unescaped &lt;&gt;&amp; in values:             pass/fail
 9.  All x/y coords multiples of 10:            pass/fail
10.  Fonts consistent:                          pass/fail
11.  Flow direction consistent:                 pass/fail
12.  No double-escaped &amp;amp; in values:          pass/fail
13.  Multi-connection nodes distributed:         pass/fail
14.  Bidirectional pairs use parallel tracks:    pass/fail
15.  I/O direction uniform per tier:             pass/fail
16.  One color per link type (no reuse):         pass/fail
17.  All containers have legend entries:          pass/fail
18.  Space allocated by edge density:            pass/fail
19.  Grid disabled or invisible in export:       pass/fail
20.  Edges take shortest orthogonal path:        pass/fail
```

---

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
