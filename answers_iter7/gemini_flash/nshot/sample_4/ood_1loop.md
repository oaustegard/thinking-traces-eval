## Reasoning trace

**1. Define the problem and relevant quantities.**
We are asked to compute the 1-loop contribution to $\log(Z/Z_0)$ for a zero-dimensional quantum field theory with action $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$. $Z = \int e^{-S(x)/\hbar}\,dx$ and $Z_0$ is the partition function for the free theory (i.e., $g=0$).

**2. General formula for $\log(Z/Z_0)$ in zero dimensions.**
The partition function $Z$ can be approximated using the saddle-point method. Let $x_c$ be the classical solution, i.e., $S'(x_c) = 0$. Expanding $S(x)$ around $x_c$:
$S(x) = S(x_c) + S'(x_c)(x-x_c) + \frac{1}{2}S''(x_c)(x-x_c)^2 + O((x-x_c)^3)$.
Since $S'(x_c)=0$, we have $S(x) \approx S(x_c) + \frac{1}{2}S''(x_c)(x-x_c)^2$.
Then the integral for $Z$ becomes a Gaussian integral:
$Z = \int_{-\infty}^\infty e^{-S(x)/\hbar}\,dx \approx e^{-S(x_c)/\hbar} \int_{-\infty}^\infty e^{-\frac{1}{2\hbar}S''(x_c)(x-x_c)^2}\,dx$.
$Z \approx e^{-S(x_c)/\hbar} \sqrt{\frac{2\pi\hbar}{S''(x_c)}}$.
Taking the logarithm:
$\log Z \approx -\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c) + \frac{1}{2}\log(2\pi\hbar)$.

For the free theory ($g=0$), the action is $S_0(x) = x^2/2$.
The classical solution is $S_0'(x) = x = 0 \implies x_{c0}=0$.
The second derivative is $S_0''(x) = 1$, so $S_0''(x_{c0})=1$.
Then $\log Z_0 \approx -\frac{S_0(x_{c0})}{\hbar} - \frac{1}{2}\log S_0''(x_{c0}) + \frac{1}{2}\log(2\pi\hbar) = 0 - \frac{1}{2}\log(1) + \frac{1}{2}\log(2\pi\hbar) = \frac{1}{2}\log(2\pi\hbar)$.

Now, we compute $\log(Z/Z_0)$:
$\log(Z/Z_0) = \log Z - \log Z_0 \approx -\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c)$.
The "1-loop contribution" typically refers to the terms independent of $\hbar$ in this expansion (i.e., $O(\hbar^0)$). The term $-S(x_c)/\hbar$ is the classical contribution ($O(\hbar^{-1})$). Therefore, the 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log S''(x_c)$.

**3. Find the classical solution $x_c$.**
The action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
First derivative:
$S'(x) = \frac{d}{dx}\left(\frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)\right)$
$S'(x) = x - \frac{g}{2} (2x \cosh(x) + x^2 \sinh(x))$.
Setting $S'(x_c)=0$:
$x_c - \frac{g}{2} (2x_c \cosh(x_c) + x_c^2 \sinh(x_c)) = 0$.
Factoring out $x_c$:
$x_c \left(1 - g \cosh(x_c) - \frac{g}{2} x_c \sinh(x_c)\right) = 0$.
One solution is clearly $x_c=0$. For sufficiently small $g$, the term in the parenthesis $1 - g \cosh(x_c) - \frac{g}{2} x_c \sinh(x_c)$ will be non-zero near $x_c=0$ (it evaluates to $1-g$ at $x_c=0$). Thus, for small $g$, $x_c=0$ is the unique and dominant classical solution.

**4. Calculate $S''(x_c)$ at $x_c=0$.**
Second derivative of $S(x)$:
$S''(x) = \frac{d}{dx}\left(x - \frac{g}{2} (2x \cosh(x) + x^2 \sinh(x))\right)$
$S''(x) = 1 - \frac{g}{2} [ (2\cosh(x) + 2x\sinh(x)) + (2x\sinh(x) + x^2\cosh(x)) ]$
$S''(x) = 1 - \frac{g}{2} [ 2\cosh(x) + 4x\sinh(x) + x^2\cosh(x) ]$.
Now, evaluate at $x_c=0$:
$\cosh(0)=1$, $\sinh(0)=0$.
$S''(0) = 1 - \frac{g}{2} [ 2\cosh(0) + 4(0)\sinh(0) + (0)^2\cosh(0) ]$
$S''(0) = 1 - \frac{g}{2} [ 2(1) + 0 + 0 ] = 1 - g$.

**5. Compute the 1-loop contribution and expand in $g$.**
The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log S''(x_c)$.
Substituting $S''(0) = 1-g$:
1-loop contribution $= -\frac{1}{2}\log(1-g)$.
Now, expand this result as a power series in $g$ through order $g^3$. The Taylor series for $\log(1-y)$ is $-\sum_{k=1}^\infty \frac{y^k}{k} = -y - \frac{y^2}{2} - \frac{y^3}{3} - O(y^4)$.
So, with $y=g$:
$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

## Final answer

The 1-loop contribution to $\log(Z/Z_0)$ is given by $-\frac{1}{2}\log S''(x_c)$, where $x_c$ is the classical solution to $S'(x)=0$.

1.  **Classical solution:**
    $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
    $S'(x) = x - \frac{g}{2} (2x \cosh(x) + x^2 \sinh(x))$.
    Setting $S'(x_c)=0$ yields $x_c(1 - g \cosh(x_c) - \frac{g}{2} x_c \sinh(x_c)) = 0$. For small $g$, the unique dominant solution is $x_c=0$.

2.  **Second derivative at $x_c=0$:**
    $S''(x) = 1 - \frac{g}{2} (2\cosh(x) + 4x\sinh(x) + x^2\cosh(x))$.
    At $x_c=0$, we have $\cosh(0)=1$ and $\sinh(0)=0$.
    $S''(0) = 1 - \frac{g}{2} (2(1) + 0 + 0) = 1 - g$.

3.  **1-loop contribution:**
    The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log S''(0) = -\frac{1}{2}\log(1-g)$.

4.  **Power series expansion:**
    Using the Taylor series expansion $\log(1-y) = -y - \frac{y^2}{2} - \frac{y^3}{3} - O(y^4)$:
    $-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$.

The 1-loop contribution to $\log(Z/Z_0)$ expanded through order $g^3$ is:
$$\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$