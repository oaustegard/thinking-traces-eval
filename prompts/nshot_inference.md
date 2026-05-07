# Vanilla n-shot prompt (no anti-copy / no recipe)

Standard few-shot ICL: show worked examples, then ask for the next solution.
No "use as hints not templates", no "state relevance and differences first",
no anti-copy guardrail. This isolates the **prompting variable** from the
**content variable** — same retrieved raw traces as the existing `raw`
condition, but with vanilla framing.

Compare to `raw_inference.md` (anti-copy framing on the same content) and
`rag_inference.md` (anti-copy framing on Structs).

---

Below are three worked examples of math/physics problems, each with full
reasoning and a final answer. Study them, then solve the new problem at
the end in the same style.

Example 1:
{trace_1}

Example 2:
{trace_2}

Example 3:
{trace_3}

Now solve this problem:
{problem_statement}

Provide your reasoning, then state the final answer in $\boxed{...}$.
