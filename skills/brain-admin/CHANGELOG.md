# Changelog

All notable changes to the brain-admin skill. Uses [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): breaking or transformative changes.
- **Minor** (0.X.0): new features, significant enhancements.
- **Patch** (0.0.X): bug fixes, documentation, small tweaks.

---

## [0.6.1] - 2026-06-24

### Added — 2 domain-filling rules

- **Rule 24 (R15): Explain Your Work** — professional domain: show inputs, formulas, intermediate steps, and evidence chain for every output. Sourced from professional practice patterns (accounting, legal, audit).
- **Rule 25 (S5): Guide, Don't Answer** — education domain: never give direct answers to assessed questions; teach with progressive hints instead. Sourced from `CarlosAOlivera/esl-portal`.

### Changed — Domain coverage

- Rules: 23 → 25 (5C + 15R + 5S)
- New domains: professional (3→4), writing/education (0→1)
- All docs, registry, Quick Reference synchronized.

---

## [0.6.0] - 2026-06-24

### Added — 3 new rules + quality improvements

- **Rule 16 (R11): Two-Way Door Decision Posture** — when uncertain, prefer the recoverable error. Sourced from `anthropics/claude-for-legal`.
- **Rule 17 (R12): Learn From Corrections** — after 2 pattern corrections, propose recording as a rule. Closes the feedback loop between user corrections and permanent rule updates.
- **Rule 22 (S3): Explore Before Edit** — minimum exploration checklist before modifying unfamiliar codebases. Sourced from rule gap analysis.

### Changed — Rule consolidation & re-tiering

- **D1**: Merged S3 (No Premature Abstraction) into R1 (Simplicity First) — rule-of-three is a specific application of "no abstractions for single-use code."
- **D2**: C3 (Language) — added "For non-CJK projects" scope note so CJK-specific bullets can be skipped on English-only projects.
- **D3**: R10 (Design Token Discipline) domain changed general→coding.
- **D4**: S4 (Bias Toward Action) and S5 (Finish the Job) promoted to recommended (R13, R14) — both are too broadly applicable to remain situational.
- **N2**: Source provenance taxonomy folded into R6 (Professional Domain Guardrails).
- **N3**: Draft-never-execute boundary pattern folded into R9 (Permission Boundaries).

### Fixed — Bugs

- B1: Added `Bash(cp:*)` to `allowed-tools` (import mode backup was silently failing).
- B2: Fixed `find` command OR-precedence bug (three locations in SKILL.md).
- B3: Fixed broken Python YAML validation one-liner.
- B4: Fixed stale `[[bash-not-powershell]]` reference in project CLAUDE.md.
- Fixed 20 broken `**Related:**` lines (missing closing `**` after renumbering).

### Added — Skill quality

- `disallowed-tools` frontmatter (blocks NotebookEdit, tool-use-capture).
- **Gotchas** section in SKILL.md (6 documented failure modes).

### Changed — Counts

- Rules: 21 → 23 (5C + 14R + 4S). All docs synchronized.

---

## [0.5.1] - 2026-06-24

### Added — 3 new rules + anti-patterns expansion

- **Rule 19 (R10): Design Token Discipline** — never hardcode visual values. Sourced from `super-productivity/super-productivity`.
- **Rule 20 (S5): Finish the Job** — don't stop at the minimum. Sourced from `thepushkarp/dotfiles`.
- **Rule 21 (S6): Replace, Don't Deprecate** — remove old code entirely. Sourced from `thepushkarp/dotfiles`.
- **Anti-patterns expanded**: 5 → 13 patterns across 3 categories (Content Quality AP 1-5, Metadata & Organization AP 6-9, Maintenance & Scope AP 10-13). Each AP now includes a `**Diagnose check:**` line for automated detection.

### Changed

- Rule count: 18 → 21. Anti-pattern count: 5 → 13.
- All docs, registry, Quick Reference, and principles synchronized.

---

## [0.5.0] - 2026-06-24

### Added — 3 new rules from GitHub research

