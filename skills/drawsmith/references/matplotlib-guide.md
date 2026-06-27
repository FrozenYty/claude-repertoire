# Matplotlib Chart Reference

Read this file before generating any matplotlib/seaborn plotting code.
It enforces the conventions that produce professional-grade figures.
For color palettes, typefaces, resolution standards, and spacing rules,
see `style-guide.md` — the single source of truth shared with draw.io.

## Workflow

When the user asks for a chart, do this in order:

1. **Pick the chart type** — if not already chosen, route through
   `prompts/chart-pick.md` first.
2. **Read the relevant template** in `matplotlib-templates.md`
   (19 templates, indexed by the same chart-type names as chart-pick).
3. **Apply the professional style block** from this file (rcParams).
   For color palettes and typefaces, see `style-guide.md`.
4. **Adapt to the user's data** — change variable names, axis labels,
   legend, but KEEP the style invariants from this file.
5. **Save**: `.png` (>=600 dpi, default) + `.pdf` (vector, optional).
   Both with `bbox_inches='tight'`.

## Professional Style Block (paste-ready)

Paste this rcParams block at the top of every plotting script.
Colors and detailed typeface options are in `style-guide.md`.

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

# --- Publication-ready rcParams ---
mpl.rcParams.update({
    # Fonts: Times New Roman is the safe default across CS/Nature/IEEE.
    # For ML/CS conferences, "Times New Roman" or "DejaVu Serif" are accepted.
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "mathtext.fontset": "stix",  # math glyphs match Times
    # Sizes (in pt): titles 12, labels 11, ticks 10, legend 10, annotation 9
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.titlesize": 13,
    # Lines & markers
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.5,
    "lines.markersize": 5,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.minor.width": 0.5,
    "ytick.minor.width": 0.5,
    # Tick direction inward (Nature/Science style); use "out" for IEEE
    "xtick.direction": "in",
    "ytick.direction": "in",
    # Grid: light, on by default for line/scatter; off for bar
    "axes.grid": False,
    "grid.linewidth": 0.5,
    "grid.alpha": 0.4,
    # Spines: keep all four; some venues prefer top/right off — leave decision
    # to per-template.
    # PDF font embedding (CRITICAL for paper submission)
    "pdf.fonttype": 42,   # TrueType, not Type-3 (Type-3 fails ACM/IEEE checkers)
    "ps.fonttype": 42,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
    # Figure size (single-column paper figure default)
    "figure.figsize": (3.5, 2.6),
    "figure.constrained_layout.use": True,
})
```

**Why each setting matters:**
- `pdf.fonttype = 42` embeds fonts as TrueType rather than Type-3 outlines,
  ensuring consistent rendering across platforms and viewers. Recommended.
- `xtick.direction = in` is a clean, journal-grade convention. Switch to
  `out` if you prefer outward ticks. Don't mix styles.
- Default `figure.figsize = (5.5, 4.1)` is the standard 4:3 ratio. Override
  per figure — see `style-guide.md` §5.3 for sizing options.
- `constrained_layout.use = True` removes the need for manual
  `plt.tight_layout()` and handles legends-outside-axes correctly.

## Figure Sizing

For detailed sizing, aspect ratios, and canvas dimensions, see
`style-guide.md` §5.2–5.3. Quick reference:

| Format | Width (in) | Ratio | Use |
|--------|-----------|-------|-----|
| Narrow | 5.5 | 4:3 | Default, general charts |
| Wide | 8.0 | 16:9 | Slides, landscape |
| Square | 5.0 | 1:1 | Scatter, heatmap, confusion matrix |

Aspect ratio: avoid arbitrary squares. Default 4:3 for charts with
a single y-axis; 5:3 for time-series; 1:1 for scatterplots and
heatmaps when both dimensions are the same kind of data.

## Color Palettes

Color palettes are the single source of truth in `style-guide.md` §1.
That file defines the IEEE semantic palette (default for technical
diagrams), four journal palettes (Nature, Science, Cell, Nature Physics),
and selection rules. Refer to it — don't duplicate palette definitions here.

**Key rules:**
- Never use matplotlib defaults or `jet`/`rainbow` colormaps.
- <=6 categories: Nature or Nature Physics palette.
- >=7 categories: Cell palette.
- Diverging data: `RdBu_r` or `coolwarm`.
- Your method vs baselines: use the IEEE semantic mapping (your method =
  attention purple `#9673A6`).

