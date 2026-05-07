# Iteration 7 — vanilla n-shot ablation isolates framing from content

## Setup

Same 4 problems, same 7-trace corpus, same retrieved raw traces (top-3
cosine), same n=8 samples per cell, same Sonnet 4.6 judge as iter-4 / 5
/ 6. **One** new condition:

- **`nshot`** — vanilla 3-shot ICL on raw traces. NO anti-copy
  guardrail, NO "use as hints not templates", NO "state relevance and
  differences first" preface. Just the standard few-shot CoT format:
  *"Below are three worked examples; study them, then solve the new
  problem in the same style."* (See `prompts/nshot_inference.md`.)

Two models: Haiku 4.5 (subagent) and Gemini 2.5 Flash. 64 inferences total.

The control compares `nshot` against the existing `raw` condition,
which uses the same retrieved raw traces but with the anti-copy
recipe framing. The diff isolates **prompting effect** from **content
effect**.

## Aggregate scores

Same 4 problems × 8 samples per condition (n=32 per cell):

| Model              | no_rag | struct (recipe) | raw (recipe) | **nshot (vanilla)** |
|--------------------|--------|-----------------|--------------|---------------------|
| Haiku 4.5          | 0.82   | 0.66            | 0.57         | **0.73**            |
| Gemini 2.5 Flash   | 0.61   | 0.74            | 0.70         | **0.63**            |

## Bootstrap CIs (10000 resamples, percentile)

### Haiku 4.5

| Comparison           | Δ        | 95% CI            | P(Δ≥0)  | Significance       |
|----------------------|----------|-------------------|---------|--------------------|
| nshot vs no_rag      | −0.084   | [−0.203, +0.034]  | 0.087   | **not significant** |
| nshot vs struct      | +0.070   | [−0.073, +0.214]  | 0.835   | not significant    |
| nshot vs raw         | **+0.161** | **[+0.019, +0.303]** | **0.986** | **significant**    |

### Gemini 2.5 Flash

| Comparison           | Δ        | 95% CI            | P(Δ≥0)  | Significance       |
|----------------------|----------|-------------------|---------|--------------------|
| nshot vs no_rag      | +0.019   | [−0.169, +0.208]  | 0.581   | not significant    |
| nshot vs struct      | −0.113   | [−0.273, +0.052]  | 0.089   | borderline (p=0.09) |
| nshot vs raw         | −0.066   | [−0.228, +0.095]  | 0.216   | not significant    |

## Per-problem on ex_3_24 (the discriminating in-distribution problem)

| Model | no_rag | struct | nshot | Δ nshot vs struct (95% CI)        | Sig |
|-------|--------|--------|-------|-----------------------------------|-----|
| Haiku | 0.61   | 0.32   | **0.51** | **+0.194 [+0.044, +0.331]**     | ✓   |
| Flash | 0.22   | 0.63   | **0.43** | **−0.200 [−0.319, −0.069]**     | ✓   |

Beautiful inversion: on the same problem with the same retrievals,
removing the anti-copy framing **lifts Haiku by 19pp** and **drops
Flash by 20pp**, both decisively significant.

## Per-problem highlights elsewhere

**ex_7_28**: Flash nshot crashes to 0.11 vs no_rag 0.32 (Δ=−0.21
[−0.27, −0.15]; **strongly significant harm**). The retrieved
`ex_7_27_quartic_1pi` trace shares so much surface structure with the
target problem that vanilla ICL drives Flash into over-imitation
without the anti-copy prompt to flag the mismatch. The recipe-style
struct on the same target was 0.34 — the anti-copy framing prevented
this specific over-imitation failure.

**ood_steepest**: All four model × condition cells at or near 1.0;
no signal.

**ood_1loop**: Both models within bootstrap noise of their
condition-specific baselines; nshot ≈ struct on both.

## What this reframes about iter-4/5/6

The mechanistic story from iter-4/5 was *"sign-convention contamination
from `ex_3_26`'s `+(1/2) log` ends up in Haiku's answers via the RAG
context."* That mechanism is real and verifiable in the trace text, but
**the anti-copy framing was amplifying it, not preventing it**. With
vanilla ICL:

- Haiku's sign-error rate on `ood_1loop` (boxed answer survey, 8
  samples): nshot 2/8 wrong-sign vs struct ~2/8 vs raw ~5/8. Roughly
  similar. Magnitude of effect is similar.
- Haiku's Taylor-coefficient gibberish on `ex_3_24` (where struct gave
  expansions like `g + 2g² + 8g³/3` instead of the correct `g + g² +
  4g³/3`) is largely **gone** under nshot. The forced
  "relevance/differences" preamble seems to have been making Haiku
  recompose Taylor expansions from the example's coefficient pattern
  — a recomposition that's wrong because the example uses a different
  prefactor on the log.

