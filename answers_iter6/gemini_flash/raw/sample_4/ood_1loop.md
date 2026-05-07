The problem asks for the 1-loop contribution to $\log(Z/Z_0)$ for a given zero-dimensional action $S(x)$.

**1. Formalism and 1-loop Approximation**
In zero-dimensional quantum field theory, the partition function is given by $Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$. The free partition function $Z_0$ corresponds to $g=0$, so $S_0(x) = x^2/2$.
The 1-loop approximation for $Z$ is obtained by expanding the action $S(x)$ around its classical minimum $x_c$ (where $S'(x_c)=0$):
$S(x) = S(x_c) + \frac{1}{2} S''(x_c) (x-x_c)^2 + O((x-x_c)^3)$.
Substituting this into the integral and performing the Gaussian integral, we get:
$\log Z \approx -\frac{S(x_c)}{\hbar} + \frac{1}{2}\log\left(\frac{2\pi\hbar}{S''(x_c)}\right)$.

For the free action $S_0(x) = x^2/2$, the classical minimum is $x_c=0$. At this point, $S_0(0)=0$ and $S_0''(0)=1$.
So, $\log Z_0 \approx -\frac{S_0(0)}{\hbar} + \frac{1}{2}\log\left(\frac{2\pi\hbar}{S_0''(0)}\right) = \frac{1}{2}\log(2\pi\hbar)$.

Now we can compute $\log(Z/Z_0)$:
$\log(Z/Z_0) = \log Z - \log Z_0 \approx -\frac{S(x_c)}{\hbar} + \frac{1}{2}\log\left(\frac{2\pi\hbar}{S''(x_c)}\right) - \frac{1}{2}\log(2\pi\hbar)$
$\log(Z/Z_0) \approx -\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c)$.

The "1-loop contribution" usually refers to the term independent of $\hbar$. In this expression, $S(x_c)/\hbar$ is the classical contribution, and $-\frac{1}{2}\log S''(x_c)$ is the 1-loop quantum correction. This interpretation is consistent with **Trace 1 (Etingof Exercise 3.26)**, which shows that the 1-loop contribution to the effective action (related to $\log Z$) is $\frac{\hbar}{2}\log S''(x_c)$, implying a term $-\frac{1}{2}\log S''(x_c)$ in $\log Z$.

**2. Find the Classical Minimum $x_c$ and $S''(x_c)$**
The given action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
First, we find the classical equation of motion $S'(x_c)=0$:
$S'(x) = \frac{d}{dx}\left(\frac{x^2}{2} - \frac{g}{2} x^2 \cosh x\right) = x - \frac{g}{2} (2x \cosh x + x^2 \sinh x)$
$S'(x) = x - gx \cosh x - \frac{g}{2} x^2 \sinh x$.
Setting $S'(x_c)=0$:
$x_c (1 - g \cosh x_c - \frac{g}{2} x_c \sinh x_c) = 0$.
One obvious solution is $x_c=0$.
To check if there are other small $x_c$ solutions, we examine the term in parentheses. Using Taylor expansions $\cosh x \approx 1 + x^2/2 + O(x^4)$ and $\sinh x \approx x + x^3/6 + O(x^5)$:
$1 - g(1 + x_c^2/2 + O(x_c^4)) - \frac{g}{2} x_c(x_c + O(x_c^3)) = 0$
$1 - g - g x_c^2 + O(g x_c^4) = 0$.
For small $g$, this would imply $x_c^2 \approx (1-g)/g$. If $g$ is very small, $x_c^2$ would be large, which contradicts the assumption of small $x_c$. Therefore, for small $g$, the only relevant classical minimum is $x_c=0$.

Now we compute the second derivative $S''(x)$:
$S''(x) = \frac{d}{dx} (x - gx \cosh x - \frac{g}{2} x^2 \sinh x)$
$S''(x) = 1 - g(\cosh x + x \sinh x) - \frac{g}{2} (2x \sinh x + x^2 \cosh x)$
$S''(x) = 1 - g \cosh x - gx \sinh x - gx \sinh x - \frac{g}{2} x^2 \cosh x$
$S''(x) = 1 - g \cosh x - 2gx \sinh x - \frac{g}{2} x^2 \cosh x$.
Evaluate $S''(x)$ at $x_c=0$:
$S''(0) = 1 - g \cosh(0) - 2g(0) \sinh(0) - \frac{g}{2} (0)^2 \cosh(0)$
$S''(0) = 1 - g(1) - 0 - 0 = 1 - g$.
For $g<1$, $S''(0)>0$, confirming that $x_c=0$ is indeed a minimum.

**3. Calculate the 1-loop Contribution to $\log(Z/Z_0)$**
Using the formula derived in step 1, the 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{S(x_c)}{\hbar} - \frac{1}{2}\log S''(x_c)$.
Since $x_c=0$, $S(x_c) = S(0) = \frac{0^2}{2} - \frac{g}{2} 0^2 \cosh(0) = 0$.
So the classical contribution vanishes, and the entire $\log(Z/Z_0)$ is just the 1-loop term:
$\log(Z/Z_0) = -\frac{1}{2}\log S''(0) = -\frac{1}{2}\log(1-g)$.

**4. Expand as a Power Series in $g$ through Order $g^3$**
We use the Taylor expansion for $\log(1-y) = -y - \frac{y^2}{2} - \frac{y^3}{3} - O(y^4)$.
Substituting $y=g$:
$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

The retrieved **Trace 1 (Etingof Exercise 3.26)** is highly relevant. It provides the general formula for the 1-loop effective action $S_{\text{eff}}(x_c) = S(x_c) + \frac{\hbar}{2}\log S''(x_c)$, which is directly used to establish the 1-loop contribution to $\log(Z/Z_0)$ as $-\frac{1}{2}\log S''(x_c)$. The main difference is the specific form of the action $S(x)$ and the request to expand in $g$. **Trace 2** and **Trace 3** are less directly relevant to this specific problem, although they cover related concepts in QFT and integral approximations.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$.