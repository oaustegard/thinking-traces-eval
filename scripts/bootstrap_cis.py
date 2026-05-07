"""Bootstrap CIs for iter-4 and iter-5 condition deltas.

Resampling at the (sample) level within each (problem, condition) cell, then
aggregating by problem or globally. 10000 resamples, BCa-style not used (kept
simple percentile bootstrap; small-sample, want transparent computation).

Run from repo root: python3 scripts/bootstrap_cis.py
"""
import json, random, statistics, sys

random.seed(20260507)
N_RESAMPLES = 10000


def load_scores(path):
    with open(path) as f:
        return json.load(f)


def cell_scores(scores, problems, condition):
    out = []
    for prob in problems:
        for k, v in scores[prob][condition].items():
            out.append(v["score"])
    return out


def cell_problem_scores(scores, prob, condition):
    return [v["score"] for v in scores[prob][condition].values()]


def bootstrap_diff(a, b, n_resamples=N_RESAMPLES):
    n_a, n_b = len(a), len(b)
    diffs = []
    for _ in range(n_resamples):
        sa = [a[random.randrange(n_a)] for _ in range(n_a)]
        sb = [b[random.randrange(n_b)] for _ in range(n_b)]
        diffs.append(statistics.mean(sa) - statistics.mean(sb))
    diffs.sort()
    return {
        "point": statistics.mean(a) - statistics.mean(b),
        "ci_lo": diffs[int(0.025 * n_resamples)],
        "ci_hi": diffs[int(0.975 * n_resamples)],
        "p_zero_or_worse": sum(1 for d in diffs if d >= 0) / n_resamples,
    }


def fmt(r):
    return (f"Δ = {r['point']:+.3f}  95%CI [{r['ci_lo']:+.3f}, {r['ci_hi']:+.3f}]"
            f"  P(Δ≥0) = {r['p_zero_or_worse']:.4f}")


def report(label, scores_path, problems):
    print("=" * 78)
    print(label)
    print("=" * 78)
    s = load_scores(scores_path)
    n = cell_scores(s, problems, "no_rag")
    st = cell_scores(s, problems, "struct")
    has_raw = "raw" in s[problems[0]]
    r = cell_scores(s, problems, "raw") if has_raw else None
    print(f"  no_rag n={len(n):2d}  mean={statistics.mean(n):.3f}")
    print(f"  struct n={len(st):2d}  mean={statistics.mean(st):.3f}")
    if has_raw:
        print(f"  raw    n={len(r):2d}  mean={statistics.mean(r):.3f}")
    print()
    print(f"Aggregate ({len(n)} samples per condition):")
    print("  Struct vs no-RAG:", fmt(bootstrap_diff(st, n)))
    if has_raw:
        print("  Raw    vs no-RAG:", fmt(bootstrap_diff(r, n)))
        print("  Struct vs Raw   :", fmt(bootstrap_diff(st, r)))
    print()
    print("Per-problem:")
    for prob in problems:
        n_p = cell_problem_scores(s, prob, "no_rag")
        s_p = cell_problem_scores(s, prob, "struct")
        r_p = cell_problem_scores(s, prob, "raw") if has_raw else None
        means = f"no_rag={statistics.mean(n_p):.3f}  struct={statistics.mean(s_p):.3f}"
        if has_raw:
            means += f"  raw={statistics.mean(r_p):.3f}"
        print(f"  {prob}:  {means}")
        print(f"    Struct vs no-RAG: {fmt(bootstrap_diff(s_p, n_p))}")
        if has_raw:
            print(f"    Raw    vs no-RAG: {fmt(bootstrap_diff(r_p, n_p))}")
    print()


if __name__ == "__main__":
    report(
        "ITER-4 (in-distribution headroom)",
        "results/scores_iter4_sonnet.json",
        ["ex_3_24", "ex_7_28"],
    )
    report(
        "ITER-5 (OOD constructed)",
        "results/scores_iter5_sonnet.json",
        ["ood_steepest", "ood_1loop"],
    )
