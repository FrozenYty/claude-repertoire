"""matplotlib-check.py — Static analysis validator for matplotlib scripts.

Checks generated Python plotting code for common anti-patterns before
the script is run. Catches legend overlap, label crowding, missing
layout config, and other issues that only become visible at render time.

Usage: python matplotlib-check.py <script.py>
"""

import sys
import re


def check(path):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    issues = []
    warnings = []

    # 1. constrained_layout vs tight_layout
    has_constrained = "constrained_layout" in code
    has_tight = "tight_layout()" in code
    if has_tight and not has_constrained:
        warnings.append(
            "Prefer constrained_layout.use=True in rcParams over "
            "calling tight_layout() after plotting"
        )

    # 2. Legend may cover data — check for bbox_to_anchor outside [0,1]
    legend_matches = re.findall(
        r"bbox_to_anchor=\(([\d.]+),\s*([\d.]+)\)", code
    )
    for mx, my in legend_matches:
        x, y = float(mx), float(my)
        if x < 0 or x > 1 or y < 0 or y > 1:
            if "constrained_layout" not in code and "bbox_inches" not in code:
                issues.append(
                    f"Legend placed at bbox_to_anchor=({x},{y}) outside [0,1] "
                    "without constrained_layout — may be clipped at save"
                )

    # 3. Pie/donut label distance too small
    pie_label = re.search(r"labeldistance=([\d.]+)", code)
    if pie_label and float(pie_label.group(1)) < 1.1:
        warnings.append(
            f"Pie labeldistance={pie_label.group(1)} is tight — "
            "increase to >=1.1 for readability"
        )

    # 4. Pie chart without figsize adjustment
    if ("plt.pie(" in code or "ax.pie(" in code or ".pie(" in code):
        figsize = re.search(r"figsize=\(([\d.]+),\s*([\d.]+)\)", code)
        if figsize:
            w, h = float(figsize.group(1)), float(figsize.group(2))
            if w < 6 and h < 6:
                warnings.append(
                    f"Pie chart with small figsize ({w}x{h}) — "
                    "increase by 15-20% for label clearance"
                )

    # 5. plt.show() before savefig()
    show_pos = code.find("plt.show()")
    save_pos = code.find("savefig")
    if show_pos >= 0 and save_pos >= 0 and show_pos < save_pos:
        issues.append(
            "plt.show() called before savefig() — "
            "figure will be empty. Swap order."
        )

    # 6. Missing pdf.fonttype
    if "pdf.fonttype" not in code and ".pdf" in code:
        warnings.append(
            "PDF output without pdf.fonttype=42 — "
            "text may render as bitmaps in some viewers"
        )

    # 7. Font too small for figure size
    fontsize = re.search(r"font\.size['\"]?\s*:\s*(\d+)", code)
    figsize = re.search(r"figsize=\(([\d.]+),\s*([\d.]+)\)", code)
    if fontsize and figsize:
        fs = int(fontsize.group(1))
        w = float(figsize.group(1))
        if fs < 8 and w > 6:
            warnings.append(
                f"Font size {fs}pt on figure width {w}in — "
                "text may be unreadable at print scale"
            )

    # 8. No legend when multiple plots exist
    plot_calls = len(re.findall(r"\.(plot|bar|scatter|fill_between)\(", code))
    has_legend = "legend(" in code
    if plot_calls > 1 and not has_legend:
        warnings.append(
            f"Multiple plot calls ({plot_calls}) without legend — "
            "reader cannot distinguish data series"
        )

    # 9. Jet/rainbow colormap
    if re.search(r"cmap\s*=\s*['\"]jet['\"]", code) or re.search(
        r"cmap\s*=\s*['\"]rainbow['\"]", code
    ):
        issues.append(
            "Using 'jet' or 'rainbow' colormap — "
            "perceptually distorted, not colorblind-safe"
        )

    # 10. title set when PDF output (caption usually handled externally)
    if ".pdf" in code and "ax.set_title" in code and "standalone" not in code.lower():
        warnings.append(
            "ax.set_title() set for PDF output — "
            "if the document has its own caption system, omit the title"
        )

    # 11. Subplot colorbar without vmin/vmax
    has_colorbar = "colorbar(" in code
    has_multi_axes = "subplots(" in code and "ravel(" in code
    has_vmin = "vmin=" in code and "vmax=" in code
    if has_colorbar and has_multi_axes and not has_vmin:
        warnings.append(
            "Shared colorbar across subplots without explicit vmin/vmax — "
            "last-plotted image range determines the colorbar; may be misleading"
        )

    # 12. tight_layout + constrained_layout conflict
    if "tight_layout()" in code and "constrained_layout" in code:
        issues.append(
            "tight_layout() used with constrained_layout — "
            "calling tight_layout() permanently disables the constraint engine"
        )

    # 13. subplots_adjust with constrained_layout
    if "subplots_adjust(" in code and "constrained_layout" in code:
        issues.append(
            "subplots_adjust() used with constrained_layout — "
            "use fig.get_layout_engine().set() instead"
        )

    # 14. Missing set_axisbelow with grid — grid lines may cover data markers
    has_grid = "grid(" in code or "grid=True" in code or "axes.grid" in code
    has_axisbelow = "set_axisbelow" in code or "axes.axisbelow" in code
    if has_grid and not has_axisbelow:
        warnings.append(
            "Grid enabled without set_axisbelow(True) — "
            "grid lines default to zorder=2, same as data markers; may cover points"
        )

    # 15. twinx() with separate legends — produces overlapping legend boxes
    if "twinx()" in code or "twinx(" in code:
        leg_count = len(re.findall(r"\.legend\(", code))
        if leg_count > 1:
            warnings.append(
                "twinx() with separate legend() calls — "
                "produces overlapping legend boxes. Merge into one combined legend."
            )

    # 16. Bar + line overlay without alpha on bars
    if ("twinx()" in code or "twinx(" in code) and ".bar(" in code:
        if "alpha=" not in code:
            warnings.append(
                "Bar chart with twinx() overlay without alpha on bars — "
                "line may be invisible behind opaque bars. Add alpha=0.3-0.5."
            )

    # 17. Multi-panel without set_axisbelow
    has_multi = len(re.findall(r"subplots\(\s*\d+\s*,\s*\d+", code)) > 0
    if has_multi and not has_axisbelow:
        warnings.append(
            "Multi-panel figure without set_axisbelow(True) — "
            "grid lines will draw on top of data markers in all panels."
        )

    # Summary
    print(f"Matplotlib Check: {path}")
    print(f"  Issues: {len(issues)}")
    print(f"  Warnings: {len(warnings)}")
    print()

    for i in issues:
        print(f"  ISSUE: {i}")
    for w in warnings:
        print(f"  WARN: {w}")

    if not issues and not warnings:
        print("  PASS: No issues detected")

    print()
    return len(issues) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python matplotlib-check.py <script.py>")
        sys.exit(1)

    ok = check(sys.argv[1])
    sys.exit(0 if ok else 1)
