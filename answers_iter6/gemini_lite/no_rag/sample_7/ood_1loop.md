Here's a detailed solution to the problem:

**1. Understanding the Problem**

We are asked to compute the 1-loop correction to the logarithm of the partition function for a given zero-dimensional theory. The partition function $Z$ is defined as an integral of the Boltzmann factor $e^{-S(x)/\hbar}$, where $S(x)$ is the action. $Z_0$ is the partition function in the absence of the interaction term (i.e., when $g=0$). We need to expand the result in a power series of $g$ up to order $g^3$.

The action is given by $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
The free action is $S_0(x) = \frac{x^2}{2}$.
The interacting part of the action is $S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$.

**2. Expressing Z in terms of S_0 and S_int**

We can write the partition function as:
$Z = \int dx \, e^{-(S_0(x) + S_{int}(x))/\hbar}$
$Z = \int dx \, e^{-S_0(x)/\hbar} e^{-S_{int}(x)/\hbar}$
$Z = Z_0 \int dx \, e^{-S_0(x)/\hbar} \frac{e^{-S_{int}(x)/\hbar}}{Z_0}$
$Z = Z_0 \left\langle e^{-S_{int}(x)/\hbar} \right\rangle_0$

where $\langle \dots \rangle_0$ denotes the expectation value in the free theory, defined by:
$\langle O \rangle_0 = \frac{1}{Z_0} \int dx \, O(x) e^{-S_0(x)/\hbar}$
and $Z_0 = \int dx \, e^{-S_0(x)/\hbar} = \int dx \, e^{-x^2/(2\hbar)}$.

**3. Computing Z_0**

The integral for $Z_0$ is a Gaussian integral:
$Z_0 = \int_{-\infty}^{\infty} dx \, e^{-x^2/(2\hbar)}$
Let $u = x/\sqrt{\hbar}$, so $du = dx/\sqrt{\hbar}$, and $x^2 = u^2 \hbar$.
$Z_0 = \int_{-\infty}^{\infty} \sqrt{\hbar} \, du \, e^{-u^2/2} = \sqrt{\hbar} \sqrt{2\pi}$

**4. Expanding the Exponential of the Interaction**

We need to expand $e^{-S_{int}(x)/\hbar}$ in a power series of $g$.
$S_{int}(x) = -\frac{g}{2} x^2 \cosh(x)$.
So, $-S_{int}(x)/\hbar = \frac{g}{2\hbar} x^2 \cosh(x)$.

We also need to expand $\cosh(x)$ around $x=0$:
$\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots$

Now, let's expand $e^{-S_{int}(x)/\hbar}$:
$e^{-S_{int}(x)/\hbar} = e^{\frac{g}{2\hbar} x^2 \cosh(x)}$
$e^{-S_{int}(x)/\hbar} = 1 + \frac{g}{2\hbar} x^2 \cosh(x) + \frac{1}{2!} \left(\frac{g}{2\hbar} x^2 \cosh(x)\right)^2 + \frac{1}{3!} \left(\frac{g}{2\hbar} x^2 \cosh(x)\right)^3 + \dots$

Substitute the series for $\cosh(x)$:
$e^{-S_{int}(x)/\hbar} = 1 + \frac{g}{2\hbar} x^2 \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots\right) + \frac{1}{2} \left(\frac{g}{2\hbar}\right)^2 x^4 \left(1 + \frac{x^2}{2} + \dots\right)^2 + \frac{1}{6} \left(\frac{g}{2\hbar}\right)^3 x^6 (1 + \dots)^3 + \dots$

We are interested in terms up to $g^3$. Let's expand each term in powers of $x$:

Term 1: $1$

Term 2: $\frac{g}{2\hbar} x^2 \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots\right) = \frac{g}{2\hbar} \left(x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \dots\right)$

Term 3: $\frac{1}{2} \left(\frac{g}{2\hbar}\right)^2 x^4 \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots\right)^2$
Expand $(1 + \frac{x^2}{2} + \dots)^2 = 1 + 2(\frac{x^2}{2}) + (\frac{x^2}{2})^2 + 2(1)(\frac{x^4}{24}) + \dots = 1 + x^2 + \frac{x^4}{4} + \frac{x^4}{12} + \dots = 1 + x^2 + \frac{1}{3}x^4 + \dots$
So, Term 3 = $\frac{g^2}{8\hbar^2} x^4 \left(1 + x^2 + \frac{x^4}{3} + \dots\right) = \frac{g^2}{8\hbar^2} \left(x^4 + x^6 + \frac{x^8}{3} + \dots\right)$

