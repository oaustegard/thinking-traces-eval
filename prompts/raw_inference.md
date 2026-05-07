# Raw-trace RAG inference prompt

Mirrors `rag_inference.md` (which uses Struct-form examples) but provides
**raw, unsummarized reasoning traces** as the retrieved examples. Tests
whether the T³-Struct compression helps or hurts Claude-family inference
relative to giving it the full reasoning context.

Anti-copy guardrail retained.

---

You are solving a math/physics problem. You have been given three retrieved
worked-out reasoning traces — full free-form derivations from related
problems, not summarized scaffolds. Use them as hints about which methods
apply, not as templates to copy.

**Critical:** the retrieved traces may share framework or notation with the
main problem but use different setups (different actions, domains,
constants). Read the main problem carefully and adapt the technique to its
specific setup. **Do not copy parameter values, action forms, or boundary
conditions from the traces — those belong to the example, not to your
problem.**

If a retrieved trace seems irrelevant, ignore it. If all three are
irrelevant, solve from your own knowledge and say so explicitly.

---

Trace 1: {trace_1}

Trace 2: {trace_2}

Trace 3: {trace_3}

Main problem: {problem_statement}

---

Solve the main problem. Begin by stating: (a) which retrieved traces are
relevant and why, (b) what specifically differs between each relevant trace
and the main problem. Then reason through the solution, ending with a final
answer in $\boxed{...}$.
