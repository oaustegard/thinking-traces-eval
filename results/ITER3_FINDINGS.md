# Iteration 3 findings

**Setup.** 6 traces (4 from earlier iterations + 2 new), 6 Structs, 6 eval problems, 2 conditions × 4 samples = 48 inference outputs. MMR top-3 retrieval (λ=0.5), anti-copy RAG inference prompt, full-trace 13-gram decontamination. Two judges: Opus 4.7 inline + Sonnet 4.6 subagent.

## Headline

| Judge   | no-RAG mean | RAG mean | Δ      |
|---------|-------------|----------|--------|
| Opus    | 0.767       | 0.778    | +0.012 |
| Sonnet  | 0.846       | 0.835    | -0.010 |

**Both judges put |Δ| ≈ 0.01 overall**, with judges *disagreeing on the sign*. At n=24 per condition with rubric-based continuous scoring, this is well inside the noise floor — there is no measurable RAG effect at this niche corpus scale.

For comparison, iter-0 (n=3, contaminated pipeline): Δ = -0.15. The methodological cleanup brought us back to ~zero.

## Per-problem breakdown

| Problem    | Opus Δ | Sonnet Δ | Agree | Notes                                                                                          |
|------------|--------|----------|-------|------------------------------------------------------------------------------------------------|
| ex_2_15    | 0.00   | 0.00     | ✓     | Both conditions perfect (1.0/1.0). Reversal from iter-0: clean prompts plus n=4 found the right answer everywhere. |
| ex_3_24    | +0.03  | -0.10    | ✗     | All 4 RAG samples explicitly noted action difference and refused to transpose. Remaining errors are Taylor-expansion slips (not the iter-0 transposition mode). |
| ex_5_17    | -0.05  | -0.10    | ✓     | Modest no-RAG win. Multi-part problem; coverage of (a)/(b) is uneven.                          |
| ex_5_19    | -0.08  | 0.00     | ~     | Both got χ = -1/42. Disagreement on (i)/(iii) coverage.                                         |
| ex_7_28    | +0.15  | +0.14    | ✓     | RAG wins despite no matched trace (ex_7_27 not yet generated). Retrieved examples acted as structured-reasoning template, not technique transfer. Half of no-RAG samples got dimensionally wrong G_1 (g/4m³ vs correct g/4m²). |
| ex_1_2_i   | +0.03  | 0.00     | ~     | Off-domain. All 8 outputs reach correct conclusion. H2 (no poisoning) supported.                |

## What changed vs iter-0

The dominant iter-0 RAG failure mode was **problem-setup transposition**: RAG-Haiku silently substituted the action from ex_3_26 (its retrieval) for the actual ex_3_24 problem (different action). Iter-3 shows **zero transposition events across 24 RAG samples**. All 4 RAG ex_3_24 samples opened with explicit identification of the action difference. Anti-copy guardrail in `prompts/rag_inference.md` worked as intended.

The other iter-0 failure mode — **single-template anchoring** — also disappeared. Iter-0 RAG ex_2_15 collapsed the i∞ regime to one stationary point because the Wallis Struct described one. Iter-3 RAG ex_2_15 correctly identifies two stationary points across all 4 samples. MMR and the anti-copy instruction together broke the anchoring.

## What did *not* change

The hoped-for **technique transfer** lift (T³ paper's H1) did not appear. RAG and no-RAG perform the same on average. Per-problem effects are small and not consistent across judges.

This is consistent with the iter-0 verdict's contamination-flip reading: the pilot's apparent +lift was contamination-driven (Opus-as-writer leaking adjacent-problem hints), not generalization-driven. Cleaning the pipeline removed both the harm AND the contamination "lift," leaving genuine signal at zero.

## Hypothesis tests

- **H1 (in-domain ≥10pp lift, paired bootstrap p<0.05)**: **falsified.** Observed |Δ| ≈ 0.01, two orders of magnitude smaller than predicted.
- **H2 (off-domain no-harm, |Δ| < 5pp)**: **supported.** ex_1_2_i Δ ≈ 0.

## Inter-judge agreement

4 of 6 problems agree on direction (ex_2_15, ex_5_17, ex_7_28, ex_1_2_i). 1 strong disagreement (ex_3_24). 1 weak disagreement (ex_5_19). The disagreements concentrate on the multi-part problems where coverage of sub-rubrics requires more interpretation. Net inter-judge κ on direction: moderate.

Sonnet runs ~0.08 higher overall — a leniency offset, not a directional bias.

## What scaling to 12 traces would test

The most diagnostic prediction: **does ex_7_28's RAG win survive once ex_7_27 (the actual matched trace) enters the corpus?** Two outcomes:
- **If yes**, then RAG benefit is "having any structured reasoning context," not "matched technique transfer" — interesting but boring.
- **If no** (or larger lift appears), then the absent-but-vaguely-related-retrievals at this iteration were *worse* than the matched ones would be, and the no-effect aggregate would shift positive.

Other 5 problems should show little change since their retrievals at 6 traces already include the matched trace. Iteration 4 has small expected effect on the aggregate but high diagnostic value on the mechanism.

## Recommendation

Continue to iteration 4: generate ex_7_27, ex_4_9, ex_4_15, ex_2_12 traces (toward target 10–12), Struct them, re-run inference on the 6 eval problems, compare. If aggregate stays at |Δ| < 0.05, declare the experiment closed with a "T³ niche-scale = no effect" result. That's a clean publishable finding given the failure-mode diagnostics already documented.

Budget: another 8 subagent inference calls + judging is the same cost as iter-3 (~1 hour wall time, modest token use against subscription).
