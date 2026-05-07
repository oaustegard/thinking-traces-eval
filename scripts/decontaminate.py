"""Decontamination: 13-gram Jaccard between an eval problem statement
and each trace's full text (problem + reasoning).

Per the iter-0 partial verdict: decontamination must run against full trace
text, not just problem statements, because action/setup leakage (ex_3_24
vs ex_3_26 example) was missed when only problem statements were compared.

Threshold from the T³ paper: any pair with 13-gram Jaccard > 0.05 is
flagged as overlap and the eval problem is rejected.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THRESHOLD = 0.05
N = 13


def normalize(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text.lower())
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    return [t for t in text.split() if t]


def ngrams(tokens: list[str], n: int = N) -> set[tuple[str, ...]]:
    return {tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def check(eval_text: str, trace_texts: list[str]) -> dict:
    eval_grams = ngrams(normalize(eval_text))
    overlaps = []
    for i, t in enumerate(trace_texts):
        j = jaccard(eval_grams, ngrams(normalize(t)))
        if j > THRESHOLD:
            overlaps.append({"trace_index": i, "jaccard": round(j, 4)})
    return {"contaminated": bool(overlaps), "overlaps": overlaps}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("usage: decontaminate.py <eval_problems.json> [traces_dir]")
        sys.exit(1)
    eval_path = Path(sys.argv[1])
    traces_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "traces"

    eval_problems = json.loads(eval_path.read_text())
    trace_texts = [p.read_text() for p in sorted(traces_dir.glob("*.md"))]

    results = {}
    for pid, prob in eval_problems.items():
        results[pid] = check(prob.get("statement", ""), trace_texts)

    print(json.dumps(results, indent=2))
