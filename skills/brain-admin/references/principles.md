# Principles Database

Why each rule exists, with real case studies. Edit to add your own case studies or replace with your team's examples.

---

## Rule 1: Think Before Coding

**Why:** LLMs are wired to produce output, not to pause and admit ignorance. Faced with ambiguity, they silently guess — pick the most statistically likely interpretation and charge ahead. This creates plausible-but-wrong code built on false assumptions.

**Case:** An agent was asked to generate a drawio XML diagram. Instead of checking whether a referenced template existed, it assumed the path and generated invalid output. A two-second existence check would have caught it.

---

## Rule 6: Simplicity First

**Why:** LLMs have an instinct for over-engineering. Training data is saturated with production-grade code, so models pattern-match "code that solves X" to the most complex version, not the simplest.

**Case:** A simple "add a config flag" request produced a plugin system with abstract factories and extension points — hundreds of lines that nobody asked for.

---

## Rule 7: Surgical Changes

**Why:** LLMs edit files like a well-meaning houseguest tidying your apartment — they "optimize" nearby formatting, rewrite comments they find unclear, and refactor helper functions in the same file. These drive-by cleanups drown the actual change in noise.

**Case:** A one-line bug fix came with 40 lines of formatting changes and a renamed variable in an adjacent function. The reviewer spent more time verifying the noise than the fix.

---

## Rule 2: Goal-Driven Execution

**Why:** Vague success criteria produce two symmetric failures: the agent stops too early (delivers something that "looks ready" but fails under scrutiny) or never stops (endlessly polishing because "good enough" is undefined).

**Case:** "Refactor the auth module" took 3 sessions because there was no definition of "done." After adding "all existing tests must pass + no new linter warnings," the refactor completed in one session.

---

## Rule 3: Language

**Why:** LLMs don't know about the chat-vs-file language split, and don't understand CJK typography. They default to English or mix languages inconsistently within the same response. For CJK languages, ASCII quotes adjacent to Chinese characters produce broken typography that looks correct to human eyes but is technically wrong — `""` (U+201C/U+201D) and `""` (U+0022) are visually identical in most editors. The Edit tool will silently fail on a quote-swap because it sees identical rendered characters with different byte representations.

**Case:** A file teaching a toolkit to use correct CJK typography was itself the biggest source of quote bugs in the repo — nobody had run the hex verification on the rules file itself. Multiple sessions wasted debugging Edit tool "no difference" errors that were actually invisible ASCII-vs-fullwidth quote mismatches, resolved only by falling back to Python `chr(0xNNNN)` insertion.

---

## Rule 8: Output Workspace

**Why:** LLM sessions produce artifacts — temporary scripts, generated reports, screenshots, logs. Without a designated location, these accumulate in the project root, indistinguishable from permanent source files. The worst case is when artifacts leak into different project subdirectories, each with its own convention. A single workspace-level output directory (`CLAUDE_CODE_FILES/`) with dated session subfolders solves this with minimal cognitive overhead.

**Case:** A project root accumulated 15 `fix_*.py` scripts, 8 `output_*.txt` files, and 3 screenshots over two weeks. Nobody could tell which were still needed. After adopting `CLAUDE_CODE_FILES/YYYYMMDD-topic/`, cleanup became trivial — delete the dated folder when the session is archived.

---

## Rule 9: Cross-Reference Discipline

**Why:** LLMs treat tasks as point edits — fix one file, declare success, move on. But projects are graphs of references. When you change X, every file pointing to the old X is now a bug.

**Case 1:** A template restructuring moved content to new sections. The index table was never updated — 10/10 entries pointed to wrong sections. The error spread to README, evals, and CHANGELOG.

**Case 2:** `max_retries` renamed to `retry_limit`. Definition updated, but 14 references across 7 files (tests, CLI, env mappers, README) became runtime errors. 30 seconds of grep would have caught them all.

---

## Rule 10: Generated Artifact Self-Check

**Why:** Agents confidently deliver output that "looks right" but fails under structural review — unclosed tags, missing required attributes, wrong flow direction, unescaped characters. These aren't hidden bugs; they're detectable in ten seconds if you run a checklist.

