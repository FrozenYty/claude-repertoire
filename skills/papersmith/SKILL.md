---
name: papersmith
version: 0.4.0
description: >
  This skill should be used when the user asks to "polish my paper",
  "translate this abstract", "write a rebuttal to reviewers",
  "draft a cover letter", "analyze experiment data", "generate a LaTeX
  table", or "write a figure caption". Covers academic paper writing,
  polishing, translation (zh↔en), caption/table generation, and review
  response for papers, theses, abstracts, cover letters, and rebuttals.
when_to_use: >
  User is working on academic papers, theses, or scholarly documents:
  writing, polishing, translating between Chinese and English, drafting
  abstracts, titles, cover letters, or rebuttals, responding to reviewers,
  analyzing experiment results, generating LaTeX tables, writing figure
  and table captions. Venue signals: NeurIPS, ICML, ICLR, CVPR, ICCV,
  ECCV, ACL, EMNLP, NAACL, AAAI, IJCAI, ACM, IEEE. Lifecycle signals:
  LaTeX, .tex, camera-ready, revision, accepted, rejected, submission,
  peer review.
author: Tianyu Yao
allowed-tools: Read, Write, Edit, Bash(git:*), Bash(mkdir:*), Bash(ls:*), Bash(cat:*), Bash(head:*), Bash(python:*), Bash(pip:*), Bash(cd:*), Bash(find:*), Glob, Grep, WebSearch, WebFetch, AskUserQuestion, Agent
---

# Papersmith

Route the user's request to the correct prompt template below. Read the
matched file in full, then follow its instructions to accomplish the task.
Do not deviate from the prompt template unless the user explicitly asks.

## Prompt Index

### Translation

| User Intent | Expected Input | Prompt File |
|---|---|---|
| Translate Chinese draft to English LaTeX | Chinese text + LaTeX needed | `prompts/translate-latex-zh2en.md` |
| Translate English LaTeX to plain Chinese | English LaTeX snippet | `prompts/translate-latex-en2zh.md` |
| Translate English to Chinese for Word | English text (for Word) | `prompts/translate-word-en2zh.md` |
| Translate Chinese draft to English for Word | Chinese text (for Word) | `prompts/translate-word-zh2en.md` |

### Rewriting & Polishing

| User Intent | Expected Input | Prompt File |
|---|---|---|
| Rewrite fragmented Chinese draft into formal academic prose | Chinese draft (scattered points, colloquial) | `prompts/rewrite-zh-draft.md` |
| Polish English LaTeX for clarity and rigor | English LaTeX snippet | `prompts/polish-en.md` |
| Polish Chinese text with minimal intervention | Chinese paragraph (near-final) | `prompts/polish-zh.md` |
| Polish abstract into the 5-part structure | Current abstract + optional venue limit | `prompts/polish-abstract.md` |
| Generate 5-10 candidate titles + scoring | Abstract or summary | `prompts/polish-title.md` |
| Writing templates (14 sections: Introduction, Related Work, Methodology, Experiments, Conclusion, Abstract, General Principles, Literature Review, Research Proposal, Investigation Report, Grant Proposal, Progress Report, Thesis Defense Outline, Slide Deck Narrative) | — (loaded on demand) | `references/writing-templates.md` |

### Length Adjustment

| User Intent | Expected Input | Prompt File |
|---|---|---|
| Slightly shorten English LaTeX (~5-15 words) | English LaTeX snippet | `prompts/shorten-en.md` |
| Slightly expand English LaTeX (~5-15 words) | English LaTeX snippet | `prompts/expand-en.md` |

### Quality & Style

| User Intent | Expected Input | Prompt File |
|---|---|---|
| Final consistency and logic check before submission | English LaTeX (near-final) | `prompts/check-logic.md` |
| Remove AI-generated writing patterns from English LaTeX | English LaTeX snippet | `prompts/humanize-en.md` |
| Remove machine-translation tone from Chinese text | Chinese paragraph | `prompts/humanize-zh.md` |
| Chinese and English academic writing anti-patterns (24 patterns, Bad→Rewritten) | — (loaded on demand) | `references/writing-pitfalls.md` |
| Rewrite text to avoid plagiarism similarity while preserving meaning | Original text with similarity concerns | `prompts/rewrite-plagiarism.md` |

