## Reasoning trace

**1. Definition of 1-loop contribution to $\log(Z/Z_0)$ in zero dimensions.**

For a zero-dimensional quantum field theory with action $S(x)$, the partition function is $Z = \int e^{-S(x)/\hbar}\,dx$. The free partition function is $Z_0 = \int e^{-S_0(x)/\hbar}\,dx$, where $S_0(x) = x^2/2$.

In zero dimensions, the 1-loop contribution to $\log Z$ is given by the leading-order saddle-point (Gaussian) approximation. If $x_0$ is a critical point of $S(x)$ (i.e., $S'(x_0)=0$), then
$$Z \approx \sqrt{\frac{2\pi\hbar}{S''(x_0)}} e^{-S(x_0)/\hbar}.$$
Taking the logarithm, we get
$$\log Z \approx -\frac{S(x_0)}{\hbar} - \frac{1}{2}\log S''(x_0) + \frac{1}{2}\log(2\pi\hbar).$$
The term $-S(x_0)/\hbar$ is the classical (tree-level) contribution, and $-\frac{1}{2}\log S''(x_0)$ is the 1-loop contribution (ignoring the $\hbar$-dependent constant term, which is a normalization).

For the free theory, $S_0(x) = x^2/2$. The critical point is $x_0=0$. $S_0(0)=0$ and $S_0''(0)=1$.
So $\log Z_0 \approx -\frac{1}{2}\log S_0''(0) + \frac{1}{2}\log(2\pi\hbar) = 0 + \frac{1}{2}\log(2\pi\hbar)$.

Combining these, the 1-loop contribution to $\log(Z/Z_0)$ is:
$$\log(Z/Z_0) = \log Z - \log Z_0 \approx -\frac{S(x_0)}{\hbar} - \frac{1}{2}\log S''(x_0).$$
In this problem, we need to find the critical point $x_0$ for the given action $S(x)$ and evaluate $S(x_0)$ and $S''(x_0)$.

**2. Finding the critical point and evaluating $S(x_0)$ and $S''(x_0)$.**

The given action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh x$.
First, calculate the first derivative $S'(x)$:
$$S'(x) = \frac{d}{dx}\left(\frac{x^2}{2}\right) - \frac{g}{2}\frac{d}{dx}(x^2 \cosh x)$$
$$S'(x) = x - \frac{g}{2}(2x \cosh x + x^2 \sinh x)$$
$$S'(x) = x - gx \cosh x - \frac{g}{2}x^2 \sinh x.$$
To find the critical point $x_0$, we set $S'(x_0)=0$.
$$x_0 - gx_0 \cosh x_0 - \frac{g}{2}x_0^2 \sinh x_0 = 0.$$
One obvious solution is $x_0=0$. Let's check if $x_0=0$ is indeed the relevant critical point for the 1-loop calculation. For small $g$, the potential is still dominated by the quadratic term, so $x_0=0$ remains the minimum.
At $x_0=0$:
$S(0) = \frac{0^2}{2} - \frac{g}{2} (0)^2 \cosh(0) = 0$.

Next, calculate the second derivative $S''(x)$:
$$S''(x) = \frac{d}{dx}\left(x - gx \cosh x - \frac{g}{2}x^2 \sinh x\right)$$
$$S''(x) = 1 - g(\cosh x + x \sinh x) - \frac{g}{2}(2x \sinh x + x^2 \cosh x)$$
$$S''(x) = 1 - g\cosh x - gx \sinh x - gx \sinh x - \frac{g}{2}x^2 \cosh x$$
$$S''(x) = 1 - g\cosh x - 2gx \sinh x - \frac{g}{2}x^2 \cosh x.$$
Now, evaluate $S''(x)$ at the critical point $x_0=0$:
$$S''(0) = 1 - g\cosh(0) - 2g(0)\sinh(0) - \frac{g}{2}(0)^2\cosh(0)$$
$$S''(0) = 1 - g(1) - 0 - 0 = 1 - g.$$

**3. Computing the 1-loop contribution and expanding in $g$.**

Using the formula derived in step 1, and with $S(0)=0$:
The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log S''(0)$.
$$-\frac{1}{2}\log S''(0) = -\frac{1}{2}\log(1-g).$$
Finally, we need to expand this result as a power series in $g$ through order $g^3$.
Recall the Taylor series for $\log(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - O(x^4)$.
Substituting $x=g$:
$$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$$
$$-\frac{1}{2}\log(1-g) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

## Final answer

The 1-loop contribution to $\log(Z/Z_0)$ for the given action is $-\frac{1}{2}\log(1-g)$.
Expanding this as a power series in $g$ through order $g^3$, we get:
$$\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$