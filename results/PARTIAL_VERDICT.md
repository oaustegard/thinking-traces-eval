# Partial verdict: is the full experiment promising enough to run?

**TL;DR — Mixed signal; weakly negative-leaning. Recommend proceeding only with three methodological revisions to issue #2's spec; otherwise the full $120–175 run risks being noise-dominated.**

## What the partial run showed

3 traces (Opus inline, methodologically clean — no contamination), 3 in-domain eval problems (1 sample each), 2 conditions (no-RAG, full-corpus context as proxy for top-3 retrieval).

| Eval | Match | No-RAG | RAG | Δ |
|---|---|---|---|---|
| ex_2_15 (Bessel asymptotic) | matched (same chapter as ex_2_14) | ~0.7 | ~0.3 | −0.4 |
| ex_3_24 (1-loop graphs) | matched (same chapter as ex_3_26) | ~0.4 | ~0.2 | −0.2 |
| ex_1_2_i (variational mechanics) | off-domain (no matching trace) | ~0.8 | ~0.95 | +0.15 |
| Mean | | 0.63 | 0.48 | −0.15 |

**At n=1×3 the direction is negative, but the signal is well within sampling noise.** No statistical conclusion is supported.

## Two RAG failure modes exposed (qualitatively informative)

These are diagnostic findings — they would have been missed by larger-n, wider-eval runs that aggregate to a single number.

### Failure mode 1 — single-template anchoring (ex_2_15, i∞ regime)

The retrieved Wallis Struct describes single-boundary-maximum Laplace expansion. The Bessel a→i∞ regime requires combining **two stationary points** into a cosine. RAG-Haiku anchored on the single-point template and produced a wrong $\propto e^{ib}/\sqrt{b}$ answer instead of the correct $\sqrt{2/(\pi b)}\cos(b-\pi/4)$. **No-RAG-Haiku, with no template, correctly identified both stationary points and combined them.**

This is the inverse of the pilot's earlier observation that no-RAG-Haiku failed on this regime. The difference: pilot's contaminated Struct *helped* by leaking "stationary phase / two stationary points" into the example. The clean Struct (with leakage removed) does the opposite — it actively confines reasoning to one stationary point.

### Failure mode 2 — problem transposition (ex_3_24)

ex_3_26 (in trace corpus) has $S(x)=x^2/2 - gx^3/6$. ex_3_24 (eval) has $S(x)=x^2/2 - g(x^2 + x^3/6)$ — same chapter, same flavor, but a critical $-gx^2$ mass-shift term added. RAG-Haiku silently copied the action from the retrieved example and analyzed *ex_3_26's* problem. No-RAG-Haiku kept the right action (and still botched the calculation, but in a different way).

When retrievals are framework-twin to the target, the model treats them as the problem rather than as hints.

## What this means for the full experiment

These are real failure modes that **scale up adversarially** with corpus size in a niche domain:
- Larger corpus ⇒ more chance of a near-twin retrieval ⇒ stronger transposition risk
- T³ paper's corpus (59K) avoids this because for any single query, retrievals are statistically distant from each other in technique-space
- Niche corpus (~30) over a single textbook ⇒ retrievals concentrate around the target's chapter and are framework-twins by construction

The result raises the possibility that **the niche-scale T³ pattern may actually be harmed by tight topical clustering, even though it benefits from it at frontier scale.** This is the opposite of the issue's H1 prediction.

## Three recommended revisions before scaling up

If the full $120–175 experiment is run as-specified, the partial signal suggests it will likely produce an inconclusive result dominated by anchoring/transposition noise. Three revisions to make the result diagnostic:

1. **Drop "top-k" retrieval; use top-3 always with diversity reranking.** A single near-twin retrieval is the worst case (failure modes above). Forcing 3 diverse retrievals dilutes the anchoring effect. At N=30 corpus, simple MMR (Maximal Marginal Relevance) on cosine + 1-Jaccard suffices.
2. **Add an instruction to the RAG inference prompt: "The retrieved examples may share framework with the main problem but use different setups; treat them as hints about technique, not as templates to copy."** This is a direct guardrail against failure mode 2. Test with vs without this line as an ablation.
3. **Decontaminate eval set by 13-gram Jaccard against the *trace's full text*, not just problem statements.** The pilot's lesson was about Struct leakage; this partial's lesson is about action/setup leakage. ex_3_24 vs ex_3_26 share an action structure that wasn't caught by problem-statement Jaccard.

With these revisions, run the full N=30 experiment as specified in the issue. Without them, the full run risks delivering a number without a story.

## Honest counter-argument

It's also possible the partial result is just n=3 noise and the real experiment will lift cleanly. A defender of the original spec would say:
- ex_2_15 is intra-chapter to ex_2_14 — the pilot already flagged this as bad eval design; a stratified eval set would not include this pair.
- ex_3_24 and ex_3_26 are also intra-chapter — same critique.
- ex_1_2_i is the only well-stratified problem and it showed a small lift.
- So the partial's negative direction reflects a known-bad eval choice, not the underlying pattern.

This is a legitimate read. But the failure modes (anchoring, transposition) are real mechanisms, not artifacts of bad eval design — they will appear at full scale whenever the retrieval lands a framework-twin, which is *more likely* in niche corpora than frontier ones. So even a stratified eval will hit these cases occasionally; the full run should be designed to detect and report them, not paper over them.

## Recommendation

**Conditional go.** Make the three revisions above, then run the full experiment. Budget unchanged (~$120-175). Expect a more informative result regardless of which way the lift goes.

**Hard no-go condition:** if you don't want to refine the methodology, skip the full run. The partial already gives a publishable null/negative diagnostic and the full run as-specified would mostly add a noisier version of the same signal.
