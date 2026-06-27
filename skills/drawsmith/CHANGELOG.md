# Changelog

All notable changes to the drawsmith skill. Uses [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): breaking or transformative changes.
- **Minor** (0.X.0): new features, significant enhancements.
- **Patch** (0.0.X): bug fixes, documentation, small tweaks.

---

## [0.2.0] - 2026-06-28

### Added — Professional layout enforcement

- **7 new Hard Rules (12-18)**: I/O direction uniformity, one-color-per-link-type,
  space-by-edge-density, grid-off-for-export, uniform line weight, no decorative
  containers, jump-over crossings.
- **Professional Layout Principles** section in `drawio-guide.md`: bus-style routing,
  density-based gap table, I/O convention, component alignment, tier labels.
- **4 new Common Pitfalls (10-13)**: scenic detour edges, color reuse, inverted
  space allocation, decorative containers with no legend.
- Self-check expanded from 15 to 20 items.
- **drawio.md prompt rewritten**: 12 Key Rules enforced during generation (not
  just post-hoc), 11-item Self-Audit with per-rule visual inspection steps.
- Based on draw.io official best practices and iterative feedback on generated
  microservices architecture diagrams.

## [0.1.0] - 2026-06-27

### Added — Initial release

- Extracted diagram and chart generation from papersmith into a standalone
  general-purpose skill.
- Two engines: draw.io (structural diagrams) and matplotlib (data charts),
  with automatic routing based on request type.
- **draw.io**: 18 reusable layout templates (§1-18 in `drawio-layouts.md`),
  15-item XML self-check, multi-connection node routing, bidirectional edge
  pair handling.
- **matplotlib**: 19 chart type templates (`matplotlib-templates.md`),
  professional rcParams block, seaborn integration (5 styles + 4 contexts),
  statistical honesty enforcement.
- **Shared design system** (`style-guide.md`): 24 color palettes sourced from
  [Academic-Color](https://github.com/Rookie-00001/Academic-Color) (18 journal-
  extracted + 6 curated), IEEE semantic palette, colorblind-safe colormaps,
  Material Design palette, typeface system, resolution standards, line weights,
  spacing rules.
- User-customizable DPI (150-1200), figure size, color palette, and font.
- 3 prompts: `drawio.md`, `matplotlib.md`, `chart-pick.md`.
- 5 reference files: `drawio-guide.md`, `drawio-layouts.md`,
  `matplotlib-guide.md`, `matplotlib-templates.md`, `style-guide.md`.
- 7 iron rules (6 mandatory + 1 recommended).
