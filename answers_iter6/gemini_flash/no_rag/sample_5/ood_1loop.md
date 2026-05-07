The problem asks for the 1-loop contribution to $\log(Z/Z_0)$ for a zero-dimensional action $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$. We need to expand this result as a power series in $g$ through order $g^3$.

**1. Define the Partition Functions**

The partition function $Z$ is given by the integral:
$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$
where $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.

The free partition function $Z_0$ corresponds to $g=0$, so $S_0(x) = x^2/2$:
$Z_0 = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx$

**2. Compute $Z_0$**

This is a standard Gaussian integral: $\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\pi/a}$.
Here, $a = 1/(2\hbar)$.
$Z_0 = \sqrt{\pi / (1/(2\hbar))} = \sqrt{2\pi\hbar}$.

**3. The 1-Loop Approximation**

In a zero-dimensional integral, the "loop expansion" is equivalent to the saddle-point approximation (also known as the WKB or semi-classical approximation). The action is expanded around its classical minimum $x_0$.
$S(x) = S(x_0) + \frac{1}{2}S''(x_0)(x-x_0)^2 + \frac{1}{6}S'''(x_0)(x-x_0)^3 + \frac{1}{24}S^{(4)}(x_0)(x-x_0)^4 + \dots$

First, let's find the classical minimum $x_0$.
$S'(x) = x - (g/2) (2x \cosh(x) + x^2 \sinh(x)) = x(1 - g \cosh(x) - (g/2) x \sinh(x))$.
Setting $S'(x_0) = 0$, we find $x_0=0$ is a solution for any $g$. (For $g>1$, there can be other minima, but for perturbative expansion in $g$, we assume $g$ is small and $x=0$ is the dominant saddle point).

Now, evaluate the derivatives of $S(x)$ at $x_0=0$:
$S(0) = 0$.

$S''(x) = \frac{d}{dx} [x(1 - g \cosh(x) - (g/2) x \sinh(x))]$
$S''(x) = (1 - g \cosh(x) - (g/2) x \sinh(x)) + x(-g \sinh(x) - (g/2) (\sinh(x) + x \cosh(x)))$.
At $x=0$:
$S''(0) = (1 - g \cosh(0) - 0) + 0 = 1 - g$.

Since $S(x)$ is an even function of $x$ (because $x^2$ and $\cosh(x)$ are even), all odd derivatives $S^{(2k+1)}(0)$ are zero.
$S'''(0)=0$, $S^{(5)}(0)=0$, etc.

The path integral can be expanded around the classical minimum $x_0=0$:
$Z = e^{-S(0)/\hbar} \int e^{-\frac{1}{2\hbar} S''(0)x^2 - \frac{1}{24\hbar} S^{(4)}(0)x^4 - \dots} dx$
Since $S(0)=0$:
$Z = \int e^{-\frac{1}{2\hbar} S''(0)x^2} e^{-\frac{1}{24\hbar} S^{(4)}(0)x^4 - \dots} dx$

The "1-loop contribution" to $\log Z$ is typically defined as the term proportional to $\hbar^0$ (or $\hbar^1$ if the classical action is included) in the expansion of $\log Z$, arising from the Gaussian integral of the quadratic part of the action.
In this case, the 1-loop approximation for $Z$ is obtained by keeping only the quadratic term in the action:
$Z_{1-\text{loop}} = \int_{-\infty}^{\infty} e^{-S''(0)x^2/(2\hbar)} dx$
This is another Gaussian integral with $a = S''(0)/(2\hbar)$.
$Z_{1-\text{loop}} = \sqrt{\frac{\pi}{S''(0)/(2\hbar)}} = \sqrt{\frac{2\pi\hbar}{S''(0)}}$.
Substituting $S''(0) = 1-g$:
$Z_{1-\text{loop}} = \sqrt{\frac{2\pi\hbar}{1-g}}$.

**4. Compute $\log(Z_{1-\text{loop}}/Z_0)$**

Now we can compute the 1-loop contribution to $\log(Z/Z_0)$:
$\log(Z_{1-\text{loop}}/Z_0) = \log\left(\frac{\sqrt{2\pi\hbar/(1-g)}}{\sqrt{2\pi\hbar}}\right)$
$= \log\left(\frac{1}{\sqrt{1-g}}\right)$
$= -\frac{1}{2} \log(1-g)$.

**5. Expand the Result in Powers of $g$**

We need to expand $-\frac{1}{2} \log(1-g)$ as a power series in $g$ through order $g^3$.
Recall the Taylor series expansion for $\log(1-x)$:
$\log(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \frac{x^4}{4} - \dots$

Substitute $x=g$:
$-\frac{1}{2} \log(1-g) = -\frac{1}{2} \left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

This result represents the 1-loop contribution to $\log(Z/Z_0)$, expanded to order $g^3$. It is independent of $\hbar$, which is characteristic of the 1-loop term when the classical action $S(x_0)=0$.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$.