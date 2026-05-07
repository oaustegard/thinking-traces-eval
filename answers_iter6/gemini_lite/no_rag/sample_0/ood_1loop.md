Here's a step-by-step solution to compute the 1-loop contribution to log(Z/Z_0):

**1. Understanding the Problem**

We are asked to find the 1-loop correction to the logarithm of the partition function, $\log(Z/Z_0)$, for a given zero-dimensional action. The action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$. $Z$ is the full partition function, and $Z_0$ is the partition function in the absence of the interaction (i.e., when $g=0$). We need to expand this correction as a power series in $g$ up to order $g^3$.

**2. The Free Partition Function ($Z_0$)**

When $g=0$, the action is $S_0(x) = \frac{x^2}{2}$. The free partition function is:
$Z_0 = \int_{-\infty}^{\infty} e^{-S_0(x)/\hbar} dx = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx$
This is a standard Gaussian integral. The result is $Z_0 = \sqrt{2\pi\hbar}$.

**3. The Full Partition Function ($Z$) and Perturbation Theory**

The full action is $S(x) = S_0(x) + S_{int}(x)$, where $S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$.
The partition function is $Z = \int dx \, e^{-S(x)/\hbar} = \int dx \, e^{-(S_0(x) + S_{int}(x))/\hbar}$.
We can rewrite this as:
$Z = \int dx \, e^{-S_0(x)/\hbar} e^{-S_{int}(x)/\hbar} = Z_0 \int dx \, e^{-S_0(x)/\hbar} \frac{e^{-S_{int}(x)/\hbar}}{Z_0}$
$Z = Z_0 \left\langle e^{-S_{int}(x)/\hbar} \right\rangle_0$
where $\langle \dots \rangle_0$ denotes the expectation value with respect to the free measure $e^{-S_0(x)/\hbar}$.

Taking the logarithm:
$\log(Z/Z_0) = \log \left\langle e^{-S_{int}(x)/\hbar} \right\rangle_0$

Using the Taylor expansion of the exponential $e^A = 1 + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \dots$, and then taking the logarithm of $1 + (\text{series})$, we get:
$\log(1+A) = A - \frac{A^2}{2} + \frac{A^3}{3} - \dots$

In our case, $A = -\frac{S_{int}(x)}{\hbar}$. So,
$\log \left\langle e^{-S_{int}(x)/\hbar} \right\rangle_0 = \left\langle -\frac{S_{int}(x)}{\hbar} \right\rangle_0 - \frac{1}{2} \left\langle \left(-\frac{S_{int}(x)}{\hbar}\right)^2 \right\rangle_0 + \frac{1}{3} \left\langle \left(-\frac{S_{int}(x)}{\hbar}\right)^3 \right\rangle_0 - \dots$

We need to expand $S_{int}(x)$ in powers of $g$.
$S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$
The Taylor series for $\cosh(x)$ is $\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots$.
So, $S_{int}(x) = -\frac{g}{2} x^2 \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots \right)$
$S_{int}(x) = -\frac{g}{2} \left(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \frac{x^8}{720} + \dots \right)$

Let's denote the terms in the expansion of $\log(Z/Z_0)$ as $\mathcal{O}(g)$, $\mathcal{O}(g^2)$, and $\mathcal{O}(g^3)$.

**4. Calculating the $\mathcal{O}(g)$ Contribution**

The $\mathcal{O}(g)$ term is $\left\langle -\frac{S_{int}(x)}{\hbar} \right\rangle_0$.
$-\frac{S_{int}(x)}{\hbar} = \frac{g}{2\hbar} x^2 \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots \right)$
The $\mathcal{O}(g)$ contribution to $\log(Z/Z_0)$ is $\frac{g}{2\hbar} \left\langle x^2 + \frac{x^4}{2} + \dots \right\rangle_0$.

