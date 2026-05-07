# One-Loop Computation for Zero-Dimensional QFT

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$
where $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$ and $Z_0$ is the free $(g=0)$ partition function.

Expand the answer as a power series in $g$ through order $g^3$.

## Solution

### Step 1: Identify the saddle point
For the saddle-point approximation, find where $S'(x) = 0$:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x)$$

At $x = 0$:
$$S'(0) = 0 - 0 - 0 = 0$$

So the saddle point is at $x_c = 0$ for all values of $g$.

### Step 2: Compute the second derivative at the saddle
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$
$$= 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g$$

For the free theory ($g=0$):
$$S''(0)\big|_{g=0} = 1$$

### Step 3: One-loop formula for $\log(Z/Z_0)$
In the saddle-point approximation, the 1-loop contribution is:
$$\log(Z/Z_0) = -\frac{1}{2}\log\frac{S''(0)}{S''(0)\big|_{g=0}}$$

Substituting:
$$\log(Z/Z_0) = -\frac{1}{2}\log(1-g)$$

### Step 4: Taylor expand $-\frac{1}{2}\log(1-g)$
Using the standard series $\log(1-g) = -\sum_{k=1}^{\infty} \frac{g^k}{k}$:

$$-\frac{1}{2}\log(1-g) = -\frac{1}{2} \left(-\sum_{k=1}^{\infty} \frac{g^k}{k}\right) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}$$

$$= \frac{1}{2}\left(\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right)$$

$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

### Step 5: Why cubic terms don't contribute at 1-loop
The interaction term in $S$ is $-\frac{g}{2}x^2\cosh(x)$. Expanding $\cosh(x)$ around $x=0$:
$$\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$$

So the interaction is:
$$-\frac{g}{2}x^2\left(1 + \frac{x^2}{2} + \cdots\right) = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \cdots$$

The cubic terms ($x^3$) do not appear in this expansion. Moreover, at 1-loop, we only evaluate the effective action at the saddle point $x_c = 0$. Higher-order cumulants (like the cubic vertex contributions) enter only at 2-loop and higher. The 1-loop correction is purely determined by the change in the second derivative of $S$ with respect to $g$.

## Final Answer

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

More explicitly:
$$\log(Z/Z_0) = \sum_{k=1}^{3} \frac{g^k}{2k} + O(g^4) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

**Key identifications:**
- Saddle point: $x_c = 0$
- Second derivative at saddle: $S''(0) = 1 - g$
- 1-loop formula: $-\frac{1}{2}\log(1-g)$
- Power series coefficients: $\frac{1}{2k}$ for $g^k$, giving $(1/2, 1/4, 1/6, \ldots)$ for $k = (1, 2, 3, \ldots)$
- Cubic interaction terms do not contribute to the 1-loop correction; they appear only at 2-loop and beyond
