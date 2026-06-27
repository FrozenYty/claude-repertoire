# Brain Admin

A Claude Code skill that manages your project's three-tier instruction system: **CLAUDE.md**, **.claude/rules/**, and **auto memory**.

## What it does

Claude Code has three places where instructions live. Without governance, they drift. Brain Admin gives you seven tools to keep them healthy:

| Mode | What it does |
|------|-------------|
| `diagnose` | Audit all three tiers: conflicts, vague rules, size issues, format violations, promotion candidates |
| `init` | Interview you about your project, then generate a tailored CLAUDE.md from the rule template |
| `split` | Identify CLAUDE.md content that should be path-scoped into `.claude/rules/` |
| `promote` | Scan auto memory for repeated corrections and turn them into rules |
| `upgrade` | Diagnose + fix in one pass: remove vague rules, rewrite weak ones, add missing ones |
| `compact` | Check MEMORY.md size and archive old entries to topic files before the 200-line limit hits |
| `import` | Load custom rules from any agent instruction file, with anti-pattern check, MCP enrichment, and format validation |

## Quick start

### Install

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git
ln -s $(pwd)/claude-repertoire/skills/brain-admin ~/.claude/skills/brain-admin
```

### Use

Trigger the skill from any Claude Code session:

```
/brain-admin diagnose        -- health check
/brain-admin init            -- generate CLAUDE.md
/brain-admin split           -- split CLAUDE.md into rules/
/brain-admin promote         -- promote memory patterns to rules
/brain-admin upgrade         -- diagnose + fix
/brain-admin compact         -- trim MEMORY.md
/brain-admin import          -- load custom rules
```

Or just describe what you want naturally -- the skill triggers on phrases like "my CLAUDE.md is too long", "why does Claude keep making the same mistake", or "import my company's rules".

## The three tiers

| Tier | Who writes | When loaded | Best for |
|------|-----------|-------------|----------|
| `CLAUDE.md` | You | Every session, in full | Coding standards, build commands, architecture |
| `.claude/rules/` | You | Session start or when matching file read | Language-specific or directory-specific guidelines |
| Auto memory | Claude | First 200 lines of `MEMORY.md` | Accumulated knowledge: debugging insights, preferences |

## Decision framework

- **Not needed every session?** Make it a Skill (on-demand)
- **Needed every session + applies to all files?** Put it in `CLAUDE.md`
- **Needed every session + only applies to some files?** Add `paths:` frontmatter, put it in `.claude/rules/`

## Project structure

```
brain-admin/
├── SKILL.md                    # Core methodology + 7 mode workflows
└── references/
    ├── rules.md                # 25 rule templates with registry for auto-matching
    ├── principles.md           # Why each rule exists + real case studies
    ├── anti-patterns.md        # 13 anti-patterns (AP-1 through AP-13) across 3 categories
    └── formats.md              # Technical specs: file locations, frontmatter, size limits
```

## Customizing rules

The skill ships with 25 rules organized by priority tier (5 core → 15 recommended → 5 situational). Each rule carries a § ID in the registry — `init` reads the registry to match rules to projects automatically. To use your own rules:

1. Run `/brain-admin import` and point it at your rule file (company CLAUDE.md, AGENTS.md, .cursorrules, .windsurfrules, team playbook)
2. The skill auto-detects the format, extracts rules and principles, enriches rationale via Context7/GitHub MCP, and checks for anti-patterns
3. Choose to replace the defaults entirely or merge them in
4. Imported rules are saved and used by all future `init` and `upgrade` sessions

You can also edit `references/rules.md` directly -- it is plain markdown.

## Design principles

1. **Every recommendation explains why** -- not "move this to rules/", but why path-scoping saves context
2. **Never write without review** -- present a draft and get confirmation before modifying instruction files
3. **Cite official thresholds** -- 200 lines (CLAUDE.md), 200 lines/25KB (MEMORY.md), 500 lines (SKILL.md)
4. **Self-audit after changes** -- after modifying any instruction file, search for stale references

## Related

- [Claude Code memory system docs](https://code.claude.com/docs/en/memory)
- [Claude Code skills docs](https://code.claude.com/docs/en/skills)
