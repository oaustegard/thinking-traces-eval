Here's a step-by-step solution to compute the 1-loop contribution to $\log(Z/Z_0)$:

The action is given by $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
We are interested in the $\log(Z/Z_0)$, where $Z = \int dx e^{-S(x)/\hbar}$ and $Z_0$ is the partition function for $g=0$.
The free action is $S_0(x) = \frac{x^2}{2}$.
The partition function $Z$ can be written as:
$Z = \int dx e^{-S_0(x)/\hbar} e^{-(S(x)-S_0(x))/\hbar}$
$Z = Z_0 \int dx e^{-S_0(x)/\hbar} e^{-V(x)/\hbar} / Z_0$, where $V(x) = S(x) - S_0(x) = -\frac{g}{2} x^2 \cosh(x)$.
So, $\frac{Z}{Z_0} = \int dx e^{-S_0(x)/\hbar} e^{-V(x)/\hbar}$.

We are asked for the 1-loop contribution. In quantum field theory, the 1-loop contribution to $\log(Z)$ is given by $\frac{1}{2} \text{Tr} \log(M)$, where $M$ is the Hessian matrix of the action evaluated at the classical saddle point. In this zero-dimensional case, the "matrix" is just a number, and the trace becomes a logarithm. The 1-loop contribution to $\log(Z)$ is $\frac{1}{2} \log(\det(M_{ij})) = \frac{1}{2} \log(\text{det}(S''(x_{cl})))$.

However, the problem is formulated in a way that suggests an expansion of $\log(Z/Z_0)$ in powers of $g$.
We have $\frac{Z}{Z_0} = \int dx e^{-S_0(x)/\hbar} e^{-V(x)/\hbar}$.
Taking the logarithm:
$\log(\frac{Z}{Z_0}) = \log \left( \int dx e^{-S_0(x)/\hbar} e^{-V(x)/\hbar} \right)$.

We can use the expansion $e^{-V(x)/\hbar} = 1 - \frac{V(x)}{\hbar} + \frac{V(x)^2}{2\hbar^2} - \frac{V(x)^3}{6\hbar^3} + \dots$
$\frac{Z}{Z_0} = \int dx e^{-S_0(x)/\hbar} \left( 1 - \frac{V(x)}{\hbar} + \frac{V(x)^2}{2\hbar^2} - \frac{V(x)^3}{6\hbar^3} + \dots \right)$
$\frac{Z}{Z_0} = \int dx e^{-S_0(x)/\hbar} - \frac{1}{\hbar} \int dx e^{-S_0(x)/\hbar} V(x) + \frac{1}{2\hbar^2} \int dx e^{-S_0(x)/\hbar} V(x)^2 - \frac{1}{6\hbar^3} \int dx e^{-S_0(x)/\hbar} V(x)^3 + \dots$

The first term is $Z_0$. So,
$\frac{Z}{Z_0} = 1 - \frac{1}{\hbar} \langle V(x) \rangle_0 + \frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0 - \frac{1}{6\hbar^3} \langle V(x)^3 \rangle_0 + \dots$,
where $\langle \dots \rangle_0 = \frac{\int dx e^{-S_0(x)/\hbar} (\dots)}{\int dx e^{-S_0(x)/\hbar}}$ denotes the expectation value in the free theory.

Now we take the logarithm:
$\log(\frac{Z}{Z_0}) = \log \left( 1 - \frac{1}{\hbar} \langle V(x) \rangle_0 + \frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0 - \frac{1}{6\hbar^3} \langle V(x)^3 \rangle_0 + \dots \right)$
Using the expansion $\log(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \dots$, where $u = - \frac{1}{\hbar} \langle V(x) \rangle_0 + \frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0 - \frac{1}{6\hbar^3} \langle V(x)^3 \rangle_0 + \dots$.

We need to expand up to order $g^3$.
$V(x) = -\frac{g}{2} x^2 \cosh(x)$.
The expansion of $\cosh(x)$ is $\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots$.
$V(x) = -\frac{g}{2} x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots \right)$
$V(x) = -\frac{g}{2} \left( x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \frac{x^8}{720} + \dots \right)$

The free action is $S_0(x) = \frac{x^2}{2}$. The free partition function is $Z_0 = \int dx e^{-x^2/(2\hbar)}$. This is a Gaussian integral.
We know that for a Gaussian integral $\int dx e^{-ax^2/2} x^{2n} = \sqrt{\frac{2\pi}{a}} \frac{(2n)!}{n! 2^n a^n}$.
Here, $a = 1/\hbar$.
$\langle x^{2n} \rangle_0 = \frac{\int dx e^{-x^2/(2\hbar)} x^{2n}}{\int dx e^{-x^2/(2\hbar)}} = \frac{\sqrt{2\pi\hbar} \frac{(2n)!}{n! 2^n (1/\hbar)^n}}{\sqrt{2\pi\hbar}} = \frac{(2n)!}{n! 2^n} \hbar^n$.

