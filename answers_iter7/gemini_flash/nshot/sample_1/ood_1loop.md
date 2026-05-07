## Reasoning trace

**1. Define the partition functions and the goal.**
The problem asks for the 1-loop contribution to $\log(Z/Z_0)$, where $Z = \int e^{-S(x)/\hbar}\,dx$ and $Z_0$ is the free partition function ($g=0$).
The action is $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2} x^2 \cosh(x)$.
The free action is $S_0(x) = \tfrac{x^2}{2}$.

**2. Evaluate $Z$ and $Z_0$ using the 1-loop (Gaussian) approximation.**
In zero-dimensional quantum field theory, the 1-loop approximation for a partition function $Z = \int e^{-S(x)/\hbar}\,dx$ is given by the Gaussian integral around the classical minimum of the action.
If $x_0$ is a minimum of $S(x)$, then $S'(x_0)=0$. The 1-loop approximation for $Z$ is:
$$Z \approx e^{-S(x_0)/\hbar} \sqrt{\frac{2\pi\hbar}{S''(x_0)}}.$$
For the given action $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2} x^2 \cosh(x)$:
First, find the minimum $x_0$.
$S'(x) = x - \frac{g}{2}(2x \cosh x + x^2 \sinh x)$.
$S'(0) = 0 - \frac{g}{2}(0+0) = 0$. So $x_0=0$ is a critical point.
$S(0) = 0$.

Next, calculate the second derivative at the minimum:
$S''(x) = 1 - \frac{g}{2}(2\cosh x + 2x \sinh x + 2x \sinh x + x^2 \cosh x)$
$S''(x) = 1 - \frac{g}{2}(2\cosh x + 4x \sinh x + x^2 \cosh x)$.
At $x_0=0$:
$S''(0) = 1 - \frac{g}{2}(2\cosh 0 + 0 + 0) = 1 - \frac{g}{2}(2) = 1-g$.

Using the 1-loop approximation for $Z$:
$Z \approx e^{-0/\hbar} \sqrt{\frac{2\pi\hbar}{1-g}} = \sqrt{\frac{2\pi\hbar}{1-g}}$.

For the free partition function $Z_0$, we set $g=0$ in the action, so $S_0(x) = \tfrac{x^2}{2}$.
$S_0(0)=0$.
$S_0'(x) = x \implies S_0'(0)=0$.
$S_0''(x) = 1 \implies S_0''(0)=1$.
So, $Z_0 \approx \sqrt{\frac{2\pi\hbar}{1}} = \sqrt{2\pi\hbar}$.

**3. Compute $\log(Z/Z_0)$ and expand in $g$.**
Now we compute $\log(Z/Z_0)$:
$$\log\left(\frac{Z}{Z_0}\right) = \log\left(\frac{\sqrt{2\pi\hbar/(1-g)}}{\sqrt{2\pi\hbar}}\right) = \log\left(\frac{1}{\sqrt{1-g}}\right) = -\frac{1}{2}\log(1-g).$$
This is the 1-loop contribution. The higher-order terms in the Taylor expansion of $S(x)$ around $x_0=0$ (e.g., $x^4, x^6, \dots$) contribute to higher-loop corrections (2-loop, 3-loop, etc.) in the $\hbar$ expansion of $\log Z$. The "1-loop contribution" specifically refers to the Gaussian part.

Finally, expand the result as a power series in $g$ through order $g^3$. Recall the Taylor series for $\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$.
$$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$$
$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

## Final answer

The 1-loop contribution to $\log(Z/Z_0)$ is given by the change in the Gaussian part of the integral, which is determined by the second derivative of the action at its minimum.
The action is $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2} x^2 \cosh(x)$.
The minimum of $S(x)$ is at $x_0=0$, where $S(0)=0$.
The second derivative at the minimum is $S''(0) = 1 - g$.
The 1-loop contribution to $\log Z$ is $\frac{1}{2}\log(2\pi\hbar) - \frac{1}{2}\log(S''(0))$.
The free partition function $Z_0$ has $S_0''(0)=1$, so $\log Z_0 = \frac{1}{2}\log(2\pi\hbar)$.
Therefore, the 1-loop contribution to $\log(Z/Z_0)$ is:
$$-\frac{1}{2}\log(1-g).$$
Expanding this result as a power series in $g$ through order $g^3$:
$$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right).$$
$$\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$