- **Rule 14 (R9): Permission Boundaries** — green/yellow/red three-tier decision framework for autonomous vs. collaborative vs. permission-required actions. Sourced from `harperreed/dotfiles` and `thepushkarp/dotfiles`.
- **Rule 17 (S3): No Premature Abstraction** — don't DRY until the third repetition; concrete duplication beats wrong abstraction. Sourced from `thepushkarp/dotfiles`.
- **Rule 18 (S4): Bias Toward Action** — limit exploration to 3-5 files before first change; state assumptions for reversible decisions; stop after 2 consecutive tool failures. Complements Rule 1 (Think Before Coding). Sourced from `thepushkarp/dotfiles`.

### Changed — Full renumbering & registry upgrade

- Rules renumbered 1-18 sequentially within priority tiers (core 1-5, recommended 6-14, situational 15-18). § IDs (C1-C5, R1-R9, S1-S4) are the stable identifiers.
- Quick Reference tag index upgraded to use § IDs for maintainability.
- All `Related:` references updated to new numbering.
- Principles expanded with case studies for all 3 new rules.

---

## [0.4.0] - 2026-06-24

### Changed — Major Architecture Refactor

- **Profile-based rule matching system** (inspired by ESLint's metadata architecture):
  - Each rule now carries self-declaring metadata: `**Profile:**` (domain, audience, team, activity) and `**Priority:**` (core / recommended / situational).
  - Rules grouped by priority tier instead of sequential numbering — core rules always load, recommended rules match by domain, situational rules require multi-dimension intersection.
  - `init` interview redesigned: 4 questions produce a profile → matching algorithm selects rules automatically. No more scanning all 15 manually.
  - Quick-reference tag index at the bottom of `rules.md` for fast lookup.

- `SKILL.md` init flow rewritten to describe profile-based matching.
- `README.md` updated to reflect the priority-tier organization.

---

## [0.3.5] - 2026-06-24

### Changed

- **Rule 5 (Language)**: upgraded from generic "use project's primary language" to CJK-specific — chat-vs-file language split, hex verification for invisible quote mismatches, Edit tool `chr(0xNNNN)` fallback for quote-swap failures. Merged from production CLAUDE.md.
- **Rule 6 (Output Workspace)**: renamed directory to `CLAUDE_CODE_FILES/` (matching production convention), added workspace-level override awareness.
- **Rule 9 (Sub-Agent Dispatch)**: added pre-dispatch question ("Can parts of this run in parallel?"), `run_in_background` notification behavior, synchronous-vs-background dispatch guidance. Merged from production CLAUDE.md.
- **Principles updated** for Rules 5, 6, 9 with updated case studies.

---

## [0.3.4] - 2026-06-24

### Added

- **3 new communication & workflow rule templates** sourced from GitHub research (dtolan/Claude_Code_Optimization, taylorsatula/mira-OSS, Adeflesk/loop-breaker, vijayclarion/vibecoding):
  - **Rule 13: Incremental Delivery with Checkpoints** — stop at natural boundaries, show diffs, let the user verify before continuing. Prevents "10-minute run on a wrong assumption."
  - **Rule 14: Technical Candor** — push back on unsound requests; reject, explain why, offer alternatives. Prevents silent compliance with bad ideas.
  - **Rule 15: Scaled Communication** — concise for routine tasks, thorough for complex decisions. No internal deliberation narration for simple work.

- 3 corresponding principle entries in `references/principles.md` with real-world case studies.
- All docs updated: rule count 12 → 15.

---

## [0.3.3] - 2026-06-24

### Added

- **3 new rule templates** sourced from GitHub research (anthropics/claude-for-legal, by32/bestofclaude, b-open-io/prompts):
  - **Rule 10: Professional Domain Guardrails** — source attribution, no-fabrication, currency awareness, and `[review]` flagging for regulated professional domains (accounting, legal, tax, medical).
  - **Rule 11: Role-Consistent Output** — persona definition, output templates, pre-task contracts, and domain-appropriate vocabulary for fixed-role assistants.
  - **Rule 12: Self-Documenting Configuration** — section comments, inline rationales, copy-pasteable commands, and maintenance lifecycle for non-technical CLAUDE.md maintainers.

- 3 corresponding principle entries in `references/principles.md` with real-world case studies.
- README and SKILL.md updated: rule count 9 → 12.

---

## [0.3.2] - 2026-06-24

### Fixed

- **Critical:** Renamed `rules-db.md` → `rules.md` and `principles-db.md` → `principles.md` on disk to match SKILL.md references (v0.3.0 claimed this rename but it was never executed — caused `init`/`upgrade`/`import` to reference nonexistent files).
- CONTRIBUTING.md updated to reference new filenames.

### Added

- Diagnose checklist: memory frontmatter validation (`name:` matches filename, `description:` one-line, `type:` valid enum).
- Diagnose checklist: `[[link]]` dangling reference detection (grep all `[[...]]` across topic files, verify each resolves to an existing `name:` slug).
- Trigger keywords: "audit my memory", "validate memory" for memory-only audit entry points.
- Edge cases: Windows path pitfalls (backslash-as-escape in Git Bash, forward-slash requirement for glob patterns and filesystem commands).
- formats.md: Memory topic file format section with `[[link]]` cross-reference syntax and validation checklist.

---

## [0.3.1] - 2026-06-03

### Fixed

- AP-3 false-positive: reasonable-scope universal rules no longer flagged as errors.
- `find` command in diagnose now includes `./.claude/CLAUDE.md`.
- Post-import now estimates `init` output size against 200-line budget.
- MCP enrichment distinguishes "no library found" from "no relevant docs".

### Changed

- README and CHANGELOG updated to reflect latest feature set.

---

## [0.3.0] - 2026-06-03

### Added

- **MCP enrichment for import**: Context7 MCP queries official library docs for authoritative rationale (`[context7]`). GitHub MCP searches public CLAUDE.md/AGENTS.md for community conventions (`[github:*]`).
- **Auto-generated principles**: four-level priority chain (source file -> Context7 -> GitHub -> auto-generate). Every principle tagged with its source.
- **Quick reference table**: maps each mode to files read and written.
- **AAPEV workflow pattern** (Assess/Analyze/Plan/Execute/Verify) applied to all mode descriptions.

### Changed

- Reference files renamed: `rules-db.md` to `rules.md`, `principles-db.md` to `principles.md`.
- Anti-patterns numbered AP-1 through AP-5 (trailofbits convention).
- SKILL.md restructured: Quick reference -> Tiers -> Decision framework -> Modes -> Edge cases -> Behavioral rules.
- Behavioral rules now include WHY explanations per skill-creator best practices.
- Diagnose checklist cross-references anti-patterns by number (AP-1 through AP-5).

---

## [0.2.1] - 2026-06-03

### Fixed

- YAML frontmatter: description field uses `|-` block scalar (was causing parse errors).
- Promote mode duplicate numbering (4,4,5 -> 4,5,6).
- README mode count synced (6 -> 7).
- CLAUDE.md locations table in formats.md properly formatted (removed `<br>` tags).
- MEMORY.md thresholds aligned across all files: warn >150 lines, critical >=200 lines.

---

## [0.2.0] - 2026-06-03

### Added

- **import** mode: load custom rules from any agent instruction file (CLAUDE.md, AGENTS.md, .cursorrules, .windsurfrules, .github/copilot-instructions.md). Auto-detect and convert formats.
- **Format validation** in diagnose and execution modes: YAML edge cases (string vs array, empty `paths:`, missing delimiters), glob edge cases (leading `./`, backslashes, unanchored `**`), MEMORY.md index format, CLAUDE.md structure.
- Monorepo CLAUDE.md tree scan in diagnose.
- Dual CLAUDE.md detection (`./CLAUDE.md` vs `./.claude/CLAUDE.md`).
- Diagnose checklist expanded to 22 items.

### Changed

- Init mode: drop "Applies to/Relax when/Solves" from output, reorder by relevance.

### Removed

- **sync-rules.py**: skill is fully standalone.
- All claude-md-guide external references.
- `${CLAUDE_SKILL_DIR}` replaced with `references/` paths.

---

## [0.1.0] - 2026-06-03

### Initial release

- **brain-admin** skill: manage CLAUDE.md, .claude/rules/, and auto memory.
- Six modes: `diagnose`, `init`, `split`, `promote`, `compact`, `upgrade`.
- Four reference files: rules-db.md, principles-db.md, anti-patterns.md, formats.md.
- Decision framework: where each piece of knowledge belongs.
- Five edge cases and six behavioral rules.
