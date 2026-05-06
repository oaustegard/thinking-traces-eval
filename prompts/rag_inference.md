# RAG inference prompt (with anti-copy guardrail)

Base template from Arabzadeh et al. 2026, Figure 7. Augmented with an
anti-copying instruction targeting the **problem-transposition** failure
mode observed in the iter-0 partial run on issue #2 (RAG-Haiku silently
substituted ex_3_26's action into the ex_3_24 problem because the two share
chapter and framework).

---

You are solving a math/physics problem. You have been given three retrieved
worked examples that share *technique* with the target problem. Use them as
hints about which methods apply, not as templates to copy.

**Critical:** the retrieved examples may share framework or notation with
the main problem but use different setups (different actions, different
domains, different constants). Read the main problem carefully and adapt the
technique to its specific setup. **Do not copy parameter values, action
forms, or boundary conditions from the examples — those belong to the
example, not to your problem.**

If a retrieved example seems irrelevant, ignore it. If all three are
irrelevant, solve from your own knowledge and say so explicitly.

---

Example 1: {struct_1}

Example 2: {struct_2}

Example 3: {struct_3}

Main problem: {problem_statement}

---

Solve the main problem. Begin by stating: (a) which retrieved examples are
relevant and why, (b) what specifically differs between each relevant
example and the main problem. Then reason through the solution, ending with
a final answer in $\boxed{...}$.
