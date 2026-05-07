Here's a step-by-step solution to compute the 1-loop contribution to $\log(Z/Z_0)$:

**1. Understanding the Problem**

We are asked to compute the 1-loop contribution to the logarithm of the ratio of partition functions, $Z/Z_0$, for a given zero-dimensional action. $Z_0$ is the partition function for the free theory, meaning when the interaction term (dependent on $g$) is absent. The 1-loop contribution arises from expanding the interaction term around the classical vacuum and considering the quantum fluctuations.

The action is given by:
$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$

The partition function is defined as:
$Z = \int dx \, e^{-S(x)/\hbar}$

The free action is $S_0(x) = \frac{x^2}{2}$.
The free partition function is $Z_0 = \int dx \, e^{-S_0(x)/\hbar} = \int dx \, e^{-x^2/(2\hbar)}$.

**2. Relating Partition Functions and Logarithms**

We are interested in $\log(Z/Z_0) = \log(Z) - \log(Z_0)$.
The logarithm of the partition function is related to the free energy. In quantum field theory, the 1-loop contribution to $\log(Z)$ is typically calculated by expanding the action around the classical minimum and performing a Gaussian integral.

Let $S(x) = S_0(x) + S_I(x)$, where $S_I(x) = -\frac{g}{2} x^2 \cosh(x)$ is the interaction term.

Then, $Z = \int dx \, e^{-(S_0(x) + S_I(x))/\hbar} = \int dx \, e^{-S_0(x)/\hbar} e^{-S_I(x)/\hbar} = Z_0 \int dx \, e^{-S_0(x)/\hbar} \frac{e^{-S_I(x)/\hbar}}{Z_0}$.
So, $\frac{Z}{Z_0} = \int dx \, e^{-S_0(x)/\hbar} e^{-S_I(x)/\hbar}$.

Taking the logarithm:
$\log\left(\frac{Z}{Z_0}\right) = \log\left(\int dx \, e^{-S_0(x)/\hbar} e^{-S_I(x)/\hbar}\right)$.

**3. 1-Loop Approximation**

The 1-loop approximation involves expanding the exponential of the interaction term around the classical vacuum. The classical vacuum is the minimum of the classical action $S(x)$. For a zero-dimensional theory, this is simply the value of $x$ that minimizes $S(x)$.

Let's find the classical minimum. We need to find $x_{cl}$ such that $\frac{dS}{dx}(x_{cl}) = 0$.
$\frac{dS}{dx} = x - \frac{g}{2} \left( 2x \cosh(x) + x^2 \sinh(x) \right) = x \left( 1 - \frac{g}{2} \left( 2 \cosh(x) + x \sinh(x) \right) \right)$.

For small $g$, the classical vacuum $x_{cl}$ is close to $x=0$.
If $x=0$, then $\frac{dS}{dx}(0) = 0$. So, $x_{cl} = 0$ is a classical minimum for any $g$.

Now, we expand the action around $x=0$. We can write $S(x)$ as a Taylor series around $x=0$:
$\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots$

