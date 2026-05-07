# Iteration 8 — Replicating T³'s actual setup against Haiku 4.5

## Why

Iters 1–7 used a niche custom corpus (7 Opus 4.7 traces over Etingof QFT). The
iter-7 blog post claimed framing-vs-content effects against T³. Reading T³'s
actual source code (https://github.com/Narabzad/t3) afterwards revealed three
material gaps in my replication:

1. **T³'s shipped inference prompt is mild.** From `eval/tasks/aime/utils.py`:

   > "Considering the following examples as hints, try to answer the question.
   >  Use any useful hints and strategies from the retrieved examples.
   >  Example 1: ...  Example 2: ...  Example 3: ...
   >  main problem: ...  Present the answer in LaTeX format: \boxed{Your answer}"

   That's it. NO "state relevance and differences first," NO anti-copy guardrail,
   NO recipe-style scaffold. Iter-7's "vanilla nshot" condition is closer to T³'s
   actual prompt than my "struct/raw" recipe-RAG conditions were.

2. **T³ evaluates on AIME 2025/26, GPQA-Diamond, LCB v4** with auto-scoring
   (exact-match on integer answers, no LLM judge). Iter-3..7 used custom Etingof
   problems with Sonnet judging.

3. **T³'s traces are from open models** (Gemini-2-thinking, QwQ-32B,
   GPT-OSS-120B), not Opus. Iter-3..7 used 7 hand-curated Opus 4.7 traces.

Iter-8 fixes all three: re-runs T³'s exact AIME 2025 setup against Haiku 4.5.

## Setup

- **Problems**: AIME 2025 indices 0–9 (the first 10 AIME 25 problems from T³'s
  shipped queries file `aime_2025_2026_queries.jsonl`). Smoke scope.
