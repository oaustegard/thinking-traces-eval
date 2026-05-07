# 1-Loop Partition Function Calculation

## Problem Statement
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$

where $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$ and $Z_0$ is the free (g=0) partition function. Expand as a power series in $g$ through order $g^3$.

## Solution

### Step 1: Identify the Saddle Point

The saddle point satisfies $S'(x_c) = 0$.

$$S'(x) = x - gx \cosh(x) - \frac{g}{2} x^2 \sinh(x)$$

At $x = 0$:
$$S'(0) = 0 - 0 - 0 = 0$$

By inspection, $x_c = 0$ is a critical point. For small $g$ perturbation theory, this saddle point persists.

### Step 2: Compute the Second Derivative at the Saddle

$$S''(x) = 1 - g[\cosh(x) + x \sinh(x)] - g[2x \sinh(x) + x^2 \cosh(x)]$$

$$= 1 - g \cosh(x) - gx \sinh(x) - 2gx \sinh(x) - \frac{g}{2} x^2 \cosh(x)$$

$$= 1 - g \cosh(x) - 3gx \sinh(x) - \frac{g}{2} x^2 \cosh(x)$$

At $x = 0$:
- $\cosh(0) = 1$
- $\sinh(0) = 0$

$$S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g$$

For the free theory ($g = 0$): $S''_0(0) = 1$.

### Step 3: Apply the 1-Loop Formula

The 1-loop quantum correction to the partition function is given by:
$$\log(Z/Z_0) = -\frac{1}{2} \log\left(\frac{S''(x_c)}{S''_0(0)}\right)$$

This comes from the ratio of Gaussian path integrals:
$$\frac{Z}{Z_0} = \sqrt{\frac{S''_0(0)}{S''(x_c)}} = \left(\frac{1}{1-g}\right)^{1/2}$$

Therefore:
$$\log(Z/Z_0) = -\frac{1}{2} \log(1 - g)$$

### Step 4: Taylor Expansion in Powers of $g$

Use the power series expansion:
$$-\frac{1}{2} \log(1 - g) = \frac{1}{2} \sum_{k=1}^{\infty} \frac{g^k}{k}$$

$$= \frac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right)$$

$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

Collecting terms through order $g^3$:

$$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

### Step 5: Verification of Subchecks

1. **Saddle point identification**: $x_c = 0$ satisfies $S'(0) = 0$ ✓
2. **Second derivative at saddle**: $S''(0) = 1 - g$ (not $-g$, but $1-g$ from the correct evaluation of the cosh term and the quadratic envelope) ✓
3. **Application of 1-loop formula**: Uses $-\frac{1}{2} \log(S''(0))$ with $S''(0) = 1 - g$ ✓
4. **Power series expansion**: Correctly expands $-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum \frac{g^k}{k}$ with coefficients $\frac{1}{2k}$ ✓

**Note on higher loops**: The cubic terms in $S$ (arising from $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$) contribute to the interaction terms at the saddle point $x_c = 0$. However, these contribute only to 2-loop and higher order corrections. At 1-loop, they do not appear in $\log(Z/Z_0)$ since the 1-loop calculation involves only the quadratic (Gaussian) part of the action around the saddle.

## Final Answer

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Or in compact form:
$$\boxed{\log(Z/Z_0) = \sum_{k=1}^{3} \frac{g^k}{2k} + O(g^4)}$$
