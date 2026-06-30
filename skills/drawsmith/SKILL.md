---
name: drawsmith
version: 0.3.0
description: >
  Professional diagram and chart generation using draw.io and matplotlib.
  Use when the user asks to draw, plot, visualize, diagram, chart, or
  graph anything — architectures, flowcharts, network topologies, UML,
  ERDs, timelines, org charts, Venn diagrams, bar charts, line plots,
  scatter plots, heatmaps, or any other conceptual diagram or data chart.
  Two engines — draw.io for structural diagrams (discrete components and
  arrows), matplotlib for numerical charts (X/Y axes). Routes automatically
  based on the request type.
---

# Drawsmith

Professional diagram and chart generation.

Two engines:
- **draw.io** — conceptual diagrams (structural, discrete components + arrows)
- **matplotlib** — data charts (numerical, X/Y axes)

Quality bar: papersmith-grade visual polish. General-purpose workflows —
no paper-specific ceremony (no caption generation, no venue sizing tables,
no abstract integration).

---

## Figure Routing (READ FIRST)

When the user asks for a "figure", "diagram", "chart", "plot", "graph",
or "illustration", decide which engine to use BEFORE starting work.

**Decision rules — evaluate in order:**

1. **Is it a conceptual structure with discrete components connected by
   arrows?** -> Route to **draw.io**. Covers: architectures, pipelines,
   flowcharts, swimlanes, network topologies, ERDs, UML, state machines,
   timelines, org charts, Venn diagrams, 2x2 matrices. No numerical axes.
   -> Goto **Diagram Workflow (draw.io)** below.

2. **Does it have numerical axes (X/Y bar, line, scatter, curve)?** →
   Route to **matplotlib**. Covers: bar charts, line curves, scatter
   plots, ROC/PR, heatmaps, violin/box, Pareto, etc. → Goto
   **Chart Workflow** below.

3. **Still ambiguous?** **Ask the user to clarify.**

| Feature | draw.io | matplotlib |
|---------|---------|------------|
| Arrows connecting discrete components | Yes | No |
| Numerical axes (X/Y) | No | Yes |
| Architecture / flowchart / topology | Yes | No |
| Bar / line / scatter / heatmap | No | Yes |
| Output format | `.drawio` | `.py` (produces `.png` + `.pdf`) |


---

## Prompt Index

| User Intent | Prompt File | Engine |
|---|---|---|
| Draw a conceptual diagram | `prompts/drawio.md` | draw.io |
| Pick the best chart type for data | `prompts/chart-pick.md` | — (bridge) |
| Plot a data chart | `prompts/matplotlib.md` | matplotlib |

---

## Diagram Workflow (draw.io)

1. **Check templates** — if the request matches a known layout (§1-§18
   in `references/drawio-layouts.md`), adapt it. Skip Phase 1 planning
   when a template fits — the layout math is already done.
2. **Plan** (if no template fits) — follow Phase 1 in `prompts/drawio.md`.
   Decide flow direction up front (TB or LR), then determine canvas,
   layout zones, node table, and edge table.
3. **Read `references/drawio-guide.md`** — XML skeleton, hard rules, arrow
   routing, container layout, self-check.
4. **Read `references/style-guide.md`** — colors (IEEE palette for
   technical diagrams), fonts, line weights, spacing.
5. **Generate XML** — write the `.drawio` file. Place nodes on exact grid
   (col*180+40, row*120+40, coords multiples of 10). Hand-route edges
   where needed (exitY distribution, waypoints — see `drawio-guide.md`
   Arrow Routing). Follow all hard rules from `drawio-guide.md`:
   every vertex has geometry, every edge has `<mxGeometry relative="1"
   as="geometry"/>`, rough grid placement, no overlap.
6. **Self-check** — run the 15-item checklist from `drawio-guide.md`.
   Fix failures before delivering.

---

## Chart Workflow (matplotlib)

1. **Pick chart type** — if the user hasn't chosen, route through
   `prompts/chart-pick.md` first.
