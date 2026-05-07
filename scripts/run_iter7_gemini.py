"""Iter-7: vanilla n-shot prompting (no anti-copy guardrail) on Gemini Flash.

Same 4 problems, same retrieved raw traces (top-3 cosine), same n=8 per cell.
Single new condition `nshot` using prompts/nshot_inference.md (drops the
"use as hints not templates" framing of the existing raw condition).

Usage:
    python3 scripts/run_iter7_gemini.py gemini-2.5-flash gemini_flash
"""

from __future__ import annotations
import json, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/mnt/skills/user/invoking-gemini/scripts")
from gemini_client import invoke_gemini  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
N_SAMPLES = 8
PROBLEMS = {
    "ex_3_24": ("data/eval_problems.json", "data/retrievals_iter4.json"),
    "ex_7_28": ("data/eval_problems.json", "data/retrievals_iter4.json"),
    "ood_steepest": ("data/eval_ood.json", "data/retrievals_iter5.json"),
    "ood_1loop": ("data/eval_ood.json", "data/retrievals_iter5.json"),
}

NSHOT_TEMPLATE = (REPO / "prompts/nshot_inference.md").read_text()


def load_eval(path, prob_id):
    return json.loads((REPO / path).read_text())[prob_id]["statement"]


def load_retrievals(path, prob_id):
    return [r["id"] for r in json.loads((REPO / path).read_text())[prob_id]]


def build_nshot_prompt(prob_id):
    eval_path, ret_path = PROBLEMS[prob_id]
    statement = load_eval(eval_path, prob_id)
    rids = load_retrievals(ret_path, prob_id)
    traces = [(REPO / f"traces/{rid}.md").read_text() for rid in rids[:3]]
    body = NSHOT_TEMPLATE.split("---", 1)[1]
    return (
        body.replace("{trace_1}", traces[0])
        .replace("{trace_2}", traces[1] if len(traces) > 1 else "(none)")
        .replace("{trace_3}", traces[2] if len(traces) > 2 else "(none)")
        .replace("{problem_statement}", statement)
    )


def one_inference(args):
    model, subdir, prob_id, sample_idx = args
    out_dir = REPO / f"answers_iter7/{subdir}/nshot/sample_{sample_idx}"
    out_path = out_dir / f"{prob_id}.md"
    if out_path.exists() and out_path.stat().st_size > 200 and "boxed" in out_path.read_text():
        return f"SKIP nshot/{sample_idx}/{prob_id}"
    out_dir.mkdir(parents=True, exist_ok=True)
    prompt = build_nshot_prompt(prob_id)
    t0 = time.time()
    try:
        resp = invoke_gemini(
            prompt=prompt,
            model=model,
            temperature=0.7,
            max_output_tokens=32000,
        )
        if not resp:
            return f"FAIL nshot/{sample_idx}/{prob_id} (null)"
        out_path.write_text(resp)
        return f"OK   nshot/{sample_idx}/{prob_id} ({len(resp)} ch, {time.time()-t0:.1f}s)"
    except Exception as e:
        return f"EXC  nshot/{sample_idx}/{prob_id} {type(e).__name__}: {e}"


def main():
    if len(sys.argv) != 3:
        print("Usage: run_iter7_gemini.py <model_alias> <subdir>")
        sys.exit(1)
    model, subdir = sys.argv[1], sys.argv[2]
    jobs = []
    for prob_id in PROBLEMS:
        for s in range(N_SAMPLES):
            jobs.append((model, subdir, prob_id, s))
    print(f"Model: {model}  subdir: {subdir}  n_jobs: {len(jobs)}")
    t0 = time.time()
    completed = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        for fut in as_completed([ex.submit(one_inference, j) for j in jobs]):
            res = fut.result()
            completed += 1
            print(f"[{completed:3d}/{len(jobs):3d}] {res}")
    print(f"Done in {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
