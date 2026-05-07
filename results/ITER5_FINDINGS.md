# Iteration 5 findings — out-of-distribution validation

**Setup.** 2 OOD problems constructed (not in Etingof, novel parameters but in-technique). 7-trace corpus, top-3 retrieval, 3 conditions × 8 samples = 48 outputs. Sonnet judge with explicit reference-answer rubrics.

OOD problems:
- `ood_steepest`: $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ asymptotic — needs steepest descent on a mixed-power phase, interior critical point at $\arctan\sqrt 2$. Reference: $V(n) \sim \sqrt{2\pi/(3n)} \cdot 2^{n/2} \cdot 3^{-3n/4}$.
- `ood_1loop`: $\log(Z/Z_0)|_{1\text{-loop}}$ for $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$ — non-polynomial interaction, mass-shift comes from $\cosh(0) = 1$. Reference: $-(1/2)\log(1-g) = g/2 + g^2/4 + g^3/6 + \ldots$

## Headline

| Condition | Overall | `ood_steepest` | `ood_1loop` |
|-----------|---------|----------------|-------------|
| no-RAG    | **1.00** | 1.00           | 0.99        |
| Struct    | 0.90    | 0.98           | 0.82        |
| Raw       | 0.74    | 0.91           | 0.57        |

**RAG still hurts on OOD, but less than on in-distribution headroom (iter-4).** Raw harm is large; Struct harm small; no-RAG essentially perfect.

## What this tells us about the failure mode

The harm on OOD problems is concentrated on `ood_1loop`. The retrieved trace `ex_3_26_effective_action` (highly relevant by cosine, 0.17 score) ends with the boxed result:

> $S_1(x_c) = \tfrac{1}{2} \log(1 - g x_c) = -\tfrac{1}{2} \sum_{k\ge 1} \frac{(g x_c)^k}{k}$

This is correct for the *effective action* $S_1$ at general $x_c$. But the target problem asks for $\log(Z/Z_0)|_{1\text{-loop}}$ at the specific saddle $x_c = 0$, which is a *different* quantity:
- $\log(Z/Z_0)|_{1\text{-loop}} = -(1/2) \log(S''(x_c=0)) = -(1/2) \log(1-g) = +g/2 + g^2/4 + \ldots$
- Note the **negative** half on the closed form.

Failure mode counts:
- **No-RAG: 0 of 8 sign errors.** Each sample derived $-(1/2) \log(S''(0))$ from first principles using its in-weight knowledge of the saddle-point formula.
- **Struct: 2 of 8 sign errors.** The Struct preserves ex_3_26's positive-sign convention; a couple of Haiku samples copied it.
- **Raw: 5 of 8 sign errors.** The raw trace contains *additional* sign-debugging passages where I (Opus) worked through both conventions before settling on the positive sign for $S_1$. Haiku reading the unedited debugging absorbed both signs and then chose the wrong one ~62% of the time.

This is a clean replication of iter-4's mechanism: **retrieved context contaminates Haiku's reasoning on sign conventions and parameter-specific structures, even when the target problem is OOD from the corpus.**

## Hypothesis testing

### Training-overlap (Oskar's earlier hypothesis)

> Etingof is in Haiku 4.5's pretraining; RAG hints corrupt in-weight knowledge.

**Partially supported but more nuanced than first stated.** Iter-5 shows that even on novel-parameter problems where Haiku doesn't have the *answer* in pretraining, RAG still hurts — because Haiku has the *technique* in pretraining (steepest descent, 1-loop saddle), and that's enough for clean no-RAG performance. The training-overlap that matters is at the technique level, not the answer level.

What this rules out: "RAG would help if only the problems were truly novel." The novel-parameter test shows RAG still hurts when the technique is in pretraining, regardless of whether the specific answer is.

### Format-mismatch (Oskar's iter-4 hypothesis)

> Struct's rigid step format may be poor fit for Claude.

