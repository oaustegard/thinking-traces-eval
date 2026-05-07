## Reasoning trace

**1. Definition of 1-loop contribution in zero-dimensional QFT**

For a zero-dimensional quantum field theory with action $S(x)$, the partition function is $Z = \int e^{-S(x)/\hbar}\,dx$. The free partition function $Z_0$ corresponds to the case $g=0$, where $S_0(x) = x^2/2$. Thus $Z_0 = \int e^{-x^2/(2\hbar)}\,dx = \sqrt{2\pi\hbar}$.

The 1-loop approximation to $Z$ is obtained by evaluating the integral using the saddle-point method, expanding $S(x)$ around its classical minimum $x_c$. The classical field $x_c$ satisfies $S'(x_c)=0$.
Expanding $S(x)$ around $x_c$: $S(x) = S(x_c) + \frac{1}{2}S''(x_c)(x-x_c)^2 + O((x-x_c)^3)$.
The Gaussian integral approximation gives:
$Z \approx e^{-S(x_c)/\hbar} \int e^{-S''(x_c)(x-x_c)^2/(2\hbar)}\,d(x-x_c) = e^{-S(x_c)/\hbar} \sqrt{\frac{2\pi\hbar}{S''(x_c)}}$.
Taking the logarithm:
$\log Z \approx -\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c) + \frac{1}{2}\log(2\pi\hbar)$.

For $Z_0$, the action is $S_0(x) = x^2/2$. The classical minimum is $x_c=0$, and $S_0(0)=0$, $S_0''(0)=1$.
$\log Z_0 = -\frac{0}{\hbar} - \frac{1}{2}\log(1) + \frac{1}{2}\log(2\pi\hbar) = \frac{1}{2}\log(2\pi\hbar)$.

Therefore, the 1-loop contribution to $\log(Z/Z_0)$ is given by:
$\log(Z/Z_0) = \log Z - \log Z_0 = -\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c)$.
This expression gives the 1-loop contribution in the context of the $\hbar$ expansion (i.e., the $O(\hbar^0)$ terms in $\log Z$ after subtracting the free part, if $S(x_c)$ is $O(\hbar)$ or higher, and the $O(\hbar^1)$ terms from the $\log S''(x_c)$ factor). The problem specifically asks for the "1-loop contribution", which in zero dimensions is typically taken to mean this saddle-point evaluation.

**2. Identify the action and its derivatives**

The given action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.

First, find the classical minimum $x_c$ by solving $S'(x_c)=0$.
$S'(x) = \frac{d}{dx}\left(\frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)\right)$
$S'(x) = x - \frac{g}{2}(2x\cosh(x) + x^2\sinh(x))$
$S'(x) = x\left(1 - g\cosh(x) - \frac{g}{2}x\sinh(x)\right)$.
One obvious solution to $S'(x_c)=0$ is $x_c=0$. (We assume $g$ is small enough that $x_c=0$ is indeed a minimum, i.e., $S''(0)>0$).
At $x_c=0$, $S(0) = 0$.

Next, calculate $S''(x)$ and evaluate it at $x_c=0$.
$S''(x) = \frac{d}{dx}\left(x - \frac{g}{2}(2x\cosh(x) + x^2\sinh(x))\right)$
$S''(x) = 1 - \frac{g}{2}(2\cosh(x) + 2x\sinh(x) + 2x\sinh(x) + x^2\cosh(x))$
$S''(x) = 1 - \frac{g}{2}(2\cosh(x) + 4x\sinh(x) + x^2\cosh(x))$.
Now, substitute $x=0$:
$S''(0) = 1 - \frac{g}{2}(2\cosh(0) + 4(0)\sinh(0) + (0)^2\cosh(0))$
$S''(0) = 1 - \frac{g}{2}(2(1) + 0 + 0) = 1 - g$.

**3. Compute the 1-loop contribution**

Substitute $S(0)=0$ and $S''(0)=1-g$ into the formula for $\log(Z/Z_0)$:
$\log(Z/Z_0) = -\frac{0}{\hbar} - \frac{1}{2}\log(1-g) = -\frac{1}{2}\log(1-g)$.

**4. Expand as a power series in $g$ through order $g^3$**

Use the Taylor expansion for $\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$.
Let $u=g$:
$\log(Z/Z_0) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$
$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

## Final answer

The 1-loop contribution to $\log(Z/Z_0)$ is given by $-\frac{1}{2}\log S''(x_c)$, where $x_c$ is the classical minimum of the action $S(x)$.
For the given action $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$:
1. The classical minimum is $x_c=0$.
2. The second derivative of the action at the minimum is $S''(0) = 1 - g$.
Therefore, the 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log(1-g)$.

Expanding this expression as a power series in $g$ through order $g^3$ using $\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - \dots$:
$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$