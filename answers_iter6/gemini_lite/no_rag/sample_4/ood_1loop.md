Here's a step-by-step solution to compute the 1-loop contribution to $\log(Z/Z_0)$:

**1. Understanding the Problem**

We are asked to find the leading correction to the logarithm of the partition function due to a non-linear interaction term in a zero-dimensional theory. The action is given by $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$. The partition function $Z$ is defined as $Z = \int dx \, e^{-S(x)/\hbar}$, and $Z_0$ is the partition function for the free theory, where $g=0$. We need to expand the result in powers of $g$ up to order $g^3$.

**2. Free Theory Partition Function ($Z_0$)**

When $g=0$, the action is $S_0(x) = \frac{x^2}{2}$. The free partition function is:
$Z_0 = \int dx \, e^{-x^2/(2\hbar)}$
This is a Gaussian integral. We can solve it by completing the square in the exponent if we consider it a standard Gaussian integral form $\int dx \, e^{-ax^2}$. In our case, $a = 1/(2\hbar)$. The result of a Gaussian integral $\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\frac{\pi}{a}}$.
So, $Z_0 = \sqrt{\frac{\pi}{1/(2\hbar)}} = \sqrt{2\pi\hbar}$.

**3. Perturbative Expansion**

We are interested in $\log(Z/Z_0)$. We can write $Z$ in terms of $Z_0$ and the interaction term:
$Z = \int dx \, e^{-S_0(x)/\hbar} e^{-S_{int}(x)/\hbar} = Z_0 \int dx \, e^{-S_{int}(x)/\hbar}$
where $S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$.

Then, $\frac{Z}{Z_0} = \int dx \, e^{-S_{int}(x)/\hbar}$.
And $\log\left(\frac{Z}{Z_0}\right) = \log\left(\int dx \, e^{-S_{int}(x)/\hbar}\right)$.

We need to expand this in powers of $g$. The interaction term $S_{int}(x)$ is proportional to $g$. The exponential $e^{-S_{int}(x)/\hbar}$ can be expanded using the Taylor series:
$e^{-S_{int}(x)/\hbar} = 1 - \frac{S_{int}(x)}{\hbar} + \frac{1}{2!} \left(\frac{S_{int}(x)}{\hbar}\right)^2 - \frac{1}{3!} \left(\frac{S_{int}(x)}{\hbar}\right)^3 + \dots$

So, $\frac{Z}{Z_0} = \int dx \left( 1 - \frac{S_{int}(x)}{\hbar} + \frac{1}{2\hbar^2} S_{int}(x)^2 - \frac{1}{6\hbar^3} S_{int}(x)^3 + \dots \right)$
$\frac{Z}{Z_0} = 1 - \frac{1}{\hbar} \int dx \, S_{int}(x) + \frac{1}{2\hbar^2} \int dx \, S_{int}(x)^2 - \frac{1}{6\hbar^3} \int dx \, S_{int}(x)^3 + \dots$

