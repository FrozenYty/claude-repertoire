# Changelog

All notable changes to the drawsmith skill. Uses [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): breaking or transformative changes.
- **Minor** (0.X.0): new features, significant enhancements.
- **Patch** (0.0.X): bug fixes, documentation, small tweaks.

---

## [0.5.0] - 2026-07-02

### Changed — Batch 3 patterns encoded

- **Section 8 UML Class**: off-center inheritance arrows use mid-column waypoints
  (same corridor principle — WeChatPay→Payment routes through x=410 midpoint).
- **Section 11 DFD**: process and data store positioning guidelines for balanced layout.
- **Section 17 Swimlane**: cross-lane edges confirmed using corridor routing.

### Changed — Golden XML refined from user ground-truth (Batch 1)

- **Section 6 Flowchart**: branch edges now use waypoints through mid-column
  corridors (not direct diagonals). Pattern: waypoints at midpoint x between
  spine and branch columns → clean L-shaped orthogonal routing.
- **Section 13 Org Chart**: off-center parent→child edges use a horizontal
  routing bus at intermediate y. Center-positioned child uses direct vertical.
  Pattern: CEO→left VP routes through bus at y=140, CEO→center VP goes straight.
- **Section 10 State Machine**: self-loop patterns expanded. Left-side arc
  (2 waypoints) for tight spaces. Right-side box loop (4 waypoints) wraps
  above and right of the node — completely visible.
- **Key Rules**: Rule 4 (self-loops) now describes both left and right patterns.
  Rule 7 (cross-panel) refined with mid-column corridor strategy.

## [0.4.0] - 2026-07-01

### Added -- Specific architecture templates (from papersmith)

- **Section 20 Transformer encoder-decoder**: complete 296-line XML skeleton manually
  debugged for production use. Includes all edges, residual connections, K,V
  cross-attention alignment, container layout, and legend.
- **Section 21 Diffusion** forward/reverse process (DDPM/DDIM)
- **Section 22 RAG pipeline** (retrieval-augmented LLM systems)
- **Section 23 Multi-stage training** (Pretrain -> SFT -> RLHF)
- Ported from papersmith v0.3.7 drawio-templates.md

### Changed

- Complete XML examples: 7 (Section 1-4, 6, 13, 20) (Section 1-4, 6, 13, 20-23)
- Template count: 19 -> 23

## [0.3.0] - 2026-07-01

### Added — MCP integration + Cross-Functional Table

- **MCP enhancement section** in `SKILL.md`: plugin-based drawio-mcp install
  instructions (`search_shapes` + `create_diagram` with libavoid/ELK routing).
  Skill auto-detects MCP availability and switches between Tier 1 (auto-routing)
  and Tier 2 (proven manual rules).
- **§19 Cross-Functional Table** template in `drawio-layouts.md`: actor x phase
  grid using draw.io native `tableLayout`.

### Changed — Two-tier routing architecture

- **Arrow Routing rewritten**: Tier 1 (MCP available) declares source/target only,
  router handles placement. Tier 2 (MCP unavailable) uses restored practical
  rules: exitY distribution for multi-connection nodes, bidirectional pair
  parallel tracks, shortest orthogonal path, coords multiples of 10.
- **Hard Rules**: restored parent-child containers and I/O direction consistency.
  Total: 21 rules (renumbered 1-21).
- **Self-Check**: 24 items -> 15 items. Merged official CRITICAL rules (10)
  with practice-verified checks (5): flow direction, coords, multi-connection,
  color reuse.
- **drawio.md prompt**: Phase 1 simplified to 3-line plan. MCP Detection section
  added. Key Rules split by tier (13 items). Self-Audit updated to 15 items.

### Removed

- **Mermaid**: all references, `drawio-mermaid.md`, and routing priority removed.
  All diagrams now route through draw.io XML exclusively.

## [0.2.0] - 2026-06-28

### Added — Professional layout enforcement

- **7 new Hard Rules (12-18)**: I/O direction uniformity, one-color-per-link-type,
  space-by-edge-density, grid-off-for-export, uniform line weight, no decorative
  containers, jump-over crossings.
- **Professional Layout Principles** section in `drawio-guide.md`: bus-style routing,
  density-based gap table, I/O convention, component alignment, tier labels.
- **4 new Common Pitfalls (10-13)**: scenic detour edges, color reuse, inverted
  space allocation, decorative containers with no legend.
- Self-check expanded from 15 to 20 items (later revised to 15 in v0.3.0).
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
