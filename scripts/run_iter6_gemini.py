"""Iter-6: Gemini capability-ladder ablation.

Tests training-overlap hypothesis on a weaker inference model than Haiku 4.5.
Same 4 problems, same 3 conditions (no_rag, struct, raw), 8 samples per cell.

Usage:
    python3 scripts/run_iter6_gemini.py <model_alias> <subdir>
    e.g.   python3 scripts/run_iter6_gemini.py gemini-2.5-flash-lite gemini_lite
           python3 scripts/run_iter6_gemini.py gemini-2.5-flash      gemini_flash

Outputs to answers_iter6/<subdir>/{no_rag,struct,raw}/sample_{0..7}/<prob>.md
"""

from __future__ import annotations
import json
import os
import sys
import time
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

NO_RAG_TEMPLATE = """You are solving a math/physics problem from scratch using only your own knowledge.

Problem:
{problem}

Solve carefully. Show your reasoning. End with the final answer in $\\boxed{{...}}$. ~400-800 words."""

RAG_TEMPLATE = (REPO / "prompts/rag_inference.md").read_text()
RAW_TEMPLATE = (REPO / "prompts/raw_inference.md").read_text()


def load_eval(path: str, prob_id: str) -> str:
    return json.loads((REPO / path).read_text())[prob_id]["statement"]


def load_retrievals(path: str, prob_id: str) -> list[str]:
    return [r["id"] for r in json.loads((REPO / path).read_text())[prob_id]]


def load_struct(rid: str) -> str:
    return (REPO / f"struct/{rid}.md").read_text()


def load_trace(rid: str) -> str:
    return (REPO / f"traces/{rid}.md").read_text()


def build_no_rag_prompt(prob_id: str) -> str:
    eval_path, _ = PROBLEMS[prob_id]
    statement = load_eval(eval_path, prob_id)
    return NO_RAG_TEMPLATE.format(problem=statement)


def build_struct_prompt(prob_id: str) -> str:
    eval_path, ret_path = PROBLEMS[prob_id]
    statement = load_eval(eval_path, prob_id)
    rids = load_retrievals(ret_path, prob_id)
    structs = [load_struct(rid) for rid in rids[:3]]
    body = RAG_TEMPLATE.split("---")[2]
    body = (
        body.replace("{struct_1}", structs[0])
        .replace("{struct_2}", structs[1] if len(structs) > 1 else "(none)")
        .replace("{struct_3}", structs[2] if len(structs) > 2 else "(none)")
        .replace("{problem_statement}", statement)
    )
    closing = RAG_TEMPLATE.split("---")[3]
    return body + "\n---\n" + closing


def build_raw_prompt(prob_id: str) -> str:
    eval_path, ret_path = PROBLEMS[prob_id]
    statement = load_eval(eval_path, prob_id)
    rids = load_retrievals(ret_path, prob_id)
    traces = [load_trace(rid) for rid in rids[:3]]
    body = RAW_TEMPLATE.split("---")[2]
    body = (
        body.replace("{trace_1}", traces[0])
        .replace("{trace_2}", traces[1] if len(traces) > 1 else "(none)")
        .replace("{trace_3}", traces[2] if len(traces) > 2 else "(none)")
        .replace("{problem_statement}", statement)
    )
    closing = RAW_TEMPLATE.split("---")[3]
    return body + "\n---\n" + closing


BUILDERS = {"no_rag": build_no_rag_prompt, "struct": build_struct_prompt, "raw": build_raw_prompt}


def one_inference(args):
    model, subdir, prob_id, condition, sample_idx = args
    out_dir = REPO / f"answers_iter6/{subdir}/{condition}/sample_{sample_idx}"
    out_path = out_dir / f"{prob_id}.md"
    if out_path.exists() and out_path.stat().st_size > 200 and "boxed" in out_path.read_text():
        return f"SKIP {condition}/{sample_idx}/{prob_id}"
    out_dir.mkdir(parents=True, exist_ok=True)
    prompt = BUILDERS[condition](prob_id)
    t0 = time.time()
    try:
        # temperature ~0.7 to match diversity of Haiku subagent draws
        # max_output_tokens=16000 — flash-lite uses many tokens for working,
        # 4000 truncated 77% of outputs mid-derivation in the first sweep.
        resp = invoke_gemini(
            prompt=prompt,
            model=model,
            temperature=0.7,
            max_output_tokens=16000,
        )
        if not resp:
            return f"FAIL {condition}/{sample_idx}/{prob_id} (null response)"
        out_path.write_text(resp)
        return f"OK   {condition}/{sample_idx}/{prob_id} ({len(resp)} ch, {time.time()-t0:.1f}s)"
    except Exception as e:
        return f"EXC  {condition}/{sample_idx}/{prob_id} {type(e).__name__}: {e}"


def main():
    if len(sys.argv) != 3:
        print("Usage: run_iter6_gemini.py <model_alias> <subdir>")
        sys.exit(1)
    model, subdir = sys.argv[1], sys.argv[2]

    jobs = []
    for prob_id in PROBLEMS:
        for condition in ("no_rag", "struct", "raw"):
            for s in range(N_SAMPLES):
                jobs.append((model, subdir, prob_id, condition, s))

    print(f"Model: {model}  subdir: {subdir}  total jobs: {len(jobs)}")
    t0 = time.time()
    completed = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = [ex.submit(one_inference, j) for j in jobs]
        for fut in as_completed(futures):
            res = fut.result()
            completed += 1
            print(f"[{completed:3d}/{len(jobs):3d}] {res}")
    print(f"Done in {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
