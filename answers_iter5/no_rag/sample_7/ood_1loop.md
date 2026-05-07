# 1-Loop Partition Function: Saddle Point Expansion

## Problem Statement
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$$

where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free (g=0) partition function. Expand the answer as a power series in $g$ through order $g^3$.

## Solution

### Step 1: Identify the Saddle Point

The saddle point is determined by $S'(x) = 0$:
$$S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)$$

At $x = 0$:
- $\cosh(0) = 1$
- $\sinh(0) = 0$

So $S'(0) = 0$ exactly for any $g$. Therefore, the saddle point is $\boxed{x_c = 0}$.

### Step 2: Compute the Second Derivative at the Saddle Point

We need $S''(x)$:
$$S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)$$

$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$
$$= 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
$$S''(0) = 1 - g \cdot 1 - 2g \cdot 0 - \frac{g}{2} \cdot 0 \cdot 1 = 1 - g$$

For reference, when $g = 0$: $S''(0)|_{g=0} = 1$.

### Step 3: Apply the 1-Loop Saddle Point Formula

In the semiclassical approximation, the 1-loop correction to the partition function (assuming a single non-degenerate saddle point) is:
$$\log\left(\frac{Z}{Z_0}\right) = -\frac{1}{2}\log\left(\frac{S''(0)}{S''(0)|_{g=0}}\right) = -\frac{1}{2}\log(1 - g)$$

### Step 4: Expand as a Power Series in g

We use the Taylor expansion:
$$-\frac{1}{2}\log(1 - g) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}$$

$$= \frac{1}{2}\left(\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right)$$

$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

Through order $g^3$:
$$\log\left(\frac{Z}{Z_0}\right) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

### Step 5: Why Higher-Order Interactions Don't Contribute at 1-Loop

A natural question: don't the nonlinear terms in $S(x)$ (from expanding $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$) contribute at 1-loop?

Answer: No. At the saddle point $x_c = 0$, the action is:
$$S(0) = 0 - \frac{g}{2} \cdot 0 \cdot \cosh(0) = 0$$

When we expand $\cosh(x)$ in powers of $x$:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots\right)$$
$$= \frac{x^2}{2} - \frac{g}{2}x^2 - \frac{g}{4}x^4 - \frac{g}{48}x^6 - \cdots$$

The cubic term is absent (all terms are even powers). The 1-loop determinant depends only on $S''(0)$, which receives contributions only from the $x^2$ terms. The cubic and higher terms affect only 2-loop and higher-order corrections, not the 1-loop logarithmic term.

## Final Answer

Through order $g^3$:

$$\boxed{\log\left(\frac{Z}{Z_0}\right) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Or equivalently:
$$\boxed{\log\left(\frac{Z}{Z_0}\right) = -\frac{1}{2}\log(1-g) = \sum_{k=1}^{\infty} \frac{g^k}{2k}}$$

**Critical checks:**
1. Saddle point: $x_c = 0$ ✓
2. Second derivative at saddle: $S''(0) = 1 - g$ ✓
3. 1-loop formula: $-\frac{1}{2}\log(1-g)$ ✓
4. Series coefficients: $\frac{1}{2k}$ for $g^k$ term, giving $\frac{1}{2}, \frac{1}{4}, \frac{1}{6}$ for $k=1,2,3$ ✓
