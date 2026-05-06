# thinking-traces-eval

Does RAG over Opus-generated thinking traces from a niche-domain reference text improve Haiku 4.5 reasoning? Niche-scale test of the T³ pattern (Arabzadeh et al. 2026, arXiv:2605.03344).

## Status: partial pilot complete (~10% of issue #2 spec)

Results, analysis, and a recommended go/no-go for the full run are in `results/`:

- `results/PARTIAL_NOTES.md` — scope of the partial vs the full spec; methodological fixes applied from the in-conversation pilot on issue #2.
- `results/JUDGE.md` — Opus-judge scoring of the 6 (3 problem × 2 condition) Haiku outputs, with diagnostic breakdowns per sub-judgment.
- `results/PARTIAL_VERDICT.md` — verdict and three recommended methodological revisions before scaling to full N=30.

**Headline.** At n=1 sample × 3 problems, RAG (full-corpus context) shows no in-domain lift over no-RAG; direction trends slightly negative on matched problems and slightly positive on the off-domain poisoning-check problem. Most informative finding: two distinct RAG failure modes were exposed that **scale adversarially with niche-corpus tightness** — single-template anchoring (ex_2_15) and problem-setup transposition (ex_3_24). These suggest the full $120–175 experiment as-spec'd risks delivering an inconclusive number; with three small methodological revisions (diversity-reranked retrieval, anti-copying prompt instruction, more aggressive decontamination) it would deliver a diagnostic result.

## Layout

```
.
├── extract.py              — pull Exercise statements from Etingof PDF dump
├── data/
│   ├── etingof.txt         — pdftotext output of references/2409.03117v1.pdf (gitignored if too large)
│   ├── etingof_problems.jsonl  — 35 extracted problems
│   ├── eval_problems.json  — 3 held-out eval problems with rubrics
│   └── t3paper.txt         — pdftotext of Arabzadeh et al. for prompt extraction
├── traces/                 — 3 Opus 4.7 traces (generator: this conversation, Opus extended thinking)
├── struct/                 — 3 Haiku 4.5 T³-Struct rewrites (transformer: separate Haiku subagent)
├── answers/
│   ├── no_rag/             — Haiku solutions, baseline condition (3 files)
│   └── rag/                — Haiku solutions, full-corpus context condition (3 files)
├── references/             — original PDFs (Etingof + two T³/Wu papers)
└── results/                — analysis writeup
```

## What was actually run

| Pipeline step | Spec | Partial implementation |
|---|---|---|
| Extract problems | regex from Etingof markdown | ✅ 35 problems via `extract.py` |
| Generate traces | Opus 4.7 ext-thinking, 30 problems | ✅ 3 problems, generated inline by this Opus 4.7 conversation |
| T³-Struct transform | Haiku 4.5, paper Fig 4 prompt | ✅ Haiku subagent applied Fig 4 prompt verbatim, with explicit anti-leakage instruction |
| Embed + retrieve | gemini-embedding-001 + cosine top-3 | Skipped: at N=3 corpus, top-3 ≡ all; embeddings would not differentiate |
| Inference (no-RAG) | Haiku, 30 problems × 4 samples | ✅ 3 problems × 1 sample, Haiku subagent |
| Inference (RAG) | Haiku, top-3 retrievals as context | ✅ 3 problems × 1 sample, all 3 Structs as context |
| Judge | Opus + Gemini 3.1 spot-check | ✅ Opus inline; Gemini calibration skipped at this scale |

## Cost

Approximately the equivalent of 2 small Haiku batch jobs (transformation + 2× inference rounds via subagents in CCotw) plus inline Opus tokens. Materially zero in API spend; absorbed in the session.

## Next step (if pursuing)

Read `results/PARTIAL_VERDICT.md`. Decision is conditional, not unconditional. The methodological revisions are cheap — each is a one-line change to the inference prompt or a switch in the retriever — but skipping them risks running the full $120–175 experiment to inconclusive noise.