**Case:** A drawio XML diagram was delivered with all nodes having `source.y < target.y` — arrows pointing upward when they should point downward. Visually "looked fine" at a glance.

---

## Rule 20: Sub-Agent Dispatch

**Why:** A single agent working sequentially on large tasks hits context limits, loses focus between subtasks, and produces inconsistent output. The key insight is the pre-dispatch question: "Can parts of this run in parallel?" If yes, sequential execution is pure waste. The background-vs-synchronous dispatch distinction also matters: `run_in_background` for independent work you don't need immediately, synchronous parallel dispatch when you need all results to continue. Both are faster than solo.

**Case:** A 22-file audit took one agent 45 minutes with degraded quality in later files. Three parallel agents completed the same audit in 12 minutes with consistent quality. The pre-dispatch question ("can parts of this run in parallel?") would have caught this upstream — 22 files naturally partition by subsystem, and the agent should have dispatched from the start.

---

## Rule 11: Professional Domain Guardrails

**Why:** In regulated professional domains (accounting, law, tax, medicine), a wrong number isn't just a bug — it's liability. LLMs trained as generalists will confidently invent tax rates, cite nonexistent regulations, and produce plausible-but-wrong financial analyses. Without explicit guardrails, the model's default behavior (fill in the blank, sound confident) is exactly the wrong behavior for professional work.

**Case:** Anthropic's `claude-for-legal` plugin encodes this as a first-order rule: "No silent supplement — three values, not two." When a skill needs information it doesn't have, it must either (1) supplement with a source tag, (2) stop and ask, or (3) flag-but-don't-use. Silence about known doubt is as misleading as confident assertion. The same principle applies to accounting: a wrong tax threshold propagated through a calculation is harder to catch than a flagged gap.

---

## Rule 12: Role-Consistent Output

**Why:** Without an explicit persona definition, Claude defaults to a generic helpful-assistant tone. For a professional user (accountant, lawyer, executive), this means explaining basic domain terms they already know, or worse, using casual language in a context that demands professional precision. For a non-technical user, it means jargon-dense responses they can't follow. A defined role constrains both failures.

**Case:** The `executive-assistant` agent (b-open-io/prompts) defines "Tina" with a specific role, output templates, behavioral rules, and skill set — all in one self-contained markdown file. The result: every interaction follows the same professional format (daily agenda table, meeting brief structure, pre-task contract stating scope/approach/done-criteria). Users know exactly what to expect.

---

## Rule 13: Self-Documenting Configuration

**Why:** Most CLAUDE.md files are written once by a technical user and never touched again. Non-technical users who inherit them find opaque instruction blocks they don't understand and therefore ignore. Section comments (the `<!-- PURPOSE -->` pattern), inline rationales ("this rule exists because..."), and copy-pasteable commands turn a black-box config into a self-teaching document.

**Case:** The `bestofclaude` template (by32/bestofclaude) ships with HTML-style comments above every section explaining what to customize and why. Each code block has a concrete command, not a prose description. The template functions as both a working CLAUDE.md and its own documentation — a non-programmer can read the comments, understand the structure, and customize it without asking a developer for help.

---

## Rule 4: Incremental Delivery with Checkpoints

**Why:** LLMs are single-pass engines — they receive a task, produce output, and stop. Without explicit checkpoints, Claude will complete an entire multi-step task in one run, building each step on the output of the previous. If step 2 was wrong, steps 3-10 are all wrong too — and the user can't intervene until the entire run is complete. Checkpoints turn a one-shot transaction into a collaborative loop.

**Case:** The `vibe-coding-presentation.md` (vijayclarion/vibecoding) encodes this explicitly: "Implement the tasks in order. Stop and show me the diff after each task. I'll approve or ask for changes before you proceed." Multiple CLAUDE.md templates from `dtolan/Claude_Code_Optimization` include "Stop-and-verify" as a first-order behavioral rule — deliver one change, verify, then continue. Without this rule, a 10-minute run on a wrong assumption produces output the user discards entirely.

---

## Rule 21: Technical Candor

