# Iteration 9 — Simulated Reasoning Memory (Wu et al. 2026) on Haiku 4.5

## Why this iteration exists

I had [arXiv:2604.01348](https://arxiv.org/abs/2604.01348) — Meta FAIR's
*Procedural Knowledge at Scale Improves Reasoning* (Wu, Sachan, Yih, Chen,
April 2026) — sitting in `references/` from day 1. **I never opened it**.
Reading it post-publication revealed:

1. **Meta's §5.1 pilot study independently demonstrates the iter-4..6
   headline finding**: standard document/trajectory-level RAG gains
   *little or even degrades* on reasoning models, while it modestly helps
   instruction-tuned models. They show this on three reasoning models
   (DeepSeek-R1-Distill-Llama-8B, OpenThinker3-7B, Qwen3-32B) across AIME
   2024, GPQA-D, LCB. My niche-scale finding is a corroboration, not a
   novel observation.
2. **Meta's proposed fix — Reasoning Memory (RM)** — replaces trajectory
   retrieval with retrieval over (subquestion, subroutine) pairs, where
   the *query* is a model-verbalized subquestion (mid-thought), not the
   original problem. Pre-built datastore: 32M items from 1.2M
   OpenThoughts traces.
3. **They report +18 to +25pp lift over no-retrieval on AIME 2025** with
   RM, on the same models where trajectory RAG hurt by 3–18pp.

iter-9 tests whether RM's directional premise — *subquestion-driven
retrieval over decomposed procedural units, not problem-driven retrieval
over whole trajectories* — recovers a lift on Haiku 4.5 at niche scale,
on the same 10 AIME 2025 problems iter-8 used.

## What I actually ran (and what I couldn't)

**What Meta runs:** 1.2M raw traces → teacher-LLM decomposition into 32M
(subquestion, subroutine) pairs → ReasonIR embedding index → at inference,
the model verbalizes its current subquestion as a query, retrieves top-k
subroutines, and they are *injected mid-thought* via a thought-hijacking
prompt. Multiple retrievals per problem as the model progresses.

**What's feasible in this container:** No GPUs, no vLLM, no ReasonIR, no
1.2M-trace corpus. So this is a *simulation* of the directional change,
not a port of their pipeline:

| Aspect | Meta RM | iter-9 simulation |
|---|---|---|
| Source corpus | OpenThoughts3-1.2M raw traces | T³'s shipped t3_struct cheatsheets, top-10 retrievals per problem |
| Decomposition | (subquestion, subroutine) pairs | Whole T³ Struct cheatsheets (already step-decomposed) |
| Datastore size | 32M items | 100 unique cheatsheets |
| Embedder | ReasonIR | TF-IDF (sklearn, no API needed; same as iter-3..7) |
| Query | Model-verbalized subquestion (mid-thought) | Haiku-verbalized first subquestion (one shot, before solving) |
| Injection | Mid-thought thought-hijacking | Prepended to problem as "procedural hints" |
| Retrievals per problem | k=3 retrieved at multiple thinking steps | k=3, single retrieval |
| Inference model | DeepSeek-R1-Distill-Llama-8B, OpenThinker3-7B, Qwen3-32B | Haiku 4.5 (subagent) |
| Samples | agg@8 | n=1 per problem |

What survives the simplification: **the structural change from
problem-as-query to subquestion-as-query, on the same source pool**. Same
10 AIME 2025 problems as iter-8.

## Pipeline

Two-call protocol per problem:

1. **Subagent call A — verbalize subquestion**
   - Input: AIME problem statement + "What is the FIRST procedural
     subquestion you need to answer to make progress? Output ONE
     concise natural-language query (≤25 words)."
   - Output (10 examples):
     | P# | Haiku's subquestion |
     |---:|---|
     | 0 | How do I express base-b numbers 17_b and 97_b as algebraic expressions in b? |
     | 1 | How do I use the area constraint of quadrilateral DEGF to determine the geometric configuration of triangle ABC? |
     | 2 | How many ways can we partition 9 into three positive integers C > V > S? |
     | 3 | How do I factor the quadratic form 12x² − xy − 6y²? |
     | 4 | What are the divisibility conditions for a number to be divisible by 22? |
     | 5 | What properties must a tangential trapezoid have for an inscribed circle? |
     | 6 | How many possible pairings of the twelve letters are there, and how are they structured? |
     | 7 | What is the geometric locus of points satisfying \|z−4−k\|=\|z−3i−k\|? |
     | 8 | How do I rotate a curve in the plane using rotation transformation matrices? |
     | 9 | How many ways can we fill a 3×9 grid where each row and each 3×3 block contains 1-9? |

2. **TF-IDF retrieval** — query = subquestion, pool = 100 unique
   cheatsheets from `t3_struct_e5base_full.jsonl`'s top-10 ctxs across
   problems 0–9. Top-3 by cosine.

3. **Subagent call B — solve with retrieved subroutines** — Haiku is
   given the AIME problem PLUS the top-3 retrieved cheatsheets framed as
   procedural hints, and produces a `\boxed{N}` answer.

## Per-problem results

| idx | truth | iter-8 no_rag | iter-8 t3_struct | iter-9 RM-sim | retrieval-source-overlap |
|----:|---:|---:|---:|---:|:---|
|  0  |  70 | 70 ✓ | 70 ✓ | 70 ✓ | 1/3 from same problem |
|  1  | 588 | 504 ✗ | 882 ✗ | 300 ✗ | 3/3 from same problem |
|  2  |  16 | 16 ✓ | 16 ✓ | 16 ✓ | 0/3 from same problem |
|  3  | 117 | 117 ✓ | 117 ✓ | 117 ✓ | 1/3 from same problem |
|  4  | 279 | 279 ✓ | 279 ✓ | **2583 ✗** | 3/3 from same problem |
|  5  | 504 | 504 ✓ | 504 ✓ | 504 ✓ | 3/3 from same problem |
|  6  | 821 | 16 ✗ | 7 ✗ | 16 ✗ | 3/3 from same problem |
|  7  |  77 | 77 ✓ | 77 ✓ | 77 ✓ | 2/3 from same problem |
|  8  |  62 | 47 ✗ | 20 ✗ | 48 ✗ | 0/3 from same problem |
|  9  |  81 | 59 ✗ | 47 ✗ | 56 ✗ | 3/3 from same problem |

**Aggregate scores:**
- iter-8 no_rag: **6/10**
- iter-8 t3_struct: **6/10** (Δ = 0.0pp vs no_rag)
- **iter-9 RM-sim: 5/10** (Δ = **−0.1pp** vs no_rag, **−0.1pp** vs t3_struct)

Single discordant pair: P4. Both iter-8 conditions correct (279); iter-9
produced 2583. Subquestion was *"divisibility conditions for a number to
be divisible by 22"* — relevant to the actual problem (AIME 2025 #5
involves divisibility) but the retrieved hints framed the wrong solution
path, and Haiku was misled into a wrong order-of-magnitude answer.

