# OOD 1-Loop Partition Function Solution

## Problem Setup

We compute the 1-loop contribution to $\log(Z/Z_0)$ for the action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$

where $Z$ is the partition function at coupling $g$ and $Z_0$ is the free theory ($g=0$) partition function. We expand the result as a power series in $g$ through order $g^3$.

## Step 1: Identify the Saddle Point

By inspection, $S'(0) = 0$ at $x = 0$, and this is the dominant saddle point (the boundary terms at $\pm\infty$ are suppressed for small $g$).

Thus: $x_c = 0$

## Step 2: Compute the Second Derivative of the Action

Taking derivatives of $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$:

$$S'(x) = x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x)$$

$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

$$S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
- $\cosh(0) = 1$
- $\sinh(0) = 0$

Therefore:
$$S''(0) = 1 - g$$

## Step 3: Apply the 1-Loop Formula

In the saddle-point approximation, the logarithm of the partition function ratio is:
$$\log\frac{Z}{Z_0} = -\frac{1}{2} \log\frac{S''(0)}{S''(0)|_{g=0}}$$

where $S''(0)|_{g=0} = 1$.

Thus:
$$\log\frac{Z}{Z_0} = -\frac{1}{2} \log(1 - g)$$

## Step 4: Taylor Expand in Powers of $g$

Using the series expansion $\log(1-u) = -\sum_{k=1}^{\infty} \frac{u^k}{k}$:

$$-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}$$

$$= \frac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right)$$

$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

## Step 5: Why Higher-Order Terms Don't Contribute at 1-Loop

The cubic and higher terms in the cosh expansion ($\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$) create vertices in the action like $x^4, x^6$, etc. These would appear in Feynman diagrams with internal propagators, which start at 2-loop order. At 1-loop, only the quadratic terms in the action (the second derivative at the saddle) matter; they determine the propagator. Corrections to the 1-loop log come only from the second derivative, which we have computed exactly.

## Answer

$$\boxed{\log\frac{Z}{Z_0} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Key features:
- Saddle point: $x_c = 0$
- Second derivative at saddle: $S''(0) = 1 - g$
- 1-loop formula: $\log(Z/Z_0) = -\frac{1}{2}\log(1-g)$
- Taylor coefficients: $\frac{1}{2k}$ for the $g^k$ term
- Cubic interactions in $S$ (from cosh) do not contribute to the 1-loop term; they enter only at 2-loop and beyond