Let's compute the terms in the expansion of $\log(Z/Z_0)$:

Term 1: $-\frac{1}{\hbar} \langle V(x) \rangle_0$
$V(x) = -\frac{g}{2} (x^2 + \frac{x^4}{2} + \dots)$
$\langle V(x) \rangle_0 = -\frac{g}{2} \left( \langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \dots \right)$
$\langle x^2 \rangle_0 = \frac{2!}{1! 2^1} \hbar^1 = \hbar$.
$\langle x^4 \rangle_0 = \frac{4!}{2! 2^2} \hbar^2 = \frac{24}{2 \cdot 4} \hbar^2 = 3\hbar^2$.
$\langle V(x) \rangle_0 = -\frac{g}{2} (\hbar + \frac{1}{2} (3\hbar^2) + \dots) = -\frac{g}{2} \hbar - \frac{3g}{4} \hbar^2 + \dots$
So, $-\frac{1}{\hbar} \langle V(x) \rangle_0 = -\frac{1}{\hbar} (-\frac{g}{2} \hbar - \frac{3g}{4} \hbar^2 + \dots) = \frac{g}{2} + \frac{3g}{4} \hbar + \dots$

Term 2: $\frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0$
$V(x)^2 = \left(-\frac{g}{2} x^2 \cosh(x)\right)^2 = \frac{g^2}{4} x^4 \cosh^2(x)$
$\cosh^2(x) = \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots\right)^2 = 1 + x^2 + \left(\frac{1}{4} + \frac{2}{24}\right) x^4 + \dots = 1 + x^2 + \frac{5}{12} x^4 + \dots$
$V(x)^2 = \frac{g^2}{4} x^4 \left( 1 + x^2 + \frac{5}{12} x^4 + \dots \right) = \frac{g^2}{4} \left( x^4 + x^6 + \frac{5}{12} x^8 + \dots \right)$
$\langle V(x)^2 \rangle_0 = \frac{g^2}{4} \left( \langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{5}{12} \langle x^8 \rangle_0 + \dots \right)$
$\langle x^6 \rangle_0 = \frac{6!}{3! 2^3} \hbar^3 = \frac{720}{6 \cdot 8} \hbar^3 = 15\hbar^3$.
$\langle x^8 \rangle_0 = \frac{8!}{4! 2^4} \hbar^4 = \frac{40320}{24 \cdot 16} \hbar^4 = 105\hbar^4$.
$\langle V(x)^2 \rangle_0 = \frac{g^2}{4} (\hbar^2 + \hbar^3 + \frac{5}{12} \hbar^4 + \dots)$
$\frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0 = \frac{1}{2\hbar^2} \frac{g^2}{4} (\hbar^2 + \hbar^3 + \dots) = \frac{g^2}{8} (1 + \hbar + \dots)$

Term 3: $-\frac{1}{6\hbar^3} \langle V(x)^3 \rangle_0$
$V(x)^3 = \left(-\frac{g}{2} x^2 \cosh(x)\right)^3 = -\frac{g^3}{8} x^6 \cosh^3(x)$
$\cosh^3(x) = \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots\right)^3 = 1 + 3(\frac{x^2}{2}) + \dots = 1 + \frac{3}{2} x^2 + \dots$
$V(x)^3 = -\frac{g^3}{8} x^6 (1 + \frac{3}{2} x^2 + \dots) = -\frac{g^3}{8} (x^6 + \frac{3}{2} x^8 + \dots)$
$\langle V(x)^3 \rangle_0 = -\frac{g^3}{8} (\langle x^6 \rangle_0 + \frac{3}{2} \langle x^8 \rangle_0 + \dots)$
$\langle V(x)^3 \rangle_0 = -\frac{g^3}{8} (\hbar^3 + \frac{3}{2} (3\hbar^4) + \dots) = -\frac{g^3}{8} (\hbar^3 + \frac{9}{2} \hbar^4 + \dots)$
$-\frac{1}{6\hbar^3} \langle V(x)^3 \rangle_0 = -\frac{1}{6\hbar^3} (-\frac{g^3}{8} (\hbar^3 + \dots)) = \frac{g^3}{48} (1 + \dots)$

