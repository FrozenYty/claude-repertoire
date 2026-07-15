# Academic Writing Templates

Canonical section structures for CS/ML papers. Read this file when the user
asks you to draft or restructure a paper section. Each template gives a
structure skeleton and a concrete example. Adapt the skeleton to the user's
content; keep the paragraph-level logic intact.

Templates are organized by section. When the user's request matches a named
section ("introduction", "related work", etc.), use the matching template.
If unmatched, fall back to the general principles in §7.

## §1 Introduction (CARS Model)

The three-move CARS model (Swales 1990, adapted for CS):

**Move 1 — Establish territory (1 paragraph, ~3-4 sentences)**
- Sentence 1: State the broad domain and its importance.
- Sentence 2-3: Narrow to the sub-problem. Define key terms.
- Sentence 4: Bridge to Move 2 — signal that a gap exists.

**Move 2 — Establish niche (1 paragraph, ~3-5 sentences)**
- Sentence 1: State the gap explicitly. What prior work cannot do.
- Sentence 2-3: Evidence for the gap (quantitative if possible).
- Sentence 4-5: Why the gap matters. What is blocked by it.

**Move 3 — Occupy the niche (1-2 paragraphs, ~5-8 sentences)**
- Sentence 1: "In this paper, we propose [named method]."
- Sentence 2-4: The key technical idea (1-3 sentences, accessible).
- Sentence 5-6: Experimental setup and headline result.
- Sentence 7-8: Contributions (3-4 items, each one sentence).

**Example (NLP/ML paper):**

> Large language models have achieved remarkable performance across diverse
> NLP benchmarks. However, their inference cost scales with model size,
> making deployment in resource-constrained environments impractical.
> Existing compression methods (quantization, pruning, distillation)
> reduce model size but often degrade performance on long-tail or
> specialized tasks — the very tasks where small models are most needed.
>
> We identify a key limitation: prior compression techniques treat all
> tokens uniformly, discarding information that is critical for rare
> linguistic patterns. On the Bamboo rare-language benchmark, compressed
> Llama-7B models lose 12.3% accuracy on low-frequency tokens versus
> 1.7% on high-frequency ones, confirming that uniform compression is
> the bottleneck.
>
> We propose Token-Adaptive Compression (TAC), a method that dynamically
> allocates representation capacity based on token importance. TAC learns
> a lightweight importance predictor that runs in parallel with the main
> forward pass, adjusting the compression ratio per token at inference
> time with negligible overhead. On Llama-7B and Llama-13B, TAC
> preserves 98.2% of the original accuracy on rare tokens while reducing
> overall inference cost by 1.8×. Our contributions are: (1) the
> token-adaptive compression framework; (2) an importance predictor that
> adds less than 2% latency overhead; and (3) empirical demonstration
> that adaptive strategies close the rare-token gap left by uniform
> methods.

---

## §2 Related Work (Taxonomy Structure)

**Structure: 3-4 thematic groups, not chronological.**

Group the literature by *problem approach*, not by paper. Each group is
one paragraph:

1. **Opening sentence**: Name the approach and its representative works.
   "Prior work on X has primarily followed [approach A]."
2. **Body (2-3 sentences)**: What this approach achieves and where it
   falls short. Cite 2-4 key papers per group.
3. **Closing sentence**: Transition. "While [approach A] addresses Y,
   it does not handle Z."

**The final group is always your position**: "Our work differs from the
above in that..." or "We build on [approach B] and extend it with..."