For colorblind-safe options, see `style-guide.md` §1.3.

## Statistical Conventions

**Error bars / confidence intervals — pick one and disclose it:**
- 1 standard deviation: `yerr=std`. Common in ML.
- 95% CI from N runs: `yerr=1.96 * std / sqrt(N)`. Better for ≤10 runs.
- 95% CI from bootstrap: use `seaborn.barplot(errorbar="ci")` or compute
  with `scipy.stats.bootstrap`.

State which one in the figure caption: "Error bars indicate ±1 SD over 5
seeds." Don't use error bars without disclosing what they represent.

**Significance markers (only when statistically tested):**
- `ns` (not significant)
- `*` p < 0.05
- `**` p < 0.01
- `***` p < 0.001
Place over the bar pair being compared with a horizontal bracket. Don't add
stars to figures where the test wasn't run.

**Multiple-run plotting (e.g., training curves):**
- Show the mean as a solid line.
- Show the variance as a semi-transparent band: `ax.fill_between(x,
  mean-std, mean+std, alpha=0.2, color=color)`.
- Don't use individual run lines unless N ≤ 3 (otherwise noise dominates).

## Scale Treatments

**Broken axis** (when a few outliers compress the rest):

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, height_ratios=[1, 3])
# Plot the same data on both
ax1.bar(...); ax2.bar(...)
# Limit each
ax1.set_ylim(80, 100)   # outlier range
ax2.set_ylim(0, 20)     # main range
# Hide the spines between
ax1.spines["bottom"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax1.tick_params(labeltop=False, top=False)
ax2.xaxis.tick_bottom()
# Diagonal break marks
d = .015
kwargs = dict(transform=ax1.transAxes, color="k", clip_on=False, lw=0.8)
ax1.plot((-d, +d), (-d, +d), **kwargs)
ax1.plot((1-d, 1+d), (-d, +d), **kwargs)
kwargs.update(transform=ax2.transAxes)
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
ax2.plot((1-d, 1+d), (1-d, 1+d), **kwargs)
```

**Log scale** (data spans orders of magnitude, e.g. parameter counts):

```python
ax.set_yscale("log")
# Major ticks at decades; minor at 2,3,...,9
from matplotlib.ticker import LogLocator, NullFormatter
ax.yaxis.set_major_locator(LogLocator(base=10, numticks=8))
ax.yaxis.set_minor_locator(LogLocator(base=10, subs=range(2,10), numticks=80))
ax.yaxis.set_minor_formatter(NullFormatter())
```

**Symlog** (data crosses zero with wide range): `ax.set_yscale("symlog",
linthresh=1)`. Linthresh is the cutoff below which the scale is linear.

## Saving Figures

```python
out = "fig_results"
fig.savefig(f"{out}.pdf")           # vector, for paper
fig.savefig(f"{out}.png", dpi=600)  # raster, for slides / preview
```

**Don't:** save as `.jpg` (lossy compression on text), `.eps` (deprecated;
modern paper systems prefer PDF), or low-dpi PNG (600 dpi minimum).

### DPI Selection Guide

Choose PNG DPI based on the figure type and intended use. The default is 600;
scale up when the figure demands it. Always match the DPI to what the user
specified; when unspecified, use the following defaults:

| DPI | When to use |
|-----|-------------|
| 600 | Standard figures: bar charts, line plots, ROC/PR curves, box/violin plots, donut/pie charts, radar charts — clean lines and solid fills don't benefit from higher DPI |
| 800 | Detailed figures: scatter plots (many points), heatmaps, multi-panel faceted grids, bar+line combos, dual-axis plots, Pareto fronts — finer pixel grid needed when data density is higher |
| 1000 | Maximum fidelity: camera-ready final submission, images with fine text or thin lines, plots intended for poster printing (A0), high-detail visualizations, or when the user explicitly asks for "highest quality" |

The `savefig.dpi` rcParam is a floor (600). Override it per `fig.savefig(..., dpi=N)` when the figure needs >600.

**Self-check:** Did the user mention a specific DPI or a venue known to require higher raster quality (e.g., Nature Methods, Cell)? If yes, match it. If not, apply the table above.

**Don't:** use `plt.show()` in a script intended for batch generation; it
blocks. Use `plt.close(fig)` after saving.

## Common Pitfalls (real failures observed)

1. **Type 3 font failure** — text renders as outlines in some PDF viewers.
   Fix: `pdf.fonttype = 42`. Recommended.
2. **Default matplotlib blue/orange** — looks "made with matplotlib" rather
   than designed. Fix: set a palette from this file, or pass
   `color=palette[i]` explicitly.
3. **Unreadable axis ticks** — auto-generated dense labels. Fix: set
   `MaxNLocator(6)` or specify ticks explicitly.
4. **Legend covering data** — happens with `loc='best'` or when data
   extends to the legend corner. Fix: for horizontal bar charts, use
   `loc='upper left'` (bars extend right, not left). For vertical bar
   charts, use `loc='upper right'`. Only move outside as last resort.
5. **Dual-panel legend duplication** — each subplot getting its own
   `ax.legend()` wastes space and risks overlap in narrow panels. Fix:
   merge into a single `fig.legend(handles, ..., loc='upper center',
   bbox_to_anchor=(0.5, 0.98), ncol=N)`. When legends differ between
   subplots, still merge all handles; if >4 items, place below:
   `bbox_to_anchor=(0.5, -0.08), ncol=4`. Separated per-axis legends
   are the fallback, and only in the empty quadrant.
6. **Pie/donut labels clipped at edge** — default `labeldistance≈1.1`
   places labels too close to wedges. Fix: set `labeldistance=1.12` and
   increase `figsize` by 15-20%. Validate: longest label in inches
   (chars × ~0.09" Latin, ~0.12" Chinese at 8-10pt) must fit within
   half the figure width minus the pie radius.
7. **Legend pushed off-canvas by `bbox_to_anchor`** — occurs when
   `bbox_to_anchor=(1.02, 1.0)` places the legend outside without
   `constrained_layout` accounting for it. Fix: pair `fig.legend()`
   with `constrained_layout.use = True`. Prefer coordinates inside
   [0, 1] (e.g., `(0.5, 0.96)`) so the layout engine manages space.
8. **Inconsistent units** — "Time (s)" vs "Time" vs "time(s)". Fix: pick
   one convention per paper. Usually "Time (s)" with capitalized first
   letter and unit in parens.
9. **Stretched aspect ratio** — figure is 12:3 because the user copied the
   default. Fix: set `figsize` per the venue table above.
10. **No baseline comparison** — bar chart with only the proposed method.
   Always include baselines for ML comparisons.
11. **Error bars without disclosure** — caption says "results" but doesn't
   say if bars are SD/SE/CI. Always disclose.
12. **Color carrying critical info** — only color distinguishes lines, fails
   for colorblind readers and B&W printing. Fix: also vary linestyle (`-`,
   `--`, `:`, `-.`) or marker (`o`, `s`, `^`, `D`).
13. **Title management** — for figures embedded in documents with their
    own caption system (LaTeX, Word, HTML), omit `ax.set_title(...)` to
    avoid duplication. For standalone images or slides, set the title.

## Anti-Patterns (API misuse)

14. **Mixing pyplot and OO APIs** — never call `plt.plot()` inside a script
    that also uses `fig, ax = plt.subplots()`. Use the OO API exclusively:
    `ax.plot()`, `ax.set_xlabel()`, `fig.savefig()`.
15. **`plt.show()` before `savefig()`** — `plt.show()` clears the figure.
    Always `savefig()` first. Never call `plt.show()` in script code.
16. **Global state (`plt.gca()`, `plt.gcf()`)** — implicit state-machine
    behavior breaks with multiple figures. Always pass explicit `fig`/`ax`.
17. **`tight_layout()` vs `constrained_layout`** — prefer
    `constrained_layout.use = True` in rcParams.

## Hybrid Export (large datasets)

For scatter/contour plots with >10k points, rasterize only the
data while keeping axes/text as sharp vectors:

```python
ax.scatter(x, y, s=1, rasterized=True)
fig.savefig('output.pdf', dpi=300)
```

## Self-check (before delivering)## Self-check (before delivering)

```
 1. fonttype 42 set (recommended):              pass/fail
 2. Figure size appropriate (not default 6.4x4.8): pass/fail
 3. Palette from style-guide.md (not matplotlib default): pass/fail
 4. Legend doesn't cover data:                  pass/fail
 5. Multi-panel uses shared fig.legend():       pass/fail
 6. Pie labels fit within figure width:         pass/fail
 7. bbox_to_anchor inside [0,1] (or constrained): pass/fail
 8. Axis labels include units:                  pass/fail
 9. Error bars disclosed (if present):          pass/fail
10. Title set (standalone) or omitted (embedded in document): pass/fail
11. Lines distinguishable in B&W (linestyle):   pass/fail
12. No `jet` / `rainbow` colormap:             pass/fail
13. Saved as .png (>=600 dpi) + .pdf (optional): pass/fail
```

## Optional: SciencePlots integration

If `SciencePlots` (`pip install SciencePlots`) is installed, you can shorten
the rcParams block to:

```python
import scienceplots
plt.style.use(["science", "ieee"])  # or "nature", "high-vis"
```

This sets fonts, sizes, ticks, and colors close to IEEE / Nature
conventions in one line. Still set `pdf.fonttype = 42` afterward
because some SciencePlots styles miss it.

---

## Seaborn Quick Integration

Seaborn (`import seaborn as sns`) provides a high-level styling wrapper over
matplotlib. It is an optional accelerator — the full rcParams block from
this guide works identically with or without seaborn.

### One-liner Setup

```python
import seaborn as sns
sns.set_theme(style="ticks", context="paper", palette="deep")
```

This sets fonts, grid, tick direction, and color cycle in one call.
Override individual rcParams afterward if needed:

```python
sns.set_theme(style="ticks", context="paper")
mpl.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42})  # always after
```

### Style + Context Matrix

**Style** (background/grid):

| Style | Best for |
|-------|----------|
| `ticks` | Publication / print (recommended default) |
| `whitegrid` | Data-dense charts (box, violin) |
| `darkgrid` | Quick exploration |
| `white` | Embedded in documents |
| `dark` | Slides, dark backgrounds |

**Context** (scale):

| Context | Use |
|---------|-----|
| `paper` | Journal columns, academic papers |
| `notebook` | Jupyter, general work |
| `talk` | Presentation slides |
| `poster` | Conference posters |

Use context to scale uniformly — don't manually tweak individual font sizes
inside the same project.

### Despine (Remove Unnecessary Spines)

```python
sns.despine()                    # top + right
sns.despine(offset=10, trim=True) # with offset
```

### Scoped Styles (No Global Leak)

```python
with sns.axes_style("ticks"), sns.plotting_context("talk"):
    fig, ax = plt.subplots()
    ax.bar(...)
    sns.despine()
    fig.savefig("chart.png", dpi=600)