Now we combine these terms for $\log(Z/Z_0)$. We need to expand $\log(1+u)$ up to order $g^3$.
$u = - \frac{1}{\hbar} \langle V(x) \rangle_0 + \frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0 - \frac{1}{6\hbar^3} \langle V(x)^3 \rangle_0 + \dots$
$u = (\frac{g}{2} + \frac{3g}{4} \hbar + \dots) + (\frac{g^2}{8} + \frac{g^2}{8} \hbar + \dots) + (\frac{g^3}{48} + \dots)$

The 1-loop contribution is often understood as the term proportional to $\hbar$. Let's re-evaluate the definition of 1-loop contribution.
The 1-loop correction to $\log Z$ is given by $\frac{1}{2} \log(\det(S''(x_{cl})))$.
$S''(x) = \frac{d^2}{dx^2} (\frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x))$
$S''(x) = 1 - \frac{g}{2} \frac{d^2}{dx^2}(x^2 \cosh(x))$
$\frac{d}{dx}(x^2 \cosh(x)) = 2x \cosh(x) + x^2 \sinh(x)$
$\frac{d^2}{dx^2}(x^2 \cosh(x)) = 2 \cosh(x) + 2x \sinh(x) + 2x \sinh(x) + x^2 \cosh(x) = 2 \cosh(x) + 4x \sinh(x) + x^2 \cosh(x)$
$S''(x) = 1 - \frac{g}{2} (2 \cosh(x) + 4x \sinh(x) + x^2 \cosh(x))$

The classical saddle point $x_{cl}$ is where $S'(x) = 0$.
$S'(x) = x - \frac{g}{2} (2x \cosh(x) + x^2 \sinh(x)) = 0$
$x \left( 1 - \frac{g}{2} (2 \cosh(x) + x \sinh(x)) \right) = 0$.
One solution is $x=0$. Let's evaluate $S''(x)$ at $x=0$.
$S''(0) = 1 - \frac{g}{2} (2 \cosh(0) + 0 + 0) = 1 - \frac{g}{2} (2) = 1-g$.
The 1-loop contribution to $\log Z$ is $\frac{1}{2} \log(S''(0)) = \frac{1}{2} \log(1-g)$.
This doesn't involve $\hbar$.

Let's go back to the $\log(Z/Z_0)$ expansion. The question asks for the "1-loop contribution", which in this context of a $g$ expansion likely refers to the terms that arise from the expansion of the exponential of the interaction.

Let's consider the expansion of $\log(\frac{Z}{Z_0})$ again:
$\log(\frac{Z}{Z_0}) = \log \left( 1 + \sum_{n=1}^{\infty} \frac{1}{n!} \langle (-V(x)/\hbar)^n \rangle_0 \right)$
Using $\log(1+u) = u - u^2/2 + u^3/3 - \dots$
$\log(\frac{Z}{Z_0}) = \left( -\frac{1}{\hbar} \langle V \rangle_0 + \frac{1}{2\hbar^2} \langle V^2 \rangle_0 - \frac{1}{6\hbar^3} \langle V^3 \rangle_0 + \dots \right) - \frac{1}{2} \left( -\frac{1}{\hbar} \langle V \rangle_0 + \dots \right)^2 + \frac{1}{3} \left( -\frac{1}{\hbar} \langle V \rangle_0 + \dots \right)^3 + \dots$

We need terms up to $g^3$.
The first term is $-\frac{1}{\hbar} \langle V \rangle_0 = \frac{g}{2} + \frac{3g}{4} \hbar + O(g\hbar^2)$.
The second term is $\frac{1}{2\hbar^2} \langle V^2 \rangle_0 = \frac{g^2}{8} + \frac{g^2}{8} \hbar + O(g^2\hbar^2)$.
The third term is $-\frac{1}{6\hbar^3} \langle V^3 \rangle_0 = \frac{g^3}{48} + O(g^3\hbar)$.

Now consider the quadratic term in the $\log(1+u)$ expansion:
$-\frac{1}{2} \left( -\frac{1}{\hbar} \langle V \rangle_0 + \dots \right)^2 = -\frac{1}{2} \left( \frac{g}{2} + \frac{3g}{4} \hbar + \dots \right)^2$
$= -\frac{1}{2} \left( \frac{g^2}{4} + 2 \frac{g}{2} \frac{3g}{4} \hbar + \dots \right) = -\frac{1}{2} \left( \frac{g^2}{4} + \frac{3g^2}{4} \hbar + \dots \right) = -\frac{g^2}{8} - \frac{3g^2}{8} \hbar + \dots$

