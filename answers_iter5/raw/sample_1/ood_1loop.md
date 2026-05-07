# Raw-trace RAG: OOD 1-Loop Effective Action Problem

## Relevance Assessment

**Trace 1 (ex_3_26_effective_action):** Highly relevant. The problem directly parallels the OOD setup: both compute the 1-loop contribution $S_1(x_c)$ to the effective action via saddle-point expansion and Feynman diagrams. The methodology — identifying the saddle, computing the second derivative of the action at the saddle, applying the 1-loop formula $S_1 = \tfrac{1}{2}\log S''(x_c)$, and expanding as a power series in the coupling — is identical. The key difference is the specific action form: Trace 1 has $S(x) = x^2/2 - gx^3/6$ (cubic interaction), while the OOD has $S(x) = x^2/2 - (g/2)x^2\cosh(x)$ (quadratic times cosh).

**Trace 2 (ex_2_14_wallis):** Marginally relevant. It uses steepest descent / Laplace methods for asymptotic analysis, but applied to an *integral* with oscillatory powers of sine, not to an effective action or saddle-point expansion. The technique of expanding around a critical point and computing the second derivative is conceptually related, but the context (integral asymptotics vs. quantum effective action) differs substantially.

**Trace 3 (ex_7_27_quartic):** Weakly relevant. It computes loop diagrams for a 1-loop self-energy in field theory, including Feynman rules and symmetry factors for multi-loop graphs. While loop counting and diagram enumeration appear in both problems, the OOD is purely 1-loop and does not involve multi-leg diagrammatic analysis — it is a zero-dimensional partition function.

## Differences from Trace 1

The retrieved cubic effective action (ex_3_26) differs from the OOD in these ways:

1. **Interaction form:** Trace 1 has $S_{\text{int}} = -gx^3/6$ (cubic). The OOD has $(g/2)x^2\cosh(x)$ (quadratic times hyperbolic cosine). The cosh introduces infinitely many powers of $x$ when expanded, not just a single cubic term.

2. **Saddle location:** In Trace 1, the cubic interaction and the quadratic kinetic term do not shift the saddle from $x_c = 0$; the cubic only appears in the phase at orders higher than the quadratic. In the OOD, the saddle is still $x_c = 0$ by inspection (since $S'(0) = 0$), but the second derivative is affected by the cosh expansion at that point.

3. **Second derivative computation:** Trace 1 finds $S''(x) = 1 - gx$ (linear correction from the cubic). The OOD has $S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - (g/2)x^2\cosh(x)$, which at $x = 0$ simplifies to $S''(0) = 1 - g$ (the cosh term contributes $-g$ and the other terms vanish at $x=0$).

4. **Expansion structure:** Trace 1 expands the log as a geometric series $\log(1 - gx_c) = -\sum_{k\ge1} (gx_c)^k/k$, all stemming from the linear dependence of $S''$ on $x_c$. The OOD has $S''(0) = 1 - g$ independent of the saddle value (since saddle is at 0), so the expansion is purely in powers of $g$, not in $gx_c$.

## Solution

**Saddle-point identification.**

The action is $S(x) = x^2/2 - (g/2)x^2\cosh(x)$. By inspection,
$$S'(x) = x - g\left[x\cosh(x) + (x^2/2)\sinh(x)\right].$$

At $x = 0$: $S'(0) = 0 - g[0 + 0] = 0$. So $x_c = 0$ is the saddle.

**Second derivative at the saddle.**

$$S''(x) = 1 - g[\cosh(x) + x\sinh(x) + x\sinh(x) + (x^2/2)\cosh(x)] = 1 - g\cosh(x) - 2gx\sinh(x) - (g/2)x^2\cosh(x).$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g.$$

**1-loop formula.**

By the determinant formula (Etingof, or the trace 1 derivation),
$$S_1 = \tfrac{1}{2}\log S''(x_c) = \tfrac{1}{2}\log(1 - g).$$

**Power-series expansion through order $g^3$.**

Using $\log(1 - u) = -\sum_{k\ge1} u^k/k$ with $u = g$:
$$S_1 = \tfrac{1}{2}\log(1-g) = -\tfrac{1}{2}\sum_{k\ge1} \frac{g^k}{k} = -\tfrac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + O(g^4)\right).$$

Simplify:
$$S_1 = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4).$$

**Critical check:** At the saddle $x_c = 0$, the interaction terms $\cosh(x), \sinh(x), x^2\cosh(x)$ all evaluate to their zeroth-order Taylor coefficients at $x=0$. The cosh expansion $\cosh(x) = 1 + x^2/2 + x^4/24 + \cdots$ contributes only the constant term 1 to $S''(0)$, leaving a correction of $-g$ to the propagator. Cubic and higher terms in the $x$ expansion of $\cosh(x) \cdot x^2$ do NOT affect the 1-loop effective action — they contribute only at 2-loop and beyond through the background-field effective action or renormalization group flows. The 1-loop log formula captures only the tree-level action's second derivative.

$$\boxed{S_1 = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + \cdots}$$

with (1) saddle at $x_c = 0$ ✓, (2) $S''(0) = 1 - g$ ✓, (3) 1-loop formula $\tfrac{1}{2}\log(1-g)$ ✓, (4) Taylor expansion with coefficients $1/(2k)$ for order $g^k$ ✓.
