# Partial run notes

## Scope (~10% of issue #2)

| Dimension | Full spec (post-pilot revision) | This partial run |
|---|---|---|
| Trace corpus size | ~30 problems | **3 problems** |
| In-domain eval set | ~30 problems | **3 problems** |
| Off-domain eval set | 30 AIME 2025–2026 | **0** (deferred — no internet to fetch problems; not needed for "promising?" decision) |
| Samples per (problem, condition) | 4 | **1** |
| Conditions | no-RAG vs T³-Struct top-3 | no-RAG vs full-corpus context (k=N) |
| Trace generator | Opus 4.7 ext. thinking via API | Opus 4.7 inline (this conversation) |
| Struct transformer | Haiku 4.5 via API | Haiku 4.5 via subagent |
| Inference target | Haiku 4.5 via API | Haiku 4.5 via subagent (1 sample) |
| Judge | Opus 4.7 + Gemini 3.1 spot-check | Opus 4.7 inline (no Gemini check) |
| Embedding/retrieval | Gemini-embedding-001 + cosine top-3 | **Skipped** (k=3 over N=3 ≡ all) |

**Why this is OK for a pilot.** With N_traces = 3, top-k=3 retrieval ≡ full-corpus context. So "did embedding work?" is not a question we can answer; we're isolating "does Struct context help when given to Haiku?" If even with full-corpus context provided, Struct doesn't lift — no need to go bigger. If it does lift, retrieval is the next experiment.

## Methodological fixes from pilot

The pilot (in-conversation, 2026-05-06, on issue #2) flagged:
1. **Trace-generator and Struct-writer must be different models.** Otherwise the writer leaks adjacent-problem hints into the Struct (pilot's contaminated Wallis Struct mentioned "stationary phase ... oscillatory regime" because the writer was thinking ahead to ex 2.15).
2. **Stratify eval by chapter/technique.** Don't trivially put ex 2.14 trace next to ex 2.15 eval.

What we did:
- ✅ Generator (Opus, inline) and transformer (Haiku, subagent) are now distinct calls. Haiku was given an instruction to *not* introduce techniques absent from the source trace; the resulting Wallis Struct correctly omits "stationary phase."
- ⚠ Eval set still includes ex 2.15 (intra-chapter to ex 2.14 trace). This is partly intentional — we want at least one eval problem where the matched trace technique should help, to test H1. But it also means a positive lift on ex 2.15 isn't fully diagnostic of "transfer" vs "trivial neighborhood help."
- ✅ Off-technique poisoning check via ex 1.2(i) — no trace covers Lagrangian variational mechanics.

## Trace selection (3 traces)

| ID | Topic | Technique |
|---|---|---|
| ex_2_14 | Wallis formula | Steepest descent on Laplace integrals (boundary maximum) |
| ex_3_25 | Labeled trees with 1/4-valent vertices | Tree-level Feynman calculus, dissymmetry theorem, implicit (polynomial) inversion |
| ex_3_26 | 1-loop effective action for cubic potential | 1PI necklace diagrams, dihedral symmetry factors, log-determinant |

## Eval selection (3 problems)

| ID | Match | Expected lift |
|---|---|---|
| ex_2_15 | Steepest descent (intra-chapter to trace 1) | Should lift on a→+∞; a→i∞ requires stationary phase technique not in Wallis trace |
| ex_3_24 | 1-loop / Feynman (chapter 3) | Should lift — closely matches trace 3 (necklaces) and trace 2 (combinatorial enumeration) |
| ex_1_2_i | Variational uniqueness, concave potential | **No matching trace.** Poisoning check: should NOT lift, ideally not hurt |
