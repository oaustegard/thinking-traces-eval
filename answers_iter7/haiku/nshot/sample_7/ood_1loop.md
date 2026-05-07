# Solution: ood_1loop (1-loop partition function with cosh interaction)

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 \cosh(x)$, where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free partition function. Expand as a power series in $g$ through order $g^3$.

## Solution

**Saddle-point identification.** First, find the critical point:
$$S'(x) = x - \frac{g}{2}(2x \cosh(x) + x^2 \sinh(x)) = x - g x \cosh(x) - \frac{g}{2}x^2 \sinh(x)$$

At $x = 0$: $S'(0) = 0$ and $\cosh(0) = 1$, $\sinh(0) = 0$. So $x_c = 0$ is the saddle point.

**Second derivative at saddle.** We need:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$
$$= 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g$$

**1-loop effective action formula.** Using the standard result:
$$S_1(x_c) = \frac{1}{2}\log S''(x_c) = \frac{1}{2}\log(1-g)$$

Therefore:
$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{1}{2}\log(1-g)$$

**Power series expansion.** Apply the Taylor expansion $\log(1-u) = -\sum_{k \geq 1} \frac{u^k}{k}$:
$$\frac{1}{2}\log(1-g) = -\frac{1}{2}\sum_{k \geq 1} \frac{g^k}{k}$$

Computing term-by-term:
$$= -\frac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right)$$

$$= -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \frac{g^4}{8} - \cdots$$

Through order $g^3$:
$$\boxed{\log(Z/Z_0)|_{1\text{-loop}} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4)}$$

Or equivalently in standard form:
$$\log(Z/Z_0)|_{1\text{-loop}} = \sum_{k \geq 1} \frac{-g^k}{2k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \cdots \text{ (note sign)}$$

Wait, let me recalculate: $\frac{1}{2}\log(1-g)$ with $\log(1-g) < 0$ for $g > 0$, so the result is **negative**:
$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{1}{2}\log(1-g) = \frac{1}{2}\left(-\sum_{k=1}^\infty \frac{g^k}{k}\right) = -\sum_{k=1}^\infty \frac{g^k}{2k}$$

$$= -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \cdots$$

**Critical checks:**
1. Saddle point: $x_c = 0$ is correct (action is even-preserving at zeroth order). ✓
2. Second derivative: $S''(0) = 1 - g \cdot 1 = 1 - g$. ✓ (The key is that $\cosh(0) = 1$ dominates and other derivatives vanish.)
3. 1-loop formula applied: $\frac{1}{2}\log(1-g)$. ✓
4. Expansion coefficients: At order $g^k$, coefficient is $-1/(2k)$:
   - Order $g$: $-1/2$. ✓
   - Order $g^2$: $-1/4$. ✓
   - Order $g^3$: $-1/6$. ✓

**Note on higher-order contributions.** The cubic and higher terms in $S$ from $\cosh(x) = 1 + x^2/2 + x^4/24 + \cdots$ do NOT contribute to the 1-loop $\log(Z/Z_0)$ at the saddle $x_c = 0$ because the 1-loop result depends only on $S''(0)$, which is determined by the mass term and the leading cosh term. All polynomial corrections (cubic, quartic, ...) from the cosh expansion contribute only at 2-loop and higher order.

$$\boxed{\text{Final Answer: } \log(Z/Z_0)|_{1\text{-loop}} = \frac{1}{2}\log(1-g) = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4)}$$
