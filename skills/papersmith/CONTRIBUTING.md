# Contributing

Thanks for considering a contribution. The toolkit is organized for easy
extension — adding a new prompt should not require touching unrelated
files.

## Quick map of where things live

```
papersmith/
├── SKILL.md             # routing index — register new prompts here
├── prompts/             # one .md per task (Role/Task/Constraints/Output/Self-Audit)
├── references/          # loaded on demand: long-form rules + templates
│   ├── writing-anti-patterns.md     (24 patterns: 12 zh + 12 en)
│   ├── writing-templates.md         (7 section structure templates)
│   └── venue-citation-guide.md      (10+ venue citation formats)
├── CHANGELOG.md
├── CONTRIBUTING.md      # you are here
└── README.md
```

**Naming conventions:**

| What | Pattern | Example |
|------|---------|---------|
| Prompt file | `<verb>-<target>-<optional-modifier>.md` | `translate-zh-to-en-latex.md` |
| Reference file | `<topic>-reference.md`, `<topic>-templates.md`, `<topic>-anti-patterns.md`, or `<topic>-guide.md` | `writing-anti-patterns.md`, `venue-citation-guide.md` |

## Commit Rules

### Format

```
<type>: <short description>

<optional body — why, not what>

Author: <Your English Name>
```

**Types:** `feat` (new feature/template/prompt), `fix` (bug fix), `docs`
(documentation only), `refactor` (cleanup, renames, reorganization),
`style` (formatting, whitespace), `chore` (gitignore, CI).

### Staging discipline

Stage files individually — **never use `git add -A` or `git add .`**:

```bash
git add path/to/changed-file.md
git add path/to/another-file.md
git commit -m "..."
```

This keeps diffs auditable and prevents accidentally committing temp files,
editor artifacts, or unrelated changes.

### What to commit

| Commit These | Never Commit These |
|-------------|-------------------|
| `prompts/*.md` | `.pyc`, `__pycache__/` |
| `references/*.md` | `.DS_Store`, `Thumbs.db` |
| `SKILL.md`, `README.md` | Editor temp files (`*~`, `*.swp`) |
| `CHANGELOG.md`, `CONTRIBUTING.md` | `.vscode/`, `.idea/` (unless `settings.json`) |
| `evals/evals.json` | `Claude_Code_Files/` |
| `.gitignore` | `*.egg-info/`, `dist/` |

### Batch size

Commit in small, topic-focused batches. Don't bundle "added 6 templates +
renamed 3 files + updated README + fixed typos" into one commit — split
into one commit per logical change.

```bash
# Good: one topic per commit
git add references/writing-anti-patterns.md
git commit -m "docs: add new anti-pattern to writing-anti-patterns"

# Bad: unrelated changes squashed together
git add references/ prompts/ README.md
git commit -m "various updates"
```

### Before committing

```bash
git pull --rebase          # avoid push conflicts
git status                 # review what changed
git diff --stat            # confirm scope
```

## Adding a new prompt

The toolkit's prompts share a four-section structure. Match it.

**File:** `prompts/<kebab-case-name>.md`. The name should describe the
*action*, not the input. Examples that work: `polish-abstract`,
`respond-to-reviewers`. Examples that don't: `for-conferences`,
`chinese-output`.

**Required sections:**

```markdown
# <Title Case Name>

## Role
You are <a specific persona with credibility for this task>.

## Task
<One paragraph: what the prompt does, what it produces.>

## Constraints
### <Constraint group 1>
- specific rule
- specific rule

## Output Format
<Structure of the output. Use Part 1 / Part 2 / Part 3 if multi-part.>

## Self-Audit (before delivering)
1. <Check 1>
2. <Check 2>

## Input
{{PLACEHOLDER}}
```

**Style conventions:**
- Imperative mood (`Polish the snippet`, not `This prompt polishes...`).
- One placeholder per input, in `{{ALL_CAPS}}` form.
- If the prompt outputs Chinese, reference the Chinese typography rules
  in SKILL.md explicitly: "Apply the Chinese typography rules from
  SKILL.md when outputting Chinese."
- For Word-targeted output: ban Markdown bold/italic in the output (Word
  doesn't render them).
- For LaTeX-targeted output: preserve `\cite{}`, `\ref{}` etc. verbatim.
- **See also language**: Write See also descriptions in Chinese, using
  full-width punctuation per SKILL.md § Chinese Typography Rules. This
  keeps cross-prompt navigation consistent for the primary user base.

**Register the prompt in SKILL.md:**

Find the appropriate "### Category" section in the Prompt Index table
and add a row:

```markdown
| User Intent | Expected Input | Prompt File |
|---|---|---|
| <one-line description of when to trigger> | <input description> | `prompts/<your-file>.md` |
```

Categories so far: Translation, Rewriting & Polishing, Length Adjustment,
Quality & Style, Captions & Tables, Analysis & Review. Add a new category
section if your prompt doesn't fit.

## Adding a new reference file

Add a `<topic>-reference.md` in `references/` if you're documenting a
new toolkit area.

Add a row to the SKILL.md Prompt Index marked "loaded on demand".

Don't add a new reference file just to extend an existing area — extend
the existing reference instead.

## Style: the rest of the toolkit's writing

- **Imperative voice** in instructions ("Apply the rule", not "The user
  should apply the rule").
- **State the why.** When a rule seems arbitrary, add one sentence on
  the rationale.
- **No "MUST" / "SHALL" all-caps unless rare.** If you find yourself
  capitalizing every directive, consider whether the prompt is too
  rigid; smarter LLMs follow soft guidance better than rigid commands.
- **One placeholder per input.** Templates with 5+ placeholders are
  fragile.

## Testing your changes

1. **Read the new file in full.** Manual once-over catches more than
   any tool.
2. **Try the prompt on a realistic input.** If you added
   `polish-japanese-paper.md`, write a short Japanese paragraph and run
   the toolkit on it.
3. **Add a representative case to `evals/evals.json`** if your addition
   is non-trivial. The eval set is also a regression check for future
   contributors.

## What NOT to do

- Don't introduce new tools / dependencies.
- Don't write prompts that depend on each other ("call X then Y then
  Z"). Each prompt should be standalone; SKILL.md handles composition.
- Don't add LICENSE-style headers to individual files. The repo's
  license (or absence thereof) is at the root.
- Don't hardcode personal lab information (institution names,
  funding sources, author names) in templates. Use placeholders.
- Don't write Markdown documents (ad-hoc analysis notes, design
  rationales) unless they're a `*-reference.md` registered in
  SKILL.md.

## Submitting

1. Fork the repo, branch off `main`.
2. Make your changes, commit with a message that names the feature
   (`Add prompt for X` not `Update files`).
3. Open a PR with:
   - What was added/changed
   - Why (one sentence)
   - Verification: how you tested

Substantive feedback over rubber-stamps. Honest reviews of edge cases
and counter-examples make the toolkit stronger.