**Anti-patterns to avoid:**
- Paper-by-paper listing ("Smith et al. proposed X. Jones et al.
  proposed Y. Lee et al. proposed Z.")
- Starting with "There has been a lot of work on..."
- Omitting the "why prior work is insufficient" for each group

**Example (first group):**

> Prior work on efficient LLM inference has largely followed three
> directions. Quantization methods [Dettmers et al. 2022, Frantar et
> al. 2023, Xiao et al. 2023] reduce numerical precision to 4-bit or
> below, achieving 2-4× compression with minimal accuracy loss on
> standard benchmarks. However, these methods apply a static precision
> budget to all tokens, ignoring the fact that some tokens (rare words,
> named entities) require higher precision for accurate prediction.
> Pruning approaches [Sun et al. 2023, Ma et al. 2023] remove entire
> attention heads or FFN neurons but risk degrading performance on
> specialized domains. Our work complements both directions: we keep
> static compression as a base and add token-level adaptation on top.

---

## §3 Methodology (Algorithm Description)

**Structure: Top-down. Architecture → Components → Details.**

**Paragraph 1 — Overview (3-4 sentences)**
- Sentence 1: "We propose [Method Name], a [high-level description]."
- Sentence 2-3: The core idea in one sentence, then the main components.
- Sentence 4: "Figure 1 illustrates the overall architecture."

**Paragraph 2 — Component 1 (3-5 sentences)**
- What it does, what its inputs/outputs are, the key design choice.
- When relevant: a simplified equation or pseudocode.

**Paragraph 3 — Component 2 (same structure)**

**Paragraph 4 — Training / optimization details (3-4 sentences)**
- Loss function, optimizer, key hyperparameters.
- "We train on [dataset] using [optimizer] with learning rate [lr] for
  [N] epochs on [hardware]."

**Conventions:**
- Name the method once (Paragraph 1, Sentence 1). Use the name thereafter.
- Define every symbol before it appears in an equation.
- Write "We" not "The model" or passive voice.
- Equations are prose-connected: "The loss is L = A + B, where A is..."

---

## §4 Experiments (Three-Part Structure)

### §4.1 Setup (1 paragraph, no results)

- Datasets: name, size, metrics. "We evaluate on [D1] (N samples,
  metric M1), [D2] (N2 samples, metric M2)."
- Baselines: name each one, state why it's included. "We compare against
  [B1] as the SOTA in [task], [B2] as a representative of [approach]."
- Implementation: framework, hardware, hyperparameters, seeds. "All
  experiments use 5 random seeds; we report mean ± 1 SD."

### §4.2 Main Results (2-4 paragraphs)

**Paragraph 1 — Headline table.** "Table 1 shows..." followed by the
key takeaway in prose, not a re-listing of numbers. "Our method
outperforms the strongest baseline by 3.4 points on MMLU (p < 0.01,
paired t-test)."

**Paragraph 2-3 — Drill-down.** One finding per paragraph. Connect
results to claims. "The gains are largest on [subset], consistent with
our hypothesis that [mechanism] is the key driver."

### §4.3 Ablation / Analysis (2-3 paragraphs)

- Remove one component at a time. Show it matters.
- Sensitivity analysis (hyperparameters, seeds).
- Qualitative examples if applicable (1-2 representative cases).

**Conventions:**
- Every table/figure reference must have a prose takeaway.
- Never write "Table 2 shows the results." Write "Table 2 shows that
  removing [component] reduces accuracy by X%, confirming its role."
- Report statistical significance for all headline claims.
- State the hardware and runtime for reproducibility.

---

## §5 Conclusion (Three-Part)

**Paragraph 1 — Summary (2-3 sentences)**
- Restate the problem, method name, and headline result.
- No new information. No citations.

**Paragraph 2 — Limitations (2-4 sentences)**
- Be honest. Scope limitations, methodological caveats, dataset bias.
- "Our method requires labeled data for the importance predictor,
  limiting applicability to fully unsupervised settings."

**Paragraph 3 — Future work (1-2 sentences)**
- One or two concrete directions. Not "more research is needed."
- "We plan to extend TAC to vision-language models and investigate
  online importance prediction for streaming inputs."

**Anti-patterns:**
- "Future work will explore..." (vague) → "We plan to extend X to Y."
- Ending with a grand societal claim unrelated to the method.
- Introducing new results or claims not supported by the paper.

---

## §6 Abstract (Five-Part)

See `prompts/polish-abstract.md` for the full template. The five parts
in order: (1) Background — 1-2 sentences. (2) Gap — 1-2 sentences.
(3) Method — 2-4 sentences, name the method. (4) Results — 2-3
sentences, concrete numbers. (5) Impact — 1 sentence.

---

## §7 General Principles

When no template matches the user's request, follow these:

1. **Structure before prose.** Name the 2-4 logical blocks before
   writing any sentence. If you can't name them, the section is
   under-organized.
2. **One claim per paragraph.** A paragraph that makes two unrelated
   points should be two paragraphs.
3. **Numbers over adjectives.** "3.4 points improvement" beats
   "significant improvement."
4. **Breadcrumb the reader.** The first sentence of each paragraph
   should connect to the previous paragraph's conclusion.
5. **Active voice, present tense.** "We propose X." "Table 1 shows Y."
   Past tense only for completed experimental actions.
