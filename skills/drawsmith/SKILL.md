---
name: drawsmith
version: 0.7.2
description: >
  Professional diagram and chart generation using draw.io and matplotlib.
  Use whenever the user asks to draw, create, generate, design, plot,
  visualize, diagram, chart, or graph anything — architectures, flowcharts,
  network topologies, UML, ERDs, timelines, org charts, Venn diagrams,
  bar charts, line plots, scatter plots, heatmaps, or any other conceptual
  diagram or data chart. Activate aggressively — even if the user doesn't
  explicitly say "draw" or "diagram", if they describe a system layout,
  process flow, data relationship, or structural overview, this skill
  should trigger. Two engines auto-routed: draw.io for structural
  (discrete components + arrows), matplotlib for numerical (X/Y axes).
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

### Layout Selection (evaluate BEFORE planning)

Match the user's request to the closest template. Copy its Golden XML;
replace labels, keep coordinates.

| Description | Template | Canvas | Color Palette |
|-------------|----------|--------|---------------|
| Cloud infra (AWS/Azure/GCP), enterprise topology | **§22 System Architecture** | 1100×850 | Industry (§1.1c) |
| CLI/tool/platform architecture, core + side panels | **§22 System Architecture** | 1100×850 | System Arch (§1.1b) |
| ML model architecture (Transformer, CNN, etc.) | See Flow Direction rule | varies | IEEE (§1.1) |
| Vertical layers, protocol stacks | §1 Vertical Stack | 600×750 | IEEE / System Arch |
| Horizontal stages, CI/CD, data pipeline | §2 Horizontal Pipeline | 1100×300 | IEEE / System Arch |
| Central hub + satellites, star topology | §3 Center Hub | 750×600 | IEEE / System Arch |
| Before/after, method A vs B | §4 Side-by-Side | 900×650 | IEEE / System Arch |
| Process flow, decision tree | §6 Flowchart | 650×800 | IEEE / System Arch |
| DB schema, table relationships | §7 ERD | 800×600 | IEEE |
| OOP design, inheritance | §8 UML Class | 800×700 | IEEE |
| State transitions | §10 State Machine | 800×650 | IEEE |

If no template matches, fall back to the general workflow in
`prompts/drawio.md` and apply the Flow Direction rule manually.

**Color palette routing:** ML architecture diagrams → IEEE Semantic (§1.1).
System/infra/tool diagrams → System Architecture (§1.1b). Cloud infrastructure
(AWS/Azure/GCP) → Industry Architecture (§1.1c). All palettes in
`references/style-guide.md`.

## Diagram Workflow (draw.io)

1. **Pick layout** — use the Layout Selection table above. Jump directly
   to the matching § in `references/drawio-layouts.md`. Copy the Golden XML.
2. **Read `references/quickstart.md`** — self-contained: XML skeleton, escape
   cheat sheet, color palettes (IEEE + System Arch), grid formula, edge
   routing patterns, non-negotiable rules, self-check checklist. This single
   file covers 80% of needs; only reach for `drawio-guide.md` or
   `style-guide.md` for niche edge cases.
3. **Adapt the template** — rename labels, adjust row positions by adding
   the same offset to all y values. Keep the coordinate math intact.
   All coordinates MUST be multiples of 10. Use the color palette that
   matches the diagram type (IEEE for ML, System Arch for general).
4. **Generate XML** — write the `.drawio` file. Follow all hard rules:
   every vertex has `<mxGeometry x y w h as="geometry"/>`, every edge has
   `<mxGeometry relative="1" as="geometry"/>`, `verticalAlign=middle` on
   content nodes, `jumpStyle=arc` on `<mxGraphModel>`.
5. **Self-check** — run the 10-item checklist from `quickstart.md` Step 9.
   Then run `python scripts/drawio-check.py <file.drawio>`. Fix failures
   before delivering.
6. **Refine on feedback** — if the user reports overlapping, cramped layout,
   or missing elements, do NOT redo from scratch. Instead: (a) for overlap:
   increase canvas size and widen zone gaps; (b) for cramped: scale pageWidth/
   pageHeight by 1.3× and multiply all coordinates proportionally; (c) for
   missing elements: find the nearest empty zone and add a node there,
   rerouting only affected edges.

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
| Title | n/a | yes / no (embedded in image) | yes (self-documenting) |

---

## Reference Index

| File | Content | Read when |
|------|---------|-----------|
| `references/quickstart.md` | 1-page cheat sheet: draw.io + matplotlib essentials | Diagram workflow step 2 |
| `references/style-guide.md` | Colors (18+ journal palettes + 6 curated), fonts, resolution, line weights, spacing | Always — shared design system |
| `references/drawio-guide.md` | XML skeleton, hard rules, arrow routing, 15-item self-check | Every draw.io XML diagram |
| `references/drawio-layouts.md` | 22 reusable draw.io layout templates (14 with complete XML) | Matching diagram patterns |
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

3. **IRON RULE — Text vertical centering.** Every content node MUST
   use `verticalAlign=middle`. Container section labels are the ONE
   exception (they use `verticalAlign=top` for top-left placement).
   Misaligned text is the most common visual defect across ALL diagram types.

4. **IRON RULE — Error bars disclosed.** If a chart shows error bars,
   confidence bands, or significance markers, the output must state
   what they represent (+/-1 SD, 95% CI, etc.) and over how many runs/
   seeds. Never show error bars silently.

5. **IRON RULE — Template first.** Before writing ANY XML, find the
   matching template in `drawio-layouts.md`. Copy its Golden XML skeleton.
   Change labels, keep coordinates. Designing from scratch when a template
   fits is a HARD ERROR. Same for charts: adapt from `matplotlib-templates.md`;
   don't guess rcParams or parameters.

6. **IRON RULE — Full-width Chinese punctuation.** Any Chinese text
   output must use `""` (U+201C/U+201D) for quotation marks and `，。；：`
   for punctuation. ASCII `"` adjacent to Chinese text is a hard error.

7. **IRON RULE — Respect the palette.** Use color palettes from
   `style-guide.md`. Never use matplotlib default colors or `jet`/
   `rainbow` colormaps. Max 5-6 distinct colors per figure.

### Best Practices

8. **RECOMMENDED — Professional resolution.** Output >=600 dpi PNG.
   For vector output (PDF/SVG), set `pdf.fonttype = 42` to embed fonts
   for cross-platform consistency. These are best practices, not
   hard requirements — the user's needs may vary.

---

## Template Variables

Prompt files under `prompts/` use `{{VARIABLE}}` placeholders
(e.g., `{{DIAGRAM_DESCRIPTION}}`, `{{CHART_TYPE}}`, `{{DATA}}`).
These are filled at runtime by Claude Code when the skill is invoked —
the LLM sees the user's actual input substituted in place of each variable.
