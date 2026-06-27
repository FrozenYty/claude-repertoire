# 5. Language

[中文版本](05-language-zh.md)

## Why this rule exists

This rule has two layers: (a) the two-track language strategy, and (b) the
Unicode typography discipline required for Chinese output.

The two-track strategy exists because the user is a Chinese university student
who thinks and communicates most comfortably in Chinese, but project files —
code, documentation, configs — must be in English for international
compatibility. The rule separates the interaction language (always Chinese)
from the output language (always English) so neither gets compromised.

The typography layer exists because LLMs routinely produce ASCII `"`
(U+0022) adjacent to Chinese text — the single most common formatting
error in Chinese LLM output. The full-width quotation marks `""`
(U+201C/U+201D) are mandatory in Chinese typography, but they are
visually indistinguishable from ASCII `"` in most monospace editors. You
cannot trust your eyes to catch this error.

A concrete case: during an audit of 24 prompt files, one file —
`humanize-zh.md`, the file that *defines the Chinese typography rules* —
had five distinct quote bugs. They included ASCII quotes in Chinese
context, a reversed quote pair (`U+201D...U+201C` instead of
`U+201C...U+201D`), and a left-quote used as a closing right-quote. A
human proofreader scanning the file would see no difference.

## What it looks like in practice

**The two-track strategy:**

| Context | Language | Example |
|---------|----------|---------|
| Chatting with the user | Chinese (Simplified) | "好的，我来帮你修复这个 bug" |
| Writing files to disk | English | Code, docs, CLAUDE.md, rules, memory, comments |
| User explicitly requests Chinese | Chinese | Academic papers, Chinese-facing docs |

**Bad — chat in English, or files written in Chinese without request:**
```
# In chat: "I'll fix that bug for you now."
# In a file: 这是一个工具函数，用于解析配置文件
```
The user has to mentally translate; the file isn't accessible to
international collaborators or tooling.

**Good — chat in Chinese, files in English:**
Chat: "好的，我现在来修复这个 bug。"
File: `# Utility to parse configuration files`

**Bad — invisible typography error:**
```
carries an obvious "machine flavor" or "translationese" into natural academic prose
```
The quotes around "machine flavor" and "translationese" are ASCII `"`
(U+0022). They look correct but are typographically wrong in Chinese
context.

**Good — verified at byte level:**
```python
python -c "print([hex(ord(c)) for c in line if ord(c)>127])"
```
This one-liner reveals every non-ASCII character in the string. U+201C
and U+201D are correct; U+0022 is not.

## When to relax it

The two-track strategy relaxes only when the user explicitly requests
Chinese output files (e.g., Chinese academic papers, Chinese-facing
documentation).

For typography: when the entire surrounding paragraph is in English (e.g.,
a code comment or an all-English technical section), ASCII quotes are
acceptable. The Unicode typography rules activate specifically when
Chinese characters appear in the output.