6. **Citations are evidence, not decoration.** Every citation should
   support a claim the sentence makes. If a sentence with three
   citations could mean any of them, it's under-specified.

---

## §8 Literature Review (Standalone)

A standalone literature review paper synthesizes and critiques existing
research on a defined topic. Unlike the Related Work section of a
research paper (§2), this is a full paper in its own right.

**Structure: 5 parts, typically 4,000-10,000 words.**

### §8.1 Introduction (1-2 paragraphs)
- Sentence 1: Define the topic and its significance.
- Sentence 2-3: State the scope — what is included and excluded, and why.
- Sentence 4: Outline the review's organization (by theme, chronology, or
  methodology).

### §8.2 Search Strategy (1 paragraph, optional for non-systematic reviews)
- Databases searched, keywords used, inclusion/exclusion criteria.
- Date range and justification.
- "We searched [DB1], [DB2] for [keywords], yielding N papers after
  deduplication and screening."

### §8.3 Thematic Synthesis (4-8 sections, the core body)
Organize literature into thematic clusters. Each section:
- **Opening**: Name the theme and its representative works (2-4 citations).
- **Body (3-5 sentences)**: What the consensus is, where disagreement
  exists, what methods dominate.
- **Critical gap statement**: "While [theme] research has established X,
  three open questions remain: [Q1], [Q2], [Q3]."

**Anti-patterns:**
- Paper-by-paper listing ("Smith found X. Jones found Y. Lee found Z.")
- Summary without critique — state what's missing, not just what's there.
- Chronological ordering without thematic grouping.

### §8.4 Critical Discussion (1-2 paragraphs)
- Cross-cutting patterns across themes.
- Methodological limitations shared by multiple studies.
- Contradictions in the literature and their likely causes.

### §8.5 Future Directions & Conclusion (1-2 paragraphs)
- 3-5 concrete research opportunities the review reveals.
- One-sentence summary of the state of the field.
- No new literature introduced here.

**Example (thematic section opening):**

> Research on token-adaptive compression has followed two broad strategies.
> Post-hoc importance estimation [Dettmers 2022, Xiao 2023] computes token
> saliency after the forward pass and applies compression retroactively,
> achieving 2-4× speedup with simple heuristics but missing dynamic
> interactions between layers. Online importance prediction [Kim 2024,
> Liu 2024] learns a lightweight predictor that runs in parallel with the
> main model, enabling real-time adaptation. However, existing online
> methods require labeled importance data — a circular dependency that
> limits their applicability to pre-trained models where importance
> annotations exist. No method to date addresses the cold-start problem:
> how to estimate token importance for a freshly initialized model.

---

## §9 Research Proposal

A research proposal argues for a planned project — for a thesis proposal,
PhD candidacy exam, or pre-registration. The goal is to convince the
committee that the question is worth answering and the plan is feasible.

**Structure: 6 sections, typically 3,000-8,000 words.**

### §9.1 Introduction & Problem Statement (1-2 pages)
- **Broad context**: Why this area matters (2-3 sentences).
- **Specific problem**: The gap or unsolved question (1-2 sentences).
- **Research questions**: 2-4 concrete, answerable questions. Number them.
  "RQ1: Does X affect Y under condition Z?"
- **Significance**: Who benefits if this succeeds?

### §9.2 Literature Review (1-3 pages)
- **Strategic, not exhaustive.** Show you know the landscape and where
  your work fits.
- Group by approach/theory, not by paper.
- End with: "The above reveals a gap: [precise statement of what's
  missing]. Our proposed work directly addresses this gap."

### §9.3 Methodology (2-4 pages, the most scrutinized section)
- **Research design**: Qualitative, quantitative, or mixed. Justify.
- **Data**: Source, size, collection method, inclusion/exclusion criteria.
- **Procedure**: Step-by-step. A new PhD student should be able to follow it.
- **Analysis plan**: Specific statistical tests or qualitative coding
  approaches. Name the software. "We will use [test] to compare [groups]
  on [metric], with α = 0.05 after Bonferroni correction."
- **Timeline**: Month-by-month Gantt or table with milestones.
- **Ethical considerations**: IRB, informed consent, data privacy.

### §9.4 Expected Outcomes & Contributions (0.5-1 page)
- What you expect to find and why (based on theory or pilot data).
- Intellectual merit: how this advances knowledge.
- Broader impacts: practical implications.

