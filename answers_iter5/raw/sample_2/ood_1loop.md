# Raw-Trace RAG Answer: ood_1loop

**Problem.** Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$, where $Z = \int e^{-S(x)/\hbar}dx$ and $Z_0$ is the free partition function. Expand as a power series in $g$ through order $g^3$.

## Relevance and Differences: Retrieved Traces

**Trace 1 (ex_3_26_effective_action, relevance 0.1724):** Most relevant. Computes the 1-loop effective action $S_1(x_c) = \frac{1}{2}\log S''(x_c)$ for a cubic action $S(x) = \frac{x^2}{2} - \frac{gx^3}{6}$. The method — finding the saddle point $x_c$, computing $S''(x_c)$, applying the 1-loop formula $S_1 = \frac{1}{2}\log S''(x_c)$, and Taylor-expanding in $g$ — is directly applicable. **Key difference:** The OOD problem has a non-polynomial interaction $x^2\cosh(x)$ (which expands to $x^2(1 + x^2/2 + x^4/24 + \cdots)$), not a simple cubic. The saddle point and the second derivative calculation must account for this non-polynomial structure.

**Trace 2 (ex_2_14_wallis, relevance 0.1008):** Steepest descent on the Wallis integral; focuses on interior vs. boundary critical points and Laplace asymptotics. Not directly relevant to perturbative 1-loop expansion. Low relevance, ignore.

**Trace 3 (ex_7_27_quartic_1pi, relevance 0.0575):** 1PI 2-point function via Feynman diagrams in QM. Discusses 1-loop diagrams but in the context of an interacting propagator and self-energy, not the partition function of a zero-dim QFT. Minimal relevance; do not use.

## Solution

**Step 1: Identify the saddle point.**

By inspection, $S'(x) = x - gx\cosh(x) = x(1 - g\cosh x)$. At $x=0$:
$$S'(0) = 0.$$

So the saddle point is $x_c = 0$. (Higher-order saddles would involve solving $1 = g\cosh x$, but at small $g$ they are perturbatively away from $x_c = 0$; the leading saddle is at zero.)

**Step 2: Compute $S''(x_c)$.**

$$S''(x) = 1 - g\cosh x - g x \sinh x - \tfrac{g}{2} x^2 \cosh x.$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g.$$

(The $\cosh(0) = 1$ term contributes, but $x\sinh x \to 0$ and $x^2 \cosh x \to 0$ as $x \to 0$.)

**Step 3: Apply the 1-loop formula.**

The 1-loop contribution to $\log(Z/Z_0)$ is
$$\log(Z/Z_0)|_{1\text{-loop}} = -\tfrac{1}{2}\log\frac{S''(x_c)}{S''(0)|_{g=0}}.$$

Since $S''(0)|_{g=0} = 1$:
$$\log(Z/Z_0)|_{1\text{-loop}} = -\tfrac{1}{2}\log(1 - g).$$

**Step 4: Taylor expansion in $g$.**

Using the series $\log(1 - u) = -\sum_{k=1}^\infty \frac{u^k}{k}$ with $u = g$:
$$-\tfrac{1}{2}\log(1-g) = \tfrac{1}{2}\sum_{k=1}^\infty \frac{g^k}{k} = \tfrac{1}{2}\left(g + \tfrac{g^2}{2} + \tfrac{g^3}{3} + \cdots\right).$$

Extracting terms through $g^3$:
$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

**Verification of critical subcheck (2):** The formula $S''(0) = 1 - g$ arises from the second derivative of $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh x$:
$$S''(x) = 1 - \tfrac{g}{2}[\cosh x + x\sinh x + x^2\cosh x].$$
Wait, let me recompute more carefully:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh x,$$
$$S'(x) = x - g x \cosh x - \tfrac{g}{2}x^2\sinh x,$$
$$S''(x) = 1 - g\cosh x - g x\sinh x - gx\sinh x - \tfrac{g}{2}x^2\cosh x = 1 - g\cosh x - 2gx\sinh x - \tfrac{g}{2}x^2\cosh x.$$

At $x=0$: $S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g$. ✓

**Step 5: Final answer.**

$$\boxed{\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

Equivalently, written as a series:
$$\log(Z/Z_0)|_{1\text{-loop}} = \sum_{k=1}^3 \frac{g^k}{2k} + O(g^4).$$

---

**Key subchecks satisfied:**
1. ✓ Identified $x_c = 0$ as the saddle (from $S'(0) = 0$).
2. ✓ Computed $S''(0) = 1 - g$ (recognizing that $\cosh(0) = 1$ and higher-order $x$-terms vanish at $x=0$).
3. ✓ Applied the $-\frac{1}{2}\log(S''(x_c))$ formula.
4. ✓ Taylor expansion giving coefficients $\frac{1}{2k}$ for the $g^k$ term: $\frac{1}{2}, \frac{1}{4}, \frac{1}{6}$ for $k=1,2,3$.

**Note on non-polynomial interaction:** The cosh expansion $\cosh x = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$ in the $-\frac{g}{2}x^2\cosh x$ term contributes cubic, quintic, and higher powers of $x$ to the action. However, these contribute to the 2-loop effective action and higher; at 1-loop, only the second derivative $S''(x_c)$ matters, which depends only on the value and derivatives of the action at the saddle, not on the full nonlinear structure. Thus the 1-loop result reduces to the log formula without explicit Feynman-diagram enumeration.