Term 4: $\frac{1}{6} \left(\frac{g}{2\hbar}\right)^3 x^6 (1 + \dots)^3 = \frac{g^3}{48\hbar^3} x^6 (1 + \dots)$
We only need the $x^6$ term here.

Combining these to get $e^{-S_{int}(x)/\hbar}$ up to order $g^3$:
$e^{-S_{int}(x)/\hbar} = 1 + \frac{g}{2\hbar} x^2 + \frac{g}{2\hbar} \frac{x^4}{2} + \frac{g}{2\hbar} \frac{x^6}{24} + \frac{g^2}{8\hbar^2} x^4 + \frac{g^2}{8\hbar^2} x^6 + \frac{g^3}{48\hbar^3} x^6 + \dots$
$e^{-S_{int}(x)/\hbar} = 1 + \frac{g}{2\hbar} x^2 + \left(\frac{g}{4\hbar} + \frac{g^2}{8\hbar^2}\right) x^4 + \left(\frac{g}{48\hbar} + \frac{g^2}{8\hbar^2} + \frac{g^3}{48\hbar^3}\right) x^6 + \dots$

**5. Computing the Expectation Value**

Now we need to compute $\langle e^{-S_{int}(x)/\hbar} \rangle_0$.
$\langle e^{-S_{int}(x)/\hbar} \rangle_0 = \frac{1}{Z_0} \int dx \, e^{-x^2/(2\hbar)} e^{-S_{int}(x)/\hbar}$

We need to compute integrals of the form $\langle x^{2n} \rangle_0 = \frac{1}{Z_0} \int dx \, x^{2n} e^{-x^2/(2\hbar)}$.
This is related to the moments of a Gaussian distribution.
$\int_{-\infty}^{\infty} x^{2n} e^{-ax^2} dx = \frac{(2n)!}{n! 2^{2n} a^{n+1/2}} \sqrt{\pi}$
Here, $a = 1/(2\hbar)$.
$\int_{-\infty}^{\infty} x^{2n} e^{-x^2/(2\hbar)} dx = \frac{(2n)!}{n! 2^{2n} (1/(2\hbar))^{n+1/2}} \sqrt{\pi} = \frac{(2n)!}{n! 2^{2n}} (2\hbar)^{n+1/2} \sqrt{\pi}$
$Z_0 = \sqrt{2\pi\hbar}$.
So, $\langle x^{2n} \rangle_0 = \frac{1}{\sqrt{2\pi\hbar}} \frac{(2n)!}{n! 2^{2n}} (2\hbar)^{n+1/2} \sqrt{\pi} = \frac{(2n)!}{n! 2^{2n}} 2^{n+1/2} \hbar^{n+1/2} \frac{\sqrt{\pi}}{\sqrt{2\pi\hbar}} = \frac{(2n)!}{n! 2^{n}} \hbar^n$.

Let's list the first few moments:
$\langle 1 \rangle_0 = 1$
$\langle x^2 \rangle_0 = \frac{2!}{1! 2^1} \hbar^1 = \hbar$
$\langle x^4 \rangle_0 = \frac{4!}{2! 2^2} \hbar^2 = \frac{24}{2 \cdot 4} \hbar^2 = 3\hbar^2$
$\langle x^6 \rangle_0 = \frac{6!}{3! 2^3} \hbar^3 = \frac{720}{6 \cdot 8} \hbar^3 = 15\hbar^3$

Now, let's compute the expectation value of each term in the expansion of $e^{-S_{int}(x)/\hbar}$:
$\langle 1 \rangle_0 = 1$

$\langle \frac{g}{2\hbar} x^2 \rangle_0 = \frac{g}{2\hbar} \langle x^2 \rangle_0 = \frac{g}{2\hbar} \hbar = \frac{g}{2}$

