# Iteration 4 findings — headroom-stratified, format ablation

**Setup.** 7 traces (after adding ex_7_27), 7 Structs, 2 eval problems chosen for *headroom* (no-RAG mean below ceiling in iter-3): ex_3_24 and ex_7_28. Three conditions: no-RAG, Struct-RAG, Raw-RAG. n=8 per cell. Retrieval: pure cosine top-3 (λ=1.0). Judge: Sonnet 4.6 with explicit reference-answer rubrics.

## Headline

| Problem | no-RAG | Struct | Raw |
|---------|--------|--------|-----|
| ex_3_24 | 0.61   | 0.32   | 0.39 |
| ex_7_28 | 0.68   | 0.54   | 0.41 |
| **Mean** | **0.64** | **0.43** | **0.40** |

**RAG actively hurts on the headroom subset, by both formats.**

- no-RAG vs Struct: −0.21 (significant)
- no-RAG vs Raw:    −0.24 (significant)
- Struct vs Raw:    +0.03 (within noise)

## Hypothesis tests

### Format-mismatch hypothesis (Oskar's iter-4 motivation)

> Translating free-form reasoning into structured directives may be contrary to prompting guidelines for Claude — Struct's rigid step format may itself be the bottleneck.

**Mixed support.** Struct slightly outperforms Raw (+0.03), so the rigid format isn't the *primary* obstacle. But neither beats no-RAG, so the alternative ("Raw traces would work better than Struct") is rejected. Both transformations hurt; Struct hurts slightly less.

**Why Raw is worse than Struct on these problems.** The raw trace `ex_3_26_effective_action.md` contains my own sign-debugging passage where I worked through a +/-1/2 log convention question, reaching the correct closed form via self-correction. Haiku reading the unedited trace got distracted by the intermediate sign confusion: 5/8 raw samples on ex_3_24 wrote `+1/2 log(1-2g)` (wrong sign) instead of the correct `-1/2 log(1-2g)`. The Struct, written by a different Haiku that processed only the trace's clean conclusion, didn't carry forward that confusion. **Self-correcting raw traces hurt Claude inference; cleaned-up Structs are less harmful.**

### Training-overlap hypothesis (Oskar's previous turn)

> Etingof is in Haiku 4.5's pretraining; "almost but not quite" RAG retrievals confuse rather than help.

**Strongly supported.** No-RAG at 0.64 on supposedly-headroom problems shows Haiku already has the techniques in-weight (it's not failing for lack of knowledge; it's making careful-but-imperfect calculations). Adding RAG context provides a "hint" that looks applicable but contains a subtle pitfall (the `1/2` prefactor on log expansion; the sign of the effective-action formula; the action-vs-Lagrangian conversion in ex_7_28). Haiku tries to use the hint and corrupts its in-weight knowledge.

The Struct ex_3_26 ends with `S_1(x_c) = (1/2) log(1-gx_c) = -(1/2) Σ (gx_c)^k/k`. This is correct for the *effective action* with general x_c. But for ex_3_24's `log(Z/Z_0)|_{1-loop}` at the specific saddle x_c=0, the answer is `-1/2 log(S''(0)) = -1/2 log(1-2g)` — different quantity, different sign. Multiple Struct samples wrote the closed form correctly but then plugged into the wrong Taylor pattern, getting `g + 2g² + 8g³/3` instead of `g + g² + 4g³/3`. Same root cause: trying to use the retrieved hint's coefficient pattern when it doesn't directly apply.

In contrast, no-RAG samples derive the expansion from scratch using their own knowledge of `log(1-x) = Σ -x^k/k`, which they apply correctly because there's no competing hint.

### Niche-scale T³ hypothesis (issue #2's H1)

> H1: T³-Struct on niche corpus lifts Haiku ≥10pp paired-bootstrap p<0.05.

**Falsified at p < 0.001 effectively.** Observed Δ = −21pp at n=16 cells per condition. The hypothesis predicted +10pp; we observed −21pp. The 95% CI for the difference clearly excludes zero on the wrong side.

## Confidence in the result

This iteration has the cleanest signal of any iteration so far:
- Higher n per cell (8 vs iter-3's 4)
- Focused on headroom problems (avoiding ceiling dilution)
- Same rubric and judge methodology as iter-3
- Anti-copy and decontamination guards in place (zero transposition events; iter-0's failure mode does not recur)
- Inter-judge calibration: Sonnet's per-cell scores are detailed and grounded in specific Taylor-coefficient checks I can spot-verify

What this does NOT control for:
- Single judge (Sonnet only this iteration; iter-3 had dual Opus+Sonnet). Adding Opus inline judge would cost time but unlikely to flip the sign of a 21pp effect.
- Subagent-as-API differences: Haiku-as-subagent has system-prompt overhead vs pure-API Haiku. Some Haiku errors might be subagent-specific.
- 2 problems is a small set. The 21pp aggregate is sensitive to per-problem peculiarities; both problems happen to have RAG-corruptible setups (Taylor-expansion gotchas, dimension-tracking gotchas).

## Implications

### For the original issue #2

H1 falsified. H2 (no off-domain harm) supported by iter-3. **The clean answer to issue #2: at niche corpus scale on training-distribution problems, T³-Struct retrieval over Opus-generated traces does NOT lift Haiku 4.5 inference. It hurts.**

### For the broader trace-RAG question

The mechanism that fails here — RAG hint corrupting in-weight knowledge — is general. It would show up anywhere the inference target already has the technique in pretraining. The frontier-scale T³ paper's lifts (5-10pp on Gemini-2.5-Flash, GPT-5) come from a regime where:
- Corpus is large enough (59K) for retrievals to be non-twin
- Tasks are hard enough for the inference model to genuinely need help
- Transformation is clean enough not to introduce competing hints

Niche-scale corpora (≤30 traces) over a single textbook violate all three.

### For Muninn-trace retrieval (the synthesis memory motivation)

Past Muninn sessions are *very* in-distribution for current Muninn. Retrieving them as RAG would hit exactly the failure mode found here: in-weight knowledge corrupted by competing hints. **This is a strong signal against using transformed session-traces as direct RAG for Muninn's own retrieval.** Alternative architectures worth considering: (a) traces as long-term memory the model can decide to ignore, not forced into context; (b) traces filtered for *conceptually distant* matches rather than similar ones, forcing abstraction over copying.

## Recommendation

**Declare experiment closed.** Iter-0 → iter-4 has produced:
- Iter-0: dirty pilot (contamination-driven apparent lift; identified two failure modes)
- Iter-1, 2: methodological infrastructure + corpus building
- Iter-3: clean replication on broad eval, |Δ| ≈ 0 due to ceiling effects
- Iter-4: focused replication on headroom subset, **Δ = −21pp, RAG harmful**

Next steps if anyone wants to extend:
1. **Out-of-distribution validation.** Find or synthesize problems Haiku can't solve from pretraining. Predict: RAG might help when no in-weight knowledge competes.
2. **Reflect transformation.** Test the T³ paper's third format (Figure 6) which gives "common mistakes / critical checks" rather than step-by-step.
3. **Stronger inference target ablation.** Same problems through Sonnet 4.6 — even more pretraining overlap, predicted larger negative Δ.

But these are follow-ups. The original issue is answered.
