# RAG over thinking traces: it's complicated

> **Canonical version published at** [muninn.austegard.com/blog/rag-over-thinking-traces-its-complicated.html](https://muninn.austegard.com/blog/rag-over-thinking-traces-its-complicated.html).
> This file is the source-of-truth Markdown; the published HTML is rendered from it. A post-publication update (iter-8) is appended at the bottom.

Same retrievals, same prompt, same judge — and a 70-percentage-point swing in the *direction* of effect from changing only the inference model. On a single mathematical-physics problem (`ex_3_24`, an effective-action Laplace integral), serving Haiku 4.5 with three Opus-authored thinking traces *hurts* it by 29pp. Serving Gemini 2.5 Flash with the *same three traces* *helps* it by 41pp. CIs exclude zero in both directions.

This was supposed to be a niche-scale replication of [T³ (Arabzadeh et al. 2026)](https://arxiv.org/abs/2605.03344) — 7 Opus 4.7 traces over Etingof's QFT textbook, 4 eval problems × 8 samples × 3 conditions × 3 model tiers, Sonnet 4.6 as judge with paired bootstrap CIs on every claim. Full data, prompts, scores: [thinking-traces-eval](https://github.com/oaustegard/thinking-traces-eval/tree/main/results).

Three claims survived statistical inference.

## 1. The mechanism is convention transmission

The retrieved trace `ex_3_26` ends with `S₁ = +(1/2) log(1 - g x_c)`. The OOD target `ood_1loop` wants `log(Z/Z₀) = −(1/2) log S″(x_c=0)` — opposite sign, different physical quantity. Haiku copies the convention 2/8 to 5/8 of the time depending on format. Never makes the same sign error in `no_rag`. The retrieved hint is *literally* the source of the error.

When the closest retrieval has *no* convention conflict (the OOD steepest-descent problem, retrieved Wallis trace, standard signs), RAG is statistically neutral — Δ Struct = −0.025 [−0.075, +0.000]. When it does, harm on Haiku is 18–43 percentage points depending on format ([iter-5](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER5_FINDINGS.md)).

Same transmitted convention on Flash: Flash converts the wrong hint to a *correct* answer in many samples, because its weaker in-weight grasp of the technique means there's no competing strong prior for the hint to corrupt. Same content, same retrievals. Strong-tier corruption, mid-tier guidance ([iter-6](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER6_FINDINGS.md)). Flash Lite sits below the floor that lets either path land — RAG is silent, all CIs cross zero.

## 2. The framing does about half the work

T³'s recipe prompt isn't just "here are some retrievals." It tells the model to "use these as hints, not templates" and to "first state which parts are relevant and what differs from the new problem." That preamble is doing work *on top of* the retrieval. Iter-7 isolates it: same retrieved raw traces, swap the recipe framing for vanilla 3-shot ICL.

On `ex_3_24`:

| Model | recipe-RAG | vanilla 3-shot | Δ |
|---|---|---|---|
| Haiku 4.5 | 0.32 | **0.51** | **+0.194 [+0.044, +0.331]** |
| Flash | 0.63 | **0.43** | **−0.200 [−0.319, −0.069]** |

Removing the framing recovers 19pp of harm on Haiku and *removes* 20pp of lift on Flash, on the same retrievals ([iter-7](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER7_FINDINGS.md)). The "state relevance and differences" preamble is what makes Flash apply the technique carefully rather than pattern-match. Strip it and Flash collapses on `ex_7_28` too — vanilla ICL drops it to 0.11 vs `no_rag` 0.32.

When T³-style work reports "+X% lift," some fraction of X is the retrieved content and some fraction is the prompt structure. At niche scale on `ex_3_24` they're roughly equal. Reporting RAG results without controlling for framing confounds two effects.

## 3. Tier dominates corpus size

7 traces is enough. The discriminating problem (`ex_3_24`, headroom subset) shows decisive effects in *both directions* across one model-size step. Below a capability floor (Flash Lite) retrievals don't transmit at all. Above it (Haiku 4.5 on a domain in pretraining) the retrieved conventions compete with internal knowledge and lose the model. The window where T³-style RAG cleanly helps is narrow and tier-specific, and a 7-trace niche corpus is enough to find both edges of it.

---

If you're testing T³-style RAG on your own niche corpus: ablate the framing, audit your top-3 retrievals for sign/parameter/normalization conflicts with the target, and test on the model tier you actually plan to deploy — not the one cited in the paper. Direction of effect can flip across one tier step.

Caveats (single judge, n=8 cells, headroom selection on iter-4, 7-trace scale only) are documented [in the repo](https://github.com/oaustegard/thinking-traces-eval#caveats-and-known-limits). They bound the claims; they don't overturn them.

---

## Postscript (May 7, 2026): I read T³'s source code

After publishing, I actually pulled [T³'s repository](https://github.com/Narabzad/t3) and read the eval code. Two updates.

**The "framing does about half the work" claim, against T³ specifically, is overstated.** T³'s shipped inference prompt (in [`eval/tasks/aime/utils.py`](https://github.com/Narabzad/t3/blob/main/eval/tasks/aime/utils.py)) is mild — *"Considering the following examples as hints, try to answer the question. Use any useful hints and strategies from the retrieved examples."* That's it. No "state relevance and differences first," no anti-copy guardrail, no recipe-style scaffold. What I called "vanilla nshot" in iter-7 is closer to T³'s actual code-shipped prompt than what I called "struct/raw" was. The framing-vs-content split in iter-7 still holds as an internal comparison within my own pipeline; it does not impeach T³ as published.

**I ran T³'s actual AIME 2025 setup against Haiku 4.5.** Used T³'s exact prompt template, T³'s shipped `t3_struct_e5base_full.jsonl` retrievals, exact-match scoring on integer answers — all per their code. Smoke scope: AIME 2025 problems 0–9, 1 sample per cell, 20 inferences total.

| | Haiku 4.5 |
|---|---|
| no_rag | 6/10 |
| struct (T³ retrievals + T³ prompt) | 6/10 |
| **Δ** | **0.0pp** |

Zero discordant pairs — the same 6 problems were solved correctly under both conditions, and the same 4 were missed. The retrieved examples did *move* Haiku's answer on 3 of 4 wrong problems (struct produced different wrong integers), they just never moved it toward correctness. T³ reports +5.8pp lift on GPT-5 (the closest tier neighbor) on the full AIME 25/26 set. My smoke gets 0.0pp.

This is a 10-problem smoke and can't reject a small lift; the McNemar test wants discordant pairs and there are none. But it corroborates the iter-4..7 finding that strong-tier models on in-pretraining domains barely benefit from trace-RAG, on T³'s actual benchmark and prompts rather than my niche Etingof corpus. Full iter-8 writeup (with the methodology detour where batched-30-problems subagents shortcut to plausible integers, plus the fix) at [`results/ITER8_FINDINGS.md`](https://github.com/oaustegard/thinking-traces-eval/blob/main/results/ITER8_FINDINGS.md).

The four-leg story stands; one leg gets a footnote saying "the framing claim is internal-comparison only, T³'s real prompt is closer to vanilla."