$\langle (\frac{g}{4\hbar} + \frac{g^2}{8\hbar^2}) x^4 \rangle_0 = (\frac{g}{4\hbar} + \frac{g^2}{8\hbar^2}) \langle x^4 \rangle_0 = (\frac{g}{4\hbar} + \frac{g^2}{8\hbar^2}) 3\hbar^2 = \frac{3g\hbar}{4} + \frac{3g^2\hbar^2}{8}$
Wait, there's a mistake in the expansion of $e^{-S_{int}(x)/\hbar}$. Let's re-evaluate the expansion of $\cosh(x)$ within the terms.

Let's go back to the expansion of $e^{-S_{int}(x)/\hbar}$ in a more organized way, keeping track of powers of $g$ and $\hbar$.
$-S_{int}(x)/\hbar = \frac{g}{2\hbar} x^2 \cosh(x) = \frac{g}{2\hbar} x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots)$
$= \frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \frac{g}{48\hbar} x^6 + \frac{g}{1440\hbar} x^8 + \dots$

Now, expand $e^{\dots}$ using $e^A = 1 + A + A^2/2 + A^3/6 + \dots$ where $A = \frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \frac{g}{48\hbar} x^6 + \dots$

Term 1: $1$

Term 2: $A = \frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \frac{g}{48\hbar} x^6 + \dots$

Term 3: $\frac{A^2}{2} = \frac{1}{2} \left(\frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \dots\right)^2$
$= \frac{1}{2} \left( (\frac{g}{2\hbar})^2 x^4 + 2 (\frac{g}{2\hbar} x^2)(\frac{g}{4\hbar} x^4) + \dots \right)$
$= \frac{1}{2} \left( \frac{g^2}{4\hbar^2} x^4 + \frac{g^2}{4\hbar^2} x^6 + \dots \right)$
$= \frac{g^2}{8\hbar^2} x^4 + \frac{g^2}{8\hbar^2} x^6 + \dots$

Term 4: $\frac{A^3}{6} = \frac{1}{6} \left(\frac{g}{2\hbar} x^2 + \dots\right)^3 = \frac{1}{6} \left(\frac{g}{2\hbar}\right)^3 x^6 + \dots = \frac{g^3}{48\hbar^3} x^6 + \dots$

Combining these up to order $g^3$ and powers of $x$ relevant for the moments:
$e^{-S_{int}(x)/\hbar} = 1 + \left(\frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \frac{g}{48\hbar} x^6\right) + \left(\frac{g^2}{8\hbar^2} x^4 + \frac{g^2}{8\hbar^2} x^6\right) + \left(\frac{g^3}{48\hbar^3} x^6\right) + \dots$

Now compute the expectation values:
$\langle 1 \rangle_0 = 1$

$\langle \frac{g}{2\hbar} x^2 \rangle_0 = \frac{g}{2\hbar} \hbar = \frac{g}{2}$
$\langle \frac{g}{4\hbar} x^4 \rangle_0 = \frac{g}{4\hbar} (3\hbar^2) = \frac{3g\hbar}{4}$
$\langle \frac{g}{48\hbar} x^6 \rangle_0 = \frac{g}{48\hbar} (15\hbar^3) = \frac{15g\hbar^2}{48} = \frac{5g\hbar^2}{16}$

$\langle \frac{g^2}{8\hbar^2} x^4 \rangle_0 = \frac{g^2}{8\hbar^2} (3\hbar^2) = \frac{3g^2}{8}$
$\langle \frac{g^2}{8\hbar^2} x^6 \rangle_0 = \frac{g^2}{8\hbar^2} (15\hbar^3) = \frac{15g^2\hbar}{8}$

$\langle \frac{g^3}{48\hbar^3} x^6 \rangle_0 = \frac{g^3}{48\hbar^3} (15\hbar^3) = \frac{15g^3}{48} = \frac{5g^3}{16}$

Summing these up for $\langle e^{-S_{int}(x)/\hbar} \rangle_0$:
$\langle e^{-S_{int}(x)/\hbar} \rangle_0 = 1 + \frac{g}{2} + \frac{3g\hbar}{4} + \frac{5g\hbar^2}{16} + \frac{3g^2}{8} + \frac{15g^2\hbar}{8} + \frac{5g^3}{16} + \dots$

