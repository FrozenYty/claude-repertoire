# Contributing to Claude Repertoire

## General Guidelines

- All documentation in English.
- Skill names use kebab-case, lowercase.
- Each skill has its own `CONTRIBUTING.md` with domain-specific conventions.
- Follow the existing file structure: `skills/<name>/SKILL.md` with
  `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, plus optional
  `prompts/` and `references/`.

## Adding a New Skill

1. Create `skills/<skill-name>/` with:
   - `SKILL.md` — YAML frontmatter (`name`, `description`) + markdown body
   - `README.md` — install instructions and feature documentation
   - `CONTRIBUTING.md` — contribution conventions specific to that skill
   - `CHANGELOG.md` — version history (follow [Semantic Versioning](https://semver.org))
2. Keep `SKILL.md` under 500 lines; split large content into `references/`.
3. Push. The skill is now browsable in the `skills/` directory and
   installable via the wildcard command in the root README.

## Modifying an Existing Skill

1. Update the skill's `CHANGELOG.md` with the change.
2. Run a real Claude Code session to verify the skill still triggers correctly.

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
- [ ] Skill's `CHANGELOG.md` is updated.