- **Conditions**: `no_rag` (T³'s default `QUERY_TEMPLATE = '{Question}'`) and
  `struct` (T³'s `t3_struct_e5base_full` retrieved-results JSONL,
  top-3 passages, prepended via T³'s exact prompt template — see
  `scripts/run_iter8_aime.py`).
- **Model**: Haiku 4.5 invoked as a Claude Code subagent (no external API).
- **Samples**: 1 per cell. Smoke run.
- **Scoring**: exact-match on integer extracted from the last `\boxed{...}`.

Total: 20 inferences (10 problems × 2 conditions × 1 sample).

## Architecture detour

First attempt (batched 30 problems per subagent) produced 30/30 correct in
30 seconds on the contaminated batch (truth field leaked) and ≈5/30 on the
clean v2 batch (just-plausible-integers when Haiku had no shortcut to truth).
The "write JSON for 30 problems" instruction lets Haiku optimize for "produce
plausible integers" rather than actually solving. Pivoted to one subagent per
(problem × condition); each writes its full reasoning to an .md file then
reports `ANSWER: N`. Reasoning depth verified — see
`answers_iter8/results_v3/*.md`.

## Result

Same 10 problems, both conditions:

| idx | truth | no_rag | struct | nr ✓ | st ✓ |
|----:|------:|-------:|-------:|:-----|:-----|
|  0  |    70 |     70 |     70 |  ✓   |  ✓   |
|  1  |   588 |    504 |    882 |  ✗   |  ✗   |
|  2  |    16 |     16 |     16 |  ✓   |  ✓   |
|  3  |   117 |    117 |    117 |  ✓   |  ✓   |
|  4  |   279 |    279 |    279 |  ✓   |  ✓   |
|  5  |   504 |    504 |    504 |  ✓   |  ✓   |
|  6  |   821 |     16 |      7 |  ✗   |  ✗   |
|  7  |    77 |     77 |     77 |  ✓   |  ✓   |
|  8  |    62 |     47 |     20 |  ✗   |  ✗   |
|  9  |    81 |     59 |     47 |  ✗   |  ✗   |

**no_rag:  6/10 = 0.60**
**struct:  6/10 = 0.60**
**Δ = 0.00**

Discordant pairs: 0 no_rag-only-correct, 0 struct-only-correct.

Same 6 problems right under both conditions. Same 4 problems wrong. On the
4 wrong problems, struct produced *different* wrong integers than no_rag in
3 cases (P1, P6, P8) — so the retrieved hints did move Haiku's answer, just
never toward correctness.

## Comparison to T³ paper headline

T³ reports on AIME 2025–2026 (60 problems, agg@8):
- Gemini 2.5 Flash: **+50.1pp** with t3_struct
- GPT-OSS-120B: **+8.6pp**
- GPT-5 (2025-08-07): **+5.8pp**

iter-8 Haiku 4.5 on AIME 2025 problems 0–9, 1 sample each: **0.0pp**.

Haiku 4.5 sits roughly where GPT-5 sat in their results (the strong-tier
inference end). GPT-5 lifted +5.8pp; Haiku 4.5 lifts 0pp on this slice.
Consistent with the iter-4..7 finding that strong-tier models on
in-pretraining domains do not measurably benefit from T³-style RAG.

## Caveats

This is a SMOKE run. Confidence bounds are weak.

- **n=10 problems × 1 sample.** McNemar's test would need ≥1 discordant pair
  to even compute a p-value; we have 0. Cannot reject a small-magnitude lift
  from this data alone.
- **AIME 25 problems 0–9, not the full set.** The first 10 AIME problems are
  generally easier than 11–30. Haiku is at 60% baseline on this slice; the
  back-row problems would have more headroom for retrieval to help (or hurt).
- **No multi-sample variance.** T³ aggregates over 8 samples per problem
  (agg@8). My single-sample-per-cell smoke can't capture sampling variance.
- **Single tier (Haiku 4.5).** Cross-tier comparison requires running the
  same setup against Sonnet 4.6 or Opus 4.7.
- **Subagent surface, not direct API.** Haiku as subagent may behave slightly
  differently from Haiku via API (system prompt, default sampling, tool
  budget). Effect is unmeasured but bounded — the single-problem subagent
  pilot reproduced the canonical AIME 25 #1 answer (70) with full reasoning,
  matching expectations.

## What this changes about the iter-7 blog post

The post overstates the "framing does about half the work" claim *against
T³ specifically*. T³'s shipped prompt is closer to my iter-7 vanilla-nshot
than to my recipe-RAG. The framing-effect finding holds as an internal
comparison within my own pipeline; it does not directly impeach T³'s
reported results, which use a milder framing.

The "RAG over thinking traces hurts strong models" claim from iters 4–6 is
now *corroborated* on T³'s actual setup (AIME, exact-match scoring), but
the magnitude on this 10-problem smoke is "no measurable lift" rather than
"measurable harm." The finding "strong-tier models gain less from
trace-RAG than mid-tier models" survives; "strong-tier models are *harmed*"
needs more samples on harder problems before claiming generality.

## Scope to expand if results justify

The expensive next step is the full T³ AIME 25/26 run: 60 problems × 4
samples × 2 conditions = 480 single-problem subagent calls (~2-3 hours
of background-agent time at this rate). Per-problem CIs and a real
McNemar would settle the magnitude question. Not warranted from a 0/0
discordant smoke — would only be warranted if a richer signal emerged.

## Files

- `scripts/run_iter8_aime.py` — prompt builder ported from T³'s
  `eval/tasks/aime/utils.py:doc_to_text_with_retrieval`.
- `data/t3_aime26/` — `queries.jsonl` (60 AIME 25/26 problems) and
  `struct_retrievals.jsonl` (top-3 t3_struct retrievals per problem)
  fetched from T³'s git-LFS via media URLs.
- `answers_iter8/prompts_v3/{cond}_{idx}.txt` — 60 individual prompts
  (10 problems × 2 conditions × 3 unused; see scope note).
- `answers_iter8/results_v3/{cond}_{idx}.md` — Haiku's full reasoning per
  problem, ending in `\boxed{N}`.
- `answers_iter8/scored_v3.json` — extracted answers and exact-match scores.
- `answers_iter8/v2_truth.json` — held-out truth table (not visible to
  subagents).
