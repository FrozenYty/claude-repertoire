# Claude Repertoire

A curated repertoire of Claude Code skills and guides. One `git clone` gets everything.

## Skills

| Skill | Purpose | Install |
|-------|---------|---------|
| [papersmith](skills/papersmith/) | Academic paper writing — translate, polish, diagram, review, submit | `ln -s $(pwd)/skills/papersmith ~/.claude/skills/` |
| [drawsmith](skills/drawsmith/) | Professional diagram & chart generation — draw.io + matplotlib | `ln -s $(pwd)/skills/drawsmith ~/.claude/skills/` |
| [brain-admin](skills/brain-admin/) | Manage the three-tier CLAUDE.md instruction system | `ln -s $(pwd)/skills/brain-admin ~/.claude/skills/` |

## Docs

| Doc | Description |
|-----|-------------|
| [claude-md-guide](docs/claude-md-guide/) | A practical guide to building and using `CLAUDE.md` — nine behavioral rules, three-tier system, real case studies |

## Quick Install

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git ~/claude-repertoire
ln -s ~/claude-repertoire/skills/* ~/.claude/skills/
```

## Philosophy

Each tool works standalone. Together they form a complete Claude Code
workshop — write papers with papersmith, draw figures with drawsmith,
and manage project instructions with brain-admin, all guided by the
claude-md-guide.