Now consider the cubic term in the $\log(1+u)$ expansion:
$\frac{1}{3} \left( -\frac{1}{\hbar} \langle V \rangle_0 + \dots \right)^3 = \frac{1}{3} \left( \frac{g}{2} + \dots \right)^3 = \frac{1}{3} \left( \frac{g^3}{8} + \dots \right) = \frac{g^3}{24} + \dots$

Summing the contributions to $\log(Z/Z_0)$ up to $g^3$:
Order $g$: $\frac{g}{2}$
Order $g^2$: $\frac{g^2}{8} - \frac{g^2}{8} = 0$. This seems suspicious. Let's recheck the calculation of $\langle V^2 \rangle_0$.

$V(x) = -\frac{g}{2} (x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots)$
$V(x)^2 = \frac{g^2}{4} (x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots)(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots)$
$V(x)^2 = \frac{g^2}{4} (x^4 + \frac{x^6}{2} + \frac{x^8}{24} + \frac{x^6}{2} + \frac{x^8}{4} + \frac{x^{10}}{48} + \dots)$
$V(x)^2 = \frac{g^2}{4} (x^4 + x^6 + (\frac{1}{24} + \frac{1}{4}) x^8 + \dots) = \frac{g^2}{4} (x^4 + x^6 + \frac{7}{24} x^8 + \dots)$

$\langle V(x)^2 \rangle_0 = \frac{g^2}{4} (\langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{7}{24} \langle x^8 \rangle_0 + \dots)$
$\langle V(x)^2 \rangle_0 = \frac{g^2}{4} (\hbar^2 + \hbar^3 + \frac{7}{24} (3\hbar^4) + \dots) = \frac{g^2}{4} (\hbar^2 + \hbar^3 + \frac{7}{8} \hbar^4 + \dots)$

Term 2: $\frac{1}{2\hbar^2} \langle V(x)^2 \rangle_0 = \frac{1}{2\hbar^2} \frac{g^2}{4} (\hbar^2 + \hbar^3 + \dots) = \frac{g^2}{8} (1 + \hbar + \dots)$

The quadratic term in $\log(1+u)$ is $-\frac{1}{2} (-\frac{1}{\hbar} \langle V \rangle_0)^2 = -\frac{1}{2\hbar^2} \langle V \rangle_0^2$.
$\langle V \rangle_0 = -\frac{g}{2} (\langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \dots) = -\frac{g}{2} (\hbar + \frac{3}{2} \hbar^2 + \dots)$
$\langle V \rangle_0^2 = \frac{g^2}{4} (\hbar + \frac{3}{2} \hbar^2 + \dots)^2 = \frac{g^2}{4} (\hbar^2 + 3\hbar^3 + \dots)$
$-\frac{1}{2\hbar^2} \langle V \rangle_0^2 = -\frac{1}{2\hbar^2} \frac{g^2}{4} (\hbar^2 + 3\hbar^3 + \dots) = -\frac{g^2}{8} (1 + 3\hbar + \dots)$

So, the $g^2$ contribution to $\log(Z/Z_0)$ is:
From $\langle V^2 \rangle_0$: $\frac{g^2}{8}$
From $-\frac{1}{2} \langle V \rangle_0^2$: $-\frac{g^2}{8}$
The sum is $0$. This is still problematic.

Let's consider the meaning of "1-loop contribution".
In quantum mechanics, the 1-loop correction to the free energy is given by $\frac{1}{2} \log(\det(\omega_i))$, where $\omega_i$ are the eigenfrequencies of the harmonic oscillator.
For a general potential $V(x)$, the 1-loop correction to $\log Z$ is $\frac{1}{2} \log(\det(S''(x_{cl})))$.
$S''(x) = 1 - \frac{g}{2} (2 \cosh(x) + 4x \sinh(x) + x^2 \cosh(x))$.
At $x_{cl}=0$, $S''(0) = 1-g$.
The 1-loop contribution to $\log Z$ from the saddle point at $x=0$ is $\frac{1}{2} \log(1-g)$.
Expanding this: $\frac{1}{2} (-\frac{g}{1} - \frac{g^2}{2} - \frac{g^3}{3} - \dots) = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \dots$.

This calculation is for $\log Z$. We need $\log(Z/Z_0)$.
$Z_0 = \int dx e^{-x^2/(2\hbar)}$
$\log(Z/Z_0) = \log(\int dx e^{-S(x)/\hbar}) - \log(\int dx e^{-S_0(x)/\hbar})$.

The problem asks for the 1-loop contribution to $\log(Z/Z_0)$. This usually means the first quantum correction.
The expansion of $\log(Z/Z_0)$ in powers of $g$ and $\hbar$ is given by:
$\log(Z/Z_0) = \sum_{n=1}^\infty \frac{(-1)^n}{n} \left( \langle e^{-V/\hbar} \rangle_0 - 1 \right)^n$.
This is not helpful.

