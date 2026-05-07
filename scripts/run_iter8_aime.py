"""iter-8: replicate T3's AIME 25 setup against Haiku 4.5.

Ports T3's exact prompt template from
https://github.com/Narabzad/t3/blob/main/eval/tasks/aime/utils.py
to make per-problem prompts. We DO NOT use the recipe-style framing
from iter-3..7 — this is T3's actual code-shipped prompt.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERIES = [json.loads(l) for l in (ROOT / "data/t3_aime26/queries.jsonl").open()]
RAG     = [json.loads(l) for l in (ROOT / "data/t3_aime26/struct_retrievals.jsonl").open()]

# T3's no-RAG default: just the question (QUERY_TEMPLATE = '{Question}')
# T3's RAG: the "Considering the following examples as hints..." block.

def build_examples(ctxs, top_k=3):
    parts, seen = [], set()
    for c in ctxs:
        text = c.get('retrieval text', c.get('text', ''))
        if not text or not text.strip(): continue
        text = text.replace('<think>', '').replace('</think>', '')
        if text in seen: continue
        seen.add(text)
        parts.append(f"Example {len(parts)+1}: {text}")
        if len(parts) >= top_k: break
    return "\n".join(parts)

def make_prompt(idx, condition):
    q = QUERIES[idx]
    if condition == 'no_rag':
        return q['problem']
    examples = build_examples(RAG[idx]['ctxs'], top_k=3)
    return (
        "Considering the following examples as hints, try to answer the question.\n\n"
        "Use any useful hints and strategies from the retrieved examples.\n"
        f"\n{examples}\n"
        f"\n\nmain problem:\n{q['problem']}\n"
        "Present the answer in LaTeX format: \\boxed{Your answer}"
    )

def extract_boxed(text):
    """Return integer string from \\boxed{N} or None."""
    if not text: return None
    # Last \boxed{...} wins (typical CoT outputs)
    matches = re.findall(r'\\boxed\{([^{}]*)\}', text)
    if not matches:
        # Try double-brace nesting
        matches = re.findall(r'\\boxed\{(\d+)\}', text)
    if not matches: return None
    last = matches[-1].strip().rstrip('.')
    # AIME answers are 0-999 ints; strip $, ,, etc
    last = re.sub(r'[\$\\\s,]', '', last)
    m = re.match(r'-?\d+', last)
    return m.group(0) if m else last

def score(pred, truth):
    if pred is None: return 0
    try:
        return 1 if int(pred) == int(truth) else 0
    except (ValueError, TypeError):
        return 0

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if cmd == "stats":
        print(f"Problems: {len(QUERIES)}, retrievals: {len(RAG)}")
        print(f"First answer: {QUERIES[0]['answer']}")
        print(f"First no_rag prompt len: {len(make_prompt(0,'no_rag'))}")
        print(f"First struct prompt len: {len(make_prompt(0,'struct'))}")
    elif cmd == "build":
        # Output all 30 prompts for both conditions, for batch handoff.
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        out = []
        for idx in range(n):
            for cond in ('no_rag', 'struct'):
                out.append({
                    "problem_idx": idx,
                    "condition": cond,
                    "answer_truth": str(QUERIES[idx]['answer']),
                    "prompt": make_prompt(idx, cond),
                })
        print(json.dumps(out, indent=None))