```

### seaborn vs matplotlib: When to Use Which

| Scenario | Use |
|----------|-----|
| Quick professional styling | `sns.set_theme()` |
| Fine-grained control over every parameter | matplotlib rcParams (this guide's style block) |
| Statistical plots (box, violin, bar with CI) | `sns.boxplot()`, `sns.barplot()` etc. |
| Custom chart types not in seaborn | matplotlib directly, with seaborn style |
| Batch scripts (minimal dependencies) | matplotlib rcParams only |

The `matplotlib-templates.md` templates work with either approach — seaborn
is optional but recommended for quicker setup.

---

## Subplots & Composite Charts

Subplots and multi-panel figures are the most error-prone matplotlib pattern.
Get these right or the entire figure is broken.

### Layout engine

Use the modern `layout='constrained'` parameter (matplotlib >= 3.8):

```python
fig, axes = plt.subplots(2, 3, figsize=(10, 6), layout='constrained')
```

Never mix `tight_layout()` with constrained layout — calling
`tight_layout()` permanently disables the constraint solver. Never call
`subplots_adjust()` with constrained layout active — use
`fig.get_layout_engine().set()` instead:

```python
fig.get_layout_engine().set(w_pad=0.1, h_pad=0.1, wspace=0.2, hspace=0.2)
```

### Panel labels

Use `ScaledTranslation` for physical offsets. Place labels OUTSIDE the
axes (above top-left corner) to avoid overlapping axis tick labels:

```python
import matplotlib.transforms as mtransforms