2. **Read `references/matplotlib-guide.md`** — professional rcParams block,
   statistical conventions, scale treatments, common pitfalls.
3. **Read `references/style-guide.md`** — color palettes (Nature/Science/
   Cell/IEEE), typeface system, resolution standards.
4. **Read the matching template** in `references/matplotlib-templates.md`
   (19 chart types). Copy the template, adapt to the user's data; keep
   the style invariants.
5. **Generate script** — one self-contained `.py` file. rcParams at top,
   data middle, plot, save. Output `.png` (>=600 dpi) + optional `.pdf`.
6. **Self-check** — run the checklist from `matplotlib-guide.md`. Fix
   failures before delivering.

---

## Customization

Users may override any default. Honor these requests:

| Parameter | draw.io | matplotlib | Default |
|-----------|---------|------------|---------|
| DPI | n/a | 150/300/600/800/1000/1200 | 600 |
| Figure size | `pageWidth` x `pageHeight` | `(w, h)` in inches | 5.5x4.1 (4:3) |
| Color palette | Name from style-guide §1 | Name from style-guide §1 | Nature (2025) |
| Font | `fontFamily` in XML | Font family string | Times New Roman |
| Output format | `.drawio` | `.png` + `.pdf` (or one) | Both |
| Title | n/a | yes / no (embedded in image) | no (caption in document) |

---

## Reference Index

| File | Content | Read when |
|------|---------|-----------|
| `references/style-guide.md` | Colors (18+ journal palettes + 6 curated), fonts, resolution, line weights, spacing | Always — shared design system |
| `references/drawio-guide.md` | XML skeleton, hard rules, arrow routing, 15-item self-check | Every draw.io XML diagram |
| `references/drawio-layouts.md` | 18 reusable draw.io layout templates | Matching diagram patterns |
| `references/matplotlib-guide.md` | rcParams, seaborn integration, statistical conventions, scale treatments | Every matplotlib chart |
| `references/matplotlib-templates.md` | 19 runnable chart code skeletons | Adapting a known chart type |

---

## Iron Rules

These are non-negotiable unless marked "recommended."

1. **IRON RULE — No fabricated content.** Never invent data points,
   benchmark scores, or statistics. If the user hasn't provided a
   number, don't make one up. Use a placeholder comment or ask.

2. **IRON RULE — Flow direction before drawing.** Every draw.io
   diagram must declare its flow direction before any coordinate is
   written. TB stacks: data bottom-to-top (`source.y > target.y`).
   LR pipelines: data left-to-right (`source.x < target.x`). Inverted
   stacks are the single most common diagram bug.

3. **IRON RULE — Error bars disclosed.** If a chart shows error bars,
   confidence bands, or significance markers, the output must state
   what they represent (+/-1 SD, 95% CI, etc.) and over how many runs/
   seeds. Never show error bars silently.

4. **IRON RULE — Template first.** Before writing ANY XML, find the
   matching template in `drawio-layouts.md`. Copy its Golden XML skeleton.
   Change labels, keep coordinates. Designing from scratch when a template
   fits is a HARD ERROR. Same for charts: adapt from `matplotlib-templates.md`;
   don't guess rcParams or parameters.

5. **IRON RULE — Full-width Chinese punctuation.** Any Chinese text
   output must use `""` (U+201C/U+201D) for quotation marks and `，。；：`
   for punctuation. ASCII `"` adjacent to Chinese text is a hard error.

6. **IRON RULE — Respect the palette.** Use color palettes from
   `style-guide.md`. Never use matplotlib default colors or `jet`/
   `rainbow` colormaps. Max 5-6 distinct colors per figure.

### Best Practices

7. **RECOMMENDED — Professional resolution.** Output >=600 dpi PNG.
   For vector output (PDF/SVG), set `pdf.fonttype = 42` to embed fonts
   for cross-platform consistency. These are best practices, not
   hard requirements — the user's needs may vary.

---

## Template Variables

Prompt files under  use  placeholders
(e.g., , , ).
These are filled at runtime by Claude Code when the skill is invoked —
the LLM sees the user's actual input substituted in place of each variable.