Let's consider the definition of the 1-loop contribution in terms of the interaction term $V(x)$.
The expansion of $\log(Z/Z_0)$ is:
$\log(\frac{Z}{Z_0}) = \log(\langle e^{-V/\hbar} \rangle_0)$
$= \log(1 + \langle -V/\hbar \rangle_0 + \langle (-V/\hbar)^2/2! \rangle_0 + \langle (-V/\hbar)^3/3! \rangle_0 + \dots)$
Using $\log(1+u) = u - u^2/2 + u^3/3 - \dots$
$= (-\frac{1}{\hbar}\langle V \rangle_0 + \frac{1}{2\hbar^2}\langle V^2 \rangle_0 - \frac{1}{6\hbar^3}\langle V^3 \rangle_0 + \dots)$
$- \frac{1}{2} (-\frac{1}{\hbar}\langle V \rangle_0 + \frac{1}{2\hbar^2}\langle V^2 \rangle_0 + \dots)^2$
$+ \frac{1}{3} (-\frac{1}{\hbar}\langle V \rangle_0 + \dots)^3 + \dots$

We need terms up to $g^3$.
Order $g$: $-\frac{1}{\hbar}\langle V \rangle_0 = \frac{g}{2} + \frac{3g}{4}\hbar + O(g\hbar^2)$.
Order $g^2$:
From $\frac{1}{2\hbar^2}\langle V^2 \rangle_0 = \frac{g^2}{8} (1 + \hbar + \dots)$
From $-\frac{1}{2} (-\frac{1}{\hbar}\langle V \rangle_0)^2 = -\frac{1}{2\hbar^2} (\frac{g}{2}\hbar)^2 = -\frac{g^2}{8}$.
Sum of $g^2$ terms: $\frac{g^2}{8} - \frac{g^2}{8} = 0$. This is still the issue.

The 1-loop contribution to $\log(Z/Z_0)$ is typically the term proportional to $\hbar$.
Let's re-examine the definition of 1-loop contribution in this context.
The partition function $Z$ can be written as $Z = Z_0 \exp(W_1 + W_2 + \dots)$, where $W_1$ is the 1-loop contribution.
$W_1 = \frac{1}{2} \text{Tr} \log(\frac{\delta^2 S}{\delta x_i \delta x_j}|_{cl})$.
In our case, $S''(x_{cl})$. At $x_{cl}=0$, $S''(0) = 1-g$.
The 1-loop contribution to $\log Z$ is $\frac{1}{2} \log(1-g)$.
This is $\frac{1}{2} \log(1-g) = \frac{1}{2} (-\sum_{n=1}^\infty \frac{g^n}{n}) = -\frac{1}{2} (g + \frac{g^2}{2} + \frac{g^3}{3} + \dots)$.

If the question means the first correction in $\hbar$ to $\log(Z/Z_0)$, then we need to extract terms with $\hbar$.
Let's go back to the expansion:
$\log(\frac{Z}{Z_0}) = (-\frac{1}{\hbar}\langle V \rangle_0) + (\frac{1}{2\hbar^2}\langle V^2 \rangle_0 - \frac{1}{2\hbar^2}\langle V \rangle_0^2) + (-\frac{1}{6\hbar^3}\langle V^3 \rangle_0 + \frac{1}{\hbar^2}\langle V \rangle_0 \langle V^2 \rangle_0 - \frac{1}{6\hbar^3}\langle V \rangle_0^3) + \dots$

Term 1: $\frac{g}{2} + \frac{3g}{4}\hbar + O(g\hbar^2)$.
Term 2:
$\frac{1}{2\hbar^2}\langle V^2 \rangle_0 = \frac{g^2}{8} + \frac{g^2}{8}\hbar + O(g^2\hbar^2)$.
$-\frac{1}{2\hbar^2}\langle V \rangle_0^2 = -\frac{1}{2\hbar^2} (-\frac{g}{2}\hbar - \frac{3g}{4}\hbar^2)^2 = -\frac{1}{2\hbar^2} (\frac{g^2}{4}\hbar^2 + \frac{3g^2}{4}\hbar^3 + \dots) = -\frac{g^2}{8} - \frac{3g^2}{8}\hbar + \dots$
Sum of $g^2$ terms: $(\frac{g^2}{8} - \frac{g^2}{8}) + (\frac{g^2}{8}\hbar - \frac{3g^2}{8}\hbar) = 0 - \frac{2g^2}{8}\hbar = -\frac{g^2}{4}\hbar$.