for label, ax in zip(['a', 'b', 'c', 'd'], axes.flat):
    trans = mtransforms.ScaledTranslation(-15/72, 8/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize=8, fontweight='bold', va='bottom', fontfamily='sans-serif')
```

- `va='bottom'` anchors text above the axis top edge (no overlap with ticks).
- Negative x-offset (-15pt) shifts label left to clear the top-right corner.
- Never use raw `ax.text(-0.1, 1.1, ...)` in axes fraction — the offset
  varies with subplot size.

### Colorbar with subplots

Three patterns, ranked by reliability:

**1. Shared colorbar (simplest):**

```python
fig, axes = plt.subplots(2, 2, layout='constrained')
for ax in axes.flat:
    im = ax.pcolormesh(data, vmin=0, vmax=1, cmap='viridis')
fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.8)
```

Always set `vmin`/`vmax` explicitly — without them, the last-plotted
image's range determines the colorbar, which is misleading.

**2. Individual colorbars (complex):**

```python
from mpl_toolkits.axes_grid1 import make_axes_locatable
for ax in axes.flat:
    im = ax.imshow(data, cmap='viridis')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.1)
    fig.colorbar(im, cax=cax)
```

**3. Never pass a regular axes as `cax=`** — this steals the axis space
and destroys the subplot grid. Always use `make_axes_locatable` or
`fig.add_axes()`.

### Legend with subplots

Multi-panel figures should use ONE legend, not one per panel:

```python
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center',
           bbox_to_anchor=(0.5, 1.02), ncol=len(labels))
