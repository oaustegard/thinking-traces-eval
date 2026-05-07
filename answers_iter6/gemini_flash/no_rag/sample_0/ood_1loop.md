To compute the 1-loop contribution to $\log(Z/Z_0)$ for the given zero-dimensional action, we will use the saddle-point approximation, which is the standard method for evaluating path integrals in the semi-classical (or loop) expansion.

The partition function is given by $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$, where $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.
The free partition function $Z_0$ corresponds to $g=0$, so $S_0(x) = x^2/2$.

**1. Saddle-point approximation for $Z$:**
For small $\hbar$, we can approximate the integral $Z$ by expanding the action $S(x)$ around its classical minimum $x_{cl}$.
$S(x) = S(x_{cl}) + \frac{1}{2} S''(x_{cl}) (x-x_{cl})^2 + \frac{1}{6} S'''(x_{cl}) (x-x_{cl})^3 + \dots$
Substituting this into the integral for $Z$:
$Z = e^{-S(x_{cl})/\hbar} \int_{-\infty}^{\infty} dx \exp\left(-\frac{1}{2\hbar} S''(x_{cl}) (x-x_{cl})^2 - \frac{1}{6\hbar} S'''(x_{cl}) (x-x_{cl})^3 - \dots\right)$

The **0-loop (classical) contribution** is $e^{-S(x_{cl})/\hbar}$.
The **1-loop contribution** arises from the Gaussian integral involving the quadratic term in the expansion of $S(x)$:
$\int_{-\infty}^{\infty} dx \exp\left(-\frac{1}{2\hbar} S''(x_{cl}) (x-x_{cl})^2\right) = \sqrt{\frac{2\pi\hbar}{S''(x_{cl})}}$.
Therefore, the 1-loop approximation for $\log Z$ is:
$\log Z \approx -S(x_{cl})/\hbar - \frac{1}{2} \log(S''(x_{cl})) + \frac{1}{2} \log(2\pi\hbar)$.
The term $-S(x_{cl})/\hbar$ is the classical part, and $-\frac{1}{2} \log(S''(x_{cl}))$ is the 1-loop quantum correction.

**2. Evaluate $x_{cl}$, $S(x_{cl})$, and $S''(x_{cl})$ for the given action:**
The action is $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.
First, find the classical minimum $x_{cl}$ by setting $S'(x)=0$:
$S'(x) = \frac{d}{dx} \left(\frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)\right)$
$S'(x) = x - \frac{g}{2} (2x \cosh(x) + x^2 \sinh(x))$
$S'(x) = x (1 - g \cosh(x) - \frac{g}{2} x \sinh(x))$.
Setting $S'(x)=0$, we see that $x_{cl}=0$ is a solution. For small $g$, this is the relevant minimum.

Next, evaluate $S(x_{cl})$:
$S(0) = 0^2/2 - (g/2) 0^2 \cosh(0) = 0$.

Next, evaluate $S''(x_{cl})$:
$S''(x) = \frac{d}{dx} \left(x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x)\right)$
$S''(x) = 1 - g(\cosh(x) + x\sinh(x)) - \frac{g}{2}(2x\sinh(x) + x^2\cosh(x))$
$S''(x) = 1 - g\cosh(x) - g x\sinh(x) - g x\sinh(x) - \frac{g}{2} x^2\cosh(x)$
$S''(x) = 1 - g\cosh(x) - 2g x\sinh(x) - \frac{g}{2} x^2\cosh(x)$.
Now, evaluate at $x_{cl}=0$:
$S''(0) = 1 - g\cosh(0) - 2g (0)\sinh(0) - \frac{g}{2} (0)^2\cosh(0)$
$S''(0) = 1 - g(1) - 0 - 0 = 1-g$.

So, the 1-loop approximation for $\log Z$ is:
$\log Z \approx -0/\hbar - \frac{1}{2} \log(1-g) + \frac{1}{2} \log(2\pi\hbar) = -\frac{1}{2} \log(1-g) + \frac{1}{2} \log(2\pi\hbar)$.

**3. Evaluate $\log Z_0$:**
For the free partition function, $S_0(x) = x^2/2$.
$x_{cl,0}=0$.
$S_0(0)=0$.
$S_0''(x) = 1$, so $S_0''(0)=1$.
Using the same 1-loop formula for $\log Z_0$:
$\log Z_0 \approx -S_0(0)/\hbar - \frac{1}{2} \log(S_0''(0)) + \frac{1}{2} \log(2\pi\hbar)$
$\log Z_0 \approx -0/\hbar - \frac{1}{2} \log(1) + \frac{1}{2} \log(2\pi\hbar) = \frac{1}{2} \log(2\pi\hbar)$.
This is consistent with the exact value $Z_0 = \sqrt{2\pi\hbar}$.

**4. Compute the 1-loop contribution to $\log(Z/Z_0)$:**
$\log(Z/Z_0) = \log Z - \log Z_0$
$\log(Z/Z_0) \approx \left(-\frac{1}{2} \log(1-g) + \frac{1}{2} \log(2\pi\hbar)\right) - \left(\frac{1}{2} \log(2\pi\hbar)\right)$
$\log(Z/Z_0) \approx -\frac{1}{2} \log(1-g)$.

**5. Expand the result as a power series in $g$ through order $g^3$:**
We use the Taylor series expansion for $\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$.
Substituting $u=g$:
$\log(Z/Z_0) \approx -\frac{1}{2} \left(-g - \frac{g^2}{2} - \frac{g^3}{3}\right) + O(g^4)$
$\log(Z/Z_0) \approx \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

The 1-loop contribution to $\log(Z/Z_0)$, expanded to order $g^3$, is $\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}$.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$.