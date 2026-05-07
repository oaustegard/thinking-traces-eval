## Reasoning trace

**1. Setup and Definitions:**
We are asked to compute the 1-loop contribution to $\log(Z/Z_0)$ for a zero-dimensional quantum field theory with action $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2} x^2 \cosh(x)$.
The partition function is $Z = \int e^{-S(x)/\hbar}\,dx$.
The free partition function is $Z_0 = \int e^{-S_0(x)/\hbar}\,dx$, where $S_0(x) = \tfrac{x^2}{2}$.

**2. 1-Loop Approximation in Zero Dimensions:**
In zero-dimensional QFT, the 1-loop approximation for the partition function $Z$ (or its logarithm $W = \hbar \log Z$) is given by the Gaussian integral around the classical solution.
Let $x_c$ be the classical solution, i.e., $S'(x_c) = 0$.
The general formula for $\log Z$ up to 1-loop order is:
$$ \log Z \approx -\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c) + \frac{1}{2}\log(2\pi\hbar). $$
This formula gives the coefficient of $\hbar^0$ (the classical action term), and the coefficient of $\hbar^1$ (the 1-loop quantum correction). The problem asks for the "1-loop contribution", which usually refers to the coefficient of $\hbar$ in $\log Z$.

**3. Calculate $S(x_c)$ and $S''(x_c)$ for the full action:**
Our action is $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2} x^2 \cosh(x)$.

First, find the classical solution $x_c$ by setting $S'(x)=0$:
$S'(x) = \frac{d}{dx}\left(\frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)\right) = x - \frac{g}{2}(2x\cosh x + x^2\sinh x) = x(1 - g\cosh x - \frac{g}{2}x\sinh x)$.
Setting $S'(x)=0$, we find $x=0$ is a solution. For small $g$, this is the minimum. So, $x_c = 0$.

Next, evaluate $S(x_c)$ and $S''(x_c)$ at $x_c=0$:
$S(0) = 0$.

$S''(x) = \frac{d}{dx}\left(x - g x\cosh x - \frac{g}{2}x^2\sinh x\right)$
$S''(x) = 1 - g(\cosh x + x\sinh x) - \frac{g}{2}(2x\sinh x + x^2\cosh x)$
$S''(x) = 1 - g\cosh x - g x\sinh x - g x\sinh x - \frac{g}{2}x^2\cosh x$
$S''(x) = 1 - g\cosh x - 2g x\sinh x - \frac{g}{2}x^2\cosh x$.
At $x_c=0$:
$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g$.

**4. Compute $\log Z$ to 1-loop order:**
Using the formula for $\log Z$:
$\log Z \approx -\frac{S(0)}{\hbar} - \frac{1}{2}\log S''(0) + \frac{1}{2}\log(2\pi\hbar)$
$\log Z \approx 0 - \frac{1}{2}\log(1-g) + \frac{1}{2}\log(2\pi\hbar)$.

**5. Compute $\log Z_0$ to 1-loop order:**
For the free action $S_0(x) = \tfrac{x^2}{2}$:
$S_0'(x) = x$, so $x_c=0$.
$S_0(0) = 0$.
$S_0''(x) = 1$, so $S_0''(0) = 1$.
$\log Z_0 \approx -\frac{S_0(0)}{\hbar} - \frac{1}{2}\log S_0''(0) + \frac{1}{2}\log(2\pi\hbar)$
$\log Z_0 \approx 0 - \frac{1}{2}\log(1) + \frac{1}{2}\log(2\pi\hbar) = \frac{1}{2}\log(2\pi\hbar)$.

**6. Compute the 1-loop contribution to $\log(Z/Z_0)$:**
The 1-loop contribution to $\log(Z/Z_0)$ is the coefficient of $\hbar$ in the expansion of $\log Z - \log Z_0$.
From the formulas above, the $\frac{1}{2}\log(2\pi\hbar)$ terms cancel out.
$\log(Z/Z_0) \approx \left(-\frac{1}{2}\log(1-g) + \frac{1}{2}\log(2\pi\hbar)\right) - \frac{1}{2}\log(2\pi\hbar)$
$\log(Z/Z_0) \approx -\frac{1}{2}\log(1-g)$.
This is the 1-loop contribution to $\log(Z/Z_0)$ (as the coefficient of $\hbar$ has been extracted or $\hbar=1$ is implicitly used for the interaction terms).

**7. Expand in $g$ through order $g^3$:**
We use the Taylor series expansion for $\log(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - O(x^4)$.
Substituting $x=g$:
$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

## Final answer

The 1-loop contribution to $\log(Z/Z_0)$ is given by:
$$-\frac{1}{2}\log(1-g).$$
Expanding this as a power series in $g$ through order $g^3$, we get:
$$\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$