# One-Loop Contribution to log(Z/Z₀) with Non-Polynomial Interaction

## Problem Setup
We compute the one-loop contribution to the logarithm of the partition function ratio for
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x),$$
where $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$ and $Z_0$ is the free partition function at $g=0$.

We seek the power series expansion of $\log(Z/Z_0)$ in $g$ through order $g^3$.

## Step 1: Identify the Saddle Point
The saddle point $x_c$ satisfies $S'(x_c) = 0$:
$$S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x).$$

At $x = 0$: 
$$S'(0) = 0 - 0 - 0 = 0,$$
so $x_c = 0$ is the saddle point for all $g$.

## Step 2: Compute the Second Derivative at the Saddle
$$S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

At $x = 0$, using $\cosh(0) = 1$ and $\sinh(0) = 0$:
$$S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g.$$

Note: The crucial point is that the term $(g/2)x^2\cosh(x)$ contributes to $S''$ via its $x^2$ prefactor; at $x=0$ this vanishes, leaving only the direct coefficient $-g$ from the $-gx\cosh(x)$ term.

## Step 3: Apply the One-Loop Formula
In the saddle-point approximation, the one-loop contribution is
$$\log\left(\frac{Z}{Z_0}\right)_{\text{1-loop}} = -\frac{1}{2} \log\left(\frac{S''(0)}{S''(0)|_{g=0}}\right) = -\frac{1}{2} \log\left(\frac{1-g}{1}\right) = -\frac{1}{2} \log(1-g).$$

## Step 4: Power Series Expansion
Expand using the Taylor series $\log(1-u) = -\sum_{k=1}^{\infty} \frac{u^k}{k}$ with $u = g$:
$$\log(1-g) = -g - \frac{g^2}{2} - \frac{g^3}{3} - \frac{g^4}{4} - \cdots$$

Therefore:
$$-\frac{1}{2} \log(1-g) = \frac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \cdots\right) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \cdots$$

## Step 5: Note on Higher-Order Corrections
The cosh expansion $\cosh(x) = 1 + x^2/2 + x^4/24 + \cdots$ shows that $x^2\cosh(x)$ contains terms like $x^4/2 + x^6/24 + \cdots$. These higher-order terms do not contribute to the second derivative at $x_c = 0$ and only enter at the two-loop level and beyond. Therefore, they do not affect the one-loop result we compute.

## Summary of Key Results
- **Saddle point:** $x_c = 0$
- **Second derivative:** $S''(0) = 1 - g$
- **One-loop log ratio:** $\log(Z/Z_0) = -\frac{1}{2}\log(1-g)$
- **Power series coefficients:** Coefficient of $g^k$ is $\frac{1}{2k}$

## Final Answer

Through order $g^3$:

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Or written as a series:
$$\boxed{\log(Z/Z_0) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \cdots}$$

The general coefficient of $g^k$ is $\frac{1}{2k}$.