Now, we use the Taylor expansion of $\log(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \dots$. Let $u = \frac{Z}{Z_0} - 1$.
$\log\left(\frac{Z}{Z_0}\right) = \left( - \frac{1}{\hbar} \int dx \, S_{int}(x) + \frac{1}{2\hbar^2} \int dx \, S_{int}(x)^2 - \frac{1}{6\hbar^3} \int dx \, S_{int}(x)^3 + \dots \right) - \frac{1}{2} \left( - \frac{1}{\hbar} \int dx \, S_{int}(x) + \dots \right)^2 + \frac{1}{3} \left( - \frac{1}{\hbar} \int dx \, S_{int}(x) + \dots \right)^3 + \dots$

We are interested in the 1-loop contribution, which corresponds to the terms up to order $g^3$. The term $\log(Z/Z_0)$ can be expressed using Feynman diagrams. In zero dimensions, the 1-loop contribution is precisely the term arising from the one-loop diagram, which corresponds to the logarithm of the integral of the exponential of the interaction. The formula for the effective action $\Gamma$ in terms of the generating functional of connected diagrams is $\Gamma = - \log Z$. The 1-loop contribution to the effective action is given by $\frac{i\hbar}{2} \text{Tr} \log G$, where $G$ is the propagator. In zero dimensions, this becomes $\frac{i\hbar}{2} \log (\int dx \, e^{-S_{int}(x)/\hbar})$. However, the problem asks for $\log(Z/Z_0)$, which is directly related to the connected diagrams.

A more direct way to think about the 1-loop contribution to $\log(Z/Z_0)$ is through the expansion:
$\log Z = \log Z_0 + \log \left( \int dx \, e^{-S_{int}(x)/\hbar} \right)$
$\log Z = \log Z_0 + \log \left( 1 + \int dx \left( e^{-S_{int}(x)/\hbar} - 1 \right) \right)$
$\log Z = \log Z_0 + \int dx \left( e^{-S_{int}(x)/\hbar} - 1 \right) - \frac{1}{2} \left( \int dx \left( e^{-S_{int}(x)/\hbar} - 1 \right) \right)^2 + \dots$

Let's focus on the terms that contribute to $\log(Z/Z_0)$ up to order $g^3$.
$\log\left(\frac{Z}{Z_0}\right) = \log\left(\int dx \, e^{-S_{int}(x)/\hbar}\right)$
Using $\log(1+x) \approx x$ for small $x$:
$\log\left(\frac{Z}{Z_0}\right) \approx \int dx \, \left( e^{-S_{int}(x)/\hbar} - 1 \right)$
Expanding the exponential:
$\log\left(\frac{Z}{Z_0}\right) \approx \int dx \, \left( 1 - \frac{S_{int}(x)}{\hbar} + \frac{S_{int}(x)^2}{2\hbar^2} - \frac{S_{int}(x)^3}{6\hbar^3} + \dots - 1 \right)$
$\log\left(\frac{Z}{Z_0}\right) \approx - \frac{1}{\hbar} \int dx \, S_{int}(x) + \frac{1}{2\hbar^2} \int dx \, S_{int}(x)^2 - \frac{1}{6\hbar^3} \int dx \, S_{int}(x)^3 + \dots$

This expansion is correct if the integral $\int dx \, e^{-S_{int}(x)/\hbar}$ is close to 1. However, the problem statement implies a 1-loop contribution, which usually refers to the next-to-leading order term in the $\frac{1}{\hbar}$ expansion of $\log Z$.

The 1-loop contribution to $\log Z$ is given by $\frac{i\hbar}{2} \text{Tr} \log G$, where $G$ is the propagator. In 0D, this translates to $\frac{i\hbar}{2} \log(\text{det}(G^{-1}))$.
Alternatively, the 1-loop contribution to $\log Z$ is obtained by expanding $\log Z$ around the saddle point of the classical action. For $S(x) = x^2/2$, the saddle point is at $x=0$.
The 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log \det(M)$, where $M$ is the Hessian matrix of $S(x)$ evaluated at the saddle point.
$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$
$S_0(x) = \frac{x^2}{2}$
The saddle point for $S_0(x)$ is $x=0$.
The Hessian of $S(x)$ is $\frac{d^2S}{dx^2} = 1 - \frac{g}{2} \frac{d^2}{dx^2}(x^2 \cosh(x))$.
$\frac{d}{dx}(x^2 \cosh(x)) = 2x \cosh(x) + x^2 \sinh(x)$
$\frac{d^2}{dx^2}(x^2 \cosh(x)) = 2 \cosh(x) + 2x \sinh(x) + 2x \sinh(x) + x^2 \cosh(x) = (2+x^2)\cosh(x) + 4x \sinh(x)$.
So, $\frac{d^2S}{dx^2} = 1 - \frac{g}{2} ((2+x^2)\cosh(x) + 4x \sinh(x))$.
At the saddle point $x=0$:
$\frac{d^2S}{dx^2}\Big|_{x=0} = 1 - \frac{g}{2} (2\cosh(0) + 0) = 1 - \frac{g}{2}(2) = 1-g$.
The 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log(1-g)$.

We are asked for $\log(Z/Z_0)$.
$Z = Z_0 \int dx \, e^{-S_{int}(x)/\hbar}$
$\log(Z/Z_0) = \log\left( \int dx \, e^{\frac{g}{2\hbar} x^2 \cosh(x)} \right)$.

Let's use the expansion of $\cosh(x)$: $\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots$
$\frac{g}{2\hbar} x^2 \cosh(x) = \frac{g}{2\hbar} x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots \right)$
$= \frac{g}{2\hbar} \left( x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \frac{x^8}{720} + \dots \right)$

