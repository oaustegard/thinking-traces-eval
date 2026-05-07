# Solution: 1-Loop Partition Function for Cosh Action

## Problem Statement
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$$

where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free ($g=0$) partition function. Expand through order $g^3$.

## Solution

### Step 1: Identify the Saddle Point
By inspection, $S'(0) = 0$ since:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2}x^2\sinh(x)$$

At $x = 0$: $S'(0) = 0$ (all terms vanish).

The saddle point is $x_c = 0$.

### Step 2: Compute the Second Derivative at the Saddle
$$S'(x) = x - g x \cosh(x) - \frac{g}{2}x^2\sinh(x)$$

Taking the derivative:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

$$= 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
- $\cosh(0) = 1$
- $\sinh(0) = 0$

$$S''(0) = 1 - g(1) - 0 - 0 = 1 - g$$

For the free theory ($g=0$): $S''(0)|_{g=0} = 1$.

### Step 3: Apply the 1-Loop Formula
The 1-loop contribution to the log partition function is:
$$\log(Z/Z_0)|_{\text{1-loop}} = -\frac{1}{2}\log\left(\frac{S''(0)}{S''(0)|_{g=0}}\right)$$

$$= -\frac{1}{2}\log(1 - g)$$

### Step 4: Taylor Expand in Powers of g
Using the series expansion $\log(1-u) = -\sum_{k=1}^{\infty} \frac{u^k}{k}$:

$$-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}$$

$$= \frac{1}{2}\left(\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \ldots\right)$$

$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \ldots$$

### Step 5: Verify the Physics
The key insight is that the cubic terms in $S(x)$ (from the Taylor expansion of $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \ldots$) contribute only at **2-loop and higher** in perturbation theory. At 1-loop, we only need $S''(0)$, which is determined by the quadratic and lower terms. The interaction $x^2 \cosh(x)$ affects $S''(0)$ through its coefficient in the quadratic part: $1 - g$ accounts for the $-g\cosh(0) = -g$ correction.

## Final Answer

The 1-loop contribution through order $g^3$ is:

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

**Coefficients:**
- $g^1$: $\frac{1}{2}$
- $g^2$: $\frac{1}{4}$
- $g^3$: $\frac{1}{6}$

**Key structure:** General coefficient of $g^k$ is $\frac{1}{2k}$ for $k \geq 1$.

**Remarks:**
- Saddle point: $x_c = 0$
- Curvature at saddle: $S''(0) = 1 - g$
- No higher-loop contributions at this order in $g$
- The nonlinear interaction in $S(x)$ manifests through the $g$-dependent curvature, not through separate vertex corrections at 1-loop
