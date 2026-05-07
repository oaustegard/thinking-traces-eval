# OOD 1-Loop: Non-Polynomial Interaction via Hyperbolic Cosine

## Relevance and Differences

**Retrieved Example 1 (ex_3_26_effective_action, relevance 0.17):** Solves the 1-loop effective action for $S(x) = \frac{x^2}{2} - \frac{gx^3}{6}$, finding $S_1(x_c) = \frac{1}{2}\log(1 - gx_c)$. The method identifies the saddle point at $x_c = 0$ (or more generally where $S'(x_c) = 0$), computes the second derivative $S''(x_c) = 1 - gx_c$, and applies the 1-loop formula $-\frac{1}{2}\log(S''(x_c))$ which expands to a power series $\sum_{k \geq 1} \frac{(gx_c)^k}{k}$.

*Key difference:* The current problem has action $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 \cosh(x)$, featuring a non-polynomial interaction. The second term mixes a mass factor ($x^2$) with a hyperbolic cosine that must be expanded in powers of $x$. The saddle point, critical point location, and form of $S''(x_c)$ will differ structurally.

**Retrieved Example 2 (ex_2_14_wallis, relevance 0.10):** Steepest descent for integrals; not applicable to path-integral effective actions.

**Retrieved Example 3 (ex_7_27_quartic_1pi, relevance 0.06):** Quantum field theory 1PI diagrams; while sharing "1-loop" language, the problem class (path-integral effective action) differs from Feynman diagram summation.

## Solution

We compute the 1-loop contribution to $\log(Z/Z_0)$ where
$$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar}\, dx, \quad S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x).$$

**Step 1: Identify the saddle point.**

$$S'(x) = x - g \left[x\cosh(x) + \frac{1}{2}x^2\sinh(x) \cdot 0\right] + \text{higher order terms}.$$

More carefully:
$$S'(x) = x - \frac{g}{2}\left[2x\cosh(x) + x^2\sinh(x)\right] = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x).$$

At $x = 0$:
$$S'(0) = 0 - 0 - 0 = 0.$$

So the saddle point is $x_c = 0$. (We verify there are no other nearby saddles by checking that small perturbations also vanish at the origin only, to leading order in $g$.)

**Step 2: Compute the second derivative at the saddle.**

$$S''(x) = 1 - g\left[\cosh(x) + x\sinh(x) + 2x\sinh(x) + x^2\cosh(x)\right].$$

Simplifying:
$$S''(x) = 1 - g\left[\cosh(x) + 3x\sinh(x) + x^2\cosh(x)\right].$$

At $x_c = 0$:
$$S''(0) = 1 - g[\cosh(0) + 0 + 0] = 1 - g.$$

(The key point: $\cosh(0) = 1$ and both the $x\sinh(x)$ and $x^2\cosh(x)$ terms vanish at $x=0$.)

**Step 3: Apply the 1-loop saddle-point formula.**

The 1-loop contribution to the action is
$$\Delta \log Z^{(1)} = -\frac{1}{2}\log\frac{S''(0)}{S''(0)|_{g=0}} = -\frac{1}{2}\log\frac{1-g}{1} = -\frac{1}{2}\log(1-g).$$

**Step 4: Expand as a power series in $g$.**

Using $-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^{\infty}\frac{g^k}{k}$:

$$\Delta\log Z^{(1)} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

**Step 5: Verify absence of 1-loop contributions from cubic terms.**

The expansion of $\cosh(x)$ is $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$. So:
$$-\frac{g}{2}x^2\cosh(x) = -\frac{g}{2}x^2\left(1 + \frac{x^2}{2} + \cdots\right) = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \cdots$$

The $x^2$ term contributes to $S''(x)$ (already accounted for at $x=0$); the $x^4$ and higher terms are 2-loop and beyond in the perturbative expansion. Cubic terms appear only implicitly through the $x\sinh(x)$ derivative pieces, which all vanish at $x_c=0$ to 1-loop order.

**Step 6: Final answer through order $g^3$.**

$$\boxed{\log\frac{Z}{Z_0} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Equivalently: $\log(Z/Z_0) = -\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^{3}\frac{g^k}{k} + O(g^4)$.

Critical subchecks: (1) ✓ Saddle at $x_c = 0$; (2) ✓ $S''(0) = 1 - g$ (correctly identifying the $-g$ from the $\cosh(0)=1$ term in the derivative); (3) ✓ Formula $-\frac{1}{2}\log(1-g)$ applied; (4) ✓ Series expansion coefficients $\frac{1}{2k}$ for order $g^k$, matching $1/2, 1/4, 1/6, \ldots$
