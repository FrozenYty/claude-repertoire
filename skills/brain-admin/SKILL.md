---
name: brain-admin
version: 0.6.1
description: |-
  Manage Claude Code's three-tier instruction system: CLAUDE.md (behavioral rules), .claude/rules/ (path-scoped rules), and auto memory (Claude's self-written notes). Use whenever the user wants to create, audit, split, promote, upgrade, or maintain project instructions. Trigger aggressively on any complaint about Claude not following conventions, repeating mistakes, or ignoring project rules. Also trigger on requests like "init my project", "setup CLAUDE.md", "why is Claude doing X wrong", "Claude keeps making the same mistake", "my CLAUDE.md is too long", "split my rules", "organize project instructions", "audit my project brain", "promote memory to rules", "compact memory", or "what has Claude learned about my project". Trigger on complaints that imply instruction problems even if CLAUDE.md is not named: "Claude keeps doing X wrong", "how do I make Claude stop X", "why doesn't Claude remember X", "turn Claude's corrections into rules", "make Claude learn from my feedback". Also trigger on rule import and format conversion requests: "import my company's CLAUDE.md", "convert this AGENTS.md into rules", "load rules from my cursorrules file", "use our team playbook as the default rules".
allowed-tools: Bash(git grep:*), Bash(git diff:*), Bash(wc:*), Bash(find:*), Bash(ls:*), Bash(head:*), Bash(mkdir:*), Bash(cp:*), Bash(python:*), Read, Write, Edit, Glob, Grep
disallowed-tools: Task(tool-use-capture), NotebookEdit
---

# Brain Admin

Manage the three-tier instruction system that shapes how Claude behaves in your project.

## Quick reference

| Mode | Reads | Writes |
|------|-------|--------|
| `diagnose` | `CLAUDE.md`, `.claude/rules/*.md`, `MEMORY.md`, `references/anti-patterns.md`, `references/formats.md` | Nothing (read-only) |
| `init` | `references/rules.md` | `CLAUDE.md` (after confirmation) |
| `split` | `CLAUDE.md`, `references/formats.md` | `.claude/rules/*.md` (after confirmation) |
| `promote` | `MEMORY.md`, `CLAUDE.local.md` | `CLAUDE.md` or `.claude/rules/*.md` (after confirmation) |
| `compact` | `MEMORY.md`, `references/formats.md` | `MEMORY.md` + topic files (after confirmation) |
| `import` | User-specified file (any format), `references/anti-patterns.md` | `references/rules.md`, `references/principles.md` (after confirmation) |
| `upgrade` | `CLAUDE.md`, `references/rules.md`, `references/anti-patterns.md` | `CLAUDE.md` (after confirmation) |

