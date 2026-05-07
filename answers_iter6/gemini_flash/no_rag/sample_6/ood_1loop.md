To compute the 1-loop contribution to $\log(Z/Z_0)$ for the given zero-dimensional action, we first define the partition functions and the action.

The action is $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.
The partition function is $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$.
The free action (at $g=0$) is $S_0(x) = x^2/2$.
The free partition function is $Z_0 = \int_{-\infty}^{\infty} e^{-S_0(x)/\hbar} dx = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx$.

**1. Compute $Z_0$**:
This is a standard Gaussian integral: $\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\pi/a}$.
Here, $a = 1/(2\hbar)$.
So, $Z_0 = \sqrt{\frac{\pi}{1/(2\hbar)}} = \sqrt{2\pi\hbar}$.

**2. Interpret "1-loop contribution" in 0D**:
In zero-dimensional quantum field theory, the "1-loop contribution" to $\log Z$ (or the effective action $\Gamma[0]$) typically refers to the quadratic fluctuations around the classical minimum of the action.
For a general action $S(x)$, if $x_0$ is a classical minimum (i.e., $S'(x_0)=0$), then $\log Z$ can be approximated as:
$\log Z \approx -S(x_0)/\hbar + \frac{1}{2} \log\left(\frac{2\pi\hbar}{S''(x_0)}\right)$.
For the free theory, $S_0(x) = x^2/2$, the minimum is $x_0=0$.
$S_0'(x) = x \implies S_0'(0) = 0$.
$S_0''(x) = 1 \implies S_0''(0) = 1$.
So, $\log Z_0 = -S_0(0)/\hbar + \frac{1}{2} \log\left(\frac{2\pi\hbar}{S_0''(0)}\right) = 0 + \frac{1}{2} \log(2\pi\hbar)$.

For the interacting theory, $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.
First, find the classical minimum $x_0$.
$S'(x) = x - (g/2) (2x \cosh x + x^2 \sinh x) = x(1 - g \cosh x - (g/2) x \sinh x)$.
For $x=0$, $S'(0) = 0$. So $x_0=0$ is a classical minimum (for small $g$).
Now compute the second derivative at $x_0=0$:
$S''(x) = \frac{d}{dx} [x(1 - g \cosh x - (g/2) x \sinh x)]$
$S''(x) = (1 - g \cosh x - (g/2) x \sinh x) + x(-g \sinh x - (g/2) \sinh x - (g/2) x \cosh x)$.
$S''(x) = 1 - g \cosh x - (3g/2) x \sinh x - (g/2) x^2 \cosh x$.
Evaluating at $x=0$:
$S''(0) = 1 - g \cosh(0) - 0 - 0 = 1 - g$.

Thus, for the full theory, the 1-loop approximation for $\log Z$ is:
$\log Z \approx -S(0)/\hbar + \frac{1}{2} \log\left(\frac{2\pi\hbar}{S''(0)}\right) = 0 + \frac{1}{2} \log\left(\frac{2\pi\hbar}{1-g}\right)$.

The 1-loop contribution to $\log(Z/Z_0)$ is then:
$\log(Z/Z_0) = \log Z - \log Z_0 = \frac{1}{2} \log\left(\frac{2\pi\hbar}{1-g}\right) - \frac{1}{2} \log(2\pi\hbar)$.
$\log(Z/Z_0) = \frac{1}{2} \log\left(\frac{2\pi\hbar/(1-g)}{2\pi\hbar}\right) = \frac{1}{2} \log\left(\frac{1}{1-g}\right)$.

**3. Expand the result as a power series in $g$**:
We use the Taylor expansion for $\log(1-u)$: $\log(1-u) = - \sum_{n=1}^\infty \frac{u^n}{n}$.
Here, $u=g$.
$\log(Z/Z_0) = \frac{1}{2} (-\log(1-g)) = \frac{1}{2} \left( g + \frac{g^2}{2} + \frac{g^3}{3} + O(g^4) \right)$.
$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

This result includes terms up to order $g^3$, as requested. Note that this "1-loop" contribution in 0D is independent of $\hbar$. This is a common feature where $\hbar$ plays the role of a loop expansion parameter, and the 1-loop term is the leading quantum correction (often $\hbar^0$ in this context).

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$