$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots \right)$
$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \frac{g}{1440} x^8 - \dots$
$S(x) = \frac{1-g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \dots$

The 1-loop contribution to $\log(Z/Z_0)$ is given by the formula:
$\log\left(\frac{Z}{Z_0}\right)_{1-\text{loop}} = \frac{1}{2} \log \det \left( \frac{\partial^2 S}{\partial x \partial x} \bigg|_{x=x_{cl}} \right)$

In zero dimensions, this simplifies. The "determinant" is just the second derivative evaluated at the minimum.
Let $M^2 = \frac{d^2 S}{dx^2} \bigg|_{x=0}$.

$\frac{d^2 S}{dx^2} = \frac{d}{dx} \left( x \left( 1 - \frac{g}{2} \left( 2 \cosh(x) + x \sinh(x) \right) \right) \right)$
$\frac{d^2 S}{dx^2} = \left( 1 - \frac{g}{2} \left( 2 \cosh(x) + x \sinh(x) \right) \right) + x \frac{d}{dx} \left( 1 - \frac{g}{2} \left( 2 \cosh(x) + x \sinh(x) \right) \right)$
$\frac{d^2 S}{dx^2} = 1 - g \cosh(x) - \frac{g}{2} x \sinh(x) + x \left( - \frac{g}{2} (2 \sinh(x) + \sinh(x) + x \cosh(x)) \right)$
$\frac{d^2 S}{dx^2} = 1 - g \cosh(x) - \frac{g}{2} x \sinh(x) - \frac{3g}{2} x \sinh(x) - \frac{g}{2} x^2 \cosh(x)$
$\frac{d^2 S}{dx^2} = 1 - g \cosh(x) - 2g x \sinh(x) - \frac{g}{2} x^2 \cosh(x)$

Evaluate at $x=0$:
$M^2 = \frac{d^2 S}{dx^2} \bigg|_{x=0} = 1 - g \cosh(0) - 2g (0) \sinh(0) - \frac{g}{2} (0)^2 \cosh(0)$
$M^2 = 1 - g(1) - 0 - 0 = 1 - g$.

The 1-loop contribution is:
$\log\left(\frac{Z}{Z_0}\right)_{1-\text{loop}} = \frac{1}{2} \log(M^2) = \frac{1}{2} \log(1-g)$.

**4. Expansion in Powers of g**

We need to expand the result as a power series in $g$ through order $g^3$.
Using the Taylor series for $\log(1-g)$:
$\log(1-g) = -g - \frac{g^2}{2} - \frac{g^3}{3} - \dots$

So, the 1-loop contribution is:
$\log\left(\frac{Z}{Z_0}\right)_{1-\text{loop}} = \frac{1}{2} \left( -g - \frac{g^2}{2} - \frac{g^3}{3} - \dots \right)$
$\log\left(\frac{Z}{Z_0}\right)_{1-\text{loop}} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \dots$

The question asks for the 1-loop contribution. The 1-loop contribution is typically understood as the term coming from the Gaussian integration around the classical minimum. The formula $\frac{1}{2} \log \det(\dots)$ precisely captures this.

Let's verify the interpretation of "1-loop contribution". The full $\log(Z/Z_0)$ can be expanded using the cumulant expansion or Feynman diagrams.
$\log\left(\frac{Z}{Z_0}\right) = \log\left(\left\langle e^{-S_I/\hbar} \right\rangle_0\right)$, where $\langle \dots \rangle_0$ denotes averaging with respect to $e^{-S_0/\hbar}$.
$\log\left(\frac{Z}{Z_0}\right) = \sum_{n=1}^{\infty} \frac{(-1)^n}{n!} \left\langle S_I^n \right\rangle_0$.

The 1-loop contribution corresponds to the term where we expand $S_I$ to quadratic order and perform the Gaussian integral.
$S_I(x) = -\frac{g}{2} x^2 \cosh(x) = -\frac{g}{2} x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots \right)$
$S_I(x) = -\frac{g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \dots$

The 1-loop contribution is often defined as the result of the Gaussian integral of $e^{-S(x)/\hbar}$ where $S(x)$ is expanded up to quadratic order around the minimum.
$S(x) \approx S(x_{cl}) + \frac{1}{2} \left(\frac{d^2 S}{dx^2}\right)_{x_{cl}} (x - x_{cl})^2$.
Since $x_{cl}=0$, $S(0) = 0$.
So, $S(x) \approx \frac{1}{2} (1-g) x^2$.

$Z \approx \int dx \, e^{-\frac{1}{2} (1-g) x^2 / \hbar}$.
This is a Gaussian integral: $\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\frac{\pi}{a}}$.
$Z \approx \sqrt{\frac{2\pi\hbar}{1-g}}$.

$Z_0 = \int dx \, e^{-x^2/(2\hbar)} = \sqrt{2\pi\hbar}$.

$\frac{Z}{Z_0} \approx \frac{\sqrt{2\pi\hbar/(1-g)}}{\sqrt{2\pi\hbar}} = \frac{1}{\sqrt{1-g}} = (1-g)^{-1/2}$.

$\log\left(\frac{Z}{Z_0}\right) \approx \log((1-g)^{-1/2}) = -\frac{1}{2} \log(1-g)$.

This matches our previous result using the determinant formula.

