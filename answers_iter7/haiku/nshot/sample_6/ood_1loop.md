# Solution: ood_1loop (1-loop for cosh-modulated action)

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action 
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x),$$
where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free ($g=0$) partition function. Expand as a power series in $g$ through order $g^3$.

## Solution

### Finding the saddle point

The action is:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x).$$

Compute the first derivative:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x) = x\left[1 - g\cosh(x) - \frac{g}{2}x\sinh(x)\right].$$

At $x_c = 0$: $S'(0) = 0$. Also, $S''(0) = 0 - g\cosh(0) - 0 = -g$ (from the first-order term). Wait—let me recalculate $S''(x)$.

$$S''(x) = 1 - g\cosh(x) - g x\sinh(x) - \frac{g}{2}\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

Ah—I need to expand $S(x)$ more carefully. The interaction term is $-(g/2)x^2 \cosh(x)$. Expand $\cosh(x) = 1 + x^2/2 + x^4/24 + \cdots$:
$$-(g/2)x^2(1 + x^2/2 + \cdots) = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \cdots$$

So:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 - \frac{g}{4}x^4 - \cdots = \frac{x^2}{2}(1-g) - \frac{g}{4}x^4 - \cdots$$

Taking derivatives:
$$S'(x) = x(1-g) - g x^3 - \cdots, \quad S''(x) = 1 - g - 3gx^2 - \cdots$$

At $x_c = 0$:
$$S'(0) = 0, \quad S''(0) = 1 - g.$$

**Saddle point:** $x_c = 0$ is indeed a saddle point.

### 1-loop contribution formula

The 1-loop contribution to the effective action (and thus to $\log Z$) is given by the determinant formula:
$$\log\frac{Z}{Z_0} = -\frac{1}{2}\log\frac{S''(0)}{S''(0)|_{g=0}} = -\frac{1}{2}\log(1-g).$$

(The factor $-1/2$ comes from the standard semiclassical result $S_1 = \frac{1}{2}\log S''(x_c)$ up to a constant.)

### Power series expansion

Expand $-\frac{1}{2}\log(1-g)$ using the Taylor series $\log(1-u) = -\sum_{k=1}^\infty u^k/k$ for $|u| < 1$:
$$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-\sum_{k=1}^\infty \frac{g^k}{k}\right) = \frac{1}{2}\sum_{k=1}^\infty \frac{g^k}{k}.$$

Extracting the first three terms:
$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

### Final answer

$$\boxed{\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

**Verification of critical components:**

1. **Saddle point identification:** $x_c = 0$ satisfies $S'(0) = 0$ ✓

2. **Second derivative at saddle:** $S''(0) = 1 - g$ (with higher-order $x^2$ terms in $S''(x) = 1 - g - 3gx^2 - \cdots$ vanishing at $x=0$) ✓

3. **Determinant formula application:** The 1-loop formula yields $-\frac{1}{2}\log(1-g)$ ✓

4. **Power series coefficients through $g^3$:** 
   - Coefficient of $g$: $1/(2 \cdot 1) = 1/2$ ✓
   - Coefficient of $g^2$: $1/(2 \cdot 2) = 1/4$ ✓
   - Coefficient of $g^3$: $1/(2 \cdot 3) = 1/6$ ✓

**Note on higher-order contributions:** The cosh interaction generates $x^4, x^6, \ldots$ terms in $S(x)$ via the expansion of $\cosh(x)$. These terms contribute to the $g^2$ and higher loop orders (2-loop and beyond), but do **not** contribute to the 1-loop $\log(Z/Z_0)$ at the saddle $x_c = 0$, since they are purely cubic and higher in the saddle-point expansion. The 1-loop result depends only on $S''(0)$, which receives contributions only from the $-gx^2$ piece of the interaction.
