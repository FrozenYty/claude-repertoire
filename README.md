# Claude Repertoire

A curated repertoire of Claude Code skills and guides.

## What's Inside

**[`skills/`](skills/)** — Each directory is a self-contained Claude Code
skill with its own `README.md`, install instructions, and feature docs.

**[`docs/`](docs/)** — Guides and reference material.

## Quick Start

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git
```

Then browse [`skills/`](skills/) and install what you need. Every skill
documents its own setup in its `README.md`.

To install everything at once:

```bash
for skill in claude-repertoire/skills/*/; do
  ln -s "$(pwd)/$skill" ~/.claude/skills/
done
```

## Adding a Skill

Create `skills/<name>/` with `SKILL.md`, `README.md`, `CONTRIBUTING.md`,
and `CHANGELOG.md`. Push. Done — no root-level files need updating.

See [CONTRIBUTING.md](CONTRIBUTING.md) for conventions.
