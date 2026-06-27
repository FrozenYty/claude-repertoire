# Contributing to Claude Repertoire

## General Guidelines

- All documentation in English.
- Skill names use kebab-case, lowercase.
- Each skill has its own `CONTRIBUTING.md` with domain-specific conventions.
- Follow the existing file structure: `skills/<name>/SKILL.md` with optional
  `prompts/`, `references/`, `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`.

## Adding a New Skill

1. Create `skills/<skill-name>/` with:
   - `SKILL.md` — YAML frontmatter (`name`, `description`) + markdown body
   - `README.md` — install instructions and feature matrix
   - `CONTRIBUTING.md` — contribution conventions for that skill
2. Add the skill to the root `README.md` table.
3. Keep `SKILL.md` under 500 lines; split large content into `references/`.

## Modifying an Existing Skill

1. Update the skill's `CHANGELOG.md` with the change.
2. If the change affects public API (skill name, description, file paths),
   update the root `README.md` and the skill's own `README.md` as needed.
3. Run a real Claude Code session to verify the skill still triggers correctly.

## File Conventions

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition with YAML frontmatter |
| `README.md` | User-facing install + feature docs |
| `CONTRIBUTING.md` | Domain-specific contribution guide |
| `CHANGELOG.md` | Per-skill version history |
| `prompts/` | Prompt templates loaded by the skill |
| `references/` | Reference docs loaded on demand |

## Pull Request Checklist

- [ ] All documentation in English.
- [ ] YAML frontmatter in `SKILL.md` is valid.
- [ ] No absolute paths referencing personal directories.
- [ ] Root `README.md` reflects the change if applicable.
- [ ] Skill's `CHANGELOG.md` is updated.