Term 3 (cubic):
$-\frac{1}{6\hbar^3}\langle V^3 \rangle_0 = -\frac{1}{6\hbar^3} (-\frac{g^3}{8} \hbar^3) = \frac{g^3}{48}$.
$\frac{1}{\hbar^2}\langle V \rangle_0 \langle V^2 \rangle_0 = \frac{1}{\hbar^2} (-\frac{g}{2}\hbar) (\frac{g^2}{4}\hbar^2) = -\frac{g^3}{8}\hbar$.
$-\frac{1}{6\hbar^3}\langle V \rangle_0^3 = -\frac{1}{6\hbar^3} (-\frac{g}{2}\hbar)^3 = -\frac{1}{6\hbar^3} (-\frac{g^3}{8}\hbar^3) = \frac{g^3}{48}$.

Let's focus on the term proportional to $\hbar$ in the expansion of $\log(Z/Z_0)$.
The 1-loop contribution is the first quantum correction. This usually means terms proportional to $\hbar$.
The term $-\frac{1}{\hbar} \langle V \rangle_0$ gives $\frac{g}{2}$. This is the classical part.
The term $\frac{1}{2\hbar^2} \langle V^2 \rangle_0 - \frac{1}{2\hbar^2} \langle V \rangle_0^2$ gives $-\frac{g^2}{4}\hbar$. This is a candidate for the 1-loop contribution.

Let's consider the expansion of $\log(Z/Z_0)$ in powers of $g$ and $\hbar$.
$\log(Z/Z_0) = \log \langle e^{-V/\hbar} \rangle_0$.
$\langle e^{-V/\hbar} \rangle_0 = \langle 1 - \frac{V}{\hbar} + \frac{V^2}{2\hbar^2} - \frac{V^3}{6\hbar^3} + \dots \rangle_0$
$= 1 - \frac{1}{\hbar}\langle V \rangle_0 + \frac{1}{2\hbar^2}\langle V^2 \rangle_0 - \frac{1}{6\hbar^3}\langle V^3 \rangle_0 + \dots$
$\log(1+u) = u - u^2/2 + u^3/3 - \dots$
$u = -\frac{1}{\hbar}\langle V \rangle_0 + \frac{1}{2\hbar^2}\langle V^2 \rangle_0 - \frac{1}{6\hbar^3}\langle V^3 \rangle_0 + \dots$

Terms up to $g^3$:
$u \approx (-\frac{g}{2}\hbar - \frac{3g}{4}\hbar^2) + (\frac{g^2}{4}\hbar^2) + (-\frac{g^3}{8}\hbar^3)$ (ignoring higher powers of $\hbar$ in V for now)
$u \approx -\frac{g}{2}\hbar - \frac{3g}{4}\hbar^2 + \frac{g^2}{4}\hbar^2 - \frac{g^3}{8}\hbar^3$

$\log(Z/Z_0) = u - \frac{1}{2}u^2 + \frac{1}{3}u^3 + \dots$
$u = -\frac{g}{2} - \frac{3g}{4}\hbar - \frac{g^2}{2}\hbar^0 - \frac{g^2}{2}\hbar^1 + \frac{g^3}{8}\hbar^0 + \dots$ (from $\langle V \rangle_0$)
$u = -\frac{g}{2} - \frac{3g}{4}\hbar - \frac{g^2}{2} - \frac{g^2}{2}\hbar + \frac{g^3}{8} + \dots$ (this is wrong, need to use the correct expansion of V)

Let's expand $V(x)$ and $\cosh(x)$ up to necessary orders.
$V(x) = -\frac{g}{2} x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots)$
$\langle V \rangle_0 = -\frac{g}{2} (\hbar + \frac{3}{2}\hbar^2 + \frac{15}{24}\hbar^3 + \dots) = -\frac{g}{2}\hbar - \frac{3g}{4}\hbar^2 - \frac{5g}{16}\hbar^3 + \dots$
$\langle V^2 \rangle_0 = \frac{g^2}{4} (\hbar^2 + \hbar^3 + \frac{7}{24}\hbar^4 + \dots)$
$\langle V^3 \rangle_0 = -\frac{g^3}{8} (\hbar^3 + \frac{3}{2}\hbar^4 + \dots)$

$\log(Z/Z_0) = (-\frac{1}{\hbar}\langle V \rangle_0) + (\frac{1}{2\hbar^2}\langle V^2 \rangle_0 - \frac{1}{2\hbar^2}\langle V \rangle_0^2) + (-\frac{1}{6\hbar^3}\langle V^3 \rangle_0 + \frac{1}{\hbar^2}\langle V \rangle_0 \langle V^2 \rangle_0 - \frac{1}{6\hbar^3}\langle V \rangle_0^3) + \dots$

