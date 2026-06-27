# Claude Repertoire

A curated repertoire of Claude Code skills and guides.

## What's Inside

**[`skills/`](skills/)** — Independently installable Claude Code skills.
Each has its own `README.md` with feature docs and install instructions.
Browse the directory to see what's available.

**[`docs/`](docs/)** — Guides and reference material for Claude Code
workflows and conventions.

## Quick Install

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git ~/claude-repertoire
ln -s ~/claude-repertoire/skills/* ~/.claude/skills/
```

The wildcard `skills/*` picks up every skill automatically —
add a new skill to the repo, pull, re-link, and it's available.

## Adding a Skill

1. Create `skills/<name>/` with `SKILL.md`, `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`.
2. Push. No root-level files need updating — each skill is self-documenting.

See [CONTRIBUTING.md](CONTRIBUTING.md) for conventions.

## Philosophy

Every tool in this repo is designed to work standalone. Pick the ones
you need, install them individually, or grab the whole set with one clone.
