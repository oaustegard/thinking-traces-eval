# Solution: 1-Loop Partition Function with Nonpolynomial Coupling

We compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$$

where $Z = \int_{-\infty}^\infty e^{-S(x)/\hbar} dx$ and $Z_0$ is the free ($g=0$) result.

## Step 1: Find the Saddle Point

The saddle point satisfies $S'(x) = 0$:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2}x^2 \sinh(x)$$
$$= x\left[1 - g\cosh(x) - \frac{g}{2}x\sinh(x)\right]$$

At $x = 0$:
$$S'(0) = 0 \cdot [1 - g \cdot 1 - 0] = 0$$

So $x_c = 0$ is the saddle point (for small $g$, this remains the dominant saddle).

## Step 2: Compute the Hessian at the Saddle

The second derivative is:
$$S''(x) = 1 - g\cosh(x) - g x\sinh(x) - g x\sinh(x) - \frac{g}{2}x^2\cosh(x)$$
$$= 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g$$

(Note: $\cosh(0) = 1$ and $\sinh(0) = 0$.)

## Step 3: Apply the 1-Loop Formula

The 1-loop partition function ratio is:
$$\frac{Z}{Z_0} \approx \exp\left[-\frac{1}{2}\log\frac{S''(0)}{S''_0}\right] = \exp\left[-\frac{1}{2}\log(1-g)\right]$$

where $S''_0 = 1$ (the $g=0$ case).

Therefore:
$$\log\frac{Z}{Z_0} = -\frac{1}{2}\log(1-g)$$

## Step 4: Taylor Expansion

Using the power series $\log(1-g) = -\sum_{k=1}^\infty \frac{g^k}{k}$:

$$\log\frac{Z}{Z_0} = -\frac{1}{2} \cdot \left(-\sum_{k=1}^\infty \frac{g^k}{k}\right) = \frac{1}{2}\sum_{k=1}^\infty \frac{g^k}{k}$$

Expanding through order $g^3$:
$$\log\frac{Z}{Z_0} = \frac{1}{2}\left[\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right]$$

$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

## Step 5: Verify No Higher-Loop Contributions at This Order

The cubic and higher-order terms in $S(x)$ arise from expanding $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$ and $\sinh(x) = x + \frac{x^3}{6} + \cdots$. These give contributions like $gx^4 + O(gx^6)$ in $S(x)$. The 2-loop and higher loop diagrams involve contracting these quartic vertices, which enter at 2-loop order and higher. The 1-loop calculation depends only on $S''(0)$, which is determined by the quadratic and linear terms in the action, not by the structure of higher-order interactions.

## Final Answer

$$\boxed{\log\frac{Z}{Z_0} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

or more compactly:

$$\boxed{\log\frac{Z}{Z_0} = -\frac{1}{2}\log(1-g) = \sum_{k=1}^\infty \frac{g^k}{2k}}$$

**Critical checks:** (1) Saddle point is at $x_c = 0$. (2) Second derivative at saddle: $S''(0) = 1 - g$. (3) 1-loop formula applied correctly: $-\frac{1}{2}\log(1-g)$. (4) Taylor series coefficients: $\frac{1}{2k}$ for the $g^k$ term, giving $g/2, g^2/4, g^3/6$ for the first three orders.