For **Flash**, the iter-6 reading was *"RAG fills gaps in Flash's
in-weight technique knowledge → +41pp on ex_3_24."* Iter-7 splits this
finding: the retrieved content on its own (vanilla ICL) gives only
+0.21 on ex_3_24, while the recipe-style framing adds another +0.20.
**The anti-copy framing is doing about half the work of the iter-6
Flash lift.**

## Three-leg synthesis (post-iter-7)

| Effect                    | Haiku 4.5         | Flash             | Lite            |
|---------------------------|-------------------|-------------------|-----------------|
| Retrieval content alone (nshot vs no_rag)   | small harm trend (p=0.09) | small lift trend (p=0.41) | not measured |
| Anti-copy framing (struct vs nshot)         | small harm trend (p=0.84 wrong way wait let me recheck) | borderline lift (p=0.09) | not measured |

(Wait — the table needs re-checking; the Haiku struct is *worse* than nshot, so the framing is hurtful. Let me restate:)

| Effect                    | Haiku 4.5                              | Flash                                |
|---------------------------|----------------------------------------|--------------------------------------|
| Retrieval content alone (nshot − no_rag)    | Δ=−0.08 small harm trend (p=0.09)     | Δ=+0.02 ≈ neutral                   |
| Anti-copy framing on top of content (struct − nshot) | Δ=−0.07 small additional harm trend (p=0.16)  | Δ=+0.11 borderline lift (p=0.09)   |

The two effects roughly add:
- Haiku: −0.08 (content) + −0.07 (framing) ≈ −0.15 = struct vs no_rag observed
- Flash: +0.02 (content) + +0.11 (framing) ≈ +0.13 = struct vs no_rag observed

Both effects are small individually and in the same direction within each model. The struct-vs-no_rag effect for each model is roughly the sum of the two.

## What this means for the blog post

Pre-iter-7 reframed headline (after capability-ladder):

> When the model has the technique in-weight cleanly, retrieved trace
> context is competing-convention noise and harms (Haiku). When gaps
> exist, the same retrievals genuinely help (Flash). When too weak,
> RAG is noise (Lite).

Post-iter-7 refinement: that's correct, but the **prompt framing**
matters as much as the retrieved content. Specifically:

1. The anti-copy "use as hints, state relevance/differences" framing
   adds modest structure that helps mid-tier models (Flash) and hurts
   strong models (Haiku) on the same problem.
2. With vanilla ICL on the same retrieved content, the cross-tier
   effects are smaller (mostly within bootstrap noise on aggregate)
   but **persist in direction**: weak content-effect harm on Haiku,
   weak content-effect lift on Flash.
3. Therefore: the T³ paper's reported lifts on mid-tier inference
   models are partially attributable to its specific prompt
   structure, not just the retrieved trace content. Reproducing those
   lifts requires both the right tier and the right framing.
4. The "convention contamination from `ex_3_26`" mechanism still
   fires under vanilla ICL (sign errors persist on ~2/8 nshot Haiku
   samples), but the more spectacular Taylor-coefficient gibberish
   that recipe-prompted struct produced is largely gone. The
   "use as hints, state relevance" prompt was apparently making
   Haiku recompose Taylor coefficients from the example's pattern —
   which goes wrong when the example uses a different prefactor.

## Caveats

- 8 samples per cell, 4 problems, single judge. The aggregate effects
  are at borderline significance even at this n. Per-problem signals
  are sharper but more noise-prone.
- The iter-6 Flash dilution (ex_7_28 noise + ood_steepest Raw harm)
  also dilutes iter-7 — most of the action lives in `ex_3_24`.
- Single judge (Sonnet) for both iter-7 and iter-6/4/5 means the
  comparison is consistent but the cardinal scores depend on
  Sonnet's rubric interpretation. Spot-check against a second judge
  before publishing.
- The "vanilla nshot" prompt I used is one specific format. Other
  vanilla forms (e.g., problem-and-answer pairs without reasoning)
  could give different numbers. The result is "this specific
  vanilla framing on these specific raw traces."

## Bottom line for the post

The blog post now has four legs, not three:

1. **Haiku harm from RAG, attributable to convention contamination
   AND prompt framing.** Mechanism documented in iter-4/5; iter-7
   shows the framing was making it worse.
2. **Flash lift from RAG, attributable to content gaps + framing
   structure.** Iter-6 documents the lift; iter-7 splits content vs
   framing contributions.
3. **Lite is noise across the board** (iter-6).
4. **The framing matters as much as the content** (iter-7). The
   post should distinguish "T³ paper's recipe-style RAG" from
   "vanilla CoT few-shot" rather than treating them as the same
   thing.
