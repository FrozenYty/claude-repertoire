# CLAUDE.md — Claude Repertoire

A curated collection of Claude Code skills. Each skill is a self-contained
directory under `skills/` with its own `SKILL.md`, `README.md`,
`CONTRIBUTING.md`, and `CHANGELOG.md`.

## Project Location

This repo is the single source of truth for all skills. Skills are deployed
by symlinking from `~/.claude/skills/`:

```bash
ln -s "$PWD"/skills/<name> ~/.claude/skills/<name>
```

When editing a skill, modify files in **this repo** — not the symlinked copy.
Changes propagate automatically since both paths point to the same files.

If symlinks aren't available (e.g., Windows without Developer Mode), copy
the skill directories instead and keep the repo copy as the authoritative
version.

## Skill Structure

```
skills/<skill-name>/
├── SKILL.md          # YAML frontmatter (name, description) + markdown body
├── README.md         # Install instructions + feature documentation
├── CONTRIBUTING.md   # Domain-specific contribution conventions
├── CHANGELOG.md      # Version history (Semantic Versioning)
├── prompts/          # Prompt templates loaded by the skill
├── references/       # Reference docs loaded on demand
└── scripts/          # Validation / utility scripts
```

## Skills

See the `skills/` directory for the current list. Each subdirectory is one
standalone skill — zero runtime dependencies between them.

## Commit Conventions (MANDATORY — authoritative)

This section is the definitive reference. `CONTRIBUTING.md` mirrors these
rules but defers to this file if they ever disagree.

```
<type>[(scope)]: <short description>

<optional body — why, not what>

Author: <name>
```

- **Subject:** 72 chars max, lowercase after colon, no trailing period
- **Body:** explain why, not what. Separated by blank line
- **Author:** required on every commit
- **Scope:** skill name in parens (e.g., `fix(drawsmith):`). Omit for repo-wide
- **Types:** `feat` | `fix` | `docs` | `refactor` | `style` | `chore`
- **Breaking:** `!` after type: `feat!: ...` or `feat(scope)!: ...`
- **No megacommits:** one logical change per commit

## Workflow

1. **Edit in this repo**, not in `~/.claude/skills/`.
2. **Test with a real Claude Code session** before committing.
3. **Update CHANGELOG.md** in the affected skill(s).
4. **Commit and push directly to `main`**. Delete feature branches after merge.

## Language & Style

- All documentation in English
- Skill names: kebab-case, lowercase
- Hex colors: lowercase, 6-digit
- Python scripts: forward slashes in paths (Bash compatibility)
- Commit scope matches the skill directory name exactly

## See Also

- User-level `CLAUDE.md` — behavioral guidelines shared across all projects
  (chat language, code style, simplicity-first, surgical changes)
- Workspace-level `CLAUDE.md` — environment overrides (conda env, output
  directory, GitHub transport)
