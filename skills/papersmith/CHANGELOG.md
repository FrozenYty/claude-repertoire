# Changelog

All notable changes to the Papersmith are recorded here. The
format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] — 2026-07-15

### Changed

- **Prompts and references renamed** to follow drawsmith naming conventions:
  short, no redundant verbs, consistent `{topic}-{type}` suffixes.
  - Translation: `translate-zh-to-en-latex` → `translate-latex-zh2en`,
    `translate-en-to-zh-latex` → `translate-latex-en2zh`,
    `translate-en-to-zh-word` → `translate-word-en2zh`,
    `translate-zh-to-en-word` → `translate-word-zh2en`.
  - Polishing: `rewrite-to-avoid-plagiarism` → `rewrite-plagiarism`.
  - Review: `simulate-peer-review` → `peer-review`,
    `respond-to-reviewers` → `rebuttal`.
  - Documents: `draft-cover-letter` → `cover-letter`,
    `write-broader-impact` → `broader-impact`.
  - Captions: `write-figure-caption` → `figure-caption`,
    `write-table-caption` → `table-caption`.
  - Tables: `generate-latex-table` → `latex-table`.
  - References: `verify-references` → `check-references`.
  - Reference docs: `writing-anti-patterns` → `writing-pitfalls`,
    `venue-citation-guide` → `citation-guide`.
  - All See also links, SKILL.md Prompt Index, README, and CONTRIBUTING
    updated to match.

### Added

