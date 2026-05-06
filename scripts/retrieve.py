"""TF-IDF + MMR retrieval (no API needed, runs locally).

Replaces the issue spec's gemini-embedding-001 + cosine-top-k with a
local TF-IDF baseline plus Maximal Marginal Relevance reranking. MMR
guards against the **single-template anchoring** failure mode observed
in the iter-0 partial: when all top-k retrievals are framework-twins,
Haiku copies the template rather than abstracting. MMR forces
diversity in the top-k.

Lambda controls the trade-off:
  λ = 1.0 → pure relevance (T³ paper's default cosine-top-k)
  λ = 0.5 → balanced (recommended for niche corpora; this experiment)
  λ = 0.0 → pure diversity
"""
import json
import re
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parent.parent


def build_index(struct_paths: list[Path]) -> dict:
    docs = [p.read_text() for p in struct_paths]
    ids = [p.stem for p in struct_paths]
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
    M = vec.fit_transform(docs)
    return {"ids": ids, "vectorizer": vec, "matrix": M, "docs": docs}


def cosine(a, b):
    """Cosine similarity for sparse-or-dense vectors. Returns float."""
    from numpy.linalg import norm
    a = a.toarray().ravel() if hasattr(a, "toarray") else np.asarray(a).ravel()
    b = b.toarray().ravel() if hasattr(b, "toarray") else np.asarray(b).ravel()
    na, nb = norm(a), norm(b)
    return float(a @ b / (na * nb)) if na and nb else 0.0


def retrieve(index: dict, query: str, k: int = 3, lam: float = 0.5) -> list[dict]:
    qv = index["vectorizer"].transform([query])
    M = index["matrix"]
    rel = np.array([cosine(qv, M[i]) for i in range(M.shape[0])])

    selected: list[int] = []
    candidates = list(range(M.shape[0]))
    while candidates and len(selected) < k:
        best_score = -np.inf
        best_idx = candidates[0]
        for c in candidates:
            div = max((cosine(M[c], M[s]) for s in selected), default=0.0)
            score = lam * rel[c] - (1 - lam) * div
            if score > best_score:
                best_score = score
                best_idx = c
        selected.append(best_idx)
        candidates.remove(best_idx)

    return [
        {"id": index["ids"][i], "relevance": round(float(rel[i]), 4)}
        for i in selected
    ]


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("usage: retrieve.py <eval_problems.json> <struct_dir> [lambda]")
        sys.exit(1)
    eval_path = Path(sys.argv[1])
    struct_dir = Path(sys.argv[2])
    lam = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5

    struct_paths = sorted(struct_dir.glob("*.md"))
    if not struct_paths:
        print(f"no struct files in {struct_dir}")
        sys.exit(1)
    idx = build_index(struct_paths)

    eval_problems = json.loads(eval_path.read_text())
    out = {}
    for pid, prob in eval_problems.items():
        out[pid] = retrieve(idx, prob.get("statement", ""), k=3, lam=lam)
    print(json.dumps(out, indent=2))