### §9.5 Limitations & Risks (0.5 page)
- Honest assessment of threats to validity.
- Mitigation plans for each risk. "If [assumption] fails, we will fall
  back to [alternative approach]."

### §9.6 References
- Full bibliography in the target venue's required format.

**The 20-minute rule:** Hook the reader within the first page. State the
problem, gap, and RQs before the committee's attention drifts.

---

## §10 Investigation Report (调研报告)

An investigation report presents findings from a systematic inquiry —
field research, market analysis, user study, or organizational audit.
Common in applied disciplines, industry labs, and policy research.

**Structure: 7 sections, typically 3,000-15,000 words.**

### §10.1 Executive Summary (standalone, 200-400 words)
- Write this last. Summarize: purpose → methods → key findings (3-5
  bullet-worthy conclusions) → actionable recommendations.
- Readers should get the complete picture from this section alone.

### §10.2 Introduction (1-2 pages)
- **Background**: Why the investigation was commissioned or undertaken.
- **Objectives**: 3-5 specific goals, numbered.
- **Scope**: Boundaries — time period, geographic area, population, what
  is excluded and why.
- **Research questions**: Mirror the objectives as answerable questions.

### §10.3 Methods (1-2 pages)
- **Approach**: Qualitative (interviews, focus groups, observation),
  quantitative (survey, measurement, secondary data analysis), or mixed.
- **Data sources**: Sample size, selection criteria, period.
- **Instruments**: Survey questionnaires, interview protocols, measurement
  tools — include in appendix if lengthy.
- **Limitations**: Response rate, sampling bias, measurement error.

### §10.4 Current State Analysis (3-6 pages, the core body)
Organize by finding, not by data source. Each finding:
- **Headline statement** (bold or as section heading).
- **Evidence**: Data, quotes, figures, tables — triangulate across sources.
- **Interpretation**: What the evidence means. Connect to objectives.

Use the "现状 → 问题 → 原因" (current state → problem → root cause) chain
for each major finding. Don't just describe — diagnose.

### §10.5 Root Cause Analysis (1-2 pages)
- For each major problem identified in §10.4, drill into WHY it exists.
- Use frameworks where applicable: 5 Whys, fishbone diagram, SWOT.
- Distinguish proximate causes from systemic causes.

### §10.6 Recommendations (1-3 pages)
- **3-7 actionable recommendations**, each with:
  - Specific action (what, who, by when)
  - Expected impact (quantified if possible)
  - Feasibility (cost, risk, prerequisites)
  - Priority (P0 = urgent, P1 = important, P2 = nice-to-have)
- Recommendations must trace directly to findings. No finding →
  no recommendation.

### §10.7 Conclusion (0.5 page)
- Restate the investigation's purpose.
- Summarize the 2-3 most critical takeaways.
- One-sentence call to action.

**Chinese-language conventions (中文调研报告):**
- Title: ≤20 Chinese characters, may include subtitle.
- Abstract: ~300 characters, covering purpose → method → findings → conclusion.
- Body: 宋体 (Song Ti) small 4 (小四, ~12pt), line spacing 20pt.
- Heading hierarchy: 一、 → (一) → 1. → (1).

---

## §11 Grant Proposal (NSFC / General)

A grant proposal requests funding for a research project. While formats
vary by agency (NSFC, NSF, ERC, etc.), the persuasive logic is universal.

**Structure: adapted from NSFC (国家自然科学基金) and NSF conventions.**

### §11.1 Project Summary (0.5 page, write last)
- 3-sentence formula: (1) Problem + gap. (2) Proposed method + innovation.
  (3) Expected impact.
- NSFC limit: 400 Chinese characters for Chinese summary, 2,000 characters
  for English summary.
- Every word counts — this may be the only section some reviewers read.

### §11.2立项依据 / Introduction & Rationale (2-4 pages)
- **Problem significance**: Why this matters to the field and to society.
- **Literature review**: Concise but authoritative. Cite the 10-20 most
  relevant papers. Show you know the landscape.
- **Gap statement**: "Despite progress in [area], [specific problem]
  remains unsolved because [reason]."
- **Research questions or hypotheses**: 2-4, clearly stated.

### §11.3 研究内容 / Research Plan (3-6 pages)
- **3-4 research aims**, each as a subsection:
  - Aim 1: [Title]. Rationale → Approach → Expected outcome → Fallback plan.
