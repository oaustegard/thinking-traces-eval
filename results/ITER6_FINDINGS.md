# Iteration 6 — capability-ladder ablation reverses the headline

## Setup

Same 4 problems (`ex_3_24`, `ex_7_28`, `ood_steepest`, `ood_1loop`),
same 3 conditions (no_rag, struct, raw), same 7-trace corpus and same
top-3 cosine retrievals as iter-4 / iter-5. Two new inference models via
the Cloudflare AI Gateway:

- **Gemini 2.5 Flash Lite** (the weakest available model in the gemini
  client wrapper) — a "weak" tier
- **Gemini 2.5 Flash** — a "mid" tier

Same n=8 samples per cell, total 192 inferences. Same Sonnet 4.6 judge
with the same per-problem rubrics used in iter-4 / iter-5.

Operational notes (mostly engineering):
- First sweep on Lite at 4K output cap truncated 74/96 outputs
  mid-derivation (Flash Lite uses many tokens before reaching the
  boxed answer). Bumped to 16K, all outputs complete.
- First sweep on Flash at 16K cap got the *visible* output truncated
  because Gemini 2.5 Flash uses extended thinking by default and the
  cap covers thinking + output combined. Bumped to 32K, complete.
- 4 cells timed out at the CF gateway 120s ceiling, picked up by a
  retry pass (skip-guard checks for `boxed` substring presence).

## Aggregate scores

| Model              | no_rag | struct | raw |
|--------------------|--------|--------|-----|
| Haiku 4.5 (iter-4/5) | 0.78   | 0.66   | 0.57 |
| **Gemini 2.5 Flash** | **0.61** | **0.74** | **0.70** |
| Gemini 2.5 Flash Lite | 0.41   | 0.42   | 0.48 |

The headline "RAG hurts Haiku 4.5" was right, but it does **not**
generalize to other capability tiers. On Flash, RAG **helps** in the
aggregate; on Lite, RAG is roughly neutral (everything in noise floor).

## Per-problem aggregate is misleading

The aggregate Flash effect is **borderline**:
- Δ Struct = +0.131  95% CI [−0.031, +0.294]  P(Δ≥0) = 0.94
- Δ Raw    = +0.084  95% CI [−0.077, +0.245]  P(Δ≥0) = 0.85

Both CIs include zero. The reason the aggregate looks small is **per-
problem dilution** — the problems behave very differently:

### Flash per-problem

| Problem | no_rag | struct | raw | Δ Struct (CI) | Δ Raw (CI) |
|---------|--------|--------|-----|---------------|------------|
| ex_3_24       | 0.22   | 0.63   | 0.58 | **+0.41 [+0.28, +0.53]** ✓ | **+0.36 [+0.21, +0.49]** ✓ |
| ex_7_28       | 0.32   | 0.34   | 0.39 | +0.02 [−0.05, +0.08] noise | +0.08 [−0.01, +0.14] noise |
| ood_steepest  | 0.99   | 1.00   | 0.81 | +0.01 [+0.00, +0.02] near-ceiling | **−0.18 [−0.37, −0.04]** ✓ |
| ood_1loop     | 0.91   | 1.00   | 1.00 | +0.09 [+0.00, +0.26] near-ceiling | +0.09 [+0.00, +0.26] near-ceiling |

The clean signals on Flash:
- **ex_3_24**: RAG **helps massively** (+0.41 Struct, +0.36 Raw, both decisively significant). This is the in-distribution problem where Haiku 4.5 was harmed by −0.29 Struct.
- **ood_steepest Raw**: RAG **hurts** (−0.18 sig). The verbose Wallis trace dragged Flash off-track on a problem it could solve cleanly without RAG.

### Lite per-problem

Lite is in the noise floor across the board. Per-problem CIs all cross
zero. The model is too weak to discriminate the trace's hint from
noise — RAG is neither help nor harm at this tier.

## Cross-model comparison on the same problem

The cleanest cross-tier comparison is **ex_3_24** with the Struct
condition, evaluated on the same retrievals:

| Model | no_rag | struct | Δ Struct vs no_rag |
|-------|--------|--------|--------------------|
| Haiku 4.5 (subagent) | 0.61   | 0.32   | **−0.29** sig |
| Gemini 2.5 Flash     | 0.22   | 0.63   | **+0.41** sig |
| Gemini 2.5 Flash Lite | 0.42  | 0.42   | 0.00 noise |

Haiku has the technique in-weight cleanly (no_rag = 0.61) and the RAG
hint conflicts with that internal model → corruption. Flash has gaps in
its in-weight knowledge of the technique (no_rag = 0.22) and the RAG
hint genuinely fills those gaps → significant lift. Lite is weak enough
that the hint and the gap are both in the noise.

## What this means for the headline

The pre-iter-6 reframed headline:

> Niche-scale T³ RAG transmits sign/parameter conventions from authored
> traces to a weaker downstream model. When a retrieved trace's
> convention conflicts with the target problem, harm is statistically
> significant ...

was correct as far as Haiku 4.5 went, but it overgeneralizes the
direction of effect. Iter-6 forces a further refinement:

**The post-iter-6 reframed headline:**

> Niche-scale T³ RAG over Opus-authored thinking traces interacts with
> the inference model's pretraining: when the model has the relevant
> technique in-weight cleanly (Haiku 4.5 on Etingof problems), retrieved
> trace context functions as competing-convention noise and harms
> performance (Δ Struct = −0.29 [−0.39, −0.18] on ex_3_24). When the
> model has gaps in technique knowledge (Gemini 2.5 Flash on the same
> problems), the retrieved context functions as useful technique
> guidance and helps (Δ Struct = +0.41 [+0.28, +0.53] on ex_3_24, same
> retrievals, same prompts). When the model is weak enough that long-
> context hints don't land at all (Gemini Flash Lite), RAG is neutral.

This is genuinely interesting. It says the T³ paper's reported lifts on
mid-tier inference models are real and replicable at niche scale —
they just don't survive applying the same pipeline to a stronger model
on a domain that's in its pretraining.

## Where this leaves the blog post

The story is now a three-part finding rather than one-direction harm:

1. **Capability tier matters more than corpus size.** A 7-trace niche
   corpus produces +41pp lifts at the right tier. The same corpus
   produces −29pp harm one tier up.
2. **The mechanism is consistent across tiers.** The sign-convention
   contamination from `ex_3_26` (the failure mode I documented in
   iter-4 / iter-5) appears in *all three* models' RAG outputs. On Haiku
   it propagates from the hint to a wrong answer. On Flash it's caught
   by the model and converted to a correct answer with the same closed
   form. On Lite the model is too unfocused for either path to dominate.
3. **Format ablation reverses too.** On Flash ood_steepest, **Raw hurts
   significantly** while Struct is neutral — the verbose trace is what
   does the damage. This is the opposite direction from Haiku where
   Struct's compression helped. Suggests format-by-tier interactions.

## Confidence and caveats

Strengths from iter-6:
- The iter-4/5 mechanism story (convention contamination) is replicated
  at a different model and different family.
- The directional reversal at Flash is decisive on ex_3_24 (CI excludes
  zero by ~0.28) — not noise.
- Same corpus, same prompts, same retrievals, same judge across models.

Caveats:
- 4 problems is still a small set. The aggregate Flash lift is
  borderline (CI just touches zero); only ex_3_24 is rock-solid.
- Single judge dependency persists. Sonnet's high scores on
  Flash-Struct-ex_3_24 should be spot-checked against Opus.
- "Gemini 2.5 Flash" via CF gateway might invoke different defaults
  than direct API calls; thinking-budget interactions made this run
  finicky to set up cleanly.
- The dilution from ex_7_28 noise and ood_steepest Raw harm means the
  aggregate is not a clean number to put in a pull-quote.

## Recommended next step

The blog post can now be drafted. The story has three legs (Haiku
harm, Flash benefit, Lite noise) that mutually corroborate the
mechanism while complicating the original "RAG hurts" claim. The
headline should be **capability-tier-dependent**, not directional.