## Honest read on this result

**This is not a refutation of Meta.** The simulation is too
constrained for that. Specifically:

1. **Pool size mismatch (10⁵× smaller).** Meta has 32M (subquestion,
   subroutine) pairs from 1.2M traces. I have 100 cheatsheets. Meta's
   retrieval has the procedural diversity to find a *truly aligned*
   subroutine for any subquestion; mine retrieves the closest of 100
   surface-keyword matches. For 5 of the 10 problems, "top-3 retrieved"
   was just "the same problem's own cheatsheets" — not different
   procedural priors than iter-8 saw.
2. **Decomposition granularity mismatch.** T³ Struct cheatsheets are
   *approach-level* decompositions (one cheatsheet per approach, ~7
   steps each). RM operates at *subquestion-level* — each cheatsheet
   step would be its own retrievable unit. I did not split T³
   cheatsheets into individual steps because a single step out of context
   reads as cryptic ("Step 4 — Test 3-Digit Numbers"); meaningful only
   alongside the rest. With the right teacher LLM I could regenerate
   subroutines in Meta's style, but that's a different experiment.
3. **TF-IDF is bad for procedural matching.** ReasonIR is trained on
   reasoning-aligned retrieval; TF-IDF rewards surface-keyword overlap.
   On P0, "express base-b numbers as algebraic expressions" returned a
   Magic Square cheatsheet (cosine 0.099) because both texts mention
   algebra. The actual technique (linear-combination divisibility)
   wasn't in the top-3.
4. **Single subquestion, not progressive retrieval.** Meta's protocol
   re-retrieves as the model progresses through reasoning. I retrieve
   once at the start. This forecloses the progressive-grounding
   advantage that's a core part of their architecture.
5. **n = 10 × 1 sample.** Bootstrap CI is meaningless at this scale.

## What this iteration *does* tell us

Within the constraints, **subquestion-driven retrieval over a niche
trace pool with TF-IDF and prepended hints does not lift Haiku 4.5
above the trajectory-RAG or no-RAG baselines on AIME 2025 #1–10**.
Magnitude is one discordant pair (a wash). The structural change
alone (query construction) does not appear to be enough at this scale.

The *implication* — which iter-9 cannot test — is that Meta's reported
+18 to +25pp lift comes from the combination of (a) datastore scale
+ diversity, (b) ReasonIR-trained retrieval semantics, and (c)
mid-thought re-injection across multiple subquestions. Stripping any
of those, on this slice, gives back ~0pp.

Restated: **the iter-4..6 headline ("trajectory-level trace RAG hurts
strong reasoning models on in-pretraining domains") replicates Meta's
§5.1 pilot study at niche scale.** Iter-9 is consistent with the
*difficulty* of recovering Meta's positive direction with anything less
than their full pipeline.

## What this changes about the published blog post

The blog post needs to:

1. **Cite Meta** prominently and acknowledge their pilot study as the
   prior result.
2. **Demote my iter-4..6 finding** from "novel observation" to
   "independent niche-scale replication of [Meta §5.1]."
3. **Briefly summarize iter-9** as a smoke test of Meta's *fix*,
   noting the simulation cannot reproduce their +18pp lift but
   identifying the components (scale, retriever, injection protocol)
   most likely to be doing the work in their setup.

## Files

- `scripts/run_iter9_aime.py` — pool builder, TF-IDF retrieval, prompt
  assembly. Three subcommands: `build`, `subq_prompts`, `retrieve`.
- `answers_iter9/pool.json` — 100 unique cheatsheets pooled from t3_struct
  retrievals for problems 0–9.
- `answers_iter9/subq_prompts/subq_NN.txt` — Step-A prompts (10).
- `answers_iter9/subqs/subq_NN.txt` — Haiku's verbalized subquestions
  (10).
- `answers_iter9/retrieval_log.json` — top-3 retrieval results per
  problem (cosine sim, source-problem overlap).
- `answers_iter9/solve_prompts/solve_NN.txt` — Step-B prompts with
  retrieved hints prepended (10).
- `answers_iter9/results_v3/solve_NN.md` — Haiku's full reasoning + boxed
  answer per problem (10).
- `answers_iter9/scored_v3.json` — per-problem comparison: truth,
  iter-8 no_rag, iter-8 t3_struct, iter-9 RM-sim.