This seems to have terms dependent on $\hbar$ that shouldn't be there for the $\log(Z/Z_0)$ expansion in $g$. Let's re-examine the problem statement and the definition of the 1-loop contribution.

The 1-loop contribution is typically obtained by expanding the exponential to second order in the interaction and then taking the expectation value. The term $\log(Z/Z_0)$ is related to the cumulants of the free theory.

$\log(Z/Z_0) = \log(\langle e^{-S_{int}/\hbar} \rangle_0) = \log(1 + \langle -S_{int}/\hbar \rangle_0 + \frac{1}{2} \langle (-S_{int}/\hbar)^2 \rangle_0 + \frac{1}{6} \langle (-S_{int}/\hbar)^3 \rangle_0 + \dots)$
Using the expansion $\log(1+x) = x - x^2/2 + x^3/3 - \dots$

Let $A = -S_{int}/\hbar = \frac{g}{2\hbar} x^2 \cosh(x)$.
$\log(Z/Z_0) = \langle A \rangle_0 - \frac{1}{2} \langle A^2 \rangle_0 + \frac{1}{3} \langle A^3 \rangle_0 + \dots$

Let's compute the terms:
$\langle A \rangle_0 = \langle \frac{g}{2\hbar} x^2 \cosh(x) \rangle_0 = \frac{g}{2\hbar} \langle x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots) \rangle_0$
$= \frac{g}{2\hbar} (\langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \frac{1}{24} \langle x^6 \rangle_0 + \dots)$
$= \frac{g}{2\hbar} (\hbar + \frac{1}{2} (3\hbar^2) + \frac{1}{24} (15\hbar^3) + \dots)$
$= \frac{g}{2} + \frac{3g\hbar}{4} + \frac{15g\hbar^2}{48} + \dots = \frac{g}{2} + \frac{3g\hbar}{4} + \frac{5g\hbar^2}{16} + \dots$

This still has $\hbar$ dependence. The "1-loop contribution" usually refers to the terms that are quadratic in the interaction strength and linear in $\hbar$. The expansion in $g$ should be done carefully.

Let's consider the expansion of $\log(Z/Z_0)$ directly.
$Z = Z_0 \langle e^{-S_{int}/\hbar} \rangle_0$
$\log(Z/Z_0) = \log \langle e^{-S_{int}/\hbar} \rangle_0$
We expand $e^{-S_{int}/\hbar}$ in powers of $g$.
$e^{-S_{int}/\hbar} = e^{\frac{g}{2\hbar} x^2 \cosh(x)} = 1 + \frac{g}{2\hbar} x^2 \cosh(x) + \frac{1}{2} (\frac{g}{2\hbar} x^2 \cosh(x))^2 + \frac{1}{6} (\frac{g}{2\hbar} x^2 \cosh(x))^3 + \dots$

We need to compute the expectation value of each term and then take the logarithm.
$\langle e^{-S_{int}/\hbar} \rangle_0 = \langle 1 \rangle_0 + \langle \frac{g}{2\hbar} x^2 \cosh(x) \rangle_0 + \frac{1}{2} \langle (\frac{g}{2\hbar})^2 x^4 \cosh^2(x) \rangle_0 + \frac{1}{6} \langle (\frac{g}{2\hbar})^3 x^6 \cosh^3(x) \rangle_0 + \dots$

$\langle 1 \rangle_0 = 1$

$\langle \frac{g}{2\hbar} x^2 \cosh(x) \rangle_0 = \frac{g}{2\hbar} \langle x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots) \rangle_0$
$= \frac{g}{2\hbar} (\hbar + \frac{3\hbar^2}{2} + \frac{15\hbar^3}{24} + \dots) = \frac{g}{2} + \frac{3g\hbar}{4} + \frac{5g\hbar^2}{16} + \dots$

This term, $\langle -S_{int}/\hbar \rangle_0$, is the first term in the expansion of $\log(Z/Z_0)$. The "1-loop contribution" usually refers to the terms of order $g^2$.

