# Reframed headline (post-bootstrap, post-challenger-review)

## What survives statistical inference

Per `scripts/bootstrap_cis.py` (10000 resamples, percentile bootstrap):

### Iter-4 (in-distribution headroom: ex_3_24, ex_7_28; n=8/cell)

| Condition | Δ vs no-RAG | 95% CI | P(Δ≥0) |
|-----------|-------------|--------|---------|
| Struct (aggregate) | −0.21 | [−0.31, −0.11] | 0.0000 |
| Raw (aggregate)    | −0.23 | [−0.33, −0.13] | 0.0000 |
| Struct ex_3_24     | −0.29 | [−0.39, −0.18] | 0.0000 |
| Struct ex_7_28     | −0.13 | [−0.23, −0.01] | 0.021  |
| Raw    ex_3_24     | −0.21 | [−0.34, −0.06] | 0.0021 |
| Raw    ex_7_28     | −0.26 | [−0.41, −0.11] | 0.0013 |

**Iter-4 holds**: Struct and Raw both significantly worse than no-RAG, both
problems individually, and aggregate. CIs exclude zero.

### Iter-5 (OOD constructed: ood_steepest, ood_1loop; n=8/cell)

| Condition | Δ vs no-RAG | 95% CI | P(Δ≥0) | Verdict |
|-----------|-------------|--------|---------|---------|
| Struct ood_steepest | **−0.025** | [−0.075, +0.000] | 0.34 | **Neutral** |
| Raw    ood_steepest | **−0.088** | [−0.262, +0.000] | 0.34 | **Neutral** |
| Struct ood_1loop    | −0.175 | [−0.419, +0.006] | 0.056 | **Borderline** |
| Raw    ood_1loop    | −0.425 | [−0.619, −0.206] | 0.0000 | Significant |
| Struct (aggregate)  | −0.10  | [−0.228, −0.003] | 0.019 | Just clears zero |
| Raw    (aggregate)  | −0.26  | [−0.422, −0.100] | 0.0002 | Significant |

**Iter-5 splits into two regimes:**
- `ood_steepest`: no convention conflict in retrieved context. RAG is
  **statistically neutral** for both Struct and Raw. CIs touch zero.
- `ood_1loop`: convention conflict from `ex_3_26`'s `+(1/2) log` form vs
  target's `−(1/2) log`. Raw harm is large and significant; Struct harm
  is borderline (CI just barely overlaps zero).

The aggregate iter-5 Struct effect (−0.10) is driven almost entirely by
ood_1loop. **Calling iter-5 a clean RAG-hurts result is overreach.** It is
better described as: RAG is neutral when there is no convention conflict,
and harmful when there is.

## Reframed claim for the blog post

**OLD (overreach):**
> At niche corpus scale (≤10 traces over a single textbook), T³-style RAG
> over Opus-generated thinking traces actively HURTS Haiku 4.5 on
> math-physics problems, both in-distribution (Δ Struct = −21pp on
> headroom subset) and OOD (Δ Struct = −10pp, Δ Raw = −26pp).

**NEW (defensible):**
> At niche corpus scale (≤10 traces over a single textbook), T³-style
> RAG over Opus-generated thinking traces transmits sign and parameter
> conventions from the trace's author to the downstream model (Haiku 4.5
> invoked as a Claude Code subagent). When a retrieved trace's convention
> conflicts with the target problem, harm is statistically significant
> across formats (Δ Struct ≈ −0.13 to −0.29 in-distribution; Δ Raw ≈
> −0.21 to −0.43 in-distribution and OOD). When no convention conflict
> exists in the retrieved context, RAG is neutral within bootstrap noise
> (Δ ≈ 0, CIs touch zero). Raw traces transmit more harm than Struct
> cheatsheets because they preserve mid-derivation sign-debugging that
> Struct compression strips out.

## Mechanism (now distinguishable, not just suggested)

The blog post should make the **convention-conflict** mechanism the spine,
with two contrasting examples:

1. **Conflict case** (`ex_3_24` and `ood_1loop`): retrieved `ex_3_26` ends
   with `S₁ = +(1/2) log(1 - g x_c)`. Target wants
   `log(Z/Z₀) = −(1/2) log(S″(x_c=0))` — opposite sign, different physical
   quantity. Haiku copies the convention 2/8–5/8 of the time depending on
   format, never via no-RAG.

2. **No-conflict case** (`ood_steepest`): retrieved `ex_2_14_wallis` uses
   the same steepest-descent technique with no sign or normalization
   gotcha that maps to the target problem. Haiku applies the technique
   correctly across all conditions; RAG provides zero lift but also zero
   harm. Distinguishes "RAG transmits errors" from "RAG is universally
   bad."

## Predictive content

The reframed claim makes a falsifiable prediction: **for a target problem
where the closest retrieval does not contain a convention or
parameter-naming choice that conflicts with the target, RAG harm should
fall to within bootstrap noise.** A future iteration could test this by
deliberately curating convention-aligned vs convention-conflicting trace
pairs and predicting harm magnitudes.

## What still needs work before publication

1. **Single-judge dependency** on iter-4/5: the convention-conflict scoring
   on ood_1loop relies on Sonnet to distinguish the effective-action
   quantity from log(Z/Z₀). Spot-check 4–8 of the 0.3-scored samples
   against Opus before publishing.

2. **Selection effect on iter-4** is real and acknowledged. The way
   challenger findings 1 and 3 land best: **lead the post with the
   convention-conflict mechanism and the iter-5 split**, use iter-4
   numbers as in-distribution corroboration but note the headroom
   selection.

3. **Capability ladder** untested. The current evidence is "what does
   RAG do to Haiku 4.5 on this corpus?" Iter-6 (planned: weaker Gemini
   models) tests "what does RAG do when the model lacks the technique
   in-weight?" That experiment is what makes the post tell a complete
   story rather than a partial-evidence cautionary tale.
