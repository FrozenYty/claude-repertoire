# Contributing to Brain Admin

## How to contribute

### Improving the default rules

The 25 rules in `references/rules.md` are the skill's built-in defaults (5 core + 15 recommended + 5 situational). To suggest a new rule or improve an existing one:

1. Fork the repo and create a branch.
2. Edit `references/rules.md`. Each rule follows this format:

```markdown
## Rule N: Title

**Bold one-sentence summary.**

**Profile:** domain:xxx · activity:xxx · team:xxx · audience:xxx
**Priority:** core | recommended | situational
**Related:** Rule X, Rule Y

- Bullet point with specific behavior.
- Bullet point with specific behavior.

**Why:** ...
**Relax when:** ...
```

**Profile dimensions:**

- `domain` — `coding` (software), `writing` (documents/papers), `professional` (regulated domains), `general` (all)
- `activity` — `create` (building), `edit` (modifying), `review` (auditing), `communicate` (explaining), `all`
- `team` — `solo`, `team`, `any`
- `audience` — `technical`, `non-technical`, `any`

**Priority tiers:**

- `core` — always included (applies to all projects)
- `recommended` — included when profile domain matches
- `situational` — included only when 2+ profile dimensions intersect

Place the rule under the appropriate priority section in `rules.md`. Add a tag entry to the Quick Reference index at the bottom.

3. Add a corresponding entry in `references/principles.md` with the **Why** and a real **Case** study.
4. If the change breaks existing recommendations, update `references/anti-patterns.md` and `references/formats.md` as needed.
5. Submit a PR with a description of the problem the rule solves and a real session where the rule would have helped.

### Adding a case study

Case studies in `references/principles.md` make rules concrete. A good case study has three parts:

- **What happened**: the specific bug, waste, or confusion.
- **Root cause**: why the LLM's default behavior caused it.
- **How the rule prevents it**: the mechanism.

### Improving the skill workflow

The skill's methodology lives in `SKILL.md`. When suggesting workflow changes:

1. Identify which mode is affected.
2. Keep the trigger phrases comprehensive and natural.
3. Every mode step should have a concrete deliverable.
4. Format enforcement should always reference the relevant section of `references/formats.md`.

### Testing

Before submitting a PR:

1. Install the skill locally:
```bash
cp -r brain-admin ~/.claude/skills/brain-admin
```

2. Test each mode in a real Claude Code session:
```
/brain-admin diagnose
/brain-admin init
/brain-admin split
/brain-admin upgrade
```

3. Verify that the skill does NOT write any files without your explicit confirmation. This is behavioral rule #1.

4. Check that all `references/` paths in SKILL.md resolve to actual files.

### Format conventions

- All documentation in English.
- CLAUDE.md rules: `## N. Rule Name` with `**bold summary**` and bullet points.
- `.claude/rules/` files: YAML frontmatter with `paths:` array, globs use forward slashes.
- MEMORY.md: first line `# Memory Index`, entries as `- [Topic](file.md) — description`.
- SKILL.md: under 500 lines, YAML frontmatter with `|-` block scalar for description.

### Pull request checklist

- [ ] All `references/` files are consistent with SKILL.md.
- [ ] No external path references outside the skill directory.
- [ ] YAML frontmatter in SKILL.md is valid.
- [ ] CHANGELOG.md is updated.
- [ ] README.md mode list matches actual modes.
- [ ] Diagnose checklist reflects any new validation rules.