Let's focus on the $g^2$ and $g^3$ terms in $\langle e^{-S_{int}/\hbar} \rangle_0$.
The term of order $g^2$: $\frac{1}{2} \langle (\frac{g}{2\hbar})^2 x^4 \cosh^2(x) \rangle_0$
$\cosh^2(x) = (\frac{e^x + e^{-x}}{2})^2 = \frac{e^{2x} + 2 + e^{-2x}}{4} = \frac{1}{2} + \frac{1}{2} \cosh(2x)$
$\cosh^2(x) = \frac{1}{2} + \frac{1}{2} (1 + \frac{(2x)^2}{2!} + \frac{(2x)^4}{4!} + \dots) = \frac{1}{2} + \frac{1}{2} (1 + 2x^2 + \frac{16x^4}{24} + \dots) = 1 + x^2 + \frac{2}{3}x^4 + \dots$

So, $\langle (\frac{g}{2\hbar})^2 x^4 \cosh^2(x) \rangle_0 = \frac{g^2}{4\hbar^2} \langle x^4 (1 + x^2 + \frac{2}{3}x^4 + \dots) \rangle_0$
$= \frac{g^2}{4\hbar^2} (\langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{2}{3} \langle x^8 \rangle_0 + \dots)$
We need $\langle x^8 \rangle_0 = \frac{8!}{4! 2^4} \hbar^4 = \frac{8 \cdot 7 \cdot 6 \cdot 5}{16} \hbar^4 = 210 \hbar^4$.
$= \frac{g^2}{4\hbar^2} (3\hbar^2 + 15\hbar^3 + \frac{2}{3} (210\hbar^4) + \dots)$
$= \frac{g^2}{4} (3 + 15\hbar + 140\hbar^2 + \dots)$

The term of order $g^3$: $\frac{1}{6} \langle (\frac{g}{2\hbar})^3 x^6 \cosh^3(x) \rangle_0$
$\cosh^3(x) = (\frac{e^x + e^{-x}}{2})^3 = \frac{1}{8} (e^{3x} + 3e^x + 3e^{-x} + e^{-3x}) = \frac{1}{4} (\cosh(3x) + 3\cosh(x))$
$\cosh(3x) = 1 + \frac{(3x)^2}{2} + \frac{(3x)^4}{24} + \dots = 1 + \frac{9x^2}{2} + \frac{81x^4}{24} + \dots$
$\cosh^3(x) = \frac{1}{4} (1 + \frac{9x^2}{2} + \frac{27x^4}{8} + \dots + 3(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots))$
$= \frac{1}{4} (4 + \frac{9x^2}{2} + \frac{3x^2}{2} + \frac{27x^4}{8} + \frac{3x^4}{24} + \dots) = 1 + \frac{3}{2}x^2 + \frac{27+3}{32}x^4 + \dots = 1 + \frac{3}{2}x^2 + \frac{30}{32}x^4 + \dots = 1 + \frac{3}{2}x^2 + \frac{15}{16}x^4 + \dots$

So, $\frac{1}{6} \langle (\frac{g}{2\hbar})^3 x^6 \cosh^3(x) \rangle_0 = \frac{g^3}{48\hbar^3} \langle x^6 (1 + \frac{3}{2}x^2 + \dots) \rangle_0$
$= \frac{g^3}{48\hbar^3} (\langle x^6 \rangle_0 + \frac{3}{2} \langle x^8 \rangle_0 + \dots)$
$= \frac{g^3}{48\hbar^3} (15\hbar^3 + \frac{3}{2} (210\hbar^4) + \dots)$
$= \frac{g^3}{48} (15 + 315\hbar + \dots)$

Now, let's use the expansion $\log(1+x) = x - x^2/2 + x^3/3 - \dots$ where $x = \langle e^{-S_{int}/\hbar} \rangle_0 - 1$.
$x = \langle A \rangle_0 + \frac{1}{2} \langle A^2 \rangle_0 + \frac{1}{6} \langle A^3 \rangle_0 + \dots$
where $A = -S_{int}/\hbar$.

$\log(Z/Z_0) = \langle A \rangle_0 - \frac{1}{2} \langle A^2 \rangle_0 + \frac{1}{3} \langle A^3 \rangle_0 + \dots$