- **Technical route diagram** (研究路线图): a flowchart from inputs →
  methods → outputs, with decision points.
- **Feasibility analysis**: Why this team, with these resources, can
  execute this plan. Cite preliminary results if available.

### §11.4 关键科学问题 / Key Scientific Problems (0.5-1 page)
- 2-3 deep scientific questions the project must solve.
- Each: state the problem → why it's hard → your approach to cracking it.
- Distinguish from technical/engineering problems — these must be
  scientific unknowns.

### §11.5 创新点 / Innovation & Contributions (0.5-1 page)
- 2-4 bullet points, each: "Unlike prior work that [limitation], we [novel
  approach], which enables [new capability]."
- Avoid generic claims ("first to study X"). Be specific about what is new.

### §11.6 研究基础 / Preliminary Work & Team (1-2 pages)
- Team member roles, relevant publications, prior collaborations.
- Preliminary data or pilot results that de-risk the project.
- Available equipment, datasets, or infrastructure.

### §11.7 Budget & Timeline
- **Budget table**: Personnel, equipment, travel, consumables, misc. Each
  line justified in one sentence.
- **Timeline**: 3-4 year plan with milestones per quarter. Year 1: setup +
  baseline. Year 2: main experiments. Year 3: analysis + writing. Year 4
  (if applicable): extension + dissemination.

**NSFC-specific tips:**
- Chinese and English summaries must be consistent — reviewers check.
- 立项依据 should cite Chinese researchers where relevant (shows awareness
  of domestic landscape).
- 研究内容 must be concrete, not aspirational — name the datasets, models,
  and metrics you will use.

---

## §12 Progress Report

A progress report updates stakeholders (advisor, committee, funding
agency, team) on research status. Weekly, monthly, or quarterly cadence.

**Structure: 5-6 sections. Weekly: ~0.5 page. Monthly: 1-3 pages.**

### §12.1 Header
- Project title, reporting period, author, date.

### §12.2 Summary (2-3 sentences)
- "This period, we [main accomplishment]. Key result: [headline finding].
  The main blocker is [obstacle, if any]."

### §12.3 Accomplishments (bullet list, the core)
Each item: what was done → what it means → what's next.
- ✅ Trained baseline model on [dataset]. Achieved [metric], consistent
  with [prior work]. Ready to use as comparison point.
- ✅ Collected N = 200 survey responses (target: 150). Demographic
  distribution matches census data. Recruitment complete.
- ❌ Planned ablation on [component] was blocked by [reason].
  Mitigation: [workaround].

### §12.4 Data & Metrics (when applicable)
- A small table or 1-2 key numbers. Don't dump raw logs.
- "Training loss: 2.1 → 0.8 over 50 epochs. Validation accuracy: 83.4%
  (target: 85%)."

### §12.5 Challenges & Risks
- **Blocked**: Issues that prevent progress. State what you need.
- **At risk**: Issues that may become blockers. State your mitigation plan.
- Be honest — hiding problems wastes everyone's time.

### §12.6 Next Period's Plan (5-8 bullet items)
- Specific, measurable tasks. "Complete X" not "Work on X."
- Each task should clearly pass/fail by the next report.
- Include longer-term goals as a separate "On the horizon" section.

**The 3-part weekly format (from UWashington CS):**
1. Quote last week's plan verbatim.
2. This week: accomplishments + lessons + blockers + new ideas.
3. Next week's plan in bullets.

---

## §13 Thesis Defense Outline (答辩提纲)

A defense presentation outline structures a 20-45 minute oral defense
before a committee. It differs from the thesis itself — it tells a story,
not a reference document.

**Structure: 8-10 sections, timed for a standard 30-minute slot.**

### §13.1 Title & Hook (1 slide, 1 min)
- Title, author, advisor, date.
- **Hook**: one-sentence summary that makes the committee lean in. "We show
  that [surprising result], which challenges the assumption that [common
  belief]."

### §13.2 Problem & Motivation (2-3 slides, 3 min)
- What problem does this thesis solve?
- Why does it matter? (Real-world impact + intellectual gap.)
- One slide with the central research question, large font.

### §13.3 Background & Related Work (2-3 slides, 4 min)
- NOT a literature review dump. Show the **gap in the landscape**.
- A 2×2 or taxonomy diagram is more effective than bullet points.
- End with: "Prior work has addressed A and B, but C remains open. This
  thesis addresses C."