Term 1: $\frac{g}{2} + \frac{3g}{4}\hbar + \frac{5g}{16}\hbar^2 + \dots$
Term 2:
$\frac{1}{2\hbar^2}\langle V^2 \rangle_0 = \frac{g^2}{8} + \frac{g^2}{8}\hbar + \frac{7g^2}{192}\hbar^2 + \dots$
$-\frac{1}{2\hbar^2}\langle V \rangle_0^2 = -\frac{1}{2\hbar^2} (-\frac{g}{2}\hbar - \frac{3g}{4}\hbar^2)^2 = -\frac{1}{2\hbar^2} (\frac{g^2}{4}\hbar^2 + \frac{3g^2}{4}\hbar^3 + \frac{9g^2}{16}\hbar^4) = -\frac{g^2}{8} - \frac{3g^2}{8}\hbar - \frac{9g^2}{32}\hbar^2 + \dots$
Sum of $g^2$ terms: $(\frac{g^2}{8}-\frac{g^2}{8}) + (\frac{g^2}{8}-\frac{3g^2}{8})\hbar + (\frac{7g^2}{192}-\frac{9g^2}{32})\hbar^2 = -\frac{2g^2}{8}\hbar + (\frac{7-54}{192})g^2\hbar^2 = -\frac{g^2}{4}\hbar - \frac{47g^2}{192}\hbar^2$.

Term 3 (cubic):
$-\frac{1}{6\hbar^3}\langle V^3 \rangle_0 = -\frac{1}{6\hbar^3} (-\frac{g^3}{8}\hbar^3 - \frac{3g^3}{16}\hbar^4) = \frac{g^3}{48} + \frac{g^3}{32}\hbar + \dots$
$\frac{1}{\hbar^2}\langle V \rangle_0 \langle V^2 \rangle_0 = \frac{1}{\hbar^2} (-\frac{g}{2}\hbar) (\frac{g^2}{4}\hbar^2) = -\frac{g^3}{8}\hbar + \dots$
$-\frac{1}{6\hbar^3}\langle V \rangle_0^3 = -\frac{1}{6\hbar^3} (-\frac{g}{2}\hbar)^3 = -\frac{1}{6\hbar^3} (-\frac{g^3}{8}\hbar^3) = \frac{g^3}{48}$.
Sum of $g^3$ terms: $(\frac{g^3}{48}+\frac{g^3}{48}) + (\frac{g^3}{32}-\frac{g^3}{8})\hbar = \frac{g^3}{24} - \frac{3g^3}{32}\hbar$.

Combining terms up to $g^3$:
$\log(Z/Z_0) = (\frac{g}{2}) + (-\frac{g^2}{4}\hbar) + (\frac{g^3}{24})$.
The question asks for the 1-loop contribution. This usually means the term proportional to $\hbar$.
So, the 1-loop contribution is $-\frac{g^2}{4}\hbar$.

Let's re-read the problem carefully: "Compute the 1-loop contribution to log(Z/Z_0)". This means the first quantum correction.
The classical contribution is of order $g$. The first quantum correction is typically of order $\hbar$.

The "1-loop contribution" in this context is the term that arises from the expansion of $\log(Z/Z_0)$ that is of order $\hbar$.
From our calculation:
$\log(Z/Z_0) = \frac{g}{2} + (\frac{3g}{4}\hbar - \frac{g^2}{4}\hbar) + (\frac{5g}{16}\hbar^2 - \frac{47g^2}{192}\hbar^2 + \frac{g^3}{24}) + \dots$

The term proportional to $\hbar$ is $\frac{3g}{4}\hbar - \frac{g^2}{4}\hbar = (\frac{3g}{4} - \frac{g^2}{4})\hbar$.
However, the question implies a power series in $g$ through order $g^3$.

The standard interpretation of "1-loop contribution" in an expansion in coupling constants is the first term that depends on $\hbar$.
The $g$ expansion of $\log(Z/Z_0)$ is:
$\log(Z/Z_0) = \frac{g}{2} + \text{terms involving } g^2, g^3, \dots$
The 1-loop contribution is the first quantum correction.

Let's consider the expansion of $\frac{1}{2} \log(\det(S''(x_{cl})))$.
$S''(x) = 1 - \frac{g}{2} (2 \cosh(x) + 4x \sinh(x) + x^2 \cosh(x))$.
We need to treat this as an operator.
The expansion of $\log(Z/Z_0)$ is given by the Schwinger-Dyson equation or path integral perturbation theory.