We need the expectation values of powers of $x$ with respect to the free measure. The free measure is Gaussian with variance $\hbar$: $\langle x^{2n} \rangle_0 = (2n-1)!! \hbar^n$.
$\langle x^2 \rangle_0 = 1 \cdot \hbar = \hbar$
$\langle x^4 \rangle_0 = 3 \cdot \hbar^2 = 3\hbar^2$
$\langle x^6 \rangle_0 = 15 \cdot \hbar^3 = 15\hbar^3$

So, the $\mathcal{O}(g)$ contribution is:
$\frac{g}{2\hbar} \left( \langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \dots \right) = \frac{g}{2\hbar} \left( \hbar + \frac{1}{2} (3\hbar^2) + \dots \right)$
The leading term in $g$ is $\frac{g}{2\hbar} (\hbar) = \frac{g}{2}$.

**5. Calculating the $\mathcal{O}(g^2)$ Contribution**

The $\mathcal{O}(g^2)$ term is $-\frac{1}{2} \left\langle \left(-\frac{S_{int}(x)}{\hbar}\right)^2 \right\rangle_0 = -\frac{1}{2\hbar^2} \left\langle S_{int}(x)^2 \right\rangle_0$.
$S_{int}(x) = -\frac{g}{2} x^2 (1 + \frac{x^2}{2} + \dots)$
$S_{int}(x)^2 = \left(\frac{g}{2}\right)^2 x^4 (1 + \frac{x^2}{2} + \dots)^2 = \frac{g^2}{4} x^4 (1 + x^2 + \dots)$
The lowest order term in $g^2$ from $S_{int}(x)^2$ is $\frac{g^2}{4} x^4$.

So, the $\mathcal{O}(g^2)$ contribution is $-\frac{1}{2\hbar^2} \left\langle \frac{g^2}{4} x^4 + \dots \right\rangle_0 = -\frac{g^2}{8\hbar^2} \langle x^4 \rangle_0$.
Using $\langle x^4 \rangle_0 = 3\hbar^2$:
$\mathcal{O}(g^2) \text{ contribution} = -\frac{g^2}{8\hbar^2} (3\hbar^2) = -\frac{3g^2}{8}$.

**6. Calculating the $\mathcal{O}(g^3)$ Contribution**

The $\mathcal{O}(g^3)$ term is $\frac{1}{3} \left\langle \left(-\frac{S_{int}(x)}{\hbar}\right)^3 \right\rangle_0 = \frac{1}{3\hbar^3} \left\langle (-S_{int}(x))^3 \right\rangle_0$.
$(-S_{int}(x))^3 = \left(\frac{g}{2} x^2 (1 + \frac{x^2}{2} + \dots)\right)^3 = \left(\frac{g}{2}\right)^3 x^6 (1 + \frac{x^2}{2} + \dots)^3$
The lowest order term in $g^3$ from $(-S_{int}(x))^3$ is $\frac{g^3}{8} x^6$.

So, the $\mathcal{O}(g^3)$ contribution is $\frac{1}{3\hbar^3} \left\langle \frac{g^3}{8} x^6 + \dots \right\rangle_0 = \frac{g^3}{24\hbar^3} \langle x^6 \rangle_0$.
Using $\langle x^6 \rangle_0 = 15\hbar^3$:
$\mathcal{O}(g^3) \text{ contribution} = \frac{g^3}{24\hbar^3} (15\hbar^3) = \frac{15g^3}{24} = \frac{5g^3}{8}$.

**7. Combining the Contributions**

The 1-loop contribution to $\log(Z/Z_0)$ up to order $g^3$ is the sum of the $\mathcal{O}(g)$, $\mathcal{O}(g^2)$, and $\mathcal{O}(g^3)$ terms.

$\log(Z/Z_0) \approx \frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8}$.

**Important Note on "1-loop contribution":** In field theory, "1-loop" usually refers to diagrams with one closed loop, which corresponds to terms quadratic in the interaction. However, in this context, the question asks for the expansion of $\log(Z/Z_0)$ in powers of $g$, and the first few terms of this expansion are being requested. The phrasing "1-loop contribution to log(Z/Z_0)" is a bit ambiguous, but given the request for a power series in $g$, it implies calculating the terms of the perturbative expansion of $\log(Z/Z_0)$. If it strictly meant terms arising from single-loop Feynman diagrams, the calculation would be different and involve propagators. However, for a zero-dimensional theory, the "loop expansion" is directly related to the power series expansion of the logarithm of the partition function.