We need to compute $\log\left( \int dx \, e^{\frac{g}{2\hbar} (x^2 + \frac{x^4}{2} + \dots)} \right)$.
Let $u = \frac{g}{2\hbar} (x^2 + \frac{x^4}{2} + \dots)$.
$\int dx \, e^u = \int dx \, \left( 1 + u + \frac{u^2}{2} + \frac{u^3}{6} + \dots \right)$.

We need to integrate terms of the form $\int dx \, x^{2n}$. For a zero-dimensional theory, these integrals are typically normalized using the free partition function. The relevant integrals are related to moments of the Gaussian distribution.
$\int_{-\infty}^{\infty} dx \, x^{2n} e^{-x^2/(2\hbar)} = (2n-1)!! (2\hbar)^n \sqrt{2\pi\hbar}$.
So, $\frac{1}{Z_0} \int dx \, x^{2n} e^{-x^2/(2\hbar)} = (2n-1)!! (2\hbar)^n$. These are the moments of the free theory.

Let's consider the expansion of $\log(Z/Z_0)$ directly from the definition:
$\log\left(\frac{Z}{Z_0}\right) = \log\left( \frac{\int dx \, e^{-S(x)/\hbar}}{\int dx \, e^{-S_0(x)/\hbar}} \right)$
$= \log\left( \int dx \, e^{-(S(x)-S_0(x))/\hbar} \right)$
$= \log\left( \int dx \, e^{-S_{int}(x)/\hbar} \right)$
where $S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$.

Let $I = \int dx \, e^{-S_{int}(x)/\hbar} = \int dx \, e^{\frac{g}{2\hbar} x^2 \cosh(x)}$.
We use the expansion of $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots$
$I = \int dx \, \exp\left( \frac{g}{2\hbar} x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots \right) \right)$
$I = \int dx \, \exp\left( \frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \frac{g}{48\hbar} x^6 + \frac{g}{1440\hbar} x^8 + \dots \right)$

We are interested in $\log(I)$. We can use the formula $\log(I) = \log(\int dx \, e^A) = \log(\int dx \, (1 + A + A^2/2 + A^3/6 + ...))$.
However, this integral is not directly in the form of $\log Z_0$.

Let's use the property that for small perturbation, $\log Z \approx \log Z_0 - \langle S_{int} \rangle_0$, where $\langle \dots \rangle_0$ denotes the expectation value in the free theory. This is an approximation.
The 1-loop contribution to $\log Z$ is related to the connected diagrams.
The generating functional for connected Green's functions is $W[J] = \log Z[J] = \log \int dx \, e^{i J x - S(x)/\hbar}$.
The 1-loop contribution to $W[0]$ is $\frac{\hbar}{2} \log \det(M)$, where $M$ is the Hessian of the classical action at the minimum. We found $M|_{x=0} = 1-g$.
So, the 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log(1-g)$.

We need $\log(Z/Z_0)$.
$Z = \int dx \, e^{-\frac{x^2}{2\hbar} + \frac{g}{2\hbar} x^2 \cosh(x)}$
$\log Z = \log \int dx \, e^{-\frac{x^2}{2\hbar} + \frac{g}{2\hbar} x^2 \cosh(x)}$
Let $S_{pert}(x) = \frac{g}{2\hbar} x^2 \cosh(x)$.
$\log Z = \log \int dx \, e^{-x^2/(2\hbar)} e^{S_{pert}(x)}$
$\log Z = \log \left( Z_0 \int dx \, e^{-x^2/(2\hbar)} e^{S_{pert}(x)} / Z_0 \right)$
$\log Z = \log Z_0 + \log \left( \int dx \, e^{-x^2/(2\hbar)} e^{S_{pert}(x)} / Z_0 \right)$
$\log(Z/Z_0) = \log \left( \langle e^{S_{pert}(x)} \rangle_0 \right)$

