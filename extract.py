"""Extract Exercise statements from Etingof markdown/text dump.

Each exercise is captured from its `Exercise N.M.` header until the next
problem marker (Exercise/Example/Theorem/Proposition/Definition/Lemma/Remark)
or until a blank-line + chapter/section header appears.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "data" / "etingof.txt"
OUT = ROOT / "data" / "etingof_problems.jsonl"

START = re.compile(r"^\s*Exercise (\d+)\.(\d+)\.\s*(.*)$")
STOP = re.compile(
    r"^\s*(Exercise|Example|Theorem|Proposition|Definition|Lemma|Remark|Corollary|Conjecture)\s+\d+\.\d+\.?\s"
)
SECTION = re.compile(r"^\s*\d+(\.\d+)*\s+[A-Z]")


def extract():
    lines = SRC.read_text().splitlines()
    problems = []
    i = 0
    while i < len(lines):
        m = START.match(lines[i])
        if not m:
            i += 1
            continue
        chap, num, head = m.group(1), m.group(2), m.group(3)
        body = [head.strip()]
        j = i + 1
        while j < len(lines):
            if STOP.match(lines[j]):
                break
            body.append(lines[j])
            j += 1
        text = "\n".join(body).strip()
        text = re.sub(r"\n{3,}", "\n\n", text)
        problems.append({
            "id": f"ex_{chap}_{num}",
            "chapter": int(chap),
            "number": int(num),
            "line": i + 1,
            "text": text,
        })
        i = j
    OUT.write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in problems))
    print(f"extracted {len(problems)} problems -> {OUT}")
    return problems


if __name__ == "__main__":
    extract()