### §13.4 Approach Overview (1 slide, 2 min)
- A single architecture/pipeline diagram showing your entire system.
- Walk through the diagram left-to-right or bottom-to-top. Name each
  component in 5-10 seconds.
- The committee should understand your method from this one slide.

### §13.5 Technical Contribution 1 (2-3 slides, 5 min)
- Problem → your idea → how it works (diagram + key equation) → result.
- One equation per slide maximum. Explain every symbol.
- "Before/after" comparison slide is highly effective.

### §13.6 Technical Contribution 2 (2-3 slides, 5 min)
- Same structure as §13.5.

### §13.7 Key Results (2-4 slides, 5 min)
- **Headline result first.** Don't build suspense.
- One main table or figure per slide. Highlight YOUR method's row/bar.
- State statistical significance. "Our method outperforms SOTA by 3.4
  points (p < 0.01, paired t-test, n = 5 seeds)."
- Include a failure case or limitation slide — shows maturity.

### §13.8 Summary & Contributions (1 slide, 2 min)
- 3-4 contributions, each one sentence.
- Revisit the central research question and answer it directly.

### §13.9 Future Work (1 slide, 1 min)
- 2-3 concrete next steps. Not "more research is needed."
- "We plan to extend [method] to [new domain] and release [dataset/tool]."

### §13.10 Backup Slides (prepared, not presented unless asked)
- Detailed experiment tables, derivation steps, additional ablations.
- Expect questions on: "What if [assumption] fails?", "How did you choose
  [hyperparameter]?", "What's the runtime/memory cost?"

**Timing rule:** 1 slide per minute maximum. If a slide needs >2 minutes,
split it. Practice with a timer — running over signals poor preparation.

---

## §14 Slide Deck Narrative (PPT脚本)

A slide deck narrative is a written script that accompanies presentation
slides — used when the presenter must pre-write their talk (conference
presentation, recorded lecture, investor pitch) or when someone else
will deliver the slides.

**Structure: One narrative block per slide.**

### Slide-by-slide format:

```
## Slide N: [Slide Title]
**Duration:** [X] seconds

**Visual:** [What the audience sees — chart type, diagram, key phrase]

**Narrative:**
[The spoken words. Write in conversational academic English —
contractions OK, sentences shorter than in the paper. One paragraph
per slide, 3-6 sentences.]

**Transition:** → "This brings us to [next slide topic]."
```

### Principles for the spoken narrative:

1. **One idea per slide.** If you need two paragraphs, the slide should
   be two slides.
2. **Spoken ≠ written.** Read aloud what you wrote — if it sounds
   unnatural, rewrite. "We found that" beats "It was observed that."
3. **Anchor to the visual.** "The blue bar on the left shows..." The
   audience's eyes follow your words. If you don't reference the visual,
   you're competing with it.
4. **Signpost every transition.** "So that's the architecture. Now, does
   it actually work?" Bridges prevent the audience from getting lost.
5. **Front-load key results.** State the conclusion before the evidence.
   "Our method is 3× faster. Here's the experiment that shows this."
6. **End each section with a takeaway.** "Bottom line: [one sentence]."

### Example:

```
## Slide 7: Main Result — SOTA Comparison
**Duration:** 90 seconds

**Visual:** Grouped bar chart, 4 methods × 3 benchmarks. "Ours" bar in
attention-purple, others in gray. y-axis: Accuracy (%).

**Narrative:**
Here's the headline: our method outperforms all baselines on all three
benchmarks. Focus on the purple bars — that's us. On MMLU, we hit 87.3%,
which is 3.4 points above the previous best. That gap is statistically
significant at p < 0.01. On HellaSwag and ARC, the pattern holds — we're
2.8 and 4.1 points ahead, respectively. The gray bars cluster tightly
around 82-84%, which tells you the baselines have plateaued. Our gain
isn't from a higher baseline; it's from the adaptive mechanism.

**Transition:** → "But raw accuracy only tells half the story. Let's look
at the speed-accuracy trade-off."
```

---

## Self-Check

Before delivering a drafted section, verify:
1. Does each paragraph have a single clear topic sentence?
2. Are all quantitative claims backed by specific numbers?
3. Are all citations justified (each one supports a specific claim)?
4. Does the section match the template structure (correct number of
   paragraphs, correct flow)?
5. Are there any anti-patterns from `references/writing-pitfalls.md`?
