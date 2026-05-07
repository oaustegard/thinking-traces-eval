**(a) Relevant traces and why:**

*   **Trace 1 (Etingof Exercise 3.26 - 1-loop effective action):** This trace is highly relevant. It directly deals with calculating the 1-loop contribution to the effective action $S_{\text{eff}}$ in zero-dimensional QFT. The effective action is related to the generating functional $W(J) = \hbar \log Z(J)$, and thus to $\log Z$. Specifically, the 1-loop contribution to $\log Z$ is directly obtainable from the 1-loop effective action formula derived in Trace 1.

*   **Trace 2 (Etingof Exercise 2.14 - Wallis formula):** This trace is about integration techniques (steepest descent, integration by parts) for a specific integral. It is not directly related to zero-dimensional QFT or 1-loop calculations and is therefore not relevant.

*   **Trace 3 (Etingof Exercise 7.27 - 1PI 2-point function):** This trace calculates the 1PI 2-point function (self-energy) for a quantum mechanical particle. While it uses Feynman diagrams and loop expansion, the specific quantity requested (1PI 2-point function vs. $\log(Z/Z_0)$) and the context (quantum mechanics vs. zero-dimensional QFT) are different. The general methodology of Feynman diagrams for loop calculations is related, but the direct formula used in Trace 1 is more appropriate here.

**(b) Differences between relevant trace and main problem:**

*   **Interaction term:** The main problem has an interaction term $S_{\text{int}}(x) = -(g/2)x^2\cosh(x)$, which leads to an infinite series of even-valent vertices ($x^2, x^4, x^6, \dots$). Trace 1 uses $S_{\text{int}}(x) = -gx^3/6$, which only has a single 3-valent vertex. This means the specific calculation of $S''(x)$ will be different.
*   **Quantity requested:** Trace 1 calculates $S_1$, where $S_{\text{eff}}(x_c) = S(x_c) + \hbar S_1(x_c) + O(\hbar^2)$. The main problem asks for the 1-loop contribution to $\log(Z/Z_0)$. As detailed below, these quantities are closely related by a sign and the choice of saddle point.

---

## Reasoning for the main problem

The problem asks for the 1-loop contribution to $\log(Z/Z_0)$.
In zero-dimensional QFT, the partition function is $Z = \int e^{-S(x)/\hbar} dx$. The free partition function is $Z_0 = \int e^{-S_0(x)/\hbar} dx$, where $S_0(x) = x^2/2$.
Using the saddle-point approximation for $Z$:
$\log Z \approx -S(x_c)/\hbar - \frac12 \log S''(x_c) + \frac12 \log(2\pi\hbar)$, where $x_c$ is the classical solution satisfying $S'(x_c)=0$.
For the free theory, $S_0(x) = x^2/2$, so $S_0'(x)=x$, thus $x_{c,0}=0$. $S_0(0)=0$ and $S_0''(0)=1$.
$\log Z_0 \approx -S_0(x_{c,0})/\hbar - \frac12 \log S_0''(x_{c,0}) + \frac12 \log(2\pi\hbar) = \frac12 \log(2\pi\hbar)$.

Then, $\log(Z/Z_0) = \log Z - \log Z_0 \approx -S(x_c)/\hbar - \frac12 \log S''(x_c)$.
The term $-S(x_c)/\hbar$ is the classical (tree-level) contribution, proportional to $\hbar^{-1}$.
The term $-\frac12 \log S''(x_c)$ is the **1-loop contribution**, which is independent of $\hbar$. This is precisely what the problem asks for.

This formula for the 1-loop contribution to $\log(Z/Z_0)$ is directly related to $S_1$ from Trace 1. If $S_{\text{eff}}(x_c) = S(x_c) + \hbar S_1(x_c) + O(\hbar^2)$, and $S_1(x_c) = \frac12 \log S''(x_c)$, then the 1-loop contribution to $\log(Z/Z_0)$ is $-S_1(x_c)$.

Now we need to calculate $S''(x_c)$ for the given action $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2}x^2\cosh(x)$.

1.  **Find the classical solution $x_c$:**
    $S'(x) = \frac{d}{dx}\left(\frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)\right) = x - \frac{g}{2}(2x\cosh(x) + x^2\sinh(x))$.
    Setting $S'(x_c)=0$:
    $x_c - g x_c \cosh(x_c) - \frac{g}{2}x_c^2\sinh(x_c) = 0$.
    $x_c(1 - g\cosh(x_c) - \frac{g}{2}x_c\sinh(x_c)) = 0$.
    One solution is $x_c=0$. For small $g$, this corresponds to the global minimum of the potential, so we choose $x_c=0$.

2.  **Calculate $S''(x)$ and evaluate at $x_c=0$:**
    $S''(x) = \frac{d}{dx}\left(x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)\right)$
    $S''(x) = 1 - g(\cosh(x) + x\sinh(x)) - \frac{g}{2}(2x\sinh(x) + x^2\cosh(x))$.
    $S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$.
    $S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$.
    Now, evaluate at $x_c=0$:
    $S''(0) = 1 - g\cosh(0) - 2g(0)\sinh(0) - \frac{g}{2}(0)^2\cosh(0)$.
    Since $\cosh(0)=1$ and $\sinh(0)=0$:
    $S''(0) = 1 - g(1) - 0 - 0 = 1 - g$.

3.  **Apply the 1-loop formula:**
    The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac12 \log S''(x_c)$.
    Substituting $S''(0) = 1-g$:
    Contribution $= -\frac12 \log(1-g)$.

4.  **Expand in a power series in $g$ through order $g^3$:**
    Using the Taylor series expansion for $\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$:
    $-\frac12 \log(1-g) = -\frac12 \left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$.
    $-\frac12 \log(1-g) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

The Feynman diagrams contributing to this result are the 1-loop vacuum diagrams evaluated at the background field $x_c=0$. These correspond to summing up contributions from vertices arising from the expansion of $S_{\text{int}}(x)$ and using the propagator $1$ (in Etingof's 0D convention without $\hbar$ in propagator). Specifically, the terms in the expansion of $-\frac12 \log(1-g)$ correspond to 1-loop diagrams involving the $x^2$ term in the effective propagator (dressed by $g$).

The 1-loop contribution to $\log(Z/Z_0)$ is:
$$ \boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)} $$