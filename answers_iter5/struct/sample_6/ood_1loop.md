# Sample 6: OOD 1-Loop Partition Function Problem

## Relevance Assessment

**Retrieved examples:**
1. **ex_3_26_effective_action** (relevance: 0.1724) — 1-loop effective action for $S(x) = x^2/2 - gx^3/6$
2. **ex_2_14_wallis** (relevance: 0.1008) — steepest descent for real integrals (different technique)
3. **ex_7_27_quartic_1pi** (relevance: 0.0575) — 1PI diagrams in quantum field theory

**Relevance and differences:**

The ex_3_26_effective_action example is moderately relevant because both involve saddle-point expansion of a path integral and 1-loop logarithmic terms. However, the **target problem differs critically in the action itself**:

- **ex_3_26:** $S(x) = x^2/2 - gx^3/6$ is a simple cubic with cubic interaction term.
- **Target:** $S(x) = x^2/2 - (g/2)x^2 \cosh(x)$ is a zero-dimensional QFT action with **nonlinear, transcendental** interaction term and **quadratic structure** (not cubic).

The key difference: ex_3_26's cubic term enters at 2-loop order (necklace diagrams); the target's $\cosh$ expansion introduces $x^2, x^4, x^6, \ldots$ terms all multiplied by the prefactor $x^2$. This changes the structure of the saddle-point expansion. The Wallis integral is real analysis (not QFT), and the quartic example involves multiple coupled integrals (not zero-dimensional).

## Solution

The partition function is
$$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx, \quad S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 \cosh(x),$$

and we want the 1-loop contribution $\log(Z/Z_0)$, where $Z_0$ is the free (g=0) case.

**Step 1: Identify the saddle point.**

By inspection, $S(x) = x^2 \left(\frac{1}{2} - \frac{g}{2}\cosh(x)\right)$.

Compute $S'(x)$:
$$S'(x) = x - gx \cosh(x) - \frac{g}{2}x^2 \sinh(x).$$

At $x = 0$:
$$S'(0) = 0 - 0 - 0 = 0.$$

Thus $x_c = 0$ is the saddle point.

**Step 2: Compute the second derivative at the saddle.**

$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

Simplify:
$$S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

At $x = 0$:
$$S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g.$$

This is the **key result**: the second derivative picks up only the $\cosh(0) = 1$ term from the $g$ coupling; the $x$-dependent terms vanish at $x=0$.

**Step 3: Apply the 1-loop saddle-point formula.**

The 1-loop contribution to $\log(Z)$ is given by:
$$\log Z_{\text{1-loop}} = \log Z_0 - \frac{1}{2}\log\left(\frac{S''(x_c)}{S''(x_c)|_{g=0}}\right).$$

Since $Z_0 = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx = \sqrt{2\pi\hbar}$ is the free partition function, we define
$$\log(Z/Z_0) := -\frac{1}{2}\log\left(\frac{S''(0)}{S''(0)|_{g=0}}\right) = -\frac{1}{2}\log(1 - g).$$

**Step 4: Expand as a power series in g.**

Use the Taylor series $\log(1 - g) = -\sum_{k=1}^{\infty} \frac{g^k}{k}$:

$$-\frac{1}{2}\log(1 - g) = -\frac{1}{2} \left(-\sum_{k=1}^{\infty} \frac{g^k}{k}\right) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}.$$

Extract the first three terms:
$$\log(Z/Z_0) = \frac{1}{2}\left(\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \cdots\right) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

**Step 5: Verify the critical subchecks.**

1. **Saddle point identification:** $x_c = 0$ is the only saddle by $S'(0) = 0$ and $S'(x) \propto x(\cdots)$ for small $x$.

2. **Second derivative at saddle:** $S''(0) = 1 - g$. The crucial point is that the $\cosh$ term contributes only $-g$ (via $\cosh(0)=1$) to the $x^2$ term's coefficient; higher-order terms in the $\cosh$ expansion ($\cosh(x) = 1 + x^2/2 + \cdots$) multiply the already-present $x^2$ factor, yielding $O(x^4)$ corrections that vanish at $x=0$.

3. **1-loop formula:** Applied as $-\frac{1}{2}\log(S''(0)) = -\frac{1}{2}\log(1-g)$.

4. **Taylor expansion:** $g/2 + g^2/4 + g^3/6 + \cdots$ matches the pattern $\sum_{k=1}^{\infty} \frac{g^k}{2k}$.

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Or in closed form: $\log(Z/Z_0) = -\frac{1}{2}\log(1 - g)$.

## Distinction from ex_3_26

In ex_3_26, the cubic term $S_{\text{int}} = -gx^3/6$ enters at 2-loop and higher via necklace diagrams; the 1-loop is purely from the logarithm of the Hessian at the saddle. In the target, the $\cosh(x)$ term is also quadratic in structure (it multiplies $x^2$), so it also contributes only to the Hessian shift at 1-loop, consistent with the formula. The difference is parametric, not conceptual.
