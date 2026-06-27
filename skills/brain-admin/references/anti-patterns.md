# Anti-Patterns Reference

Common CLAUDE.md mistakes and how to fix them. Used by `diagnose` mode to flag
issues in existing CLAUDE.md files and by `init` to validate generated output.
Organized by category: rule wording, metadata, and maintenance.

---

## Content Quality (AP 1-5)

### AP-1: Aspirations instead of instructions

| Bad | Good |
|-----|------|
| "Write good code" | "If you write 200 lines and it could be 50, rewrite it" |
| "Be helpful" | "If a simpler approach exists, say so." |
| "Keep the code clean" | "Every generated artifact ships with a checklist of yes/no items" |

**Why it fails:** No operational definition. Cannot be verified or enforced.
**Diagnose check:** grep for adjectives without concrete criteria (good, clean, robust, elegant, helpful, professional).

### AP-2: Task prompts mixed into rules

| Bad | Good |
|-----|------|
| "Today, write the login page for me" | Remove entirely. Tasks belong in the chat prompt, not in CLAUDE.md. |

**Why it fails:** CLAUDE.md is read at the start of every session. A one-time task becomes meaningless on day two, confusing on day three, and harmful when it causes re-execution of completed work.
**Diagnose check:** grep for temporal words (today, now, this session, next, before Friday).

### AP-3: Universal claims with no mechanism

| Bad | Good |
|-----|------|
| "Write tests for everything" | "Write a test that reproduces the bug, then make it pass" |
| "Always use the latest dependencies" | "When you update a dependency, grep for all references to the old version" |

**Why it fails:** "Everything" is unbounded. "Always" is destructive. These rules provide a goal with no mechanism to achieve it. Exception: reasonable-scope universal rules ("use async/await for all I/O") where the domain is bounded — flag as LOW severity with "verify scope is intentional."
**Diagnose check:** grep for "always", "never", "everything", "all" — check whether the scope is bounded.

### AP-4: Vague conventions

| Bad | Good |
|-----|------|
| "Follow project conventions" | "Match existing indentation (2 spaces), import style (named imports), and file naming (kebab-case)" |
| "Use best practices" | "Minimum code that solves the problem. No abstractions for single-use code." |

**Why it fails:** Presupposes conventions exist and names none of them. "Best practices" signals nothing concrete and invites over-engineering.
**Diagnose check:** grep for "follow conventions", "best practices", "industry standard", "clean code", "properly".

### AP-5: Value statements as rules

| Bad | Good |
|-----|------|
| "Be professional" | "If multiple interpretations exist, present them — don't pick silently" |
| "Don't make mistakes" | "State your assumptions explicitly before writing code. If uncertain, ask." |
| "Make it fast" | "The endpoint must respond in under 200ms p95" |

**Why it fails:** LLMs cannot execute values. They need concrete, falsifiable behaviors.
**Diagnose check:** grep for single-adjective or abstract-noun directives that lack a falsifiable action.

---

## Metadata & Organization (AP 6-9)

### AP-6: Registry drift

| Bad | Good |
|-----|------|
| Rule body updated but registry row not synced. Profile tags in the body say `domain:coding` but the registry row says `domain:general`. | Registry is the single source of truth. When editing a rule, update the registry row first, then the body. |

**Why it fails:** `init` reads the registry to match rules. If the registry and rule body disagree, the matching algorithm produces wrong results and the user gets rules they shouldn't — or misses rules they should get. This is silent and invisible to human review.
**Diagnose check:** for each rule with a § ID, verify Profile/Priority in the body matches the registry row. Flag mismatches as Critical.

### AP-7: Wrong priority tier

| Bad | Good |
|-----|------|
| A rule that applies to "all domains, always" is tagged `situational`. A rule that only applies to a narrow coding pattern is tagged `core`. | `core` = domain-agnostic, always useful. `recommended` = useful for most projects in a domain. `situational` = only when specific conditions match. |

**Why it fails:** Priority tiers determine whether a rule loads for a given project. A miscategorized rule either pollutes every CLAUDE.md with irrelevant content (over-inclusion) or is never shown to projects that need it (under-inclusion).
**Diagnose check:** for each rule, does its priority tier match its domain tag? `domain:general` + applies to all activities → likely `core`. `domain:coding` + narrow activity → likely `situational`. Flag questionable tier assignments as Warning.

### AP-8: Profile tag mismatch

| Bad | Good |
|-----|------|
| A rule tagged `activity:create` that primarily talks about editing and reviewing. A rule tagged `audience:any` that contains jargon only a senior engineer would understand. | Tags describe the rule's actual content and target audience. If the rule body uses technical jargon throughout, it should be `audience:technical`. |

**Why it fails:** Tags drive matching. A rule with wrong tags matches the wrong projects — or fails to match the right ones. This is worse than no tags, because it looks correct.
**Diagnose check:** read the rule body and verify each tag dimension against the actual content. `audience:non-technical` rules must be jargon-free. `activity:all` rules must genuinely apply to create/edit/review/communicate equally.