Let's re-evaluate the terms considering the structure of the expansion of $\log \langle e^A \rangle$:
$\log \langle e^A \rangle = \langle A \rangle - \frac{1}{2} \langle A^2 \rangle_{c} + \frac{1}{3} \langle A^3 \rangle_{c} - \dots$
where $\langle \dots \rangle_c$ denotes cumulants. For Gaussian integrals, the connected parts are the cumulants.

Let $A = -\frac{S_{int}}{\hbar} = \frac{g}{2\hbar} x^2 \cosh(x)$.
We need to expand $\cosh(x)$ to higher orders to get the $g^3$ contribution correctly.

$S_{int}(x) = -\frac{g}{2} x^2 \left(1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots \right)$
$S_{int}(x) = -\frac{g}{2} \left(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \frac{x^8}{720} + \dots \right)$

**Term 1: $\langle A \rangle = \langle -\frac{S_{int}}{\hbar} \rangle_0$**
$= \frac{g}{2\hbar} \langle x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots \rangle_0$
$= \frac{g}{2\hbar} (\hbar + \frac{3\hbar^2}{2} + \frac{15\hbar^3}{24} + \dots)$
The leading term is $\frac{g}{2}$.

**Term 2: $-\frac{1}{2} \langle A^2 \rangle_{c} = -\frac{1}{2\hbar^2} \langle S_{int}^2 \rangle_0$**
$S_{int}^2 = \left(-\frac{g}{2}\right)^2 \left(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots\right) \left(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots\right)$
We need terms up to $x^6$ in $S_{int}$ to get a $g^3$ contribution in the final result.
$S_{int}^2 = \frac{g^2}{4} \left( x^4 + \frac{x^6}{2} + \frac{x^6}{2} + \dots \right) = \frac{g^2}{4} \left( x^4 + x^6 + \dots \right)$
$\langle S_{int}^2 \rangle_0 = \frac{g^2}{4} \langle x^4 + x^6 + \dots \rangle_0 = \frac{g^2}{4} (3\hbar^2 + 15\hbar^3 + \dots)$
The term $-\frac{1}{2\hbar^2} \langle S_{int}^2 \rangle_0 = -\frac{1}{2\hbar^2} \frac{g^2}{4} (3\hbar^2 + \dots) = -\frac{3g^2}{8}$. This matches.

**Term 3: $\frac{1}{3} \langle A^3 \rangle_{c} = \frac{1}{3\hbar^3} \langle (-S_{int})^3 \rangle_0$**
$(-S_{int})^3 = \left(\frac{g}{2}\right)^3 \left(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots\right)^3$
We need the term proportional to $x^6$ in the expansion of $(-S_{int})^3$.
The dominant term in $S_{int}$ is $-\frac{g}{2}x^2$.
So, $(-S_{int})^3 \approx \left(\frac{g}{2} x^2\right)^3 = \frac{g^3}{8} x^6$.
$\langle (-S_{int})^3 \rangle_0 = \frac{g^3}{8} \langle x^6 \rangle_0 = \frac{g^3}{8} (15\hbar^3)$.
The term $\frac{1}{3\hbar^3} \langle (-S_{int})^3 \rangle_0 = \frac{1}{3\hbar^3} \frac{g^3}{8} (15\hbar^3) = \frac{15g^3}{24} = \frac{5g^3}{8}$. This also matches.

The calculation seems correct. The interpretation of "1-loop contribution" in this zero-dimensional context as the perturbative expansion of $\log(Z/Z_0)$ is consistent with how such problems are usually posed.

Final Answer is the sum of these terms: $\frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8}$.

The final answer is $\boxed{\frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8}}$.