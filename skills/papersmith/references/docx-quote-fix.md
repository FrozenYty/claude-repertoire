# DOCX Chinese Quote Repair

Self-contained python-docx snippet for fixing ASCII `"` → full-width `""`
(U+201C/U+201D) in generated `.docx` files. **Never modify Python source
code** — fix quotes directly in the output document.

## When to use

- A Python script generates a `.docx` with Chinese content
- The source uses ASCII `"` inside Chinese strings (e.g., `'…"text"…'`)
- You need to replace them with proper Chinese quotation marks

## Complete script

```python
from docx import Document

LQ = chr(0x201C)  # "
RQ = chr(0x201D)  # "
SEP = chr(0x1F)   # Unit Separator — does not appear in document text


def has_cjk(text):
    """Return True if text contains any CJK character or punctuation."""
    for c in text:
        o = ord(c)
        if (0x2E80 <= o <= 0x2EFF   # CJK Radicals
            or 0x3000 <= o <= 0x303F  # CJK Punctuation (。，；：etc.)
            or 0x3200 <= o <= 0x32FF  # Enclosed CJK
            or 0x3400 <= o <= 0x4DBF  # CJK Extension A
            or 0x4E00 <= o <= 0x9FFF  # CJK Unified Ideographs
            or 0xF900 <= o <= 0xFAFF  # CJK Compatibility
            or 0xFF00 <= o <= 0xFFEF  # Fullwidth Forms
        ):
            return True
    return False


def fix_quotes_in_docx(path):
    """Fix ASCII quotes → Chinese full-width quotes in a .docx file.
    
    Uses paragraph-level state machine: concatenates all runs,
    pairs ALL \" as alternating LQ/RQ, then splits back.
    This handles quotes that span multiple runs correctly.
    """
    doc = Document(path)
    fixed = 0

    for p in doc.paragraphs:
        runs = p.runs
        if not runs:
            continue

        # Only process paragraphs containing Chinese
        par_text = ''.join(run.text or '' for run in runs)
        if not has_cjk(par_text):
            continue
        if '"' not in par_text and LQ not in par_text and RQ not in par_text:
            continue

        # Step 1: Revert any existing Chinese quotes to ASCII
        for run in runs:
            if run.text:
                run.text = run.text.replace(LQ, '"').replace(RQ, '"')

        # Step 2: Concatenate with sentinel, pair all " as LQ/RQ
        combined = SEP.join([run.text or '' for run in runs])
        chars = list(combined)
        quote_count = 0
        for i, ch in enumerate(chars):
            if ch == '"':
                quote_count += 1
                chars[i] = LQ if quote_count % 2 == 1 else RQ

        # Step 3: Split back into runs
        parts = ''.join(chars).split(SEP)
        for run, new_text in zip(runs, parts):
            if run.text != new_text:
                run.text = new_text
                fixed += 1

    doc.save(path)
    return fixed


def verify_quotes(path):
    """Check quote pairing. Returns (LQ_count, RQ_count, ASCII_near_CJK_count)."""
    doc = Document(path)
    lq = rq = ascii_issues = 0

    for p in doc.paragraphs:
        for run in p.runs:
            t = run.text or ''
            lq += t.count(LQ)
            rq += t.count(RQ)
            for i, ch in enumerate(t):
                if ch == '"':
                    prev = t[i - 1] if i > 0 else ''
                    nxt = t[i + 1] if i + 1 < len(t) else ''
                    if any(ord(c) > 127 for c in (prev, nxt) if c):
                        ascii_issues += 1

    return lq, rq, ascii_issues


# ── Usage ──
if __name__ == '__main__':
    import sys
    for path in sys.argv[1:]:
        lq_before, rq_before, asc_before = verify_quotes(path)
        if asc_before == 0 and lq_before == rq_before:
            print(f'{path}: already clean, skipping')
            continue

        n = fix_quotes_in_docx(path)
        lq, rq, asc = verify_quotes(path)
        paired = 'OK' if lq == rq else 'MISMATCH'
        print(f'{path}: {n} runs fixed | LQ={lq} RQ={rq} | ASCII={asc} | {paired}')
```

## Key pitfalls

1. **CJK detection must cover punctuation.** `。` is U+3002, which is
   *below* U+4E00 (`一`). A naive `'一' <= c <= '鿿'` check misses it,
   causing quotes adjacent to Chinese punctuation to remain unfixed.

2. **Quotes span runs.** An interview quote like `"text…。"` may have
   the opening `"` in one run and the closing `"` in another. The
   sentinel-separator approach handles this; per-run pairing does not.

3. **Never fix Python source.** Replacing `"` with `"`/`"` in `.py` files
   turns Python string delimiters into invalid syntax (`SyntaxError:
   invalid character U+201D`). Always fix the generated DOCX, not the
   generator script.

## See also

- SKILL.md § Chinese Typography Rules — rule #4 (strategy overview)
- SKILL.md § Iron Rules — rule #3 (full-width punctuation mandate)
