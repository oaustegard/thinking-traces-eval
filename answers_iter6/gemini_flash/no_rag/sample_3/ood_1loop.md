The problem asks for the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$, expanded as a power series in $g$ through order $g^3$.

First, let's define the partition functions:
$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$
$Z_0 = \int_{-\infty}^{\infty} e^{-S_0(x)/\hbar} dx$, where $S_0(x) = x^2/2$ is the free action (when $g=0$).

1.  **Compute $Z_0$**:
    $Z_0 = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx = \sqrt{2\pi\hbar}$.

2.  **Understand "1-loop contribution" in 0D**:
    In zero-dimensional field theory, the "1-loop" contribution to $\log Z$ is typically obtained by expanding the action around a classical minimum $x_{cl}$ and performing a Gaussian integral.
    The general formula for $\log Z$ in the saddle-point approximation is $\log Z \approx -\frac{1}{\hbar} S(x_{cl}) - \frac{1}{2} \log\left(\frac{1}{2\pi\hbar} S''(x_{cl})\right) + \text{const}$.
    The "tree-level" contribution is $-S(x_{cl})/\hbar$, and the "1-loop" contribution is $-\frac{1}{2} \log(S''(x_{cl}))$ (ignoring normalization factors that cancel for $Z/Z_0$).
    In our case, $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$.
    The classical equation of motion is $S'(x) = x - (g/2) (2x \cosh(x) + x^2 \sinh(x)) = 0$.
    This implies $x_{cl} (1 - g \cosh(x_{cl}) - (g/2) x_{cl} \sinh(x_{cl})) = 0$.
    One classical solution is $x_{cl}=0$.
    Let's check the second derivative at $x_{cl}=0$:
    $S''(x) = 1 - g(\cosh(x) + x\sinh(x)) - (g/2)(2x\sinh(x) + x^2\cosh(x))$.
    $S''(0) = 1 - g(\cosh(0) + 0) - (g/2)(0 + 0) = 1 - g$.
    For $x_{cl}=0$ to be a minimum, we require $S''(0) > 0$, so $g < 1$.
    The free action $S_0(x)=x^2/2$ has $S_0''(0)=1$.
    Thus, for $x_{cl}=0$, the 1-loop contribution to $\log(Z/Z_0)$ is:
    $\log(Z/Z_0) = -\frac{1}{\hbar} (S(0) - S_0(0)) - \frac{1}{2} \log(S''(0)) + \frac{1}{2} \log(S_0''(0))$.
    Since $S(0)=0$ and $S_0(0)=0$, the classical action terms vanish.
    So, $\log(Z/Z_0) = -\frac{1}{2} \log(1-g) + \frac{1}{2} \log(1) = -\frac{1}{2} \log(1-g)$.

3.  **Expand in $g$**:
    We need to expand $-\frac{1}{2} \log(1-g)$ in a power series in $g$ up to order $g^3$.
    Recall the Taylor series for $\log(1-u) = -u - u^2/2 - u^3/3 - \dots$
    Substituting $u=g$:
    $-\frac{1}{2} \log(1-g) = -\frac{1}{2} (-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4))$
    $= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

This interpretation of "1-loop contribution" (which refers to the lowest order in $\hbar$ in the saddle-point expansion) is standard in quantum field theory for zero-dimensional systems. If the problem had intended the full $\hbar$-dependent cumulant expansion (which contains all orders of $\hbar$ for each $g^n$ term), it would typically ask for a "perturbative expansion in $g$" or specify orders in $\hbar$. The term "1-loop" points to the $\hbar^0$ contribution from fluctuations around the classical solution.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$.