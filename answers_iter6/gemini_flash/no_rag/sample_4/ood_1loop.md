To compute the 1-loop contribution to $\log(Z/Z_0)$ for the given zero-dimensional action, we first define $Z$ and $Z_0$:
$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$
$Z_0 = \int_{-\infty}^{\infty} e^{-S_0(x)/\hbar} dx$, where $S_0(x) = x^2/2$ is the free action (corresponding to $g=0$).

**1. Compute $Z_0$:**
The free action is $S_0(x) = x^2/2$.
$Z_0 = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx$.
This is a standard Gaussian integral of the form $\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\pi/a}$.
Here, $a = 1/(2\hbar)$.
So, $Z_0 = \sqrt{\frac{\pi}{1/(2\hbar)}} = \sqrt{2\pi\hbar}$.

**2. Determine the 1-loop approximation for $Z$:**
The 1-loop contribution in zero dimensions corresponds to approximating the action $S(x)$ by its quadratic expansion around its classical minimum $x_c$.
The given action is $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.

First, find the classical minimum $x_c$ by setting the first derivative of $S(x)$ to zero:
$S'(x) = \frac{d}{dx} \left( \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x) \right)$
$S'(x) = x - \frac{g}{2} (2x \cosh(x) + x^2 \sinh(x))$
$S'(x) = x \left( 1 - g \cosh(x) - \frac{g}{2} x \sinh(x) \right)$.
Setting $S'(x)=0$, we see that $x_c=0$ is a critical point. (For small $g$, this is the dominant minimum.)

Next, evaluate the action and its second derivative at $x_c=0$:
$S(0) = 0^2/2 - (g/2) (0)^2 \cosh(0) = 0$.

Now compute the second derivative $S''(x)$:
$S''(x) = \frac{d}{dx} \left( x - gx \cosh(x) - \frac{g}{2} x^2 \sinh(x) \right)$
$S''(x) = 1 - g(\cosh(x) + x \sinh(x)) - \frac{g}{2}(2x \sinh(x) + x^2 \cosh(x))$
$S''(x) = 1 - g \cosh(x) - gx \sinh(x) - gx \sinh(x) - \frac{g}{2} x^2 \cosh(x)$
$S''(x) = 1 - g \cosh(x) - 2gx \sinh(x) - \frac{g}{2} x^2 \cosh(x)$.
Evaluate $S''(x)$ at $x_c=0$:
$S''(0) = 1 - g \cosh(0) - 0 - 0 = 1 - g$.
For $x_c=0$ to be a minimum, we require $S''(0) > 0$, so $1-g > 0$, or $g < 1$. We assume $g$ is small and positive.

The 1-loop approximation for the action is $S(x) \approx S(x_c) + \frac{1}{2} S''(x_c) (x-x_c)^2$.
With $x_c=0$ and $S(0)=0$, this becomes $S(x) \approx \frac{1}{2} (1-g) x^2$.

Now, we compute the 1-loop partition function $Z_{1-loop}$ using this approximation:
$Z_{1-loop} = \int_{-\infty}^{\infty} e^{-\frac{1}{2\hbar}(1-g)x^2} dx$.
Again, this is a Gaussian integral with $a = (1-g)/(2\hbar)$.
$Z_{1-loop} = \sqrt{\frac{\pi}{(1-g)/(2\hbar)}} = \sqrt{\frac{2\pi\hbar}{1-g}}$.

**3. Compute $\log(Z/Z_0)$:**
Using the 1-loop approximation for $Z$:
$\log(Z_{1-loop}/Z_0) = \log\left(\frac{\sqrt{2\pi\hbar/(1-g)}}{\sqrt{2\pi\hbar}}\right)$
$= \log\left(\frac{1}{\sqrt{1-g}}\right)$
$= \log\left((1-g)^{-1/2}\right)$
$= -\frac{1}{2} \log(1-g)$.

**4. Expand the result as a power series in $g$ through order $g^3$:**
We use the Taylor series expansion for $\log(1-u)$:
$\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$.
Substituting $u=g$:
$-\frac{1}{2} \log(1-g) = -\frac{1}{2} \left( -g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4) \right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

This result represents the 1-loop contribution to $\log(Z/Z_0)$, expanded up to order $g^3$.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$