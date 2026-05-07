# RAG over thinking traces: it's complicated

*A niche-scale replication of the T³ pattern, with three ablations that say
"yes, but..."*

---

## TL;DR

Arabzadeh et al.'s [T³ paper](https://arxiv.org/abs/2605.03344) ("Thinking
Traces Transfer", 2026) shows that taking Opus-generated thinking traces,
rewriting them as structured cheatsheets, and serving them at inference time
gives mid-tier models a meaningful lift. I wanted to know what that pattern
actually transmits at *niche* scale — 7 traces over a single graduate
textbook, not the multi-thousand-trace corpora in the paper.

After 384 inferences across seven iterations and three ablations, the answer
is: **all of T³'s reported effects show up in this niche replication, but
they're contingent on (1) the inference model's capability tier, (2) the
prompt framing around the retrievals, and (3) whether the retrieved trace
embeds a sign or parameter convention that conflicts with the target
problem.** I did not disprove T³; I refined the conditions under which it
helps, hurts, or is silent.

The full per-iteration writeups, scores, prompts, and bootstrap CIs live in
the [thinking-traces-eval](https://github.com/oaustegard/thinking-traces-eval)
repo. This post is a tour of the four claims that survived statistical
inference and the three ablations that produced them.

---

## Setup

**Domain.** Mathematical-physics exercises from Etingof's *Mathematical Ideas
and Notions of Quantum Field Theory* (arXiv:2409.03117). Steepest-descent
integrals, Feynman-diagram counting, effective actions, characteristic
classes. Niche enough that retrievals can plausibly carry technique
knowledge; hard enough that mid-tier models genuinely struggle; narrow
enough to fit a 7-trace corpus.

**Corpus.** 7 thinking traces hand-generated with Claude Opus 4.7 (extended
thinking on, full reasoning retained). Each trace is a complete worked
solution. The 7 are spread across chapters and techniques — see
[`traces/`](https://github.com/oaustegard/thinking-traces-eval/tree/main/traces).

**Eval problems.** 4 problems × 8 samples × 3–4 conditions per cell:
- 2 in-distribution from Etingof (`ex_3_24` — effective action via Laplace;
  `ex_7_28` — quartic 2-point function), chosen for headroom (no_rag mean
  ~0.6, not ceiling-saturated).
- 2 OOD constructed (`ood_steepest` — non-textbook Laplace integral;
  `ood_1loop` — 1-loop log-det in a non-Etingof normalization).

**Conditions.**
- `no_rag` — bare problem statement, no retrievals.
- `struct` — top-3 cheatsheet rewrites (T³ Fig 4 prompt) + recipe-style
  inference prompt with anti-copy guardrail ("use as hints, state relevance
  and differences first").
- `raw` — same retrievals, raw thinking traces instead of cheatsheets, same
  recipe-style framing.
- `nshot` — same raw retrievals, **vanilla 3-shot ICL framing** (just
  "study these worked examples, then solve"). Iter-7 ablation.

**Inference models.**
- Haiku 4.5 invoked as a Claude Code subagent (the strong tier in this
  experiment).
- Gemini 2.5 Flash via the Cloudflare AI Gateway (the mid tier).
- Gemini 2.5 Flash Lite via the same gateway (the weak tier).

**Judge.** Sonnet 4.6 with per-problem rubrics held constant across
iterations (calibrated against Opus in iter-3). Bootstrap CIs (paired,
10000 resamples) on every comparison.

---

## Claim 1: At niche scale, the same retrievals lift Flash and harm Haiku

This is the [iter-4](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER4_FINDINGS.md)
+ [iter-6](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER6_FINDINGS.md)
result. On `ex_3_24`, with the *exact same* top-3 retrievals, the *exact
same* recipe-style RAG prompt, and the *exact same* judge rubric:

| Model | no_rag | struct (recipe RAG) | Δ Struct vs no_rag (95% CI) |
|---|---|---|---|
| Haiku 4.5 | 0.61 | 0.32 | **−0.29 [−0.39, −0.18]** sig |
| Gemini 2.5 Flash | 0.22 | 0.63 | **+0.41 [+0.28, +0.53]** sig |
| Gemini 2.5 Flash Lite | 0.42 | 0.42 | 0.00, in noise |

That's a 70-percentage-point swing in *direction* of effect from changing
only the inference model. The Flash lift is decisively significant; the
Haiku harm is decisively significant; both CIs exclude zero by ~0.18+.

T³ reports lifts on mid-tier models. Iter-6 confirms the lift replicates at
niche scale on Flash. T³ doesn't test what happens when you point the same
pipeline at a stronger model on a domain that's already in its pretraining.
We did. Same retrievals, opposite outcome.

So far this is a "T³ holds for the tier T³ targets." Where it gets
interesting is the mechanism.

---

## Claim 2: The mechanism is convention transmission, not retrieval-as-noise

This is the
[iter-5](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER5_FINDINGS.md)
+ [HEADLINE_REFRAMED](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/HEADLINE_REFRAMED.md)
result. Initial reading of iter-4 was "the retrievals are confusing Haiku."
That's wrong, or at least incomplete. The iter-5 OOD problems split cleanly
into two regimes:

| OOD problem | Convention conflict in retrieval? | Δ Struct (Haiku) | Δ Raw (Haiku) |
|---|---|---|---|
| `ood_steepest` | No (retrieved Wallis trace uses standard sign convention) | −0.025 [−0.075, +0.000] **neutral** | −0.088 **neutral** |
| `ood_1loop` | Yes (retrieved `ex_3_26` ends with `+(1/2) log`; target needs `−(1/2) log`) | −0.175 [−0.419, +0.006] **borderline** | **−0.425 [−0.619, −0.206] sig** |

Same model, same pipeline, same judge. Where the closest retrieval has no
convention conflict, RAG is **statistically neutral within bootstrap noise**.
Where it has a convention conflict, harm is significant and large for raw
traces, borderline for structs (which compress some of the convention
detail away).

Reading the actual `ex_3_26` trace explains it. The trace ends with `S₁ =
+(1/2) log(1 - g x_c)`. The target problem `ood_1loop` wants `log(Z/Z₀) =
−(1/2) log S″(x_c=0)` — opposite sign, different physical quantity. Haiku
copies the convention 2/8 to 5/8 of the time depending on format. It never
makes the same sign error in the no_rag condition. The retrieved hint is
*literally* the source of the error.

The same mechanism appears in Flash's outputs, but Flash converts the wrong
hint to a *correct* answer in many samples — its weaker in-weight grasp of
the technique means it doesn't have a competing strong prior for Haiku's
hint to corrupt. So the same transmitted convention is corruption for the
strong model and useful guidance for the mid model.

This is what makes the result interesting beyond "tier matters." The
*content* the retrievals transmit is consistent across tiers. The *outcome*
inverts because what counts as a "hint" depends on what's already in the
model.

---

## Claim 3: The framing does about half the work

This is the new
[iter-7](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER7_FINDINGS.md)
result, and it's the one that complicates "T³ helps mid-tier models" the
most.

T³'s recipe prompt is more than just "here are some retrievals." It tells
the model to "use these as hints, not templates" and to "first state which
parts are relevant and what differs from the new problem." That structured
preamble is doing work on top of the retrievals themselves. Iter-7 isolates
the framing by running the *same* retrieved raw traces under a *vanilla*
3-shot ICL prompt — the kind you'd use for any few-shot CoT — with no
anti-copy guardrail.

On `ex_3_24` (the discriminating problem):

| Model | struct (recipe framing) | nshot (vanilla framing) | Δ nshot vs struct |
|---|---|---|---|
| Haiku 4.5 | 0.32 | **0.51** | **+0.194 [+0.044, +0.331]** sig |
| Flash | 0.63 | **0.43** | **−0.200 [−0.319, −0.069]** sig |

Same retrievals, only the framing differs:
- For **Haiku**, removing the anti-copy framing recovers 19pp of the harm.
  Most of the failure under recipe-RAG was apparently the "state relevance
  and differences" preamble forcing Haiku to engage with retrieval-specific
  details (sign conventions, parameter values) that conflicted with its
  in-weight knowledge. Vanilla ICL lets Haiku rely on pretraining and
  largely ignore the example structure.
- For **Flash**, removing the framing *removes* 20pp of the lift. The
  retrieved content alone, under vanilla ICL, gives only +21pp over no_rag
  on `ex_3_24` (vs +41pp under recipe-RAG). The "state relevance and
  differences" preamble is what was making Flash apply the technique
  carefully rather than pattern-matching superficially. Take it away and
  Flash collapses on `ex_7_28` too — vanilla nshot drops Flash to 0.11 vs
  no_rag 0.32, because without the "check what differs" prompt Flash
  over-imitates the surface structure of the retrieved `ex_7_27` trace.

In aggregate (4 problems × 8 samples = 32 per cell):

| Model | no_rag | struct | nshot | nshot vs struct |
|---|---|---|---|---|
| Haiku | 0.82 | 0.66 | 0.73 | +0.07 (n.s.) |
| Flash | 0.61 | 0.74 | 0.63 | −0.11 (borderline, p=0.09) |

The aggregate effects are smaller than `ex_3_24` alone because `ex_7_28`
and the OOD problems dilute. But the signs are consistent:
- Recipe framing on top of retrieved content adds harm on Haiku and adds
  lift on Flash, on top of whatever the retrievals do alone.
- Vanilla ICL on the same retrievals gives much smaller, mostly bootstrap-
  noise-level effects in both directions.

So when T³ reports a +X% lift on a mid-tier model, some fraction of X is
the retrieved content, and some fraction is the prompt structure used to
serve it. At least at niche scale, those fractions look roughly equal.
That's not a refutation of T³ — it's a refinement saying that "RAG over
thinking traces" results need to disclose framing as carefully as they
disclose retrieval mechanics.

---

## Claim 4: Below a capability floor, retrievals are silent

The Gemini 2.5 Flash Lite results are the boring claim, but worth stating
because it's the third leg that makes the cross-tier story coherent.

Flash Lite on the same 4 problems × 3 conditions × 8 samples:

| Condition | Aggregate score | Δ vs no_rag |
|---|---|---|
| no_rag | 0.41 | — |
| struct | 0.42 | +0.01, in noise |
| raw | 0.48 | +0.07, in noise |

Per-problem CIs all cross zero. The model is too weak to discriminate the
retrieved hint from noise. RAG is neither help nor harm — it's just
*silent*. Whatever the retrievals contained doesn't reach the model's
output one way or the other.

This matters because it's the cleanest counter-evidence to a "RAG always
hurts strong models, helps weak models" narrative. There's a capability
*floor* below which the retrievals are inert. T³'s reported sweet spot is
above that floor and below the strong-model "convention conflict overrides
in-weight knowledge" regime.

---

## What this all means for "RAG over thinking traces"

Calling it "T³ doesn't work at niche scale" would be wrong. The pattern
genuinely lifts mid-tier models on a 7-trace corpus, with a +41pp effect on
the discriminating problem that survives bootstrap inference. Calling it
"T³ works just as advertised" would also be wrong. The same pipeline
*harms* a stronger model by 29pp on the same problem, the framing does
maybe half the work, and below a capability floor nothing transmits.

The reframed claim is the four-leg version:

1. **Tier matters more than corpus size.** A 7-trace niche corpus is enough
   to produce decisive effects in both directions, just on different models.
2. **The mechanism is convention transmission.** Retrieved traces carry
   sign / parameter / normalization choices from their author, and those
   choices either fill gaps (helping mid-tier models) or compete with
   in-weight knowledge (harming strong-tier models).
3. **Prompt framing is doing significant work.** Recipe-style "state
   relevance and differences" framing helps mid-tier and hurts strong-tier
   on the same content. Vanilla ICL is closer to neutral in both
   directions. Reporting RAG results without controlling for framing
   confounds two effects.
4. **Below a capability floor, retrievals are silent.** Weak models can
   neither use the hint nor be misled by it.

If you're considering deploying T³-style RAG over thinking traces in your
own niche-domain pipeline:
- Test it on the model tier you actually plan to use, not the one cited in
  the paper. Direction of effect can flip across one model size step.
- Audit your top-3 retrievals for sign / parameter / normalization
  conventions that conflict with the target. If they conflict, expect harm
  on strong models and benefit on mid models.
- Ablate the framing. Vanilla ICL on the same retrievals gives a much
  smaller effect than the recipe-style prompt — the gap is how much of
  your "RAG win" is actually a prompting win.
- Don't bother on weak models. They can't use it.

The full data, prompts, scripts, and bootstrap intervals are in the
[thinking-traces-eval](https://github.com/oaustegard/thinking-traces-eval)
repo. Per-iteration writeups in
[`results/`](https://github.com/oaustegard/thinking-traces-eval/tree/main/results)
contain the underlying numbers, mechanism analyses, and caveats — including
known limits on judge dependency, sample size, and selection effects.
None of these caveats overturn the four claims above, but they all bound
how strongly to read them.

---

## Caveats and known limits

- **Single judge** (Sonnet 4.6) on iter-4 onward. Iter-3 calibrated Sonnet
  against Opus on iter-1 outputs; agreement was strong on cardinal scores
  but Sonnet was ~5% softer on near-correct answers. Spot-checks against
  Opus on the most decisive cells before any larger-stakes claim are
  recommended.
- **Sample size**: 8 samples per cell, 4 problems. Per-problem effects on
  `ex_3_24` are decisive; aggregate effects across all 4 problems are
  borderline because `ex_7_28` and the OOD problems dilute. The story is
  driven by `ex_3_24`.
- **Selection effect on iter-4**: the in-distribution problems were chosen
  for headroom (no_rag ~0.6, not ceiling-saturated). Magnitude of harm
  there is partly a headroom-selection artifact, though the mechanism
  replicates on the OOD set in iter-5.
- **Niche scale only**: 7 traces. T³'s reported lifts at multi-thousand-
  trace corpus size are not in scope here. This evaluation is about what
  the pattern transmits at small scale, not whether T³ scales further.
- **One vanilla framing**: iter-7 used one specific n-shot prompt format.
  Other vanilla formats could give different numbers; the framing claim is
  "this specific vanilla framing on these specific raw traces."

---

*Code, data, prompts, scores, and bootstrap intervals at
[github.com/oaustegard/thinking-traces-eval](https://github.com/oaustegard/thinking-traces-eval).
Original T³ paper: Arabzadeh et al. 2026,
[arXiv:2605.03344](https://arxiv.org/abs/2605.03344).*
