# Contributing to Drawsmith

## How to Contribute

### Adding a New draw.io Layout Template

Templates live in `references/drawio-layouts.md`. Each follows this format:

```markdown
## §N Template Name

**When to use:** [scenario description]

**Canvas:** WxH. [orientation]

**Layout conventions:**
- [rule]
- [rule]

**Shape vocabulary:**

| Element | Style keywords |
|---|---|

**To adapt:** [customization notes]
```

Requirements:
- Section number matches the index table at the top of the file.
- All coordinates in examples are multiples of 10.
- Every forward edge satisfies the Flow Direction rule from `drawio-guide.md`.
- Shapes reference colors from `style-guide.md` (not hardcoded hex values unless
  providing a complete ready-to-copy example).

### Adding a New Color Palette

Palettes are sourced from [Academic-Color](https://github.com/Rookie-00001/Academic-Color).
To add a new palette:

1. Verify the palette is from a published journal figure (not synthetic unless
   placing it in the Curated Recommended section).
2. Add the palette to the appropriate section in `references/style-guide.md`:
   - §1.2 Top-Tier (Nature/Science/Cell family)
   - §1.3 Medical & Life Sciences
   - §1.4 Physical Sciences & Engineering
   - §1.5 Interdisciplinary
   - §1.6 Curated Recommended
3. Include: journal name, year, hex codes (lowercase), color count, a one-line
   use-case description, and a Python list form.
4. Update the Palette Selection Rules table (§1.7) if the new palette fills a gap.

### Adding a New Matplotlib Chart Template

Templates live in `references/matplotlib-scripts.md`. Each must:
- Be a runnable self-contained Python script.
- Apply the rcParams block from `matplotlib-guide.md`.
- Use colors from `style-guide.md`.
- Output `.png` at >=600 dpi.

### Modifying Iron Rules

Iron Rules live in `SKILL.md`. When modifying:
- Rule descriptions are one sentence — what to enforce, not why.
- "IRON RULE" prefix for mandatory rules, "RECOMMENDED" for best practices.
- Each rule change needs a corresponding self-check item update in the
  affected reference file (`drawio-guide.md` or `matplotlib-guide.md`).

### Self-Check Items

Self-check checklists are the enforcement mechanism. When adding a new rule
or fixing a recurring bug:

1. Add the failure pattern to the relevant Common Pitfalls section.
2. Add a corresponding item to the Self-Check checklist.
3. The checklist item must be falsifiable — a yes/no question the model can
   answer by inspecting its own output.

### Testing

Before submitting a PR:

1. Install the skill locally:
   ```bash
   ln -s $(pwd)/skills/drawsmith ~/.claude/skills/drawsmith
   ```

2. Test with a real diagram request:
   - "Draw a system architecture diagram for a microservices app"
   - "Plot a grouped bar chart comparing sales data"

3. Verify the output passes all self-check items.

### Format Conventions

- All documentation in English.
- draw.io XML: coords multiples of 10, lowercase_underscore IDs.
- matplotlib: Times New Roman, Nature palette default, 600 dpi default.
- Hex colors: lowercase, 6-digit.
- Section headers: `## §N` for templates, `## N.` for rules.

### Pull Request Checklist

- [ ] New templates/scripts follow the existing format.
- [ ] Colors reference `style-guide.md` (not ad-hoc hex values).
- [ ] Self-check items are updated if behavior changes.
- [ ] `README.md` feature counts are updated (templates, chart types, palettes).
- [ ] Tested with a real Claude Code session.
