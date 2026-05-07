The problem asks us to compute the 1-loop contribution to $\log(Z/Z_0)$ for a zero-dimensional action $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$, expanded as a power series in $g$ through order $g^3$.

The partition function $Z$ is given by $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$.
The free partition function $Z_0$ corresponds to $g=0$, so $S_0(x) = x^2/2$.
$Z_0 = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx = \sqrt{2\pi\hbar}$.

In quantum field theory, the loop expansion is an expansion in $\hbar$. For a zero-dimensional theory, the partition function can be evaluated using the saddle-point approximation (also known as the WKB approximation or the method of steepest descent).
The general formula for the partition function $Z = \int dx e^{-S(x)/\hbar}$ in the saddle-point approximation around a minimum $x_{cl}$ of $S(x)$ is:
$Z \approx e^{-S(x_{cl})/\hbar} \sqrt{\frac{2\pi\hbar}{S''(x_{cl})}} \left(1 + O(\hbar)\right)$.
Taking the logarithm, we get:
$\log Z \approx -\frac{S(x_{cl})}{\hbar} - \frac{1}{2} \log(S''(x_{cl})) + \frac{1}{2} \log(2\pi\hbar) + O(\hbar)$.

The term $-S(x_{cl})/\hbar$ is the classical (0-loop) contribution.
The term $-\frac{1}{2} \log(S''(x_{cl}))$ is the 1-loop contribution (independent of $\hbar$, or $O(\hbar^0)$ in the exponent).
Higher order terms in $\hbar$ (e.g., from the $x^4$ term in the expansion of $S(x)$ around $x_{cl}$) would correspond to 2-loop, 3-loop, etc., contributions. Since the problem asks for the "1-loop contribution," we only need to keep the terms up to $O(\hbar^0)$ in $\log Z$.

Let's find the classical minimum $x_{cl}$ for $S(x)$.
$S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.
To find $x_{cl}$, we set the first derivative $S'(x)$ to zero:
$S'(x) = x - (g/2) (2x \cosh(x) + x^2 \sinh(x))$.
$S'(x) = x (1 - g \cosh(x) - (g/2) x \sinh(x))$.
One obvious solution is $x_{cl}=0$. Let's check if it's a minimum.
We need the second derivative $S''(x)$:
$S''(x) = 1 - (g/2) (2\cosh(x) + 2x\sinh(x) + 2x\sinh(x) + x^2\cosh(x))$
$S''(x) = 1 - (g/2) (2\cosh(x) + 4x\sinh(x) + x^2\cosh(x))$.
At $x_{cl}=0$:
$S''(0) = 1 - (g/2) (2\cosh(0) + 0 + 0) = 1 - g$.
For $x_{cl}=0$ to be a minimum, we require $S''(0) > 0$, so $1-g > 0$, or $g<1$. We assume $g$ satisfies this condition.

Now we compute $\log(Z/Z_0)$ using the 1-loop approximation:
$\log Z = -\frac{S(0)}{\hbar} - \frac{1}{2} \log(S''(0)) + \frac{1}{2} \log(2\pi\hbar) + O(\hbar)$.
For the free theory ($g=0$), $S_0(x) = x^2/2$.
$S_0(0) = 0$.
$S_0''(0) = 1$.
$\log Z_0 = -\frac{S_0(0)}{\hbar} - \frac{1}{2} \log(S_0''(0)) + \frac{1}{2} \log(2\pi\hbar) + O(\hbar)$.
$\log Z_0 = 0 - \frac{1}{2} \log(1) + \frac{1}{2} \log(2\pi\hbar) + O(\hbar) = \frac{1}{2} \log(2\pi\hbar) + O(\hbar)$.

Now we can compute $\log(Z/Z_0)$:
$\log(Z/Z_0) = \log Z - \log Z_0$.
Using the 1-loop approximation, the $O(\hbar)$ terms cancel out, as do the $\frac{1}{2}\log(2\pi\hbar)$ terms.
$\log(Z/Z_0) = \left(-\frac{S(0)}{\hbar} - \frac{1}{2} \log(S''(0))\right) - \left(-\frac{S_0(0)}{\hbar} - \frac{1}{2} \log(S_0''(0))\right)$.
Since $S(0)=0$ and $S_0(0)=0$, the classical terms ($O(1/\hbar)$) vanish.
$\log(Z/Z_0) = -\frac{1}{2} \log(S''(0)) + \frac{1}{2} \log(S_0''(0))$.
Substitute the values $S''(0) = 1-g$ and $S_0''(0) = 1$:
$\log(Z/Z_0) = -\frac{1}{2} \log(1-g) + \frac{1}{2} \log(1)$.
$\log(Z/Z_0) = -\frac{1}{2} \log(1-g)$.

Finally, we need to expand this result as a power series in $g$ through order $g^3$.
Recall the Taylor expansion for $\log(1-u)$:
$\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$.
Substituting $u=g$:
$\log(1-g) = -g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)$.
Therefore:
$\log(Z/Z_0) = -\frac{1}{2} \left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$.
$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

The 1-loop contribution to $\log(Z/Z_0)$, expanded to order $g^3$, is $\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}$.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$