### Captions & Tables

| User Intent | Expected Input | Prompt File |
|---|---|---|
| Write a figure caption in English | Chinese description of the figure | `prompts/figure-caption.md` |
| Write a table caption in English | Chinese description of the table | `prompts/table-caption.md` |
| Generate a publication-ready LaTeX table from data | CSV/table data + caption description | `prompts/latex-table.md` |

### Analysis & Review

| User Intent | Expected Input | Prompt File |
|---|---|---|
| Analyze experiment results and write LaTeX analysis | Experiment data table + key findings | `prompts/analyze-experiments.md` |
| Simulate a peer review for a paper draft | Paper PDF + target conference name | `prompts/peer-review.md` |
| Draft a point-by-point response to reviewers | Reviewer comments + optional list of changes | `prompts/rebuttal.md` |
| Draft a 250-400 word cover letter for submission | Title + venue + manuscript summary | `prompts/cover-letter.md` |
| Write broader impact / ethical considerations statement | Title + abstract + method description + optional venue | `prompts/broader-impact.md` |
| Verify reference list completeness, format, and existence | LaTeX snippet + optional target venue | `prompts/check-references.md` |
| Citation format guide (10+ venues, required fields, style files) | — (loaded on demand) | `references/citation-guide.md` |

## Chinese Typography Rules (CRITICAL)

When writing **any Chinese text** — whether in prompts, output format
descriptions, translations, or inline examples — follow these rules:

1. **Quotation marks**: ALWAYS use full-width Chinese quotation marks `""`
   (U+201C / U+201D). NEVER use ASCII half-width `""` (U+0022) around or
   within Chinese text. This is the single most common formatting error.
2. **Punctuation**: Use Chinese full-width marks throughout: `， 。 ； ：`
   (not ASCII `, . ; :`). The only exception is when the surrounding
   paragraph is entirely in English.
3. **Self-check**: Before finalizing any output containing Chinese, scan
   for ASCII `"` (0x22) characters adjacent to Chinese text and replace
   them with full-width `""`.

This rule applies to ALL prompt templates in this toolkit and to any ad-hoc
Chinese text you generate while assisting the user.

## Routing Rules

1. **Single intent**: If the user's request clearly matches one scenario, read
   and execute that file only.
2. **Ambiguous intent**: If the request could match multiple scenarios, ask the
   user to clarify before proceeding. Present the top 2-3 matches briefly.
3. **Compound request**: If the user asks for multiple operations (e.g.,
   "translate this, then polish it"), execute them sequentially in the natural
   order (translate first, then polish, then check).
4. **No match**: If no scenario fits, state that clearly and ask what the user
   intended.

## Iron Rules

These are non-negotiable. Every prompt template in this toolkit inherits
them. When a rule fires, it takes precedence over anything a prompt says.

1. **IRON RULE — No fabricated content.** Never invent citations, author
   names, benchmark scores, dataset statistics, or experimental results.
   If the user hasn't provided a number, don't make one up. Use
   `{{PLACEHOLDER}}` or ask.

2. **IRON RULE — No Markdown in Word output.** Any prompt producing
   Word-bound output must strip all Markdown syntax (`**`, `*`, `###`,
   backticks). The result must paste cleanly into Word with zero
   formatting artifacts.

3. **IRON RULE — Full-width Chinese punctuation.** Any Chinese text
   output must use `""` (U+201C/U+201D) for quotation marks and `，。；：`
   for punctuation. ASCII `"` adjacent to Chinese text is a hard error.

## Input Handling

Each prompt template expects user input signaled by `{{PLACEHOLDER}}` markers.
Before executing a prompt, confirm you have the required input from the user.
If the user already provided the content inline, use it directly. If input is
missing, ask for it explicitly before proceeding.