**Why:** LLMs are trained to be helpful and compliant. In professional contexts, this becomes a liability: Claude will silently implement a technically unsound request rather than push back. The user discovers the problem hours or days later, and the natural question is "why didn't you tell me this was wrong?" Compliance without candor is not helpful — it's harmful.

**Case:** `taylorsatula/mira-OSS` embeds this as a core value: "Immediately and bluntly reject technically unsound or infeasible ideas. Do not soften criticism or dance around problems. Call out broken ideas directly. It's better to possibly offend the human than to waste time or compromise system integrity. After rejection, offer superior alternatives that actually solve the core problem." This pattern — reject, explain why, offer alternatives — turns pushback from obstruction into constructive redirection.

---

## Rule 5: Scaled Communication

**Why:** LLMs have no native sense of "how much explanation is appropriate." They over-narrate simple tasks ("I will now read the file... I have read the file... I will now edit...") and under-explain complex decisions ("chose approach A" — but why?). The user either drowns in deliberation trace or is left confused about critical tradeoffs. Communication depth should match task complexity: concise for routine, thorough for consequential.

**Case:** `Adeflesk/loop-breaker` defines communication rules explicitly: "Short and direct: responses should be concise — one sentence updates at key moments, no narration of internal deliberation." `dtolan/Claude_Code_Optimization` adds the complementary rule: "Explain 'why' for non-obvious decisions; document trade-offs when multiple approaches exist." Together, these define a two-tier communication model: concise-by-default, thorough-on-signal. The user controls depth by asking "why."

---

## Rule 14: Permission Boundaries

**Why:** LLMs default to two symmetric failure modes: asking permission for every keystroke (paralysis-by-consent) or silently making irreversible changes (cowboy-autonomy). Neither is correct. A tiered decision framework — green (autonomous), yellow (propose first), red (always ask) — gives concrete heuristics for when to act vs. pause, calibrated to the risk of the action.

**Case:** Both `harperreed/dotfiles` and `thepushkarp/dotfiles` encode this as a first-order behavioral rule. Harperreed's CLAUDE.md defines three explicit tiers with examples: "🟢 Autonomous Actions (fix tests, lint errors, single functions) → 🟡 Collaborative Actions (multi-file changes, new features) → 🔴 Always Ask Permission (rewriting from scratch, core business logic, security, data loss)." Thepushkarp's version adds the key insight: "For debugging, state the hypothesis then fix — don't ask permission for each step." Both systems converged on the same three-tier model independently, confirming it as a stable pattern.

## Rule 18: Bias Toward Action

**Why:** LLMs have no native sense of when enough research is enough. Without explicit bounds, they either charge ahead blindly (Rule 1 prevents this) or over-research — reading 15 files before making a one-line change (this rule prevents that). The two rules work as a pair: Rule 1 defines when to pause; Rule 18 defines when to move.

**Case:** `thepushkarp/dotfiles` encodes this as: "Limit exploration scope: don't read more than 3-5 files before making the first change — get a basic understanding, act, then iterate." The 3-5 file limit is a concrete heuristic that prevents analysis-paralysis. Combined with "state your assumption before acting," it creates a tight feedback loop: act quickly on reversible choices, make your reasoning visible, and let the user correct direction early rather than after 10 minutes of research.

---

## Rule 15: Design Token Discipline

**Why:** LLMs default to raw visual values (hex colors, magic-number spacing, arbitrary font sizes) because their training data is full of them. But raw values create silent visual drift — two buttons that look "same blue" differ by 3 hex digits, margins that work on one screen break on another. Design tokens (CSS custom properties, spacing scales, typography steps) are the single source of visual truth. This applies beyond UI code — to document formatting, presentation design, and any visual output.

**Case:** `super-productivity/super-productivity` enforces this as a hard rule: "All visual styling MUST use CSS variables — never hardcode colors, spacing, shadows, transitions, or z-index." Their styling guide defines a complete 8px-grid spacing scale (`--s-quarter` through `--s8`), semantic color tokens, and responsive breakpoints — all as named variables. The result: a component written 3 years ago still matches a component written yesterday, because both reference the same tokens. `jcmrs/claude-visual-style-guide` extends this to Claude-generated artifacts with a full design system of semantic colors, typography scales, and spacing patterns optimized for AI output.

