# CLAUDE.md — Claude Repertoire

A curated collection of Claude Code skills. Each skill is a self-contained
directory under `skills/` with its own `SKILL.md`, `README.md`,
`CONTRIBUTING.md`, and `CHANGELOG.md`.

## Project Location

This repo is maintained at `D:\MYPROJS\CLAUDE_CODE_FILES\claude-repertoire`.
Skills are deployed via symlinks from `~/.claude/skills/`:

```bash
ln -s "$PWD"/claude-repertoire/skills/drawsmith ~/.claude/skills/drawsmith
```

When editing a skill, modify the **repo copy** (under this directory), not
the symlinked path. Changes to files under `~/.claude/skills/` affect the
repo copy automatically since they point to the same inode — but always
verify you're working in the repo directory before committing.

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

## Current Skills

| Skill | Purpose |
|-------|---------|
| `drawsmith` | Professional diagram + chart generation (draw.io + matplotlib) |
| `papersmith` | Academic paper writing with integrated diagram support |
| `brain-admin` | Claude Code instruction system management |

## Commit Conventions (MANDATORY)

Every commit must follow this format:

```
<type>[(scope)]: <short description>

<optional body — why, not what>

Author: FrozenYty
```

- **Subject:** 72 chars max, lowercase after colon, no trailing period
- **Body:** explain why, not what. Separated by blank line
- **Author:** required on every commit
- **Scope:** skill name in parens (e.g., `fix(drawsmith):`). Omit for repo-wide
- **Types:** `feat` | `fix` | `docs` | `refactor` | `style` | `chore`
- **Breaking:** `!` after type: `feat!: ...` or `feat(scope)!: ...`
- **No megacommits:** one logical change per commit

## Workflow

1. **Edit in repo, not in ~/.claude.** Changes under
   `D:\MYPROJS\CLAUDE_CODE_FILES\claude-repertoire\skills\<name>\`
2. **Test with a real Claude Code session** before committing.
3. **Update CHANGELOG.md** in the affected skill(s).
4. **Commit and push directly to `main`** — no PR ceremony needed for this
   personal repo. Delete feature branches after merge.

## Language & Style

- All documentation in English
- Skill names: kebab-case, lowercase
- Hex colors: lowercase, 6-digit
- Python scripts: forward slashes in paths (Bash compatibility)
- Commit scope matches the skill directory name exactly

## See Also

- `~/.claude/CLAUDE.md` — user-level behavioral guidelines (chat in Chinese,
  write in English, simplicity first, surgical changes)
- `D:\MYPROJS\.claude\CLAUDE.md` — workspace-level overrides (conda env,
  output directory, GitHub over SSH)