### AP-9: Missing or malformed metadata

| Bad | Good |
|-----|------|
| Rule section has no `**Profile:**` or `**Priority:**` line. Profile uses old format (`Applies to: ...`). Priority is a prose description instead of `core`/`recommended`/`situational`. | Every rule declares `**Profile:** domain:x · activity:y · team:z · audience:w` and `**Priority:** core|recommended|situational`. |

**Why it fails:** Without parseable metadata, `init` can't match the rule. It becomes invisible to the matching system — effectively dead. Prose descriptions ("this rule is important for coding projects") are not parseable.
**Diagnose check:** for every rule section, verify both `**Profile:**` and `**Priority:**` lines exist and use the standard format with `·` separators.

---

## Maintenance & Scope (AP 10-13)

### AP-10: Project-specific rules in global rules.md

| Bad | Good |
|-----|------|
| "Use `D:/anaconda3/envs/claude/python` for all Python commands." | Put environment-specific commands in the project's CLAUDE.md or `.claude/rules/`, not in the global rule template. |

**Why it fails:** Rules in `references/rules.md` are templates for `init` to select from. A Windows-specific conda path has no meaning for a macOS user or a Node.js project. It pollutes every generated CLAUDE.md with irrelevant content.
**Diagnose check:** grep for file paths, environment names, tool versions, or institution-specific names in rule bodies. Flag as Warning — these belong in project CLAUDE.md, not the template.

### AP-11: CJK typography violations

| Bad | Good |
|-----|------|
| `"这是一个"例子"` (ASCII `"` U+0022 adjacent to Chinese) | `"这是一个"例子""` (full-width `""` U+201C/U+201D) |

**Why it fails:** ASCII quotes adjacent to CJK characters look correct to human eyes but are technically wrong. The Edit tool silently fails on quote-swaps because it sees identical rendered characters with different byte representations. This is the single most common formatting bug in CLAUDE.md files written with Chinese content.
**Diagnose check:** `python -c "print([hex(ord(c)) for c in line if ord(c)>127])"` on any line containing CJK characters. Flag ASCII `"` (0x22) next to CJK as Critical.

### AP-12: Cross-reference rot

| Bad | Good |
|-----|------|
| `**Related:** Rule 4, Rule 14` — but Rule 4 and Rule 14 were renumbered. The references now point to wrong rules. | All `**Related:**` references use stable § IDs (C1, R6, S2) or are verified against current rule numbers. |

**Why it fails:** Rule numbers change when rules are reordered or new rules are inserted. A stale reference silently points to the wrong rule — there's no error, just wrong guidance. `init` may suggest irrelevant rule combinations.
**Diagnose check:** for each `**Related:**` line, verify every referenced rule number corresponds to the expected rule by content (not just by number). Cross-check with the registry.

### AP-13: Disproportionate rule length

| Bad | Good |
|-----|------|
| A simple rule ("use forward slashes in paths") spreads across 3 paragraphs with 2 examples and a case study. | A rule's length should match its complexity. Simple heuristics: 3-5 bullet points. Complex patterns: up to 8 bullet points + 1 example. |

**Why it fails:** Overlong rules drown their core point in prose. The user (and `init`) can't extract the actionable behavior from the surrounding explanation. Conversely, complex rules that are too short omit necessary context.
**Diagnose check:** rules under 5 lines → too short (likely missing Why or Relax when). Rules over 25 lines → too long (likely contains examples that belong in principles.md). Flag both extremes.

---

## The Three-Question Test

Every line in a CLAUDE.md rule must answer:

1. **What specific behavior should Claude perform?** (not a value, not an aspiration)
2. **How would you verify compliance?** (falsifiable check)
3. **Does this apply to every task?** (standing rule, not one-time instruction)

If a line fails any question, delete it or rewrite it.

For rules in the brain-admin registry, add a fourth question:

4. **Do the Profile tags accurately describe this rule's domain, activity, audience, and team?** (if not, the matching algorithm will misroute it)

---

## Quick Reference: Diagnose Severity

| AP | Severity | Trigger |
|----|----------|---------|
| AP-1 | Warning | Adjective without concrete criteria |
| AP-2 | Critical | Temporal word in rule text |
| AP-3 | Warning (LOW if scoped) | Unbounded universal without mechanism |
| AP-4 | Warning | Convention claim without specifics |
| AP-5 | Warning | Single-abstract-noun directive |
| AP-6 | Critical | Registry row ≠ rule body metadata |
| AP-7 | Warning | Priority tier inconsistent with domain/activity |
| AP-8 | Warning | Tag content in body doesn't match declared tags |
| AP-9 | Critical | Missing Profile or Priority line |
| AP-10 | Warning | Environment-specific content in global rule |
| AP-11 | Critical | ASCII `"` adjacent to CJK characters |
| AP-12 | Warning | Related reference points to wrong rule |
| AP-13 | Note | Rule significantly shorter/longer than median |