---

## Rule 19: Finish the Job

**Why:** LLMs have a "first success" bias — they stop at the minimum output that technically satisfies the request and declare "done." The user then discovers incomplete implementations, unhandled edge cases, and cleanup debris minutes or hours later. The cost isn't just the rework — it's the trust erosion of "why didn't you handle this obvious case?"

**Case:** `thepushkarp/dotfiles` encodes this as: "If the user asked for multiple things, implement all of them before presenting results. Handle the edge cases you can see. Clean up what you touched. If something is broken adjacent to your change, flag it. But don't invent new scope — there's a difference between thoroughness and gold-plating." This is the middle ground between "minimum viable" and "scope creep" — thorough within the known scope, restrained beyond it.

---

## Rule 23: Replace, Don't Deprecate

**Why:** LLMs are trained on codebases saturated with `@deprecated` markers, dual-path implementations, and backward-compatibility shims. They pattern-match "add new alongside old" as the safe choice. But every dual path doubles the test surface, creates confusion about which is canonical, and accumulates indefinitely. Removal is the only mechanism that prevents the old code from being accidentally used or maintained.

**Case:** `thepushkarp/dotfiles` states this bluntly: "When a new implementation replaces an old one, remove the old one entirely. No backward-compatible shims, dual config formats, or migration paths." The insight is that temporary transitions become permanent — a "6-month deprecation window" that still exists 3 years later. The exception is public APIs with documented deprecation policies, where removal follows the project's established timeline.


---

## Rule 16: Two-Way Door Decision Posture

**Why:** LLMs are trained to produce confident output. When they face subjective judgment calls — is this a P0 blocker, is this claim substantiable, does this need review — they default to either over-flagging (asking about everything, annoying the user) or under-flagging (silently deciding the threshold isn't met, hiding the risk). Under-flagging is a one-way door: the reviewer never sees what was suppressed. Over-flagging is a two-way door: a human dismisses the flag in seconds. The mechanism is the inline flag, not a separate caveat paragraph — flags travel with the content they mark.

**Case:** Anthropic's  plugin encodes this as a first-order design principle: "Default to the two-way door. Under-flagging is a one-way door; over-flagging is a two-way door an attorney closes in 30 seconds." Every skill in the plugin uses  inline flags on specific lines that need attorney judgment. The plugin's decision posture section states: "Do not silently decide a subjective threshold isn't met; do not emit a standalone caveat paragraph lecturing about the principle. The  flag IS the mechanism."

---

## Rule 17: Learn From Corrections

**Why:** The most common user complaint about AI assistants is persistent pattern repetition — "it keeps making the same mistake." Without an explicit rule to capture corrections, every user correction is a one-time fix that the model forgets by the next session. The model has no native mechanism to distinguish "this specific fact was wrong" from "my behavior should change permanently." An explicit rule to detect patterns, propose extraction, and write to memory/CLAUDE.md closes the feedback loop.

**Case:** This rule emerged from gap analysis of the existing 21-rule set — no rule addressed what happens AFTER a user correction. The auto-memory system has write capability but no trigger mechanism. Users running brain-admin for the first time often have 3-5 memory entries capturing exactly the kind of pattern corrections this rule would have proposed automatically, confirming the gap.

---

## Rule 22: Explore Before Edit

**Why:** LLMs either skip codebase exploration entirely (producing code that clashes with conventions) or over-explore (reading 20 files before a one-line change). Neither is correct. A concrete exploration checklist — scan structure, read entry point, read config, locate a reference pattern — defines the middle ground between blind action and analysis-paralysis. This complements Rule 18 (Bias Toward Action) by defining what "enough research" means for unfamiliar code.

**Case:** This rule emerged from gap analysis. Multiple existing rules touch on exploration (Rule 1: think before coding; Rule 18: limit to 3-5 files) but none define WHAT to read. The "Relax when" clause of Rule 18 explicitly acknowledges the gap — "Working in unfamiliar codebase (default to more reading)" — but provides no guidance on what "more reading" should consist of. This rule fills that gap with a concrete, falsifiable checklist.