Now, expand $e^{S_{pert}(x)}$:
$e^{S_{pert}(x)} = 1 + S_{pert}(x) + \frac{S_{pert}(x)^2}{2!} + \frac{S_{pert}(x)^3}{3!} + \dots$
$\log(Z/Z_0) = \log \left( \langle 1 + S_{pert}(x) + \frac{S_{pert}(x)^2}{2} + \frac{S_{pert}(x)^3}{6} + \dots \rangle_0 \right)$
Using $\log(1+u) = u - u^2/2 + u^3/3 - \dots$, where $u = \langle S_{pert} \rangle_0 + \frac{\langle S_{pert}^2 \rangle_0}{2} + \dots$
This is getting complicated. Let's use the formula for the cumulants.
$\log \langle e^A \rangle = \sum_{n=1}^\infty \frac{1}{n!} \langle A^n \rangle_c$, where $\langle \dots \rangle_c$ are connected cumulants.
Here $A = S_{pert}(x) = \frac{g}{2\hbar} x^2 \cosh(x)$.
We need to compute $\langle A \rangle_0$, $\langle A^2 \rangle_0$, $\langle A^3 \rangle_0$.

$A = \frac{g}{2\hbar} x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots \right)$
$A = \frac{g}{2\hbar} \left( x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \frac{x^8}{720} + \dots \right)$

The relevant moments of the free theory are:
$\langle x^2 \rangle_0 = \hbar$
$\langle x^4 \rangle_0 = 3\hbar^2$
$\langle x^6 \rangle_0 = 15\hbar^3$
$\langle x^8 \rangle_0 = 105\hbar^4$

Term 1: $\langle A \rangle_0$
$\langle A \rangle_0 = \frac{g}{2\hbar} \left( \langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \frac{1}{24} \langle x^6 \rangle_0 + \frac{1}{720} \langle x^8 \rangle_0 + \dots \right)$
$\langle A \rangle_0 = \frac{g}{2\hbar} \left( \hbar + \frac{1}{2} (3\hbar^2) + \frac{1}{24} (15\hbar^3) + \frac{1}{720} (105\hbar^4) + \dots \right)$
$\langle A \rangle_0 = \frac{g}{2} \left( 1 + \frac{3}{2} \hbar + \frac{15}{24} \hbar^2 + \frac{105}{720} \hbar^3 + \dots \right)$
$\langle A \rangle_0 = \frac{g}{2} \left( 1 + \frac{3}{2} \hbar + \frac{5}{8} \hbar^2 + \frac{7}{48} \hbar^3 + \dots \right)$

Term 2: $\frac{1}{2} \langle A^2 \rangle_0$
$A^2 = \left( \frac{g}{2\hbar} \right)^2 \left( x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots \right) \left( x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots \right)$
$A^2 = \left( \frac{g}{2\hbar} \right)^2 \left( x^4 + \frac{x^6}{2} + \frac{x^8}{24} + \frac{x^6}{2} + \frac{x^8}{4} + \frac{x^{10}}{48} + \frac{x^8}{24} + \frac{x^{10}}{48} + \dots \right)$
$A^2 = \left( \frac{g}{2\hbar} \right)^2 \left( x^4 + x^6 + \left(\frac{1}{24} + \frac{1}{4} + \frac{1}{24}\right) x^8 + \dots \right)$
$A^2 = \left( \frac{g}{2\hbar} \right)^2 \left( x^4 + x^6 + \left(\frac{1+6+1}{24}\right) x^8 + \dots \right) = \left( \frac{g}{2\hbar} \right)^2 \left( x^4 + x^6 + \frac{8}{24} x^8 + \dots \right) = \left( \frac{g}{2\hbar} \right)^2 \left( x^4 + x^6 + \frac{1}{3} x^8 + \dots \right)$

