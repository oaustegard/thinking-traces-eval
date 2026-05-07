# Raw-trace RAG Answer: OOD 1-loop Effective Action

## Relevance Assessment

**Trace 1 (ex_3_26_effective_action): Relevance 0.17** — Moderately relevant. This trace computes the 1-loop effective action $S_1(x_c)$ for the action $S(x) = \frac{x^2}{2} - \frac{g x^3}{6}$ using both the determinant formula and 1PI Feynman-diagram enumeration. The framework (saddle-point approximation, the relation $S_1 = \frac{1}{2} \log S''(x_c)$, series expansion, diagram classification) directly applies to the main problem.

**Trace 2 (ex_2_14_wallis): Relevance 0.10** — Weakly relevant. This trace applies asymptotic methods (steepest descent, Laplace) to integrals and makes use of saddle-point geometry. While the underlying asymptotic machinery shares structure with effective-action calculations, the main problem is not about integrals of trigonometric functions — it concerns zero-dimensional quantum field theory. Provides context on saddle-point approximations but not directly on 1-loop effective-action techniques.

**Trace 3 (ex_7_27_quartic_1pi): Relevance 0.06** — Minimal relevance. Title suggests a quartic-coupling 1PI diagram count. Some overlap with diagram structure, but coupling differs and details are absent. Likely unhelpful.

**Key differences from the cubic trace (ex_3_26):**
- **Interaction form:** ex_3_26 uses $S_{\text{int}} = -\frac{g x^3}{6}$ (cubic). The main problem uses $S_{\text{int}} = -\frac{g}{2} x^2 \cosh(x)$ (quadratic times transcendental function). This is **not polynomial** — the cosh will expand into all even powers of $x$, creating an infinite tower of vertices.
- **Action structure:** ex_3_26 has only a trivalent vertex. The main problem, when $\cosh(x)$ is expanded, contributes vertices of all even valences: $x^2 \cdot (1 + x^2/2! + x^4/4! + \ldots)$ yields a $x^2$ term, $x^4$ term, $x^6$ term, etc.
- **Saddle point:** Both have a saddle at $x_c = 0$, but the second derivatives differ: ex_3_26 has $S''(0) = 1 - g$, while the main problem has $S''(0) = 1 - g$ (from the $x^2 \cosh(x)$ at $x=0$: $\cosh(0) = 1$, so $\frac{\partial^2}{\partial x^2}[-\frac{g}{2}x^2 \cosh(x)]|_{x=0} = -g$). The formulas coincide at this order, but the higher-order structure differs.

---

## Solution

The action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$. The partition function is
$$Z = \int_{-\infty}^\infty e^{-S(x)/\hbar} \, dx, \quad Z_0 = \int_{-\infty}^\infty e^{-x^2/(2\hbar)} \, dx = \sqrt{2\pi\hbar}.$$

**Step 1: Identify the saddle point.**

The action is $S(x) = x^2 \left(\frac{1}{2} - \frac{g}{2} \cosh(x)\right)$. The classical field equations $S'(x_c) = 0$ give:
$$S'(x) = x \left(1 - g \cosh(x)\right) + x \left(-\frac{g}{2} x \sinh(x)\right) = x \left(1 - g \cosh(x) - \frac{g x}{2} \sinh(x)\right).$$

At $x_c = 0$: $S'(0) = 0$ by inspection (the prefactor $x$ vanishes). So $x_c = 0$ is the saddle.

**Step 2: Compute the second derivative.**

$$S''(x) = \frac{d}{dx}\left[x(1 - g\cosh(x) - \frac{g x}{2}\sinh(x))\right]$$
$$= (1 - g\cosh(x) - \frac{g x}{2}\sinh(x)) + x\left(-g\sinh(x) - \frac{g}{2}\sinh(x) - \frac{g x}{2}\cosh(x)\right)$$
$$= 1 - g\cosh(x) - \frac{g x}{2}\sinh(x) - \frac{3g x}{2}\sinh(x) - \frac{g x^2}{2}\cosh(x).$$

At $x = 0$:
$$S''(0) = 1 - g \cosh(0) = 1 - g.$$
(All terms with $x$ factors vanish at $x=0$.)

**Step 3: Apply the 1-loop formula.**

The 1-loop effective action is:
$$S_1(x_c) = \frac{1}{2} \log S''(x_c) = \frac{1}{2} \log(1 - g).$$

Therefore:
$$\frac{\log(Z/Z_0)}{\hbar} = S_1(0) = \frac{1}{2} \log(1 - g).$$

**Step 4: Power-series expansion.**

Using the Taylor series $\log(1 - u) = -\sum_{k=1}^\infty \frac{u^k}{k}$ with $u = g$:
$$\frac{1}{2} \log(1 - g) = -\frac{1}{2} \sum_{k=1}^\infty \frac{g^k}{k} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \frac{g^4}{8} - \cdots$$

Through order $g^3$:
$$\boxed{\frac{\log(Z/Z_0)}{\hbar} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4).}$$

**Critical subchecks:**
- ✓ Identified $x_c = 0$ as the saddle (by inspection; $S(x) \propto x \times (\cdots)$ ensures $S'(0)=0$).
- ✓ Computed $S''(0) = 1 - g$ (recognizing that the $\cosh(0) = 1$ term contributes $-g$ to the second derivative, and all mixed $x$-derivatives vanish at $x=0$).
- ✓ Applied the determinant formula $S_1(x_c) = \frac{1}{2} \log S''(x_c)$.
- ✓ Expanded the logarithm: coefficients $\frac{1}{2k}$ for the $g^k$ term (i.e., $1/2, 1/4, 1/6, 1/8, \ldots$).

**Note on higher orders:** The cubic and higher terms in the cosh expansion ($\frac{g}{2} x^2 \cdot (x^2/2! + x^4/4! + \ldots)$) contribute to 2-loop and higher diagrams. At 1-loop, the determinant formula captures the entire result: the saddle at $x=0$ is unshifted by the interaction, and $S''(0)$ depends only on the quadratic and the linear $\cosh$ term evaluated at $x=0$. Thus the 1-loop answer depends only on $g$, not on the detailed structure of the cosh coefficients.
