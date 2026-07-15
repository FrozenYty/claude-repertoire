# Papersmith

A Claude Code skill for academic research writing. Drop it in, and
Claude will route paper-related requests through 24 specialist prompts
and 3 reference guides.

> 🙏 Built on top of [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) by Leey21. Prompts adapted with gratitude.

> **What it covers:** translation, polishing, abstract / title /
> cover-letter / rebuttal drafting, peer-review simulation, LaTeX table
> generation, figure/table captions, and experiment analysis.

## Why this exists

LLMs writing academic prose routinely make the same mistakes:

- Abstracts that bury the contribution under three sentences of
  background.
- Cover letters that read like AI-generated form mail.
- Chinese text littered with ASCII quotation marks and half-width
  punctuation.
- Word-bound output full of Markdown syntax that doesn't render.
- Experiment analysis that reads like bookkeeping ("A is 0.5, B is
  0.6") instead of synthesis.

This toolkit encodes the conventions, hard rules, and prompt templates
that prevent each of those failures. Most rules are stated with their
*why* — past failure modes traced into prescriptions you can override
when the situation warrants.

## Install

### Claude Code (CLI)

```bash
git clone https://github.com/FrozenYty/claude-repertoire.git
ln -s $(pwd)/claude-repertoire/skills/papersmith ~/.claude/skills/papersmith
```

Claude Code auto-discovers skills under `~/.claude/skills/`. On Windows
(Git Bash / WSL), `~` works the same way; for Command Prompt or
PowerShell, clone to `%USERPROFILE%\.claude\skills\papersmith` instead.

Restart your session if Claude Code is already running, then verify:

```
> /skills
```

You should see `papersmith` in the list. Any paper-related request will
now trigger it.

**To update:** `cd ~/.claude/skills/papersmith && git pull`

### Manual / one-off use

Even without installing as a skill, you can drop the relevant prompt
content into a Claude conversation directly. Each prompt is a
self-contained Markdown file — browse them in
[`prompts/`](https://github.com/FrozenYty/claude-repertoire/tree/main/skills/papersmith/prompts).

## Quick start

After installing, ordinary conversational requests trigger the toolkit:

**Polishing an abstract:**
> Polish this abstract for ICML, 250 words max: <abstract text>

Claude routes to `prompts/polish-abstract.md`, restructures into the
canonical 5-part form (background → gap → method → results → impact),
trims to budget, and returns the rewrite + a sentence-to-part map.

**Drafting a rebuttal:**
> Reviewers said: [comments]. Help me draft a response.

Claude routes to `prompts/respond-to-reviewers.md`, produces a
point-by-point reply with the three response types (concession /
clarification / disagreement) clearly signaled.

**Generating a LaTeX table:**
> Turn this CSV into a publication-ready LaTeX table with booktabs.

Claude routes to `prompts/generate-latex-table.md`, produces a complete
`\begin{table}...\end{table}` block with proper alignment, best-result
bolding, and special-character escaping.

See [`SKILL.md`](SKILL.md) for the full prompt index — 24 prompts in 6
categories.

## Repository structure

```
papersmith/
├── SKILL.md             # entry point — Claude reads this first
├── README.md            # you are here
├── CONTRIBUTING.md      # how to add prompts
├── CHANGELOG.md         # version history
├── prompts/             # 24 task-specific prompts
└── references/          # 3 long-form references
    ├── writing-anti-patterns.md     # 24 anti-patterns (12 zh + 12 en)
    ├── writing-templates.md         # 7 section structure templates
    └── venue-citation-guide.md      # 10+ venue citation formats
```

## What's covered

**Writing tasks** — translate (zh↔en, LaTeX or Word), polish (Chinese,
English, abstract, title), shorten/expand, humanize, logic-check,
analyze experiments, simulate peer review, respond to reviewers, draft
cover letter, rewrite to avoid plagiarism.

**Captions & tables** — figure captions, table captions, publication-ready
LaTeX tables with booktabs formatting and auto-alignment.

## Design rules baked in

- **Chinese typography**: full-width quotation marks (U+201C/U+201D)
  and punctuation (， 。 ； ：) throughout any Chinese output.
- **No Markdown in Word output**: any Word-bound prompt strips all
  Markdown syntax — the result pastes cleanly.
- **No fabricated content**: never invent citations, statistics, or
  benchmark scores. Use `{{PLACEHOLDER}}` or ask.

Full rationale in the Iron Rules section of
[`SKILL.md`](SKILL.md).

## Versioning

Semver. See [`CHANGELOG.md`](CHANGELOG.md). Current: **v0.4.0**.

## Contributing

Contributions welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the
conventions — file formats, registration locations, testing guidance.

The big picture: toolkit content is roughly half *prompts* (per-task
behavior) and half *references* (rules + templates loaded on demand).
Adding a new prompt shouldn't require editing references; adding a new
reference shouldn't require editing prompts. The structure is designed
to keep these orthogonal.

## License & Attribution

**No license** — this toolkit mirrors the licensing approach of its primary
upstream source (see Acknowledgments below).

The prompt templates under `prompts/` are adapted and extended from
[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing),
a Chinese-language collection of academic writing prompts curated from
researchers at MSRA, ByteDance Seed, Shanghai AI Lab, and several
universities. The original repository carries no explicit license, so
this fork maintains the same posture: shared publicly for reference and
discussion, with the intent to defer to the upstream author's wishes.

**Original components in this repository** (SKILL.md routing structure,
contributing guide, and reference layers) are likewise shared as-is,
no specific license attached.

If you'd like to use, redistribute, or relicense any part of this work,
please reach out to the upstream author for the prompts, or open an
issue here for the original components.

## Acknowledgments

- **Prompt templates adapted from
  [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)** —
  a community-curated collection of academic writing prompts from
  researchers at top labs and universities. The `prompts/` directory in
  this repository builds on those patterns, extending them into a routed
  skill structure and adding new prompts (cover letter, response to
  reviewers, polish abstract, polish title) along with writing reference
  layers.
- Skill structure follows the patterns documented in Anthropic's
  skill-creator framework.

Inspired by, derived from, and indebted to the above. Not affiliated
with any of them.