$\langle A^2 \rangle_0 = \left( \frac{g}{2\hbar} \right)^2 \left( \langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{1}{3} \langle x^8 \rangle_0 + \dots \right)$
$\langle A^2 \rangle_0 = \left( \frac{g}{2\hbar} \right)^2 \left( 3\hbar^2 + 15\hbar^3 + \frac{1}{3} (105\hbar^4) + \dots \right)$
$\langle A^2 \rangle_0 = \frac{g^2}{4\hbar^2} \left( 3\hbar^2 + 15\hbar^3 + 35\hbar^4 + \dots \right)$
$\langle A^2 \rangle_0 = \frac{g^2}{4} \left( 3 + 15\hbar + 35\hbar^2 + \dots \right)$

$\frac{1}{2} \langle A^2 \rangle_0 = \frac{g^2}{8} \left( 3 + 15\hbar + 35\hbar^2 + \dots \right)$

Term 3: $\frac{1}{6} \langle A^3 \rangle_0$
$A^3 = \left( \frac{g}{2\hbar} \right)^3 (x^2 + \frac{x^4}{2} + \dots)^3$
$A^3 = \left( \frac{g}{2\hbar} \right)^3 (x^6 + 3 x^4 (\frac{x^2}{2}) + \dots) = \left( \frac{g}{2\hbar} \right)^3 (x^6 + \frac{3}{2} x^6 + \dots) = \left( \frac{g}{2\hbar} \right)^3 (\frac{5}{2} x^6 + \dots)$

$\langle A^3 \rangle_0 = \left( \frac{g}{2\hbar} \right)^3 \frac{5}{2} \langle x^6 \rangle_0 + \dots$
$\langle A^3 \rangle_0 = \frac{g^3}{8\hbar^3} \frac{5}{2} (15\hbar^3) + \dots = \frac{75}{16} g^3 + \dots$

$\frac{1}{6} \langle A^3 \rangle_0 = \frac{1}{6} \frac{75}{16} g^3 + \dots = \frac{25}{32} g^3 + \dots$

Now, let's collect the terms for $\log(Z/Z_0)$ as a power series in $g$:
$\log(Z/Z_0) = \langle A \rangle_0 + \frac{1}{2} \langle A^2 \rangle_0 + \frac{1}{6} \langle A^3 \rangle_0 + \dots$

Terms in $g$:
From $\langle A \rangle_0$: $\frac{g}{2} (1) = \frac{g}{2}$.
From $\frac{1}{2} \langle A^2 \rangle_0$: $\frac{g^2}{8} (3) = \frac{3g^2}{8}$.
From $\frac{1}{6} \langle A^3 \rangle_0$: $\frac{25}{32} g^3$.

Let's re-evaluate the problem statement: "Compute the 1-loop contribution to log(Z/Z_0)".
The 1-loop contribution usually refers to the terms proportional to $\hbar$.
The expression $\log(Z/Z_0) = \log \langle e^{S_{pert}(x)} \rangle_0$ is the full expression.

Let's consider the expansion of $\log Z$ itself:
$\log Z = \log Z_0 + \log \langle e^{S_{pert}} \rangle_0$.
The 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log(1-g)$.
$\log(1-g) = -g - \frac{g^2}{2} - \frac{g^3}{3} - \dots$
So, 1-loop contribution to $\log Z$ is $-\frac{\hbar}{2} g - \frac{\hbar}{2} \frac{g^2}{2} - \frac{\hbar}{2} \frac{g^3}{3} - \dots$

The problem asks for the 1-loop contribution to $\log(Z/Z_0)$. This means we should consider the terms that arise from the 1-loop calculation. In the context of field theory, the 1-loop correction to $\log Z$ is $\frac{1}{2} \text{Tr} \log G$, where $G$ is the propagator.

The action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
The free action is $S_0(x) = \frac{x^2}{2}$.
The interaction is $S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$.

