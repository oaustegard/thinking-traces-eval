# thinking-traces-eval

A niche-scale evaluation of the **T³** ("Thinking Traces Transfer") pattern from
Arabzadeh et al. 2026, [arXiv:2605.03344](https://arxiv.org/abs/2605.03344).

The T³ paper builds a corpus of Opus-generated thinking traces, transforms each
into a structured cheatsheet, and shows that mid-tier inference models lift
when given retrieved cheatsheets at test time. We replicate the pattern at a
much smaller scale (≤10 traces over a single textbook), across multiple model
tiers and prompt formats, to ask: **does this hold up at niche scale, and what
does the corpus actually transmit?**

Short answer: **it's complicated** — RAG over Opus-authored thinking traces
helps, hurts, or is neutral depending on (a) the inference model's capability,
(b) the prompt framing around the retrievals, and (c) whether the closest
retrieval contains a sign / parameter convention that conflicts with the
target. Full headline reframing in
[`results/HEADLINE_REFRAMED.md`](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/HEADLINE_REFRAMED.md),
the post-iter-7 refinement in [`results/ITER7_FINDINGS.md`](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER7_FINDINGS.md),
and the post-iter-8 corroboration on T³'s actual AIME setup in
[`results/ITER8_FINDINGS.md`](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER8_FINDINGS.md).

**Blog write-up:** [muninn.austegard.com/blog/rag-over-thinking-traces-its-complicated.html](https://muninn.austegard.com/blog/rag-over-thinking-traces-its-complicated.html).

## Domain

Mathematical-physics exercises from Etingof's *Mathematical Ideas and Notions
of Quantum Field Theory* (`references/2409.03117v1.pdf`). Steepest-descent /
Laplace-method integrals, Feynman-diagram counting, effective actions,
characteristic classes — small enough to fit a niche corpus, hard enough that
mid-tier models genuinely struggle, narrow enough that the retrievals can
plausibly carry technique knowledge.

## What was actually run

Eight iterations across 404 inferences total, judged by Sonnet 4.6 (iters
1–7) or by exact-match on integer answers (iter-8). Bootstrap CIs (10000
resamples) on every headline claim — see [`results/bootstrap_cis.txt`](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/bootstrap_cis.txt)
and [`scripts/bootstrap_cis.py`](scripts/bootstrap_cis.py).

| Iter | Scope | Inferences | Finding | Writeup |
|------|-------|-----------:|---------|---------|
| 1 | Pilot, 3 probs × 1 sample × 2 cond, Haiku 4.5 | 6 | Direction unclear; surfaced two RAG failure modes | [PARTIAL_VERDICT.md](results/PARTIAL_VERDICT.md) |
| 2 | Allocation lock, +2 traces | — | Trace corpus to 5 | (commit `a954c1d`) |
| 3 | Eval scaffolding + Sonnet calibration | 48 | Sonnet judge calibrated against Opus | [ITER3_FINDINGS.md](results/ITER3_FINDINGS.md) |
| 4 | In-distribution headroom (`ex_3_24`, `ex_7_28`), 8 samples × 3 cond | 48 | RAG **harms** Haiku 4.5: Δ Struct = −0.21 [−0.31, −0.11] | [ITER4_FINDINGS.md](results/ITER4_FINDINGS.md) |
| 5 | OOD problems (`ood_steepest`, `ood_1loop`) | 48 | Splits by convention-conflict: harm only when retrieval's sign/parameter convention conflicts with target | [ITER5_FINDINGS.md](results/ITER5_FINDINGS.md) |
| 6 | Capability ladder: Gemini 2.5 Flash + Flash Lite, same 4 problems × 3 cond | 192 | **Direction reverses on Flash**: Δ Struct = +0.41 [+0.28, +0.53] on `ex_3_24`. Lite is in noise floor. | [ITER6_FINDINGS.md](results/ITER6_FINDINGS.md) |
| 7 | Vanilla n-shot ablation: same retrievals, no anti-copy framing | 64 | Framing does ~half the work. Removing it lifts Haiku +19pp and drops Flash −20pp on `ex_3_24` | [ITER7_FINDINGS.md](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER7_FINDINGS.md) |
| 8 | Replicate T³'s shipped AIME 25 setup vs Haiku 4.5 (post-publication, after reading T³'s code) | 20 | T³'s shipped prompt is mild ("use as hints"), much closer to my "vanilla" than to my "recipe-RAG" — framing claim is overstated against T³ specifically. AIME 25 (n=10): Haiku no_rag = struct = 6/10. Δ = 0.0pp. | [ITER8_FINDINGS.md](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER8_FINDINGS.md) |
| 9 | Simulated Reasoning Memory ([Wu et al. 2026](https://arxiv.org/abs/2604.01348), Meta FAIR) on Haiku 4.5: subquestion-driven retrieval over the same T³ pool. Iter-4..6 finding turns out to be an independent niche-scale replication of Meta's §5.1 pilot study. | 20 | Haiku no_rag = 6/10, T³-style trajectory RAG = 6/10, Meta-style subquestion RAG (simulated, niche pool, TF-IDF, prepended hints) = 5/10. Smoke can't reproduce Meta's reported +18pp; spells out which components (32M datastore, ReasonIR, mid-thought injection) are likely doing the work. | [ITER9_FINDINGS.md](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER9_FINDINGS.md) |

## Headline (post-iter-9)

The story has four interacting legs, none of which is "T³ is wrong" — and a
post-iter-8/9 acknowledgment that **Meta FAIR got there first** with the
core finding ([Wu et al., arXiv:2604.01348](https://arxiv.org/abs/2604.01348),
April 2026). My iter-4..6 result is a niche-scale replication of their §5.1
pilot study, not a novel observation.

1. **Capability tier matters more than corpus size.** A 7-trace niche corpus
   produces a +41pp lift on `ex_3_24` for Gemini 2.5 Flash and a −29pp drop
   on the same problem for Haiku 4.5 — same retrievals, same prompts, same
   judge. Meta's Figure 2 shows the same direction at scale: instruction-tuned
   models benefit modestly from document RAG; reasoning models gain little
   or even degrade.
2. **The mechanism is convention transmission, not retrieval-as-noise.** When
   a retrieved trace embeds a sign / parameter / normalization choice that
   conflicts with the target (e.g., `ex_3_26`'s `+(1/2) log` vs target's
   `−(1/2) log`), strong-tier models copy the convention and produce wrong
   answers; weaker-tier models with technique gaps benefit from the same hint.
   Same mechanism, opposite outcomes. Meta diagnoses this more generally as
   "factual knowledge mis-aligned with the model's current procedural
   subquestion."
3. **The framing does about half the work — within my pipeline.** My
   "anti-copy" recipe-RAG framing ("use as hints, state relevance and
   differences") is the *source* of about half of the Flash lift on
   `ex_3_24` (recipe − vanilla ≈ +0.20pp on the same retrievals). On Haiku
   the same framing makes the harm worse; vanilla ICL recovers ~19pp on
   `ex_3_24`. **Caveat (iter-8):** T³'s actual shipped inference prompt is
   mild ("use as hints, useful strategies"), much closer to my "vanilla"
   than to my "recipe." The framing claim holds as an internal comparison
   inside this repo's pipeline; it does not impeach T³ as published. So
   "RAG over thinking traces" results are not just about the retrieved
   content — they're about
   prompt structure × content × tier.
4. **Below a capability floor, retrievals are neither help nor harm.** Gemini
   2.5 Flash Lite is at the noise floor across all conditions; it lacks the
   long-context discrimination to use a hint or to be misled by one.

## Layout

```
.
├── extract.py                   — pull problem statements from Etingof PDF
├── data/
│   ├── etingof.txt              — pdftotext of references/2409.03117v1.pdf
│   ├── etingof_problems.jsonl   — 35 extracted problems
│   ├── etingof_tagged.json      — problem-level metadata (techniques, tags)
│   ├── allocation.json          — trace/eval split
│   ├── eval_problems.json       — in-distribution eval problems
│   ├── eval_ood.json            — 2 OOD-constructed eval problems
│   ├── retrievals.json          — gemini-embedding-001 cosine top-3 (iter-3)
│   ├── retrievals_iter4.json    — top-3 retrievals for iter-4
│   ├── retrievals_iter5.json    — top-3 retrievals for iter-5/6/7
│   └── t3paper.txt              — T³ paper text (for prompt extraction)
├── traces/                      — 7 Opus 4.7 thinking traces (the T³ corpus)
├── struct/                      — 7 Haiku 4.5 cheatsheet rewrites (T³ Fig 4)
├── prompts/
│   ├── struct.md                — T³ Fig 4 cheatsheet-rewrite prompt
│   ├── rag_inference.md         — recipe-style RAG prompt (iter-3)
│   ├── raw_inference.md         — recipe-style RAG prompt for raw traces (iter-4+)
│   └── nshot_inference.md       — vanilla 3-shot ICL prompt (iter-7 ablation)
├── scripts/
│   ├── decontaminate.py         — strip Etingof citations from problem text
│   ├── retrieve.py              — embed + top-k cosine retrieval
│   ├── bootstrap_cis.py         — paired bootstrap CI runner
│   ├── run_iter6_gemini.py      — Gemini-2.5-Flash[-Lite] inference driver via CF AI Gateway
│   └── run_iter7_gemini.py      — vanilla n-shot ablation driver
├── answers/                     — iter-1 (partial pilot)
├── answers_iter3/               — iter-3 (Haiku, 6 problems × 4 samples × 2 cond)
├── answers_iter4/               — iter-4 (Haiku, 2 in-distribution probs × 8 × 3 cond)
├── answers_iter5/               — iter-5 (Haiku, 2 OOD probs × 8 × 3 cond)
├── answers_iter6/               — iter-6 (Gemini Flash + Lite, 4 probs × 8 × 3 cond)
├── answers_iter7/               — iter-7 (Haiku + Flash, 4 probs × 8 × 1 cond [nshot])
├── results/                     — per-iteration findings + headline + bootstrap CIs
├── references/                  — original PDFs (Etingof + T³)
├── PIPELINE.md                  — resumable state-machine description
└── state.json                   — pipeline state (last updated iter-1; superseded by iter writeups)
```

## Reproducibility notes

- All Sonnet-4.6 judging runs use the same per-problem rubrics. Per-problem
  scores live in `results/scores_iter*_sonnet.json`.
- Bootstrap CIs (paired, 10000 resamples, percentile method) are computed
  per `scripts/bootstrap_cis.py`. Numbers in writeups match
  `results/bootstrap_cis.txt`.
- Gemini inference goes through the Cloudflare AI Gateway. `run_iter6_gemini.py`
  documents the thinking-budget handling — Flash uses extended thinking by
  default, so the `max_output_tokens` cap covers thinking + visible output
  combined; iter-6 had to bump to 32K to stop visible-output truncation.
- The corpus (`traces/`) is 7 hand-generated Opus 4.7 traces produced inline
  in the originating session — not a scraped dataset. Each is a complete
  worked solution with the model's full chain-of-thought retained.

## Caveats and known limits

- **Single judge** (Sonnet 4.6) for iter-4 onward. Iter-3 calibrated Sonnet
  against Opus on iter-1's 6 outputs — strong agreement on cardinal scores
  but Sonnet was ~5% softer on near-correct answers. Spot-checks against
  Opus on the most decisive cells (Flash-Struct-`ex_3_24`,
  Haiku-Struct-`ex_3_24`) before any external publication are recommended.
- **Sample size**: 8 samples per cell, 4 problems, 3–4 conditions. Most
  per-problem effects are bootstrap-significant; aggregate effects are
  borderline (CIs near zero) and dominated by `ex_3_24`.
- **Selection effect on iter-4**: the in-distribution problem set
  (`ex_3_24`, `ex_7_28`) was chosen for headroom — i.e., problems where
  Haiku no_rag scored ~0.6 rather than ~1.0, because ceiling-saturated
  problems can't show RAG harm. The mechanism (convention contamination)
  is corroborated on iter-5 OOD problems too, but the magnitude on iter-4
  is partly a headroom-selection artifact.
- **Niche scale only**: 7 traces over a single textbook. The T³ paper's
  reported lifts at large scale (multi-thousand traces, multi-domain) are
  not in scope here. This evaluation is about what the pattern transmits
  at small scale, not whether T³ scales.

## What's not in this repo

- The full `references/` PDFs are gitignored (license + size). Pull from
  arXiv:2409.03117 (Etingof) and arXiv:2605.03344 (T³) to reproduce
  problem extraction.
- Raw judge transcripts. Per-cell judge scores are in
  `results/scores_iter*_sonnet.json`; the prompts are inline in the
  iteration writeups.

## Citation context

If you use these findings, please link to the writeups and to the original
T³ paper (Arabzadeh et al. 2026). The findings here **refine, do not
refute**, the T³ pattern: lifts are real and replicable at niche scale,
they're just contingent on tier and framing in ways the original paper
didn't isolate.
