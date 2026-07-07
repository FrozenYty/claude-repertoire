# Visual Style Guide

Shared design system for draw.io diagrams and matplotlib charts.
Referenced by `drawio-guide.md` and `matplotlib-guide.md`.
One source of truth for colors, typefaces, resolution, and spacing.

---

## 1. Color Palettes

All palettes sourced from real journal figures via [Academic-Color](https://rookie-00001.github.io/Academic-Color/)
([GitHub](https://github.com/Rookie-00001/Academic-Color)), a curated collection of
color schemes extracted from Nature, Science, Cell, NEJM, Lancet, and 15+ other journals.
The hex codes are the exact colors used in published figures.

---

### 1.1 IEEE Semantic Palette (default for technical diagrams)

Each component type has a fixed color mapping. Use for draw.io architecture
diagrams and matplotlib charts where method/component identity matters.

| Component | Fill | Stroke | When to use |
|-----------|------|--------|-------------|
| Attention / Key method | `#E1D5E7` | `#9673A6` | Transformer attention, your proposed method |
| Convolution / Primary | `#DAE8FC` | `#6C8EBF` | CNN layers, main processing blocks |
| Deconv / Upsample | `#DCEEF8` | `#56A5C9` | Transposed conv, pixel shuffle |
| RNN / Sequence | `#D4EDDA` | `#28A745` | LSTM, GRU, recurrent layers |
| Pooling | `#D5E8D4` | `#82B366` | Max/Avg pool, global pool |
| Normalization | `#F5F5F5` | `#999999` | LayerNorm, BatchNorm, Add & Norm |
| FC / MLP / Linear | `#FFE6CC` | `#D79B00` | Dense layers, projection heads |
| Input / Embedding | `#F8CECC` | `#B85450` | Token embeddings, data sources |
| Output / Loss | `#FFF2CC` | `#D6B656` | Softmax, classifier, final output |
| Operators / Math | `#FFFFFF` | `#666666` | Element-wise ops, concat, reshape |

```python
ieee_pal = {
    "attention":     "#9673A6",
    "convolution":   "#6C8EBF",
    "rnn":           "#28A745",
    "pooling":       "#82B366",
    "norm":          "#999999",
    "fc":            "#D79B00",
    "input":         "#B85450",
    "output":        "#D6B656",
}
```

---

### 1.1b System Architecture Palette (general system/infra/tool diagrams)

For non-ML diagrams — CLI tools, cloud infrastructure, platform architecture,
microservice topologies. Use when IEEE semantic palette (Attention/Convolution/
Pooling) doesn't match the domain.

| Component | Fill | Stroke | Use for |
|-----------|------|--------|---------|
| Core Engine / Orchestrator | `#DAE8FC` | `#6C8EBF` | Main engine, coordinator, central service |
| Instruction / Config Layer | `#E1D5E7` | `#9673A6` | CLAUDE.md, config files, rule systems |
| Tool / Processing Layer | `#D5E8D4` | `#82B366` | Tool systems, processing pipelines, workers |
| I/O Boundary | `#F8CECC` | `#B85450` | User terminal, file system, database, network I/O |
| External API / Service | `#FFF2CC` | `#D6B656` | Third-party APIs, remote backends, SaaS |
| Extension / Plugin System | `#FFE6CC` | `#D79B00` | Plugins, skills, MCP servers, add-ons |
| Section Container | `#F5F5F5` | `#BDBDBD` | Dashed box around related components |

```python
sys_arch_pal = {
    "core":         "#6C8EBF",
    "instruction":  "#9673A6",
    "tool":         "#82B366",
    "io":           "#B85450",
    "external":     "#D6B656",
    "extension":    "#D79B00",
    "container":    "#BDBDBD",
}
```

**Selection rule:** If the diagram is about an ML model architecture (Transformer,
CNN, RNN, etc.), use IEEE Semantic (§1.1). If it's about a software system,
CLI tool, cloud infra, or platform, use System Architecture (§1.1b).

---

### 1.1c Industry Architecture Palette (AWS / Azure / GCP standard)

Authoritative layer-based color coding used across major cloud providers and
enterprise architecture teams. Source: [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/),
[Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/),
[C4 Model notation](https://c4model.com/).

Each architectural layer maps to a fixed semantic color — the same convention
used by AWS, Azure, and GCP in their official architecture diagrams.

| Layer | Fill | Stroke | Use for |
|-------|------|--------|---------|
| Compute / Services | `#ED7100` | `#D05C17` | EC2, Lambda, containers, microservices, app servers |
| Storage / Database | `#7AA116` | `#5A8A0E` | S3, RDS, volumes, object stores, data lakes |
| Networking / CDN | `#8C4FFF` | `#6A30C0` | VPC, subnets, load balancers, API gateways, CDN |
| Security / IAM | `#C7131F` | `#A0101A` | IAM, firewall, encryption, WAF, secrets |
| Analytics / ML | `#116D5B` | `#0D5546` | Data pipelines, ML training, ETL, notebooks |
| Integration / Messaging | `#BC1356` | `#960F44` | Queues, event buses, pub/sub, webhooks |
| External / Users | `#232F3E` | `#1A2430` | Users, on-prem systems, third-party APIs |
| Management / DevOps | `#D05C17` | `#A84A13` | Monitoring, CI/CD, logging, dashboards |

```python
industry_pal = {
    "compute":      "#ED7100",
    "storage":      "#7AA116",
    "networking":   "#8C4FFF",
    "security":     "#C7131F",
    "analytics":    "#116D5B",
    "integration":  "#BC1356",
    "external":     "#232F3E",
    "management":   "#D05C17",
}
```

**Selection rule:** Use Industry Architecture for cloud infrastructure diagrams
(AWS/Azure/GCP), enterprise system topologies, and network architecture. The
layer-based color coding is immediately recognizable to cloud engineers and
architects. For non-cloud software systems, use System Architecture (§1.1b).
For ML model architectures, use IEEE Semantic (§1.1).

### Palette Selection Summary

| Diagram Type | Palette | § |
|-------------|---------|---|
| ML model (Transformer, CNN, RNN) | IEEE Semantic | 1.1 |
| Software system, CLI tool, platform | System Architecture | 1.1b |
| Cloud infra, AWS/Azure/GCP, enterprise | Industry Architecture | 1.1c |
| Publication chart | Nature / Science / Cell | 1.2–1.5 |

---

Highest quality, most-tested palettes. Use for publications and
professional charts where color credibility matters.

**Nature (2025) -- 6 colors**
`#433764` `#e48566` `#a05179` `#c66571` `#c6c687` `#668441`
Neutral-leaning, excellent for 5-6 categories. The gold standard.
```python
nature_pal = ["#433764", "#E48566", "#A05179", "#C66571", "#C6C687", "#668441"]
```

**Science (2025) -- 6 colors**
`#928b92` `#e3c7d5` `#fcf0e4` `#6b879d` `#72aabb` `#e48078`
Soft, pastel-like. Good for visualization-heavy figures.
```python
science_pal = ["#928B92", "#E3C7D5", "#FCF0E4", "#6B879D", "#72AABB", "#E48078"]
```

**Cell (2025) -- 8 colors**
`#fa756e` `#d68e04` `#93a906` `#13bb38` `#05c1a2` `#0eb9e4` `#639dfc` `#db70fe`
High-saturation, ideal for >=6 categories. Best color discrimination.
```python
cell_pal = ["#FA756E", "#D68E04", "#93A906", "#13BB38", "#05C1A2",
            "#0EB9E4", "#639DFC", "#DB70FE"]
```

**Nature Physics (2025) -- 6 colors**
`#ff3533` `#fec71a` `#2ad92d` `#35e7df` `#2c97ff` `#2f2ffd`
Primary-color emphasis, good for 4-6 categories of physical data.
```python
np_pal = ["#FF3533", "#FEC71A", "#2AD92D", "#35E7DF", "#2C97FF", "#2F2FFD"]
```

**Nature Methods (2025) -- 8 colors**
`#1bb5b9` `#eea78b` `#d5c1d6` `#9566a8` `#a4d2a1` `#e98d49` `#ebcc75` `#489faa`
Warm + cool balanced. Good for multi-class method comparison.
```python
nmeth_pal = ["#1BB5B9", "#EEA78B", "#D5C1D6", "#9566A8",
             "#A4D2A1", "#E98D49", "#EBCC75", "#489FAA"]
```

**Nature Machine Intelligence (2025) -- 10 colors**
`#3173a4` `#b6c7e0` `#e0822a` `#eebb8c` `#3a9339` `#9ed594` `#bf3d3e` `#f3a5a4` `#9571b1` `#c5b5cf`
Paired light/dark per hue. Best for comparing 5 methods each with a variant.
```python
nmi_pal = ["#3173A4", "#B6C7E0", "#E0822A", "#EEBB8C", "#3A9339",
           "#9ED594", "#BF3D3E", "#F3A5A4", "#9571B1", "#C5B5CF"]
```

**Nature Communications (2025) -- 7 colors**
`#d5e5c9` `#d4dee9` `#d9c2df` `#e2795a` `#eac56c` `#299d90` `#895c56`
Earthy + muted. Good for ecological/environmental data.
```python
ncomms_pal = ["#D5E5C9", "#D4DEE9", "#D9C2DF", "#E2795A",
              "#EAC56C", "#299D90", "#895C56"]
```

---

### 1.3 Journal Palettes -- Medical & Life Sciences

**NEJM (2024) -- 7 colors**
`#f6fafb` `#e5eef3` `#bed2db` `#afc7d3` `#6f9aad` `#326a81` `#1e4757`
Blue-gradient monochromatic. Ideal for severity scales and ordinal data.
```python
nejm_pal = ["#F6FAFB", "#E5EEF3", "#BED2DB", "#AFC7D3",
            "#6F9AAD", "#326A81", "#1E4757"]
```

**The Lancet (2025) -- 3 colors**
`#1b85ff` `#90353b` `#006000`
Bold, high-contrast. Good for binary + reference comparisons.
```python
lancet_pal = ["#1B85FF", "#90353B", "#006000"]
```

**JAMA (2023) -- 3 colors**
`#31496e` `#90a9b7` `#d3a05e`
Subdued, authoritative. Good for conservative medical presentations.
```python
jama_pal = ["#31496E", "#90A9B7", "#D3A05E"]
```

**Nature Medicine (2022) -- 7 colors**
`#90bbdc` `#ffbf88` `#96d096` `#e99593` `#c8b3de` `#c7a9a7` `#f3bce3`
Pastel-balanced. Good for patient group comparisons.
```python
nmed_pal = ["#90BBDC", "#FFBF88", "#96D096", "#E99593",
            "#C8B3DE", "#C7A9A7", "#F3BCE3"]
```

**Stroke (2025) -- 5 colors**
`#6094ce` `#de407a` `#4dbe93` `#fddc32` `#4c2e90`
Distinct, separable. Good for risk-group stratification.
```python
stroke_pal = ["#6094CE", "#DE407A", "#4DBE93", "#FDDC32", "#4C2E90"]
```

**Radiology (2023) -- 4 colors**
`#0b2570` `#459741` `#d0c988` `#d6022c`
High contrast with dark anchor. Good for imaging result categories.
```python
radiology_pal = ["#0B2570", "#459741", "#D0C988", "#D6022C"]
```

---

### 1.4 Journal Palettes -- Physical Sciences & Engineering

**Physical Review Letters (2016) -- 6 colors**
`#ea272a` `#435aa5` `#6cb48d` `#a47748` `#f7a25c` `#848484`
Bold primaries + earth tones. Good for detector/signal data.
```python
prl_pal = ["#EA272A", "#435AA5", "#6CB48D", "#A47748", "#F7A25C", "#848484"]
```

**Physical Review X (2017) -- 4 colors**
`#4b4b4b` `#25733d` `#316293` `#a8535e`
Dark + rich accents. Good for quantum/solid-state diagrams.
```python
prx_pal = ["#4B4B4B", "#25733D", "#316293", "#A8535E"]
```

**Chemical Reviews (2025) -- 5 colors**
`#560b0d` `#cc221b` `#dffc30` `#64c61e` `#284d31`
Dark red to green progression. Good for reaction/process stages.
```python
chemrev_pal = ["#560B0D", "#CC221B", "#DFFC30", "#64C61E", "#284D31"]
```

**Advanced Materials (2024) -- 3 colors**
`#c6c8c9` `#7da2c6` `#ce8487`
Neutral grey + blue/rose pair. Good for materials comparison.
```python
advmat_pal = ["#C6C8C9", "#7DA2C6", "#CE8487"]
```

---

### 1.5 Journal Palettes -- Interdisciplinary

**Nature Climate Change (2025) -- 3 colors**
`#88bb9a` `#c591a9` `#818181`
Green/rose/grey. Good for environmental impact categories.
```python
climate_pal = ["#88BB9A", "#C591A9", "#818181"]
```

**Nucleic Acids Research (2025) -- 5 colors**
`#9a4e96` `#38a6a5` `#1c6995` `#7eb9da` `#80ceb9`
Purple to teal progression. Good for genomic/sequence data.
```python
nar_pal = ["#9A4E96", "#38A6A5", "#1C6995", "#7EB9DA", "#80CEB9"]
```

---

### 1.6 Curated Recommended Palettes

From Academic-Color's curated recommendation set. These are synthetic
(not extracted from a specific figure) and designed for general use.

**Nature Inspired -- 5 colors**
`#2d5a27` `#5cb3a8` `#9bc53d` `#f5de01` `#ff8c00`
Earthy greens to warm orange. Good for ecological/biological data.
```python
nature_inspired = ["#2D5A27", "#5CB3A8", "#9BC53D", "#F5DE01", "#FF8C00"]
```

**Ocean Depths -- 5 colors**
`#003f5c` `#2f4b7c` `#665191` `#a05195` `#d45087`
Deep blue to vibrant pink. Good for depth/severity scales.
```python
ocean_depths = ["#003F5C", "#2F4B7C", "#665191", "#A05195", "#D45087"]
```

**Sunset Vibes -- 5 colors**
`#ff6b6b` `#feca57` `#48dbfb` `#ff9ff3` `#54a0ff`
Warm + cool balanced. Good for presentation slides and dashboards.
```python
sunset_vibes = ["#FF6B6B", "#FECA57", "#48DBFB", "#FF9FF3", "#54A0FF"]
```

**Medical Journal -- 5 colors**
`#e74c3c` `#3498db` `#2ecc71` `#f39c12` `#9b59b6`
Classic medical publication palette. Good for treatment-group comparisons.
```python
medical_journal = ["#E74C3C", "#3498DB", "#2ECC71", "#F39C12", "#9B59B6"]
```

**Minimal Dark -- 5 colors**
`#2c3e50` `#34495e` `#7f8c8d` `#95a5a6` `#bdc3c7`
Grey-scale professional. Good for single-hue multi-class charts.
```python
minimal_dark = ["#2C3E50", "#34495E", "#7F8C8D", "#95A5A6", "#BDC3C7"]
```

**Pastel Rainbow -- 8 colors**
`#ffadad` `#ffd6a5` `#fdffb6` `#caffbf` `#9bf6ff` `#a0c4ff` `#bdb2ff` `#ffc6ff`
Soft rainbow for many-category data where harsh colors would distract.
```python
pastel_rainbow = ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF",
                  "#9BF6FF", "#A0C4FF", "#BDB2FF", "#FFC6FF"]
```

---

### 1.7 Palette Selection Rules

| Scenario | Palette | Notes |
|----------|---------|-------|
| Technical diagram (draw.io) | IEEE Semantic | Each component type = fixed color |
| Publication chart, <=6 categories | Nature / Science | Gold standard, most tested |
| Publication chart, >=7 categories | Cell / Nature Methods | Best discrimination |
| Medical / clinical data | NEJM / Lancet / JAMA / Stroke | Journal-context appropriate |
| Physics / engineering data | Nature Physics / PRL / PRX | Field-appropriate |
| Genomics / bioinformatics | NAR / Nature Methods | Field-appropriate |
| Environmental / climate | Nature Climate Change / Nature Comms | Field-appropriate |
| Chemistry / materials | Chemical Reviews / Advanced Materials | Field-appropriate |
| Heatmap / diverging data | `RdBu_r` or `coolwarm` | Built-in, colorblind-safe |
| Corporate slides / dashboard | Sunset Vibes / Medical Journal | High visibility |
| Many categories (>=8), soft look | Pastel Rainbow | Avoids harsh contrast |
| Single-hue multi-class | Minimal Dark | Conservative, professional |

**Forbidden:** matplotlib defaults, `jet`, `rainbow`. Use the built-in
colorblind-safe colormaps from §8 instead.

**Custom DPI & Size:** The user may request specific DPI or figure
dimensions. Honor these overrides -- this skill is a general-purpose toolkit.
- DPI: default >=600, but accept 150/300/600/800/1000/1200 per user request
- Figure size: default 5.5x4.1" (4:3), but accept custom `(w, h)` in inches
- draw.io canvas: default per-template, but accept custom `pageWidth` x `pageHeight`
---

## 2. Typeface System

### 2.1 Print / Default (serif)

```
Family: Times New Roman (serif)
Math: STIX (matches Times)
Fallback: DejaVu Serif
```

| Element | Size (pt) |
|---------|-----------|
| Figure title | 13 |
| Axis title | 12 |
| Axis label | 11 |
| Tick labels | 10 |
| Legend | 10 |
| Annotation | 9 |

### 2.2 Screen / Slides (sans-serif)

```
Family: Arial / Helvetica
```

| Element | Size (pt) |
|---------|-----------|
| Title | 14 |
| Label | 12 |
| Tick | 10 |

### 2.3 draw.io Typeface

```
fontFamily=Times New Roman (default)
Code: Courier New
```

Module titles: 12-14px bold. Subsidiary labels: 11-12px. Details: 9-10px.
Multi-line text in `value`: use `&#xa;`. Quotes in `value`: use `&quot;`.

---

## 3. Resolution & Output

### 3.1 PNG

| DPI | When |
|-----|------|
| 600 | Standard: bar, line, ROC, box/violin, donut, radar |
| 800 | Detailed: scatter (many points), heatmap, faceted grid, combo charts |
| 1000 | Maximum: camera-ready final, poster printing, highest quality |

Default: >=600 dpi.

### 3.2 Vector (PDF / SVG)

Recommended rcParams:
```python
"pdf.fonttype": 42,   # embed fonts as TrueType (not Type-3)
"ps.fonttype": 42,
```

Reason: Type-3 fonts render as outlines, breaking copy-paste and failing
compliance checkers. This setting ensures cross-platform font rendering.

### 3.3 Output Format Convention

| Engine | Primary output | Secondary |
|--------|---------------|-----------|
| draw.io | `.drawio` | — |
| matplotlib | `.png` (>=600 dpi) | `.pdf` (vector, embed fonts) |

Always use `bbox_inches='tight'` for matplotlib saves.

---

## 4. Line Weights

### 4.1 draw.io

| Element | strokeWidth |
|---------|-------------|
| Main container / emphasis | 2.5 |
| Module box | 1.5–2.0 |
| Subtle border | 1.0 |
| Normal arrow | 1.5 |
| Key relationship arrow | 3.0–5.0 |

### 4.2 matplotlib

| Element | linewidth |
|---------|-----------|
| Axes | 0.8 |
| Plot lines | 1.5 |
| Grid | 0.5 |

---

## 5. Spacing

### 5.1 draw.io

| Rule | Value |
|------|-------|
| Vertical gap between stacked modules | 24-30px |
| Section gap (between containers) | >=30px |
| Container padding | >=10px on all sides |
| External margin | >=40px |
| Label inside container | x=c.x+10, y=c.y+6 |

### 5.2 matplotlib

| Rule | Value |
|------|-------|
| Default aspect ratio | 4:3 (narrow) |
| Time-series aspect | 5:3 (wider) |
| Scatter/heatmap | 1:1 (square) |
| Layout engine | `constrained_layout.use = True` |

### 5.3 Canvas Sizing (matplotlib)

| Format | Width (in) | Use |
|--------|-----------|-----|
| Narrow (4:3) | 5.5 | Default, single-column equivalent |
| Wide (16:9) | 8.0 | Presentation slides, landscape |
| Square (1:1) | 5.0 | Scatterplots, heatmaps, confusion matrices |

---

## 6. Visual Hierarchy

Larger + bolder + darker = more important.

```
Title > Section label > Module name > Detail > Annotation
```

- Use color to encode semantic role, not decoration
- Max 5-6 distinct colors per figure
- Legend required when colors or line styles encode meaning
- Vary linestyle (`-`, `--`, `:`, `-.`) or marker (`o`, `s`, `^`, `D`) in
  addition to color for accessibility

---

## 7. Seaborn Integration

Seaborn (`import seaborn as sns`) provides a high-level styling layer over
matplotlib. It is recommended for rapid professional styling.

### 7.1 Quick Setup

```python
import seaborn as sns

# One-line professional theme
sns.set_theme(style="ticks", context="notebook", palette="deep")
```

### 7.2 Five Built-in Styles

| Style | Background | Grid | Best for |
|-------|-----------|------|----------|
| `darkgrid` | Grey | White grid | Quick data exploration |
| `whitegrid` | White | Grey grid | Data-heavy figures (box, violin) |
| `dark` | Grey | None | Presentation slides |
| `white` | White | None | Embedded in documents |
| `ticks` | White | Tick marks only | Publication / print (gold standard) |

```python
# "ticks" + despine = current publication gold standard
sns.set_style("ticks")
sns.despine()  # removes top + right spines
```

### 7.3 Four Context Presets (Scales Everything)

| Context | Use |
|---------|-----|
| `paper` | Smallest — academic papers, journal columns |
| `notebook` | Default — Jupyter, general use |
| `talk` | Larger — presentation slides |
| `poster` | Largest — conference posters |

```python
sns.set_context("paper", font_scale=1.1)
```

Best practice: use context to scale uniformly rather than manually adjusting
individual font sizes. Inside a single project, keep one context.

### 7.4 Scoped Temporary Styles

```python
# Apply style ONLY inside this block — doesn't leak globally
with sns.axes_style("ticks"), sns.plotting_context("talk"):
    fig, ax = plt.subplots()
    ax.bar(...)
    sns.despine()
```

### 7.5 Despine Options

```python
sns.despine()                    # remove top + right
sns.despine(left=True)           # remove left too
sns.despine(offset=10, trim=True) # offset + trim tick range
```

### 7.6 Custom rc Overrides via seaborn

```python
sns.set_theme(
    style="whitegrid",
    rc={
        "axes.spines.right": False,
        "axes.spines.top": False,
        "lines.linewidth": 2.5,
    }
)
```

---

## 8. Colorblind-Safe Colormaps

For heatmaps, diverging data, and continuous color scales. All listed
colormaps are perceptually uniform and pass CB accessibility tests.

### 8.1 Sequential (ordered data, low→high)

| Colormap | Use |
|----------|-----|
| `viridis` | Default choice — perceptually uniform, CB-safe, works in B&W |
| `cividis` | Optimized for red-green CB (deuteranopia/protanopia) |
| `magma` | Dark background figures, good dynamic range |
| `plasma` | Vibrant, good for attention-grabbing |
| `inferno` | High contrast, good for small multiples |

```python
# Sequential
ax.imshow(data, cmap="viridis")
ax.scatter(x, y, c=values, cmap="cividis")
```

### 8.2 Diverging (data with a meaningful midpoint)

| Colormap | Use |
|----------|-----|
| `RdBu_r` | Standard diverging, red-white-blue |
| `coolwarm` | Softer diverging, blue-grey-red |
| `PRGn` | Purple-green, good for statistical significance |
| `BrBG` | Brown-blue-green, earth tones |

```python
ax.imshow(corr_matrix, cmap="RdBu_r", vmin=-1, vmax=1)
```

### 8.3 Cyclic (wrap-around data, e.g., angles, phases)

| Colormap | Use |
|----------|-----|
| `twilight` | Phase/angle data, 24-hour cycles |
| `hsv` | Cyclic hue — use sparingly, not CB-safe |

### 8.4 Turbo (high dynamic range)

`turbo` is a rainbow-like colormap with improved perceptual uniformity over
`jet`. Use when the data genuinely spans many orders of magnitude and needs
maximum discrimination. Still visible to most CB viewers.

```python
ax.imshow(elevation, cmap="turbo")
```

**Forbidden regardless of use case:** `jet`, `rainbow` — these distort data
perception and fail CB tests.

---

## 9. Material Design Color Palette

Google Material Design 2.0 palette. Good for UI mockups, web-facing charts,
and presentation slides. Less formal than IEEE/Nature, more vibrant.

```python
# Material Design — 10 hues, each with 5 shades
material_pal = {
    "red":    ["#FFEBEE", "#FFCDD2", "#EF9A9A", "#E57373", "#F44336"],
    "pink":   ["#FCE4EC", "#F8BBD0", "#F48FB1", "#EC407A", "#E91E63"],
    "purple": ["#F3E5F5", "#E1BEE7", "#CE93D8", "#AB47BC", "#9C27B0"],
    "blue":   ["#E3F2FD", "#BBDEFB", "#90CAF9", "#42A5F5", "#2196F3"],
    "teal":   ["#E0F2F1", "#B2DFDB", "#80CBC4", "#26A69A", "#009688"],
    "green":  ["#E8F5E9", "#C8E6C9", "#A5D6A7", "#66BB6A", "#4CAF50"],
    "amber":  ["#FFF8E1", "#FFECB3", "#FFE082", "#FFCA28", "#FFC107"],
    "orange": ["#FFF3E0", "#FFE0B2", "#FFCC80", "#FFA726", "#FF9800"],
    "grey":   ["#FAFAFA", "#F5F5F5", "#EEEEEE", "#E0E0E0", "#9E9E9E"],
    "indigo": ["#E8EAF6", "#C5CAE9", "#9FA8DA", "#5C6BC0", "#3F51B5"],
}
```

### Selection Rule

| Scenario | Palette |
|----------|---------|
| Technical diagram (draw.io) | IEEE semantic |
| Publication chart | Nature / Science / Cell |
| Corporate slides / UI | Material Design |
| Heatmap / continuous | viridis / cividis / RdBu_r |


---

## 10. draw.io Official Lane Palette

Pastel lane colors from draw.io official swimlane documentation.
Use for cross-functional flowcharts, BPMN, and process flows.

| Role | Fill | Stroke |
|------|------|--------|
| Customer / Client | `#FCE4EC` | `#B85450` |
| Internal system / IT | `#E3F2FD` | `#6C8EBF` |
| Finance / Payment | `#F3E5F5` | `#9673A6` |
| Operations / Warehouse | `#E8F5E9` | `#82B366` |
| External partner | `#FFF3E0` | `#D79B00` |
| Generic / Other | `#F5F5F5` | `#999999` |

Node shapes inside a lane use the lane stroke color as their border,
with white fill for process steps and decision-diamond yellow for branches.

---

## 11. CJK (Chinese) Typography for matplotlib

When the chart contains Chinese text, apply this font configuration.
For English-only charts, the default Times New Roman serif is used.

### 11.1 Chinese Academic Standard (GB/T 7713 convention)

| Element | Font | English name | Size |
|---------|------|-------------|------|
| Chart title | 黑体 | `SimHei` | 12pt |
| Axis labels / legend | 宋体 | `SimSun` | 9-10pt |
| Tick labels | 宋体 | `SimSun` | 8-9pt |
| Annotations / footnotes | 楷体 | `KaiTi` | 8pt |
| Numbers / English in labels | Times New Roman | `serif` | match parent |

### 11.2 Cross-Platform Font Fallback Chain

```python
mpl.rcParams.update({
    "font.sans-serif": [
        "Noto Sans CJK SC",    # Linux (open-source, preferred)
        "SimHei",              # Windows 黑体
        "PingFang SC",         # macOS 苹方
        "Microsoft YaHei",     # Windows 微软雅黑
        "Source Han Sans SC",  # 思源黑体 (open-source)
    ],
    "axes.unicode_minus": False,  # Prevent minus-sign glyph bug
})
```

### 11.3 Per-element Font Selection

For mixed CJK/English charts, use different fonts for different elements:

```python
# Title in bold 黑体, body labels in 宋体, annotations in 楷体
ax.set_title("中文图表标题", fontfamily="SimHei", fontsize=12, fontweight="bold")
ax.set_xlabel("时间", fontfamily="SimSun", fontsize=10)
ax.set_ylabel("数值", fontfamily="SimSun", fontsize=10)
ax.annotate("p < 0.01", xy=(...), fontfamily="KaiTi", fontsize=8)
```

### 11.4 Font Availability Check

Before using a CJK font, verify it is installed:

```python
from matplotlib.font_manager import FontManager
fm = FontManager()
available = {f.name for f in fm.ttflist}
required = ["SimHei", "SimSun", "KaiTi"]
missing = [f for f in required if f not in available]
if missing:
    print(f"Missing CJK fonts: {missing}. Install or use Noto Sans CJK SC.")
```

### 11.5 When to Apply

- Chart has any Chinese axis labels, title, or annotation → apply CJK chain.
- Chart is purely English/numeric → keep Times New Roman default.
- User requests a specific Chinese font → honor the request.
- Journal submission → check journal guidelines; most Chinese journals use
  SimHei (title) + SimSun (body) as the standard.