Now, expand $-\frac{1}{2} \log(1-g)$ in powers of $g$:
$-\frac{1}{2} \log(1-g) = -\frac{1}{2} \left( -g - \frac{g^2}{2} - \frac{g^3}{3} - \dots \right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \dots$

Let's re-read the question carefully: "Compute the 1-loop contribution to log(Z/Z_0)".
The 1-loop correction is the leading quantum correction. The formula $\frac{1}{2} \log \det(M^2)$ correctly gives this.

The expansion of $S(x)$ around $x=0$ is:
$S(x) = \frac{1-g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 + O(x^8)$.

The 1-loop contribution to $\log Z$ is the Gaussian integral over the quadratic part of the action.
$S_{1\text{-loop}}(x) = \frac{d S}{dx}(0) x + \frac{1}{2!} \frac{d^2 S}{dx^2}(0) x^2 = 0 \cdot x + \frac{1-g}{2} x^2$.
The 1-loop contribution to $\log Z$ is $\frac{1}{2} \log(1-g)$.

The 1-loop contribution to $\log(Z/Z_0)$ is precisely this value.

Let's consider the expansion of $\log(Z/Z_0)$ in terms of $g$:
$\log(Z/Z_0) = \log \left( \int dx e^{-S(x)/\hbar} \right) - \log \left( \int dx e^{-S_0(x)/\hbar} \right)$
$\log(Z/Z_0) = \log \left( \int dx e^{-S_0(x)/\hbar} e^{-S_I(x)/\hbar} \right) - \log \left( \int dx e^{-S_0(x)/\hbar} \right)$
$\log(Z/Z_0) = \log \left( \left\langle e^{-S_I(x)/\hbar} \right\rangle_0 \right)$
$\log(Z/Z_0) = \left\langle -S_I(x)/\hbar \right\rangle_0 - \frac{1}{2!} \left\langle \left( -S_I(x)/\hbar \right)^2 \right\rangle_0 + \frac{1}{3!} \left\langle \left( -S_I(x)/\hbar \right)^3 \right\rangle_0 - \dots$

Here, $\langle \dots \rangle_0$ means averaging with respect to the Gaussian measure $e^{-x^2/(2\hbar)} dx$.
The moments of $x$ under this measure are:
$\langle x^{2n} \rangle_0 = (2n-1)!! \hbar^n$
$\langle x^{2n+1} \rangle_0 = 0$

$S_I(x) = -\frac{g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \dots$

The 1-loop contribution is often understood as the first term in this expansion involving $S_I$, which is $\langle -S_I(x)/\hbar \rangle_0$.
$\langle -S_I(x)/\hbar \rangle_0 = \left\langle \frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \dots \right\rangle_0$
$= \frac{g}{2\hbar} \langle x^2 \rangle_0 + \frac{g}{4\hbar} \langle x^4 \rangle_0 + \dots$
$= \frac{g}{2\hbar} (\hbar) + \frac{g}{4\hbar} (3\hbar^2) + \dots$
$= \frac{g}{2} + \frac{3g\hbar}{4} + \dots$

This does not seem to match the previous result. The term "1-loop contribution" usually refers to the quantum fluctuations around the *classical* minimum, which is captured by the Gaussian integral of the quadratic part of the action.

Let's re-evaluate the definition of 1-loop contribution in this context.
The partition function is $Z = \int dx e^{-S(x)/\hbar}$.
We expand $S(x)$ around the classical minimum $x_{cl}=0$:
$S(x) = S(0) + S'(0)x + \frac{1}{2}S''(0)x^2 + \frac{1}{6}S'''(0)x^3 + \frac{1}{24}S^{(4)}(0)x^4 + \dots$
$S(0) = 0$
$S'(0) = 0$
$S''(0) = 1-g$
$S'''(0) = 0$ (since $S(x)$ is an even function of $x$)
$S^{(4)}(0) = \frac{d^3}{dx^3} (1 - g \cosh x - 2g x \sinh x - \frac{g}{2} x^2 \cosh x)$
$\frac{d^3 S}{dx^3} = -g \sinh x - 2g (\sinh x + x \cosh x) - \frac{g}{2} (2x \cosh x + x^2 \sinh x)$
At $x=0$: $\frac{d^3 S}{dx^3}(0) = 0$.

Let's compute the fourth derivative:
$\frac{d^4 S}{dx^4} = -g \cosh x - 2g (\cosh x + \cosh x + x \sinh x) - \frac{g}{2} (2 \cosh x + 2x \sinh x + 2x \sinh x + x^2 \cosh x)$
$\frac{d^4 S}{dx^4} = -g \cosh x - 4g \cosh x - \frac{g}{2} (2 \cosh x + 4x \sinh x + x^2 \cosh x)$
At $x=0$: $\frac{d^4 S}{dx^4}(0) = -g - 4g - \frac{g}{2}(2) = -g - 4g - g = -6g$.

So, $S(x) = \frac{1-g}{2} x^2 - \frac{g}{24} x^4 + \dots$

The 1-loop contribution to $\log Z$ is obtained by integrating the quadratic part:
$\log Z_{1-\text{loop}} = \log \int dx \, e^{-\frac{1}{2}(1-g)x^2/\hbar} = \frac{1}{2} \log\left(\frac{2\pi\hbar}{1-g}\right)$.

The free theory has action $S_0(x) = x^2/2$.
$Z_0 = \int dx e^{-x^2/(2\hbar)}$.
$\log Z_0 = \log \int dx e^{-x^2/(2\hbar)} = \frac{1}{2} \log(2\pi\hbar)$.

The 1-loop contribution to $\log(Z/Z_0)$ is:
$\log(Z/Z_0)_{1-\text{loop}} = \log Z_{1-\text{loop}} - \log Z_0$
$= \frac{1}{2} \log\left(\frac{2\pi\hbar}{1-g}\right) - \frac{1}{2} \log(2\pi\hbar)$
$= \frac{1}{2} \left( \log(2\pi\hbar) - \log(1-g) - \log(2\pi\hbar) \right)$
$= -\frac{1}{2} \log(1-g)$.

This confirms the result obtained from the determinant formula. The determinant formula is a direct way to compute the 1-loop contribution from the quadratic terms of the action around the minimum.

Now, we expand this in powers of $g$:
$-\frac{1}{2} \log(1-g) = -\frac{1}{2} \left( -g - \frac{g^2}{2} - \frac{g^3}{3} - \dots \right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \dots$

The question asks for the expansion through order $g^3$.

The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2} \log(1-g)$.
Expanding this:
$-\frac{1}{2} \log(1-g) = -\frac{1}{2}(-g - \frac{g^2}{2} - \frac{g^3}{3} - \dots) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \dots$

The problem phrasing "Compute the 1-loop contribution" implies we should provide the terms that arise from the 1-loop calculation. The 1-loop calculation, in this context, refers to the Gaussian integration of the quadratic part of the action around the classical minimum.

The contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log(1-g)$.
Expanding this up to $g^3$:
$-\frac{1}{2} \log(1-g) = -\frac{1}{2} \left( -g - \frac{g^2}{2} - \frac{g^3}{3} \right) + O(g^4)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}$.

Final check of the calculation.
Action $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
Classical minimum at $x=0$.
Second derivative at $x=0$: $\frac{d^2 S}{dx^2}\Big|_{x=0} = 1-g$.
1-loop contribution to $\log Z$ is $\frac{1}{2} \log(1-g)$.
$Z_0$ is the free partition function. The argument of the logarithm is $Z/Z_0$.
The 1-loop contribution to $\log(Z/Z_0)$ is the difference between the 1-loop corrected $\log Z$ and $\log Z_0$.

The 1-loop contribution is the Gaussian integral of the quadratic part of the action $S(x) \approx \frac{1}{2}(1-g)x^2$.
$\log Z_{1\text{-loop}} = \log \int dx e^{-\frac{1}{2}(1-g)x^2/\hbar} = \frac{1}{2} \log\left(\frac{2\pi\hbar}{1-g}\right)$.
$\log Z_0 = \log \int dx e^{-\frac{1}{2}x^2/\hbar} = \frac{1}{2} \log(2\pi\hbar)$.
$\log(Z/Z_0)_{1\text{-loop}} = \log Z_{1\text{-loop}} - \log Z_0 = \frac{1}{2}\log\left(\frac{2\pi\hbar}{1-g}\right) - \frac{1}{2}\log(2\pi\hbar) = -\frac{1}{2}\log(1-g)$.

Expansion:
$-\frac{1}{2}\log(1-g) = -\frac{1}{2}(-g - \frac{g^2}{2} - \frac{g^3}{3} - \dots) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \dots$

The question asks for the answer as a power series in $g$ through order $g^3$.

The final answer should be the series expansion.

The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{1}{2}\log(1-g)$.
Expanding this for small $g$:
$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} + O(g^4)\right)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$.

The terms through order $g^3$ are $\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}$.

The final answer is $\boxed{\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6}}$.