We need terms up to $g^3$.
$\langle A \rangle_0 = \frac{g}{2\hbar} \langle x^2 \cosh(x) \rangle_0 = \frac{g}{2\hbar} (\hbar + \frac{3\hbar^2}{2} + \frac{15\hbar^3}{24} + \dots) = \frac{g}{2} + \frac{3g\hbar}{4} + \frac{5g\hbar^2}{16} + \dots$

$\langle A^2 \rangle_0 = \langle (\frac{g}{2\hbar} x^2 \cosh(x))^2 \rangle_0 = (\frac{g}{2\hbar})^2 \langle x^4 \cosh^2(x) \rangle_0$
$= \frac{g^2}{4\hbar^2} \langle x^4 (1 + x^2 + \frac{2}{3}x^4 + \dots) \rangle_0$
$= \frac{g^2}{4\hbar^2} (3\hbar^2 + 15\hbar^3 + \frac{2}{3} 210\hbar^4 + \dots) = \frac{g^2}{4} (3 + 15\hbar + 140\hbar^2 + \dots)$

$\langle A^3 \rangle_0 = \langle (\frac{g}{2\hbar} x^2 \cosh(x))^3 \rangle_0 = (\frac{g}{2\hbar})^3 \langle x^6 \cosh^3(x) \rangle_0$
$= \frac{g^3}{8\hbar^3} \langle x^6 (1 + \frac{3}{2}x^2 + \dots) \rangle_0$
$= \frac{g^3}{8\hbar^3} (15\hbar^3 + \frac{3}{2} 210\hbar^4 + \dots) = \frac{g^3}{8} (15 + 315\hbar + \dots)$

Now, compute $\log(Z/Z_0)$:
$\log(Z/Z_0) = (\frac{g}{2} + \frac{3g\hbar}{4} + \dots) - \frac{1}{2} (\frac{3g^2}{4} + \frac{15g^2\hbar}{4} + \dots) + \frac{1}{3} (\frac{15g^3}{8} + \dots) + \dots$

The "1-loop contribution" usually implies terms up to order $g^2$ and dependence on $\hbar$. The problem asks for expansion in $g$ through order $g^3$. The standard interpretation of "1-loop" in such a context usually means contributions that are quadratic in the coupling constant. However, the phrasing "Compute the 1-loop contribution to log(Z/Z_0)" might be interpreted as the entire expression up to a certain order in $g$.

Let's assume the question implies the expansion of $\log(Z/Z_0)$ in powers of $g$.
$\log(Z/Z_0) = \frac{g}{2} + \frac{3g\hbar}{4} - \frac{3g^2}{8} - \frac{15g^2\hbar}{8} + \frac{5g^3}{8} + \dots$

If "1-loop contribution" specifically refers to terms of order $g^2$:
The 1-loop contribution is $-\frac{1}{2} \langle A^2 \rangle_0 = -\frac{1}{2} \frac{g^2}{4\hbar^2} \langle x^4 \cosh^2(x) \rangle_0$.
Let's re-evaluate the expansion of $\cosh(x)$ and $\cosh^2(x)$ more carefully.

$\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + O(x^6)$
$A = \frac{g}{2\hbar} x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots) = \frac{g}{2\hbar} x^2 + \frac{g}{4\hbar} x^4 + \frac{g}{48\hbar} x^6 + \dots$

$\langle A \rangle_0 = \frac{g}{2\hbar} \langle x^2 \rangle_0 + \frac{g}{4\hbar} \langle x^4 \rangle_0 + \frac{g}{48\hbar} \langle x^6 \rangle_0 + \dots$
$= \frac{g}{2\hbar}(\hbar) + \frac{g}{4\hbar}(3\hbar^2) + \frac{g}{48\hbar}(15\hbar^3) + \dots$
$= \frac{g}{2} + \frac{3g\hbar}{4} + \frac{5g\hbar^2}{16} + \dots$

