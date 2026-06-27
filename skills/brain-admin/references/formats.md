# Formats Reference

Technical specifications for each tier of the instruction system. Use these to validate file structure in `diagnose`, generate correct output in `init`/`split`/`compact`, and enforce consistency.

---

## CLAUDE.md

### File locations (loaded in order: broadest first, most specific last)

| Location | Scope |
|----------|-------|
| Managed policy (macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`, Linux/WSL: `/etc/claude-code/CLAUDE.md`, Windows: `C:\Program Files\ClaudeCode\CLAUDE.md`) | Organization-wide |
| `~/.claude/CLAUDE.md` | User-level (all projects) |
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | Project-level (team-shared) |
| `./CLAUDE.local.md` | Personal per-project (gitignored) |

All discovered files are merged into context — they don't override each other. Each directory: `CLAUDE.local.md` loads after `CLAUDE.md`.

Parent-directory CLAUDE.md files are loaded at session start. Child-directory CLAUDE.md files are lazy-loaded when Claude reads files in that directory.

### Size recommendation

Under 200 lines. Longer files consume more context and reduce compliance.

### Structure

Each rule should follow this pattern:
```markdown
## N. Rule Name

**One-sentence bold summary.**

- Bullet point with specific behavior
- Bullet point with specific behavior

Ask yourself/Test/Heuristic: one-liner self-check.
```

### Import syntax

```
@path/to/file.md       # relative to the importing file
@~/.claude/prefs.md    # absolute from home
@AGENTS.md             # import another agent's config
```

Max import depth: 4 hops.

---

## .claude/rules/

### Directory structure

```
.claude/rules/
├── code-style.md
├── testing.md
├── api/
│   └── design.md       # subdirectories supported
└── security.md
```

### YAML frontmatter

Every rule file MUST have valid YAML frontmatter if path-scoped:

```yaml
---
paths:
  - "src/api/**/*.ts"
  - "lib/**/*.ts"
---
```

No `paths:` field → rule loads every session like CLAUDE.md.
`paths:` field → rule loads only when Claude reads a matching file.

### Glob patterns

| Pattern | Matches |
|---------|---------|
| `**/*.ts` | All TypeScript files |
| `src/**/*` | Everything under src/ |
| `*.md` | Markdown in project root |
| `src/**/*.{ts,tsx}` | TS and TSX under src/ |

### Validation checklist

When auditing `.claude/rules/` files, verify:

- [ ] Every file with `paths:` has valid YAML frontmatter (run `python -c "import yaml, sys; yaml.safe_load(open(sys.argv[1]))" <target>` to verify)
- [ ] `paths:` is an array, not a string (e.g., `paths: ["src/**"]` not `paths: "src/**"`)
- [ ] `paths:` is not empty (an empty array matches nothing)
- [ ] Frontmatter has opening and closing `---` delimiters
- [ ] Glob patterns use forward slashes (even on Windows)
- [ ] Glob patterns do NOT use leading `./` prefix (use `src/**` not `./src/**`)
- [ ] Glob patterns do NOT use backslashes (use `src/api/**` not `src\\api\\**`)
- [ ] Paths are relative to project root (no absolute paths like `/home/user/` or `C:\\`)
- [ ] Unanchored `**` is intentional (e.g., `**/foo.md` matches everywhere — usually unintentional)
- [ ] No two rules files have overlapping or conflicting paths
- [ ] Rules without `paths:` are intentional (they load every session)

---

## Auto Memory

### Storage location

```
~/.claude/projects/<project>/memory/
├── MEMORY.md          # Index (first 200 lines or 25KB loaded at session start)
├── debugging.md       # Topic file (read on-demand)
├── api-conventions.md # Topic file (read on-demand)
└── ...
```

### MEMORY.md format

```markdown
# Memory Index

- [Topic](debugging.md) — One-line description of what this topic covers
- [Another topic](api-conventions.md) — One-line description of what this topic covers
```

- First line: `# Memory Index`
- Each entry: markdown link to topic file + em-dash + one-line description
- Topic files are plain markdown, named by Claude based on content

### Memory topic file format

Each topic file has YAML frontmatter and a markdown body:

```yaml
---
name: kebab-case-slug          # matches filename without .md
description: One-line summary   # used for recall relevance matching
metadata:
  type: user | feedback | project | reference
  node_type: memory             # optional — always "memory" for auto memory
  originSessionId: "uuid"       # optional — session that created this memory
---
```

**Internal cross-references:** Use `[[name-slug]]` in the body to link to another memory. The `name` is the target memory's `name:` frontmatter field. A `[[link]]` that doesn't match any existing memory's `name:` is a dangling reference — it marks a topic worth writing later, not an error. However, dangling references should be audited periodically (see diagnose checklist).

**Validation checklist** (in addition to MEMORY.md index checks above):

- [ ] Frontmatter `name:` matches filename (without `.md`)
- [ ] `description:` is a single sentence suitable for recall matching
- [ ] `metadata.type:` is one of `user`, `feedback`, `project`, `reference`
- [ ] All `[[link]]` references resolve to existing `name:` slugs

### Size limit

First 200 lines or 25KB of `MEMORY.md` (whichever comes first) loaded at session start.
Content beyond this is invisible to Claude until explicitly read with file tools.

### Validation checklist

When auditing `MEMORY.md`, verify:

- [ ] First line is `# Memory Index`
- [ ] Line count under 200 (warn at 150, critical at 200)
- [ ] File size under 25KB (warn at 20KB, critical at 25KB)
- [ ] Each entry is one line with a link to a topic file
- [ ] Referenced topic files actually exist (no dead links)
- [ ] No duplicate entries

---

## Skills

### Directory structure

```
~/.claude/skills/<skill-name>/
├── SKILL.md           # Required
└── references/        # Optional
    ├── ...
```

### SKILL.md frontmatter

```yaml
---
name: my-skill
description: What it does and when to trigger. Be specific and pushy.
allowed-tools: Bash(git:*), Read, Write     # Optional: restrict tool access
---
```

### Size recommendation

Under 500 lines for SKILL.md body. Use `references/` for detailed docs.
