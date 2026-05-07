# Solution: ood_1loop (1-loop effective action for cosh interaction)

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$
where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free partition function. Expand the answer as a power series in $g$ through order $g^3$.

## Solution

**Step 1: Identify the saddle point.**

The action is $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$.

Taking the derivative: $S'(x) = x - g x \cosh(x) - \frac{g}{2}x^2\sinh(x)$.

At $x = 0$: $S'(0) = 0$, so $x_c = 0$ is a critical point. By inspection and the dominance of the quadratic term for small $x$, this is the saddle in the semiclassical limit.

**Step 2: Compute the second derivative at the saddle.**

$$S''(x) = 1 - g\cosh(x) - g x \sinh(x) - g x\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

Simplifying: $S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$.

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) = 1 - g,$$
since $\sinh(0) = 0$ and the $x^2$ term vanishes.

At $g = 0$: $S''(0)|_{g=0} = 1$.

**Step 3: Apply the 1-loop formula.**

The 1-loop contribution to the effective action is
$$\log(Z/Z_0) = -\tfrac{1}{2}\log\frac{S''(x_c)}{S''(0)|_{g=0}} = -\tfrac{1}{2}\log(1 - g).$$

**Step 4: Taylor expansion in $g$.**

Using $\log(1-u) = -u - u^2/2 - u^3/3 - \cdots$:
$$\log(1-g) = -g - \frac{g^2}{2} - \frac{g^3}{3} - \cdots$$

Therefore:
$$-\tfrac{1}{2}\log(1-g) = \tfrac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \cdots\right) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

**Step 5: Verify the form.**

The cosh terms in $S(x)$ can be expanded: $\cosh(x) = 1 + x^2/2 + x^4/24 + \cdots$

So $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2(1 + x^2/2 + \cdots) = \frac{x^2}{2}(1 - g) - \frac{g}{4}x^4 - \cdots$

The quadratic part $\frac{x^2}{2}(1-g)$ gives the saddle-point calculation directly: $S''(0) = 1 - g$. The higher-order terms (cubic, quartic) from the cosh expansion do not contribute to the 1-loop $S_1$ at the saddle $x_c = 0$; they represent 2-loop and higher contributions. This confirms the result comes solely from the Gaussian fluctuation around the saddle.

**Step 6: Power series through order $g^3$.**

$$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4) = -\frac{1}{2}\log(1-g).$$

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

**Critical checks:**
- Saddle identified at $x_c = 0$ ✓
- Second derivative at saddle: $S''(0) = 1 - g$ ✓
- 1-loop formula applied: $-\frac{1}{2}\log(1-g)$ ✓
- Coefficients: $1/(2k)$ for order $g^k$ ✓
- No contribution from cubic terms in cosh (these are 2-loop and beyond) ✓
