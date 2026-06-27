# Claude Repertoire

A curated collection of Claude Code skills and guides —
self-contained, well-documented, ready to use.

## What's Inside

**[`skills/`](skills/)** — Each directory is a standalone skill.
A skill is a folder with a `SKILL.md` that Claude loads dynamically
to extend its capabilities. Browse the directory, pick what you need.

**[`docs/`](docs/)** — Guides and reference material. The
[claude-md-guide](docs/claude-md-guide/) is a practical handbook for
writing effective `CLAUDE.md` behavioral rules.

## Install

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git
ln -s "$PWD"/claude-repertoire/skills/* ~/.claude/skills/
```

The wildcard installs every skill at once. To install individually,
symlink a single skill directory instead.

For Claude.ai and the API, upload the skill folder directly. See the
[official skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
for details.

## How Skills Work

Claude reads `SKILL.md` at the start of every session. The file
contains YAML frontmatter — a `name` and `description` that determine
when the skill triggers — followed by markdown instructions, prompt
templates, and workflow rules. Supporting files in `prompts/` and
`references/` are loaded on demand.

## Creating a Skill

A minimal skill is just a folder with a `SKILL.md`:

```markdown
---
name: my-skill
description: What this skill does and when to use it.
---

# My Skill

Instructions for Claude go here.
```

## Philosophy

Each tool in this repo works standalone. Pick the ones you need, or
grab the whole set — nothing is coupled. Skills share a common style
guide and quality bar, but have zero runtime dependencies on each other.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for conventions, commit format,
and the full skill specification.
