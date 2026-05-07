# OOD 1-Loop: Logarithmic Divergence in Hyperbolic Potential

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$

where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free ($g=0$) partition function. Expand as a power series in $g$ through $O(g^3)$.

## Solution

### Step 1: Identify the Saddle Point
The saddle point is determined by:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x) = 0$$

By inspection, $x_c = 0$ is a solution (all terms vanish). We can verify this is the unique saddle for small $g$ by perturbation theory.

### Step 2: Compute the Second Derivative at the Saddle
$$S''(x) = 1 - g \cosh(x) - 2 g x \sinh(x) - \frac{g}{2} x^2 \cosh(x)$$

At $x = 0$:
- $\cosh(0) = 1$
- $\sinh(0) = 0$
- $x = 0$ eliminates all $x$-dependent terms

Thus:
$$S''(0) = 1 - g$$

### Step 3: Apply 1-Loop Formula
In the saddle-point approximation, the 1-loop contribution to the partition function is:
$$Z \approx \sqrt{\frac{2\pi\hbar}{S''(x_c)}} e^{-S(x_c)/\hbar}$$

The free partition function is:
$$Z_0 = \sqrt{\frac{2\pi\hbar}{S''_0(0)}} = \sqrt{2\pi\hbar}$$

where $S''_0(0) = 1$ (the $g=0$ second derivative).

Therefore:
$$\log(Z/Z_0) = \frac{1}{2} \log\left(\frac{S''(0)|_{g=0}}{S''(0)}\right) + \frac{1}{\hbar}[S(0)|_{g=0} - S(0)]$$

At $x_c = 0$, both $S(0) = 0$ and $S(0)|_{g=0} = 0$, so:
$$\log(Z/Z_0) = -\frac{1}{2} \log(1 - g)$$

(The negative sign arises because we have $\log(1 / (1-g))$.)

### Step 4: Taylor Expansion
$$-\frac{1}{2} \log(1 - g) = \frac{1}{2} \sum_{k=1}^{\infty} \frac{g^k}{k}$$

Explicitly through $O(g^3)$:
$$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

### Step 5: Verify No Higher-Order Contribution at 1-Loop
The cosh term in $S$ expands as:
$$\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \ldots$$

So:
$$x^2 \cosh(x) = x^2 + \frac{x^4}{2} + O(x^6)$$

The cubic and quartic terms generate vertices in the Feynman diagram, but 1-loop diagrams at a saddle point $x_c = 0$ receive contributions only from the quadratic part of the action (which determines $S''(0)$). Higher-order terms in the action contribute at 2-loop and higher. Thus the entire 1-loop result is captured by the logarithmic formula.

## Critical Subchecks

1. ✓ Saddle point: $x_c = 0$ (verified by $S'(0) = 0$)
2. ✓ Second derivative at saddle: $S''(0) = 1 - g$
3. ✓ 1-loop formula application: $-\frac{1}{2} \log(1-g)$
4. ✓ Taylor series coefficients: $g/2 + g^2/4 + g^3/6 + \ldots$

## Final Answer

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Or in closed form:
$$\boxed{\log(Z/Z_0) = -\frac{1}{2} \log(1-g) + O(g^4)}$$
