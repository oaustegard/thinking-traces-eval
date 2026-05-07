## T³-Struct transformation

(Verbatim from Arabzadeh et al. 2026, arXiv:2605.03344, Figure 4.)

Convert the reasoning trace into a concise step-by-step cheatsheet.

Guidelines:
- Use at most 7 steps.
- Each step should represent a meaningful action.
- Keep explanations short and clear.
- Focus on reusable reasoning patterns.
- Remove failed or irrelevant attempts.

**Critical addition (this experiment, post-pilot):** do not introduce any
technique, identity, or hint that does not appear in the source trace. If the
trace does not mention "stationary phase" you must not write it. The
transformer's job is to compress what's in the trace, not to add adjacent
knowledge that the trace's author happens to know. This guards against the
contamination failure mode observed in the in-conversation pilot of issue #2.

Output format:

    Problem: ...
    Step 1: ...
    ...
    Step N: ...
    Answer: $\boxed{[final answer]}$

Given trace: {trace}