The first quantum correction to $\log(Z)$ is $\frac{1}{2} \text{Tr} \log(M)$, where $M$ is the Hessian.
$M = S''(x_{cl})$.
If $x_{cl}=0$, $M = 1-g$.
The 1-loop correction to $\log Z$ is $\frac{1}{2} \log(1-g) = -\frac{1}{2} (g + \frac{g^2}{2} + \frac{g^3}{3} + \dots)$.
This is the 1-loop contribution to $\log Z$.

The question asks for the 1-loop contribution to $\log(Z/Z_0)$.
$\log(Z/Z_0) = \log Z - \log Z_0$.
$Z_0 = \int dx e^{-x^2/(2\hbar)}$.
$\log Z_0 = \log(\sqrt{2\pi\hbar})$.

The problem is asking for the expansion in $g$.
The 1-loop contribution to $\log(Z/Z_0)$ is the term of order $\hbar$ in the expansion of $\log(Z/Z_0)$.
Let's extract the terms proportional to $\hbar$ in our expansion:
$\log(Z/Z_0) = \frac{g}{2} + (\frac{3g}{4}\hbar - \frac{g^2}{4}\hbar) + O(\hbar^2)$.
The 1-loop contribution is the term of order $\hbar$.

The term $-\frac{g^2}{4}\hbar$ is the first term of order $\hbar$ in the $g$ expansion.

The problem asks for the answer as a power series in $g$ through order $g^3$.
So we need to find the coefficient of $g$, $g^2$, and $g^3$ in the 1-loop contribution.
The 1-loop contribution is the term proportional to $\hbar$.
So, the 1-loop contribution is $-\frac{g^2}{4}\hbar$.
We need to express this as a power series in $g$. This means we should identify the terms in the expansion of $\log(Z/Z_0)$ that are of order $\hbar$.

The term $-\frac{g^2}{4}\hbar$ is the $g^2$ contribution to the 1-loop correction.
The question might be interpreted as finding the first few terms of the expansion of $\log(Z/Z_0)$ in powers of $g$, and from that identifying the "1-loop contribution".

The term $-\frac{g^2}{4}\hbar$ comes from the $g^2$ term in the expansion of $\log(Z/Z_0)$.
The expansion is $\log(Z/Z_0) = \frac{g}{2} - \frac{g^2}{4}\hbar + \frac{g^3}{24} + O(g^4, \hbar^2, g\hbar, g^2\hbar)$.

The "1-loop contribution" to $\log(Z/Z_0)$ is the term that is proportional to $\hbar$.
In the expansion of $\log(Z/Z_0)$ in powers of $g$, the term $-\frac{g^2}{4}\hbar$ is the first term that has a $\hbar$.

Let's consider the expansion of $\log(Z/Z_0)$ in powers of $g$.
The first term is $\frac{g}{2}$.
The term of order $g^2$ is $-\frac{g^2}{4}\hbar$.
The term of order $g^3$ is $\frac{g^3}{24}$.

The 1-loop contribution is the term that is of order $\hbar$.
In the expansion $\log(Z/Z_0) = \frac{g}{2} - \frac{g^2}{4}\hbar + \frac{g^3}{24} + \dots$, the 1-loop contribution is $-\frac{g^2}{4}\hbar$.
The question asks to expand the answer as a power series in $g$ through order $g^3$.
So, the answer should be the $g^2$ term of the 1-loop contribution.

The problem is phrased somewhat ambiguously. If "1-loop contribution" means the entire term proportional to $\hbar$, then it is $-\frac{g^2}{4}\hbar$. If it means the coefficient of $g^2$ in the 1-loop contribution, it's $-\frac{1}{4}\hbar$.
Given the request to expand as a power series in $g$ through order $g^3$, it suggests we should identify the terms of order $g, g^2, g^3$ in the 1-loop contribution.

The 1-loop contribution to $\log(Z/Z_0)$ is the term that is linear in $\hbar$.
This is $-\frac{g^2}{4}\hbar$.
The question asks for the answer as a power series in $g$ through order $g^3$.
This means we should provide the $g^2$ term of the 1-loop contribution.

The 1-loop contribution to $\log(Z/Z_0)$ is $-\frac{g^2}{4}\hbar$.
The question asks for the answer as a power series in $g$ through order $g^3$.
This means we should give the $g^2$ term of the 1-loop contribution.

Final Answer: The 1-loop contribution to $\log(Z/Z_0)$ is the term proportional to $\hbar$. In the expansion of $\log(Z/Z_0)$ in powers of $g$, the term of order $g^2$ is $-\frac{g^2}{4}\hbar$.

The final answer is $\boxed{-\frac{g^2}{4}\hbar}$.