The 1-loop correction to $\log Z$ is given by:
$\Delta \log Z = \frac{\hbar}{2} \log \det(M)$, where $M$ is the Hessian of the classical action evaluated at the classical minimum.
We found $M|_{x=0} = 1-g$.
So, $\Delta \log Z = \frac{\hbar}{2} \log(1-g) = -\frac{\hbar}{2} g - \frac{\hbar}{2} \frac{g^2}{2} - \frac{\hbar}{2} \frac{g^3}{3} + \dots$

The problem asks for the 1-loop contribution to $\log(Z/Z_0)$.
$\log(Z/Z_0) = \log Z - \log Z_0$.
The 1-loop contribution to $\log Z_0$ is 0, as it is the free theory.
Therefore, the 1-loop contribution to $\log(Z/Z_0)$ is the same as the 1-loop contribution to $\log Z$.

Let's double check the wording. "Compute the 1-loop contribution to log(Z/Z_0)". This phrasing suggests we should focus on the terms that are "1-loop" in nature.

Let's expand $S(x)$ around $x=0$:
$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots)$
$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \frac{g}{1440} x^8 - \dots$
$S(x) = \frac{1-g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \frac{g}{1440} x^8 - \dots$

The 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log \det(M)$, where $M$ is the Hessian of the action.
The Hessian is $\frac{d^2S}{dx^2} = (1-g) - \frac{g}{4} (12x^2) - \frac{g}{48} (30x^4) - \dots$
At $x=0$, $\frac{d^2S}{dx^2}\Big|_{x=0} = 1-g$.
So, the 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log(1-g)$.

Since $Z_0$ is the partition function of the free theory ($g=0$), its $\log Z_0$ does not have any $g$ dependence. Thus, the 1-loop contribution to $\log(Z/Z_0)$ is the same as the 1-loop contribution to $\log Z$.

Expand $\frac{\hbar}{2} \log(1-g)$ as a power series in $g$ through order $g^3$:
$\log(1-g) = -g - \frac{g^2}{2} - \frac{g^3}{3} - \dots$
$\frac{\hbar}{2} \log(1-g) = \frac{\hbar}{2} \left( -g - \frac{g^2}{2} - \frac{g^3}{3} + \dots \right)$
$= -\frac{\hbar}{2} g - \frac{\hbar}{4} g^2 - \frac{\hbar}{6} g^3 + \dots$

The 1-loop contribution is precisely the term arising from the determinant of the Hessian. The higher-order terms in $g$ in the expansion of $\log(1-g)$ represent higher-loop contributions.

The problem asks for the 1-loop contribution, which means we should take the first term in the $\hbar$ expansion of $\log Z$.
The 1-loop contribution to $\log Z$ is $\frac{\hbar}{2} \log(1-g)$.
We need to expand this in powers of $g$ up to order $g^3$.

The expansion of $\log(1-g)$ is $-g - \frac{g^2}{2} - \frac{g^3}{3} - \dots$.
Multiplying by $\frac{\hbar}{2}$, we get $-\frac{\hbar}{2} g - \frac{\hbar}{4} g^2 - \frac{\hbar}{6} g^3$.

Final check of the question: "Compute the 1-loop contribution to log(Z/Z_0)". This is asking for the part of $\log(Z/Z_0)$ that is of order $\hbar$.
The full $\log Z$ can be written as $\log Z = \log Z_0 + \Delta_1 \log Z + \Delta_2 \log Z + \dots$, where $\Delta_n \log Z$ is the contribution of order $\hbar^n$.
Here, $\Delta_1 \log Z = \frac{\hbar}{2} \log(1-g)$.
Since $\log Z_0$ has no $\hbar$ dependence and no $g$ dependence, the 1-loop contribution to $\log(Z/Z_0)$ is simply $\Delta_1 \log Z$.

The expansion of $\frac{\hbar}{2} \log(1-g)$ to order $g^3$ is indeed $-\frac{\hbar}{2} g - \frac{\hbar}{4} g^2 - \frac{\hbar}{6} g^3$.

The final answer is $\boxed{-\frac{\hbar}{2} g - \frac{\hbar}{4} g^2 - \frac{\hbar}{6} g^3}$.