```

If placing a legend outside an axes with `bbox_to_anchor`, call
`leg.set_in_layout(False)` so the subplot doesn't shrink:

```python
leg = ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))
leg.set_in_layout(False)
```

> Note: `constrained_layout` does not yet handle `Figure.legend()` in
> matplotlib 3.10. Legends at figure level require manual adjustment.

### Common subplot failures

1. **Colorbar on single axes** — steals space, breaks alignment.
   Use `fig.colorbar(..., ax=all_axes)` or `make_axes_locatable`.
2. **Missing `vmin`/`vmax`** — inconsistent color mapping across panels
   when sharing a colorbar. Always set both explicitly.
3. **Legend on every panel** — merge into one `fig.legend()`.
4. **`tight_layout()` after constrained layout** — permanently disables
   the constraint engine. Pick one, never mix.
5. **`subplots_adjust()` with constrained layout** — raises warning,
   layout breaks. Use `get_layout_engine().set()` instead.
6. **Grid lines over data** — grid defaults to zorder=2, same as markers.
   Set `ax.set_axisbelow(True)` so grid draws behind all data artists.
7. **`fig.legend()` without `loc='outside ...'`** — older matplotlib ignores
   figure-level legends under constrained_layout. Use
   `fig.legend(loc='outside right upper')` (3.7+) or reserve a legend subplot.

### Dual-axis combo charts

For bar + line overlays with `twinx()`:

```python
fig, ax1 = plt.subplots(figsize=(8, 4), layout='constrained')

# Bars on left axis — use alpha so line is visible
ax1.bar(x, bar_data, color='tab:blue', alpha=0.5, label='Revenue (k$)')
ax1.set_ylabel('Revenue (k$)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Line on right axis — color-code axis to match
ax2 = ax1.twinx()
ax2.plot(x, line_data, color='tab:orange', marker='o', linewidth=2,
         label='Margin (%)', zorder=5)
ax2.set_ylabel('Margin (%)', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Single combined legend (never ax1.legend() + ax2.legend() separately)
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')
```

Key rules:
- Color-code Y-axis labels and ticks to match data (blue=left, orange=right).
- Combine legends into ONE box — two separate `legend()` calls overlap.
- Set `alpha=0.3-0.5` on bars so the line is visible through bar occlusion.
- Set `zorder=5` on the line to ensure it draws above bars (both default to 2).
- Align zero baselines when both datasets start near zero.
- Do NOT use dual axes for extreme scale differences (1-100 vs 0.0001-0.001).

---

## See also
- `style-guide.md` — color palettes, typefaces, resolution standards shared with draw.io
- `matplotlib-templates.md` — 19 runnable chart templates
- `cjk-fonts-guide.md` — CJK font configuration for Chinese text
