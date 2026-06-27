# Drawsmith

Professional diagram and chart generation using draw.io and matplotlib.

Two engines, auto-routed by request type:
- **draw.io** — structural diagrams (discrete components + arrows)
- **matplotlib** — data charts (numerical X/Y axes)

## Features

### Diagrams (draw.io)

18 reusable layout templates:
vertical stack, horizontal pipeline, center hub, side-by-side comparison,
grid/table, flowchart, ERD, UML class, sequence, state machine, DFD,
network topology, org chart/mind map, timeline/Gantt, Venn diagram,
conceptual coordinate framework, swimlane, wireframe/mockup.

### Charts (matplotlib)

19 chart types: grouped/horizontal/stacked bar, Pareto front, radar,
line with confidence bands, zoomed inset, scatter with fitted curve,
ROC/PR curves, heatmap, bubble, violin/box, donut/pie, dual y-axis,
bar+line combo, faceted grid.

### Visual Design

24 color palettes sourced from [Academic-Color](https://github.com/Rookie-00001/Academic-Color):
18 journal-extracted (Nature, Science, Cell, NEJM, Lancet, JAMA, etc.)
plus 6 curated synthetic palettes. IEEE semantic palette for technical
diagrams. Colorblind-safe colormaps (viridis, cividis, turbo).

### Quality

- Professional rcParams (Times New Roman, 600 dpi, font embedding)
- Seaborn integration (5 styles + 4 contexts)
- 15-item XML self-check for every draw.io diagram
- Statistical honesty enforcement for charts

## Install

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git
ln -s $(pwd)/claude-repertoire/skills/drawsmith ~/.claude/skills/
```

## See Also

- [papersmith](../papersmith/) — academic paper writing with integrated diagram support
- [style-guide.md](references/style-guide.md) — shared design system for colors, fonts, and spacing