- **DOCX Chinese quote repair strategy** added to Chinese Typography Rules
  (SKILL.md rule #4): paragraph-level state machine for fixing ASCII `"`
  → `""` in generated `.docx` files using python-docx. Never modify Python
  source — fix quotes directly in the output document.

- **7 new writing templates** in `references/writing-templates.md`:
  §8 Literature Review, §9 Research Proposal, §10 Investigation Report,
  §11 Grant Proposal (NSFC-style), §12 Progress Report, §13 Thesis
  Defense Outline, §14 Slide Deck Narrative. Total templates: 7 → 14.

## [0.4.0] — 2026-07-15

### Removed

- **Drawing and plotting functionality extracted to drawsmith**: removed
  all diagram generation (draw.io) and chart plotting (matplotlib)
  capabilities. Papersmith is now a pure academic writing skill.
  - Removed prompts: `draw-diagram.md`, `plot-figure.md`,
    `recommend-chart.md`.
  - Removed references: `drawio-reference.md`, `drawio-templates.md`,
    `plotting-reference.md`, `plotting-templates.md`,
    `cjk-fonts-guide.md`.
  - Removed Iron Rules: pdf.fonttype=42, Flow direction before drawing,
    Error bars disclosed, Prompt before template.
  - Removed Figure Routing, Diagram Workflow, and Plotting Workflow
    sections from SKILL.md.
  - Total prompts: 27 → 24. Total references: 8 → 3.

### Changed

- **SKILL.md**: description and when_to_use no longer mention drawing,
  diagramming, or plotting. Prompt Index reorganized — former "Figures
  & Charts" category replaced with focused "Captions & Tables" category
  (`figure-caption.md`, `table-caption.md`,
  `latex-table.md`). Iron Rules renumbered to 1–3.
- **README.md**: updated feature list, repository structure, quick-start
  examples, and design rules to reflect writing-only scope.
- **CONTRIBUTING.md**: removed drawio architecture template and Python
  plotting template contribution sections. Simplified testing
  instructions.
- **analyze-experiments.md**: removed See also links to `plot-figure.md`
  and `recommend-chart.md`.
- **latex-table.md**: removed See also links to `plot-figure.md`
  and `recommend-chart.md`.

## [0.3.7] — 2026-06-17

### Added

- **Layout safety pitfalls** to `references/plotting-reference.md`: extended pitfall #4 (Legend covering data) with direction-specific fixes for hbar vs vbar; added #5 (Dual-panel legend — prefer shared `fig.legend()` over per-axis legends); added #6 (Pie/donut labels clipped — `labeldistance≥1.12` + figsize increase); added #7 (Legend off-canvas — pair `bbox_to_anchor` with `constrained_layout`). Self-check checklist expanded from 10 to 13 items with layout-critical checks (#4-#7) ordered before general items.

### Changed

- `references/plotting-reference.md`: pitfall numbering realigned to 1-13 (was 1-4, 11-13, 5-10). All entries normalized to ~55-char line width for consistency.

## [0.3.6] — 2026-06-02

### Changed

- **Reverted prompts/ subdirectories back to flat structure**: subdirectory
  experiment surfaced boundary problems — several prompts resist clean
  categorization (e.g., analyze-experiments straddles review and figures).
  SKILL.md index already provides logical grouping; flat is simpler for
  maintenance. All paths reverted, README and CONTRIBUTING updated.

## [0.3.5] — 2026-06-02

### Removed

- **Removed examples/ directory**: static drawio/py/pdf/png examples are
  not loaded by Claude Code at runtime. They drift stale as templates
  evolve, bloat git history with binaries, and serve no verification
  purpose. README, CONTRIBUTING, and CHANGELOG references cleaned up.

## [0.3.4] — 2026-05-30

### Changed

- **Adopted official third-person description format**: per Context7 skill
  development docs, description now uses "This skill should be used when..."
  with quoted user trigger phrases ("polish my paper", "draw a model
  architecture diagram", etc.).

## [0.3.3] — 2026-05-30

### Changed

- **Removed Chinese from description and when_to_use**: A/B test (6 Chinese
  queries) confirmed LLM cross-lingual semantic matching handles Chinese
  triggers identically with pure English frontmatter. Removed all Chinese
  text (~400 chars). Description and when_to_use are now English-only.

## [0.3.2] — 2026-05-30

### Fixed

- **Chinese auto-triggering weak**: description was English-first with
  keyword dumps at the end. A common scenario ("reviewer said my experiments
  are insufficient, how to respond") failed to trigger. Rewrote description
  to lead with natural Chinese sentences, moved English to supporting
  position, and replaced when_to_use keyword dumps with structured
  bilingual signals covering casual terms users actually say.

## [0.3.1] — 2026-05-30

### Fixed

- **See also cross-linking**: 7 orphaned files had no inbound links from
  other prompts, making them undiscoverable in workflow chains. Added 10
  inbound See also links:
  - `analyze-experiments.md` ← `recommend-chart.md`
  - `check-references.md` ← `cover-letter.md`, `peer-review.md`
  - `broader-impact.md` ← `cover-letter.md`
  - `writing-templates.md` ← `polish-abstract.md`, `rewrite-zh-draft.md`
  - `latex-table.md` ← `analyze-experiments.md`, `table-caption.md`
  - `rewrite-plagiarism.md` ← `humanize-en.md`, `humanize-zh.md`
  - `cjk-fonts-guide.md` ← `plotting-reference.md`
  All 35 prompt + reference files now have at least one inbound See also link.

## [0.3.0] — 2026-05-30

### Added

- **LaTeX table generation prompt**: `prompts/latex-table.md` —
  converts CSV/tabular data into publication-ready `\begin{table}` blocks
  with booktabs, auto-alignment, best-result bolding, and special-character
  escaping. Total prompts: 27.
- **Plagiarism-safe rewriting prompt**: `prompts/rewrite-plagiarism.md` —
  structural paraphrase that avoids synonym-only swaps and thesaurus
  overload, with an explicit ethical-use boundary.
- **CJK font configuration guide**: `references/cjk-fonts-guide.md` —
  OS-specific font selection (Windows/macOS/Linux/Overleaf), troubleshooting
  for tofu/tofu, bold/italic workarounds, and mixed Chinese+math handling.
  Total references: 8.

### Changed

- **SKILL.md description**: added full-width Chinese trigger phrases, a
  `when_to_use` field with bilingual keywords, conference-name triggers
  (NeurIPS, ICML, ICLR, CVPR, ACL, etc.), and venue/lifecycle keywords
  (LaTeX, camera-ready, revision, accepted/rejected) to greatly improve
  automatic skill triggering for Chinese-speaking users.
- **SKILL.md frontmatter**: added `version` field.
- **README.md**: updated prompt count (25 → 27), reference count (7 → 8),
  and added `cjk-fonts-guide.md` to the repository structure.

## [0.2.0] — 2026-05-29

### Added

- **11 new drawio layout and classic diagram templates** (§5–§15):
  vertical stack, horizontal pipeline, center hub + satellites,
  side-by-side comparison, grid/table layout, flowchart, ERD, UML class
  diagram, sequence diagram, state machine diagram, data flow diagram
  (DFD). Total drawio templates: 15 (4 specific architectures + 11
  general patterns and classic types).
- **2 new prompts**: `translate-word-en2zh.md` (English → Chinese Word
  translation, Word-ready plain-text output), `broader-impact.md`
  (broader impact / ethical considerations statement, 4-dimension
  coverage, venue-specific word budgets). Total prompts: 24.
- **DPI upgrade**: plotting templates now output PNG at 600 dpi minimum,
  with a 3-tier venue-adaptive selection guide (600 / 800 / 1000 dpi).
- **Plotting templates hardening**: all 19 chart templates now include
  explicit `fig.savefig(..., dpi=600)` for PNG output, preventing
  matplotlib's default-100-dpi fallback.
- **Iron Rules**: 7 non-negotiable hard constraints added to SKILL.md
  (no fabricated content, pdf.fonttype=42, flow direction before drawing,
  error bars disclosed, no Markdown in Word, full-width Chinese
  punctuation, prompt before template).
- **Writing anti-patterns reference**: `references/writing-pitfalls.md`
  — 12 common Chinese academic writing mistakes with Bad → Why → Rewritten
  examples and self-audit checklist.
- **English writing anti-patterns**: expanded `references/writing-pitfalls.md`
  with 12 English academic writing anti-patterns covering AI-generated
  vocabulary, hollow intensifiers, copula avoidance, forced parallelism,
  padding openers, possessive overuse, passive voice overuse, overclaiming,
  vague comparisons, bookkeeping-style results, template openers, and
  em-dash overuse. Total: 24 patterns (12 Chinese + 12 English).
- **Cross-prompt See also links**: all 24 prompts now include a `## See
  also` section linking to 1-3 semantically related prompts, with I/O
  compatibility annotations for 16 sequential prompt chains (e.g.,
  "Part 1 [LaTeX] output → {{ENGLISH_LATEX}} input").
- **Writing templates reference**: `references/writing-templates.md` —
  canonical section structures for Introduction (CARS model), Related
  Work (taxonomy), Methodology (top-down), Experiments (three-part),
  Conclusion (three-part), and Abstract (five-part), with concrete
  examples and a general principles section.
- **Citation verification system**: `prompts/check-references.md` —
  5-part audit covering completeness (cite→bib mapping + required field
  check), venue-specific format validation, and optional WebSearch-driven
  existence verification (VERIFIED / MISMATCH / NOT_FOUND). Companion
  `references/citation-guide.md` documents citation formats for
  10+ top venues (NeurIPS, ICML, CVPR, ACL, IEEE, ACM, Nature, Science,
  Chinese journals). Total prompts: 25.
- **SKILL.md frontmatter**: added `author: Tianyu Yao`.
- **Orthogonal edge routing** as the default edge style in all new
  templates. Drawio's built-in `edgeStyle=orthogonalEdgeStyle` with
  `rounded=1;orthogonalLoop=1;jettySize=auto` eliminates most waypoint
  hand-coding.
- **Parent-child containment** as an alternative to absolute coordinates.
  Children use coordinates relative to their container; moving the
  container automatically moves all children. Implements drawio's native
  `container=1;pointerEvents=0;` pattern.
- **Spacing-by-complexity table** in `drawio-reference.md` — 200/280/350px
  gap recommendations based on node count (≤5 / 6-10 / >10).

### Changed

- File renames: `draw-architecture-diagram.md` → `draw-diagram.md`,
  `cover-letter.md` → `cover-letter.md`,
  `plot-academic.md` → `plot-figure.md`.
- `drawio-reference.md` now has a Table of Contents for fast navigation.
- Prompt index references updated for renamed files.

### Design

- Figure Routing section added to `SKILL.md` — explicit drawio-vs-Python
  decision tree with "ambiguous → ask" fallback.
- Renamed prompts now follow verb-object kebab-case convention throughout.

## [0.1.0] — 2026-05-29

Initial release. **No license** — mirrors the upstream
[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)
which the prompt templates are adapted from.

### Added

**Prompts (22 total, organized by category):**
- Translation: zh→en LaTeX, en→zh LaTeX, zh→en Word
- Rewriting & polishing: rewrite-zh-draft, polish-en, polish-zh,
  polish-abstract (5-part structure), polish-title (6 type candidates +
  scoring)
- Length adjustment: shorten-en, expand-en
- Quality & style: check-logic, humanize-en, humanize-zh
- Figures & charts: draw-diagram, recommend-chart,
  plot-figure, figure-caption, table-caption
- Analysis & review: analyze-experiments, peer-review,
  rebuttal (concession / clarification / disagreement
  pattern), cover-letter (250-400 word template)

**References (4 total):**
- `drawio-reference.md` — Hard rules, Flow Direction rule, No-Overlap
  rule, Cross-Stack Y-Alignment, Section Container Layout, 7 Common
  Pitfalls, Self-check
- `drawio-templates.md` — 4 canonical architecture templates: Transformer
  encoder-decoder (Vaswani 2017), Diffusion forward/reverse process, RAG
  pipeline, Multi-stage training (Pretrain → SFT → RLHF)
- `plotting-reference.md` — Publication rcParams, IEEE / Nature / Science
  / Cell color palettes, figure sizing per venue, statistical
  conventions, broken axis / log scale snippets, 10-item self-check
- `plotting-templates.md` — 19 chart-type templates aligned with
  recommend-chart numbering: grouped bar, horizontal bar, Pareto, radar,
  stacked bar, line + CI band, line + zoomed inset, scatter + fit, ROC,
  PR, heatmap, predicted-vs-true scatter, bubble, violin, box,
  donut, dual y-axis, bar+line combo, faceted grid

**Examples (3 verified end-to-end):**
- `examples/transformer.drawio` — Transformer encoder-decoder, K,V
  cross-attention as straight horizontal arrow
- `examples/diffusion.drawio` — DDPM forward/reverse Markov chain
- `examples/sota-comparison.{py,pdf,png}` — Grouped bar with ±1 SD
  error bars, IEEE single-column sizing, Type-42 font embedding verified

**Evals scaffolding:** `evals/evals.json` with 8 representative test
prompts (removed in v0.2.x — not meaningful for an atomic task-based
skill where correctness is judged by humans, not automated checks).

### Design rules baked into the toolkit

- **Drawio Flow Direction**: ML stacks flow bottom-to-top by convention
  — input at the largest y, output at the smallest y, every forward
  edge satisfies `source.y > target.y` (TB) or `source.x < target.x`
  (LR). Inverted stacks were the most common failure mode in early
  drafts.
- **Drawio No-Overlap**: no two vertex bounding boxes intersect, except
  a section container may contain modules with ≥10px padding on all
  four sides. Section labels go INSIDE the container at top-left, never
  above (which would intrude on the section above).
- **Plotting `pdf.fonttype = 42`**: enforced everywhere — Type-3 fonts
  fail ACM/IEEE PDF eXpress submission checks.
- **Chinese typography**: full-width quotation marks (U+201C/U+201D)
  and punctuation (， 。 ； ：) throughout any Chinese output.

### Known limitations

- WebSearch / WebFetch unavailable in the dev environment, so the
  templating priorities were chosen from training-knowledge survey
  rather than live GitHub research.
- The Python plotting templates assume English axis labels by default;
  Chinese-language figures require additional CJK font configuration
  not yet documented.
- Skill-creator's eval flow (run_loop.py, generate_review.py) requires
  Anthropic CLI + subagent support; `evals/evals.json` provides the
  prompt set but running them is environment-dependent.