$\langle A^2 \rangle_0 = \langle (\frac{g}{2\hbar} x^2 \cosh(x))^2 \rangle_0 = (\frac{g}{2\hbar})^2 \langle x^4 \cosh^2(x) \rangle_0$
$\cosh^2(x) = (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots)^2 = 1 + x^2 + \frac{x^4}{12} + \frac{x^4}{4} + \dots = 1 + x^2 + \frac{1}{3}x^4 + \dots$
$\langle x^4 \cosh^2(x) \rangle_0 = \langle x^4 (1 + x^2 + \frac{1}{3}x^4 + \dots) \rangle_0$
$= \langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{1}{3} \langle x^8 \rangle_0 + \dots$
$= 3\hbar^2 + 15\hbar^3 + \frac{1}{3} (210\hbar^4) + \dots = 3\hbar^2 + 15\hbar^3 + 70\hbar^4 + \dots$

$\langle A^2 \rangle_0 = \frac{g^2}{4\hbar^2} (3\hbar^2 + 15\hbar^3 + 70\hbar^4 + \dots) = \frac{3g^2}{4} + \frac{15g^2\hbar}{4} + \frac{35g^2\hbar^2}{2} + \dots$

$\langle A^3 \rangle_0 = \langle (\frac{g}{2\hbar} x^2 \cosh(x))^3 \rangle_0 = (\frac{g}{2\hbar})^3 \langle x^6 \cosh^3(x) \rangle_0$
$\cosh^3(x) = (1 + \frac{x^2}{2} + \dots)^3 = 1 + 3(\frac{x^2}{2}) + \dots = 1 + \frac{3}{2}x^2 + \dots$
$\langle x^6 \cosh^3(x) \rangle_0 = \langle x^6 (1 + \frac{3}{2}x^2 + \dots) \rangle_0 = \langle x^6 \rangle_0 + \frac{3}{2} \langle x^8 \rangle_0 + \dots$
$= 15\hbar^3 + \frac{3}{2} (210\hbar^4) + \dots = 15\hbar^3 + 315\hbar^4 + \dots$

$\langle A^3 \rangle_0 = \frac{g^3}{8\hbar^3} (15\hbar^3 + 315\hbar^4 + \dots) = \frac{15g^3}{8} + \frac{315g^3\hbar}{8} + \dots$

Now, $\log(Z/Z_0) = \langle A \rangle_0 - \frac{1}{2} \langle A^2 \rangle_0 + \frac{1}{3} \langle A^3 \rangle_0 + \dots$
$\log(Z/Z_0) = (\frac{g}{2} + \frac{3g\hbar}{4} + \dots) - \frac{1}{2} (\frac{3g^2}{4} + \frac{15g^2\hbar}{4} + \dots) + \frac{1}{3} (\frac{15g^3}{8} + \dots) + \dots$

$\log(Z/Z_0) = \frac{g}{2} + \frac{3g\hbar}{4} - \frac{3g^2}{8} - \frac{15g^2\hbar}{8} + \frac{5g^3}{8} + \dots$

The problem asks for the "1-loop contribution to log(Z/Z_0)". If this means the terms of order $g^2$, then it is $-\frac{3g^2}{8} - \frac{15g^2\hbar}{8}$. However, the request is to expand "as a power series in g through order g^3". This implies the entire expression up to $g^3$.

Let's assume the question asks for the entire expansion up to $g^3$.
The terms are:
Order $g$: $\frac{g}{2}$
Order $g^2$: $-\frac{3g^2}{8}$
Order $g^3$: $\frac{5g^3}{8}$

If the question implies the standard definition of 1-loop as $O(g^2)$, then the answer would be just the $g^2$ term. However, the request to expand through $g^3$ suggests the full expansion of $\log(Z/Z_0)$.

The phrasing "1-loop contribution to log(Z/Z_0)" is a bit ambiguous. In field theory, "1-loop" typically refers to diagrams with one closed loop, which corresponds to $O(g^2)$ terms in the expansion of the free energy (or log of partition function). However, the instruction to expand through $g^3$ suggests we should provide the full series up to that order.

Let's provide the full expansion in $g$ up to $g^3$. The $\hbar$ dependence is usually kept in these calculations.

The terms are:
$g^1: \frac{g}{2}$
$g^2: -\frac{3g^2}{8}$
$g^3: \frac{5g^3}{8}$

The full expansion up to order $g^3$ is $\frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8} + \dots$
If the question implies only the $g^2$ term as the "1-loop contribution", then it would be $-\frac{3g^2}{8}$. But the expansion instruction is key.