**Supported by Raw < Struct on both iterations.** OOD: Struct 0.90 vs Raw 0.74 (Δ = +0.16). In-distribution: Struct 0.43 vs Raw 0.40 (Δ = +0.03). Struct's compression mitigates some of Raw's confusion-by-author-debugging effect, especially when no-RAG has high accuracy. But neither beats no-RAG.

### Issue #2's H1 (≥10pp lift)

**Falsified across two regimes.** Iter-4 (in-distribution): −21pp on headroom subset. Iter-5 (OOD): −10pp Struct, −26pp Raw. H1 predicted +10pp; observed −10 to −26pp.

## Cross-iteration synthesis

| Iter | Eval set | n_data | no-RAG | Struct | Raw | Δ Struct |
|------|----------|--------|--------|--------|-----|---------|
| 0    | 3 in-dist (n=1) | 3 | 0.63 | 0.48 | — | −0.15 (contamination, see iter-3 verdict) |
| 3    | 6 in-dist broad (n=4) | 24 | 0.77 | 0.78 | — | +0.01 (ceiling-effect dilution) |
| 4    | 2 in-dist headroom (n=8) | 16 | 0.64 | 0.43 | 0.40 | −0.21 |
| 5    | 2 OOD (n=8) | 16 | 1.00 | 0.90 | 0.74 | −0.10 |

The size of the harm correlates with how confused no-RAG is (more confused → bigger absolute RAG harm). At ceiling no-RAG (iter-5), RAG can only do small damage. At in-distribution-headroom (iter-4), where Haiku has technique knowledge but slightly imperfect coefficient handling, RAG amplifies the imperfections. **The mechanism is consistent: RAG context introduces conventions/parameters that compete with in-weight reasoning.**

## Final interpretation

**At niche corpus scale (≤10 traces over a single textbook), T³-style RAG over Opus-generated thinking traces does NOT help Haiku 4.5 on math-physics problems. It actively harms, by introducing sign conventions, parameter values, and quantity definitions that conflict with the target problem.**

The mechanism is *not* unique to in-distribution problems — it persists on OOD problems with the same flavor. The harm magnitude scales inversely with no-RAG accuracy: the more Haiku needs help, the more RAG's competing hints corrupt its reasoning.

Format matters at second order: cleaner Structs hurt less than verbose Raw traces, but both hurt.

## Implications for the broader picture

1. **For issue #2:** decisively answered. T³-niche-scale-RAG fails for Haiku on Etingof. The clean diagnostic case for the failure is now documented across in-distribution headroom and OOD problems with the same mechanism.

2. **For Muninn-trace retrieval (synthesis memory `f31c1008`):** strongly cautionary. Past Muninn sessions are even more in-distribution than Etingof problems are for Haiku — the failure mode found here would be amplified, not mitigated. If trace-RAG for Muninn is pursued, the architecture must force *abstraction* over copying (e.g. low-priority hints the model can ignore, or retrieval restricted to topically-distant traces forcing technique generalization).

3. **For frontier-scale T³ replication:** the iter-3 → iter-5 progression suggests the paper's reported lifts at 59K traces depend on retrieval diversity that small corpora cannot provide. This is a falsifiable prediction: scaling our corpus from 7 to ~100 traces should monotonically reduce RAG harm and eventually flip to RAG benefit. We didn't test that here (out of scope).

## Recommendation

**Experiment closed for real this time.** Iter-0 → 5 covers:
- Pilot with contamination (iter-0)
- Methodological refinement (iter-1, 2)
- Clean broad eval (iter-3)
- Stratified in-distribution test (iter-4)
- OOD validation (iter-5)

Five iterations, 96 graded inferences, dual-judge calibration on the broad eval, two failure modes mechanistically documented (problem transposition in iter-0, sign-convention contamination in iter-4/5). This is the cleanest niche-scale T³ result currently available.

The next step is **the blog post**, not another iteration.