**Reference files** (`references/` in this skill's directory):

- `rules.md` — *What* Claude should do. 25 rule templates (5 core + 15 recommended + 5 situational) with a registry for automatic profile-based matching. Read for `init`, `upgrade`, `import`.
- `principles.md` — *Why* each rule exists. Case studies and rationale. Read when explaining recommendations.
- `anti-patterns.md` — *What not to do*. 13 anti-patterns (AP-1 through AP-13) across content quality, metadata, and maintenance categories. Read for `diagnose`, `upgrade`.
- `formats.md` — *How* to structure files. Technical specs for CLAUDE.md, .claude/rules/, and MEMORY.md. Read for `split`, `compact`, `diagnose`.

All four files are the skill's built-in knowledge base — they ship with sensible defaults but are meant to be customized. Use `import` mode to load rules from an external source, or edit `references/rules.md` directly.

## The three tiers

| Tier | Who writes | When loaded | Best for |
|------|-----------|-------------|----------|
| `CLAUDE.md` | You | Every session, in full | "Always do X" — coding standards, build commands, architecture |
| `.claude/rules/*.md` | You | Session start, or when matching file is read | Language-specific or directory-specific guidelines |
| Auto memory (`~/.claude/projects/<project>/memory/`) | Claude | First 200 lines of `MEMORY.md` | Accumulated knowledge: build commands, debugging insights, preferences |

## Decision framework

Before placing a piece of knowledge, assess where it belongs:

```
Is this needed EVERY session?
├── NO → Make it a Skill (on-demand, loaded only when relevant)
└── YES → Does it apply to ALL files?
    ├── YES → Put it in CLAUDE.md (< 200 lines ideal)
    └── NO → Add paths: frontmatter, put it in .claude/rules/
```

**When to add to CLAUDE.md** (from Claude Code docs): Claude made the same mistake twice, a code review caught something Claude should have known, or you repeated the same correction across sessions.

**When to use `paths:` in `.claude/rules/`:** API conventions → `paths: src/api/**`, test patterns → `paths: "**/*.test.ts"`, database migrations → `paths: migrations/**`.

**What auto memory is for:** Claude's self-written notes on build commands, debugging insights, and discovered preferences. It is NOT for behavioral rules — those belong in CLAUDE.md. If memory shows the same correction three or more times, it is a candidate for promotion.

**Size limits (enforced by Claude Code):** `MEMORY.md`: first 200 lines or 25KB loaded — beyond that, invisible to Claude. `CLAUDE.md`: no hard cap, but over 200 lines reduces compliance. Skills (`SKILL.md`): under 500 lines ideal.

## Modes

### diagnose — Health check

**Trigger:** "diagnose my brain", "audit CLAUDE.md", "check my memory", "audit my memory", "validate memory", "is my project healthy"

Assess the project's instruction health. Read-only — never modify files.

1. **Assess:** Read `CLAUDE.md`, all `.claude/rules/*.md`, and `MEMORY.md` (if they exist). Scan for multiple CLAUDE.md files: `find . \( -name CLAUDE.md -o -name CLAUDE.local.md -o -path ./.claude/CLAUDE.md \)`. Read `references/anti-patterns.md` and `references/formats.md` for validation criteria.

2. **Analyze:** Run the full checklist below. For each item, classify as Critical (harms behavior now), Warning (will harm soon), or Note (informational).

3. **Report:** Produce a structured report:

```markdown
## Brain Health Report

### Critical (fix now)
- Issues that actively harm behavior: conflicting rules, MEMORY.md truncated

### Warnings (fix soon)
- Vague rules, CLAUDE.md near 200 lines, patterns ready for promotion

### Notes (informational)
- Line counts, coverage gaps, observations

### Recommendations (prioritized)
- Concrete next actions, ordered by impact
```

**Checklist:**

- [ ] CLAUDE.md line count (flag if > 150, warn if > 200)
- [ ] Multiple CLAUDE.md files: check both `./CLAUDE.md` and `./.claude/CLAUDE.md` — flag if both exist
- [ ] `CLAUDE.local.md` existence (personal overrides may add undocumented rules)
- [ ] CLAUDE.md structure: each rule follows `## N. Rule Name` + **bold summary** + bullets
- [ ] MEMORY.md line count (warn if > 150, critical if ≥ 200)
- [ ] MEMORY.md file size (warn if ≥ 20KB, critical if ≥ 25KB)
- [ ] Conflicts between CLAUDE.md and rules/
- [ ] Rules that duplicate CLAUDE.md content
- [ ] Vague/aspirational rules (matches AP-1, AP-4, or AP-5)
- [ ] Task prompts mixed into rules (matches AP-2)
- [ ] Universal claims with no mechanism (matches AP-3)
- [ ] Registry drift: rule body metadata ≠ registry row (matches AP-6)
- [ ] Wrong priority tier for the rule's domain/activity (matches AP-7)
- [ ] Profile tags don't match actual rule content (matches AP-8)
- [ ] Missing or malformed Profile/Priority metadata (matches AP-9)
- [ ] Project-specific content in global rules (matches AP-10)
- [ ] CJK typography violations in rule text (matches AP-11)
- [ ] Cross-reference rot: Related references point to wrong rules (matches AP-12)
- [ ] Disproportionate rule length (matches AP-13)
- [ ] Rules without `paths:` that should have them
- [ ] Rules without `paths:` that are intentional (unscoped rules load every session)
- [ ] Rules with invalid YAML frontmatter (run `python -c "import yaml, sys; yaml.safe_load(open(sys.argv[1]))" <target-file>`)
- [ ] Rules where `paths:` is a string instead of an array (valid YAML but won't match)
- [ ] Rules where `paths:` is an empty array (matches nothing)
- [ ] Rules with absolute paths, backslashes, or leading `./` in glob patterns
- [ ] Rules with overlapping or conflicting paths between files
- [ ] MEMORY.md first line is `# Memory Index`
- [ ] MEMORY.md entries follow `- [Topic](file.md) — description` format
- [ ] MEMORY.md entries reference topic files that actually exist (no dead links)
- [ ] MEMORY.md has no duplicate entries
- [ ] Memory frontmatter valid: `name` slug matches filename, `description` is one-line summary, `type` is one of `user|feedback|project|reference`
- [ ] Memory internal `[[link]]` references: grep all `[[...]]` across topic files, verify each resolves to an existing memory's `name:` slug (dangling refs → flag as Warning)
- [ ] Memory entries that have appeared 3+ times (promotion candidates)
- [ ] Auto-generated principles in `references/principles.md` (entries marked `[auto-generated]` — flag for user review; entries marked `[context7]` or `[github:*]` are machine-sourced from documentation — note which for audit trail)
- [ ] Stale references: filenames in docs that no longer exist; README directory listings vs actual files; index tables and section numbers

4. **Verify:** After producing the report, sanity-check: was every checklist item assessed? Did any category produce "no issues found" without an explicit statement? Are all file:line references still valid (files exist, line numbers are within range)? If the report is empty, state that explicitly rather than producing a blank output.

### init — First-time setup

**Trigger:** "init my project", "setup CLAUDE.md", "generate project instructions", "create a brain for this project"

Generate a tailored CLAUDE.md for a project. Follow the AAPEV pattern.

1. **Assess — Check for existing setup.** If the project already has CLAUDE.md or has run `/init`, read it first and annotate what to keep vs improve. Do not discard existing work.

2. **Analyze — Build a project profile** (4 questions → profile dimensions):
   - **Domain:** What is the primary work? → `coding` (software) / `writing` (documents, papers) / `professional` (accounting, legal, medical) / `general`
   - **Audience:** Is the user technical? → `technical` / `non-technical` / `mixed`
   - **Team:** Solo or team? → `solo` / `team`
   - **Activity:** What's the main work mode? → `create` (building new things) / `edit` (modifying) / `review` (auditing, checking) / `communicate` (explaining, teaching)
   Also ask: *What has Claude gotten wrong here before?* and *Language preference?* — these tune rule emphasis and wording, not matching.

3. **Plan — Match rules by profile.** Read `references/rules.md`. Rules self-declare applicability via `**Profile:**` and `**Priority:**` lines. Don't scan all fifteen — use the matching algorithm:
   - **Always include:** all `Priority: core` rules (they apply to every project)
   - **Domain match:** `Priority: recommended` rules whose profile domain matches
   - **Multi-match:** `Priority: situational` rules only when 2+ profile dimensions intersect
   - **Reference-only:** rules that don't match any dimension are skipped
   For each matched rule, condense into CLAUDE.md format: keep the bold summary and bullet points; drop `Profile/Priority/Why/Relax when` metadata. Reorder by priority tier — core first, pain-point rules before general. Add one to three project-specific rules.

4. **Execute — Build the draft.** Each rule: numbered section (`## N. Rule Name`), bold one-sentence summary, two to four bullet points. Self-check line is optional — add it only when the rule benefits from a concrete yes/no verification. Validate: every rule has a falsifiable behavior, no vague aspirations. Present the full draft for review. Do NOT write to disk until the user confirms.

5. **Verify — After confirmation**, write `CLAUDE.md` to the project root. Suggest follow-ups: if any rules could be path-scoped, suggest creating `.claude/rules/`; explain the boundary between CLAUDE.md, auto memory, and skills.

### split — CLAUDE.md → rules/

**Trigger:** "CLAUDE.md is too big", "split my rules", "organize my CLAUDE.md"

Move path-specific content from CLAUDE.md into `.claude/rules/` files.

1. **Assess:** Read current `CLAUDE.md`. Read `references/formats.md` for the rules file specification.
2. **Analyze:** For each section, ask: does this apply to all files, or only some?
3. **Plan:** For path-scopable content, propose a target file, YAML frontmatter, and the keep-in-CLAUDE.md summary stub. Explain why scoping helps.
4. **Execute:** When creating rules files, enforce correct format: valid YAML frontmatter with `paths:` array, forward slashes, relative paths, no leading `./` or backslashes.
5. **Verify:** Present the full split plan. Get confirmation before writing any files.

### promote — Memory → Rule

**Trigger:** "promote memory", "what has Claude learned", "turn corrections into rules"

Identify auto memory patterns that should become formal rules.

1. **Assess:** Read `MEMORY.md` and any topic files. Also check `CLAUDE.local.md` if it exists.
2. **Analyze:** Identify entries that appear multiple times or represent behavioral corrections.
3. **Plan:** For each candidate, present it to the user with the evidence ("recorded three times") and ask whether it should become a rule.
4. **Execute:** After confirmation, add each promoted item to the appropriate tier (CLAUDE.md or rules/).
5. **Verify:** Optionally clean the promoted entries from memory to avoid duplication.

### compact — Trim MEMORY.md

**Trigger:** "compact memory", "trim memory", "memory is too full"

Archive old MEMORY.md entries to topic files before the 200-line limit is reached.

1. **Assess:** Read `MEMORY.md`. Check line count. Read `references/formats.md` for the standard index format.
2. **Analyze:** Determine severity: ≤ 150 lines (healthy), 150–199 (approaching), ≥ 200 (truncated — urgent).
3. **Plan:** Identify entries to archive. Group related entries into topic files.
4. **Execute:** Move detailed content to topic files. Rebuild `MEMORY.md` following the standard format: first line `# Memory Index`, each entry `- [Topic Name](topic-file.md) — One-line description`. One entry per line, no duplicates, all referenced files must exist.
5. **Verify:** Show before/after. Get confirmation before writing.

### import — Load custom rules

**Trigger:** "import rules from", "load rules from this file", "use these rules instead of the defaults", "import my company's CLAUDE.md"

Import rules from any agent instruction file. This makes the skill work with the user's own rule specifications instead of the built-in defaults. After import, the skill's `init` and `upgrade` modes use the imported rules, and `import` can be run again to switch or merge.

Six steps. Follow all of them — skipping validation means bad rules go undetected.

1. **Assess — Read and identify format.** Read the user-specified file. Read `references/formats.md` for the target structure specification. Detect the format:
   - `CLAUDE.md` / `AGENTS.md` / standalone `.md` → parse as markdown, extract `## Rule` sections
   - `.cursorrules` → parse as plain text, split by blank-line-separated guidelines
   - `.windsurfrules` / `.github/copilot-instructions.md` → parse as markdown or plain text
   - Unknown / mixed format → extract every line that reads like a behavioral instruction (imperative, specific, falsifiable)

   If the file is not markdown, convert it: wrap each coherent guideline in a `## Rule N: ...` section with a bold summary and bullet points.

2. **Analyze — Extract rules and principles.** For each rule found:
   - Extract the **rule text** (what to do) → goes into `references/rules.md`
   - Extract the **rationale** (why this rule exists). Try these sources in priority order:
     1. **User-provided:** If the source file has a "why", "rationale", or "context" section → use it directly. Mark as `[source]`.
     2. **Context7 MCP** (if available): If the rule mentions a specific technology (React, FastAPI, PostgreSQL, etc.), query Context7 for that library's best practices or conventions. Extract the official rationale. Mark as `[context7]`. Example: a rule "use functional components with hooks" → query React docs → "Why: React docs recommend functional components as the standard pattern since v16.8; class components are legacy. [context7]"
     3. **GitHub MCP** (if available): Search public repos for similar CLAUDE.md files, AGENTS.md, or community rulesets in the same tech stack. Cross-reference the rule against what other teams enforce. Mark as `[github:<owner>/<repo>]`. Example: a rule "never edit existing migrations" → search GitHub for database migration rules → "Why: common convention in Django/Prisma projects; editing history breaks replay. [github:org/repo]"
     - **Note:** If Context7 or GitHub return no results, distinguish: "no library found" (the technology is not indexed — e.g., RFC 7807 is an IETF standard, not a library) vs "no relevant docs" (library exists but its docs don't cover this topic). Report this distinction so the user knows whether enrichment was attempted correctly.
     4. **Auto-generation** (fallback): If none of the above produced a why, auto-generate based on what class of LLM mistake this rule prevents. Mark as `[auto-generated]`.
   - All rationales go into `references/principles.md`. Source tags (`[context7]`, `[github:*]`, `[source]`, `[auto-generated]`) let the user gauge the authority of each entry during review.

3. **Validate — Run anti-pattern check.** Before saving, check every extracted rule against `references/anti-patterns.md`:
   - Flag AP-1: rules that are aspirations, not instructions ("write good code")
   - Flag AP-2: task prompts mistaken for rules ("add login page today")
   - Flag AP-3: universal claims with no mechanism ("test everything", "validate all input"). However, do not flag reasonable-scope rules like "use async/await for all I/O operations" where "all" refers to a bounded domain (async framework handlers). If a rule uses universal language but has a clear, bounded scope, flag as LOW severity with the note "verify scope is intentional."
   - Flag AP-4: vague conventions ("follow best practices")
   - Flag AP-5: value statements as rules ("be professional")
   - Also validate format: numbered sections, bold summaries, falsifiable behaviors
   - Present all flagged issues to the user. Do NOT silently import broken rules. Ask whether to fix, skip, or import as-is with a warning.

4. **Plan — Resolve conflicts.** Ask the user: "Replace the defaults entirely, or merge with the built-in rules?"
   - If **replacing**: back up the current `references/rules.md` and `references/principles.md` (copy to `references/rules.md.bak` and `references/principles.md.bak`), then overwrite
   - If **merging**: append unique rules, flag overlapping rules for user decision, de-duplicate identical entries

5. **Execute — Write and verify.** Save to `references/rules.md` and `references/principles.md`. These are used immediately by all future `init` and `upgrade` sessions.

6. **Regenerate — Run a post-import diagnose.** Run a lightweight diagnose on the freshly imported ruleset:
   - Check structure: numbered sections, bold summaries, bullet points
   - Check line count: estimate what `init` would produce from these rules. If the combined ruleset + built-in defaults would exceed the 200-line recommendation when run through `init`, warn the user.
   - Check format compliance against `references/formats.md`
   - In the summary, list any auto-generated principles and MCP enrichment results including "no library found" vs "no relevant docs" distinctions.
   - Report: "Import complete. N rules loaded. Principles by source: S from source file, C from Context7 (X no-library, Y no-relevant-docs), G from GitHub, A auto-generated. M issues flagged. Estimated CLAUDE.md size when run through init: ~L lines (limit: 200). Run `/brain-admin diagnose` for a full health check."

### upgrade — Optimize existing CLAUDE.md

**Trigger:** "upgrade my CLAUDE.md", "improve my project rules", "my CLAUDE.md needs a refresh", "review and fix my project brain"

Diagnose and fix in one pass. Use when the user has an existing CLAUDE.md that works but could be better.

1. **Assess:** Run a full diagnose (see diagnose mode checklist). Read `references/rules.md` and `references/anti-patterns.md`.
2. **Analyze:** Group findings by action: Remove (vague, conflicting, aspirational), Rewrite (needs sharper language or examples), Move (should go to `.claude/rules/` with `paths:`), Add (project is missing rules from the template). Reference specific anti-pattern numbers (AP-1 through AP-13) when flagging issues.
3. **Plan:** Draft the proposed changes. Enforce correct format for all additions and rewrites.
4. **Execute:** Show a unified diff of proposed changes.
5. **Verify:** Get confirmation before applying any change.

## Edge cases

### No git repository
Auto memory normally requires a git repository. Without git, it is stored under the project root path instead. MEMORY.md size checks still apply.

### Monorepos with nested CLAUDE.md files
Claude Code loads CLAUDE.md files from the current directory upward. `claudeMdExcludes` in settings can skip unwanted ones. When diagnosing, scan for ALL CLAUDE.md files in the tree: `find . \( -name CLAUDE.md -o -name CLAUDE.local.md \)`. Flag each file and check for conflicts between them.

### Read-only memory directories
If the auto memory directory or CLAUDE.md is not writable, report the issue and stop. Never force writes.

### No CLAUDE.md exists yet
Suggest `init` mode. Diagnose is meaningless on an empty project.

### Windows path pitfalls
Git Bash (the shell underlying Claude Code's Bash tool) interprets backslashes as escape sequences. When diagnosing `.claude/rules/` glob patterns, flag any backslash usage — use forward slashes instead (`src/api/**` not `src\\api\\**`). Diagnose commands that scan the filesystem must use forward slashes in paths. This applies to both the skill's own operations and the rules it validates.

### User says "Claude is ignoring my rules"
This usually means one of three things: the rules are too vague to follow, conflicting rules exist, or the file is in a location Claude does not load. Run diagnose first, then check `/memory` output to verify which files are actually loaded.

## Behavioral rules

These rules govern how this skill itself operates. They are applied in every mode.

### 1. Never write without review
Always present a draft or diff and get explicit confirmation before modifying CLAUDE.md, `.claude/rules/`, or memory files. These files shape every future session — a bad change is expensive and hard to undo. This is the most important rule.

### 2. Every recommendation must explain why
Do not say "move this to rules/". Instead, explain: "This API naming convention only applies to `src/api/`. If you move it to `.claude/rules/api-design.md` with `paths: ["src/api/**"]`, it will not consume context when Claude works on frontend code." The user needs to understand the tradeoff to make informed decisions.

### 3. Cite official thresholds
When flagging size issues, always mention the actual limit: 200 lines for CLAUDE.md (recommendation), 200 lines or 25KB for MEMORY.md (hard limit — content beyond this is invisible), 500 lines for SKILL.md (recommendation). Citing thresholds lets the user gauge urgency.

### 4. Self-audit after changes
After modifying any instruction file, search the project for stale references. Check README directory listings, index tables, and config files for outdated mentions. Fix every hit in the same session. This is Rule 7 from the knowledge base, applied to the skill itself.

### 5. Respect existing structure
Do not reorganize files the user did not ask about. Match the project's existing naming and organization patterns. If you notice unrelated dead code or stale configs, mention them — do not silently clean them up.

### 6. Follow the project's primary language
Use the language specified in the project's CLAUDE.md or user preferences. If no preference is set, default to English. Match the language of the user's request.

## Gotchas

Documented mistakes Claude has made under this skill. Read before running any mode.

1. **`find` precedence trap** — `find . -name X -o -name Y` runs as `(find . -name X) -o (-name Y)` on most shells. Always wrap OR groups: `find . \( -name X -o -name Y \)`. Diagnose mode's CLAUDE.md scan silently misses files without the parentheses.

2. **Python YAML one-liner is fragile** — `python -c "import yaml; yaml.safe_load(open('file'))"` tries to open a file literally named `file`. Use `python -c "import yaml, sys; yaml.safe_load(open(sys.argv[1]))" <target>` instead.

3. **Registry is the source of truth** — when updating a rule, update the registry row FIRST, then the body. If they disagree, `init` matches by registry, and the body becomes misleading documentation. Cross-check both after any rule edit.

4. **Related: references use rule numbers, which drift** — when rules are renumbered, `**Related:**` lines point to wrong rules unless manually updated. Prefer referencing § IDs (C1, R6, S2) in new rule metadata to avoid this.

5. **Import mode needs `Bash(cp:*)`** — the backup step copies files with `cp`. Without this in `allowed-tools`, import silently fails at the backup stage.

6. **CHANGELOG historical entries are accurate for their version** — don't "fix" old changelog entries that reference outdated counts or AP numbers. They describe the state at that version.