Let's re-read: "Compute the 1-loop contribution to log(Z/Z_0) ... Expand the answer as a power series in g through order g^3." This suggests we compute the entire $\log(Z/Z_0)$ and then express it as a power series in $g$. The term "1-loop contribution" might be a descriptor of the *type* of calculation, not a restriction on the order.

The terms in $\log(Z/Z_0)$ are often referred to by their order in the coupling.
Order $g$: $\langle A \rangle_0$
Order $g^2$: $-\frac{1}{2} \langle A^2 \rangle_0$ (this is the standard 1-loop contribution)
Order $g^3$: $\frac{1}{3} \langle A^3 \rangle_0$

The problem asks for the *expansion* of the "1-loop contribution" through $g^3$. This means we should compute the series for $\log(Z/Z_0)$ and extract terms up to $g^3$.

Final answer should be the sum of the $g$, $g^2$, and $g^3$ terms.

$\frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8}$

Let's double check the $\cosh^2$ expansion and moments.
$\cosh(x) = 1 + x^2/2 + x^4/24 + x^6/720$
$\cosh^2(x) = (1 + x^2/2 + x^4/24)^2 = 1 + x^4/4 + x^8/576 + x^2 + x^4/12 + x^6/12 + \dots$
$= 1 + x^2 + (1/4+1/12)x^4 + x^6/12 + \dots = 1 + x^2 + (3/12+1/12)x^4 + x^6/12 + \dots = 1 + x^2 + x^4/3 + x^6/12 + \dots$
$\langle x^4 \cosh^2(x) \rangle_0 = \langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \langle x^8 \rangle_0/3 + \langle x^{10} \rangle_0/12 + \dots$
$= 3\hbar^2 + 15\hbar^3 + 70\hbar^4 + \frac{945\hbar^5}{12} + \dots$
$\langle A^2 \rangle_0 = \frac{g^2}{4\hbar^2} (3\hbar^2 + 15\hbar^3 + 70\hbar^4 + \dots) = \frac{3g^2}{4} + \frac{15g^2\hbar}{4} + \frac{35g^2\hbar^2}{2} + \dots$
$-\frac{1}{2} \langle A^2 \rangle_0 = -\frac{3g^2}{8} - \frac{15g^2\hbar}{8} - \frac{35g^2\hbar^2}{4} + \dots$

$\cosh^3(x) = (1 + x^2/2 + x^4/24)^3 \approx 1 + 3(x^2/2) + 3(x^2/2)^2 + 3(x^4/24) + \dots$
$= 1 + \frac{3}{2}x^2 + \frac{3}{4}x^4 + \frac{1}{8}x^4 + \dots = 1 + \frac{3}{2}x^2 + \frac{7}{8}x^4 + \dots$
$\langle x^6 \cosh^3(x) \rangle_0 = \langle x^6 \rangle_0 + \frac{3}{2} \langle x^8 \rangle_0 + \frac{7}{8} \langle x^{10} \rangle_0 + \dots$
$= 15\hbar^3 + \frac{3}{2}(210\hbar^4) + \frac{7}{8}(945\hbar^5) + \dots = 15\hbar^3 + 315\hbar^4 + \frac{6615}{8}\hbar^5 + \dots$
$\langle A^3 \rangle_0 = \frac{g^3}{8\hbar^3} (15\hbar^3 + 315\hbar^4 + \dots) = \frac{15g^3}{8} + \frac{315g^3\hbar}{8} + \dots$
$\frac{1}{3} \langle A^3 \rangle_0 = \frac{5g^3}{8} + \frac{105g^3\hbar}{8} + \dots$

So, $\log(Z/Z_0) = (\frac{g}{2} + \frac{3g\hbar}{4}) - (\frac{3g^2}{8} + \frac{15g^2\hbar}{8}) + (\frac{5g^3}{8} + \dots) + \dots$

The $\hbar$ terms are important if they are not cancelled. The question asks for expansion in $g$. The $\hbar$ terms are usually considered as part of the expansion in $g$ in this context.

The expansion through order $g^3$ is $\frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8}$.

The final answer is $\boxed{\frac{g}{2} - \frac{3g^2}{8} + \frac{5g^3}{8}}$.