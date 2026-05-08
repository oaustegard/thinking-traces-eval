"""iter-9: simulated Reasoning Memory (Wu et al. 2026, arXiv:2604.01348)
on AIME 25 problems 0-9 vs Haiku 4.5.

Since the real Reasoning Memory pipeline requires a 32M-item datastore,
ReasonIR embeddings, vLLM servers, and thought-stream injection, we
simulate the protocol on the SAME T3 corpus iter-8 used:

  iter-8 (T3 trajectory RAG):  query = original problem
                               retrieve top-3 cheatsheets by problem-similarity
  iter-9 (RM-style):           Haiku verbalizes a SUBQUESTION as the query
                               retrieve top-3 cheatsheets by subquestion-similarity
                               inject as procedural hints

Same problems, same scoring. Tests whether subquestion-driven retrieval
helps where problem-driven retrieval did not.

This is a niche-scale, simplified version of Meta's pipeline. Caveats are
spelled out in results/ITER9_FINDINGS.md.
"""
import json, re, sys
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parents[1]
RAG  = [json.loads(l) for l in (ROOT / "data/t3_aime26/struct_retrievals.jsonl").open()]
QUERIES = [json.loads(l) for l in (ROOT / "data/t3_aime26/queries.jsonl").open()]

def build_pool(problem_indices, per_problem_top=10):
    """Pool the top-N retrievals across the given problems, dedup."""
    seen, pool = set(), []
    for idx in problem_indices:
        for c in RAG[idx]['ctxs'][:per_problem_top]:
            text = c.get('retrieval text', c.get('text', '')).strip()
            if not text or text in seen: continue
            text = text.replace('<think>', '').replace('</think>', '')
            seen.add(text)
            pool.append({'source_problem': idx, 'text': text})
    return pool

def build_tfidf_index(pool):
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
    M = vec.fit_transform([p['text'] for p in pool])
    return vec, M

def topk_for_query(query, vec, M, pool, k=3):
    qv = vec.transform([query])
    sims = (M @ qv.T).toarray().ravel()
    order = np.argsort(-sims)
    out, seen = [], set()
    for i in order:
        if i in seen: continue
        out.append({'rank': len(out)+1, 'sim': float(sims[i]), **pool[i]})
        seen.add(i)
        if len(out) >= k: break
    return out

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    problem_indices = list(range(n))

    if cmd == "build":
        pool = build_pool(problem_indices, per_problem_top=10)
        out_dir = ROOT / "answers_iter9"; out_dir.mkdir(exist_ok=True)
        (out_dir / "pool.json").write_text(json.dumps(pool, indent=2))
        print(f"Pool: {len(pool)} unique cheatsheets from {len(problem_indices)} problems x top-10")

    elif cmd == "subq_prompts":
        # Step A prompts: "What's the first subquestion?"
        out_dir = ROOT / "answers_iter9/subq_prompts"; out_dir.mkdir(parents=True, exist_ok=True)
        for idx in problem_indices:
            q = QUERIES[idx]
            prompt = (
                f"Read this AIME (American Invitational Mathematics Examination) problem:\n\n"
                f"{q['problem']}\n\n"
                "What is the FIRST procedural subquestion you need to answer to make progress?\n"
                "Output ONE concise natural-language query (≤25 words) describing what mathematical "
                "technique or sub-computation you need to perform first.\n\n"
                "Format: just the query, no quotes, no preamble. Example: \"How do I find the divisors of an integer N?\""
            )
            (out_dir / f"subq_{idx:02d}.txt").write_text(prompt)
        print(f"Wrote {n} subquestion-prompts to answers_iter9/subq_prompts/")

    elif cmd == "retrieve":
        # Step B: read collected subqs from answers_iter9/subqs/{idx}.txt; retrieve top-3
        pool = json.loads((ROOT / "answers_iter9/pool.json").read_text())
        vec, M = build_tfidf_index(pool)
        out_dir = ROOT / "answers_iter9/solve_prompts"; out_dir.mkdir(parents=True, exist_ok=True)
        retrieval_log = []
        for idx in problem_indices:
            subq_file = ROOT / f"answers_iter9/subqs/subq_{idx:02d}.txt"
            if not subq_file.exists():
                print(f"WARN: missing {subq_file}"); continue
            subq = subq_file.read_text().strip().splitlines()[-1].strip()
            top3 = topk_for_query(subq, vec, M, pool, k=3)
            retrieval_log.append({'idx': idx, 'subq': subq, 'top3': [{'rank':t['rank'],'sim':t['sim'],'source_problem':t['source_problem']} for t in top3]})

            q = QUERIES[idx]
            hints = "\n".join(f"Procedural hint {t['rank']} (cosine sim={t['sim']:.3f} to your subquestion):\n{t['text']}\n" for t in top3)
            prompt = (
                f"Procedural hints retrieved from prior reasoning traces:\n\n{hints}\n"
                f"---\n\nNow solve this AIME problem using the relevant techniques:\n\n"
                f"{q['problem']}\n\n"
                "Show your full reasoning. End with the answer in `\\boxed{N}` form (integer 0-999)."
            )
            (out_dir / f"solve_{idx:02d}.txt").write_text(prompt)
        (ROOT / "answers_iter9/retrieval_log.json").write_text(json.dumps(retrieval_log, indent=2))
        print(f"Wrote {n} solve prompts; logged retrievals.")
