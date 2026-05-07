We are asked to compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$. The partition function is given by $Z = \int dx \, e^{-S(x)/\hbar}$, and $Z_0$ is the free (g=0) partition function. We need to expand the answer as a power series in $g$ through order $g^3$.

First, let's write down $S(x)$ and $S_0(x)$, the action for $g=0$:
$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$
$S_0(x) = \frac{x^2}{2}$

The partition function $Z$ is given by:
$Z = \int dx \, e^{-(\frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x))/\hbar} = \int dx \, e^{-\frac{x^2}{2\hbar}} e^{\frac{g}{2\hbar} x^2 \cosh(x)}$

The free partition function $Z_0$ is:
$Z_0 = \int dx \, e^{-S_0(x)/\hbar} = \int dx \, e^{-\frac{x^2}{2\hbar}}$
This is a Gaussian integral. Let's assume $\hbar=1$ for simplicity, as it is a common convention in these types of problems. If needed, we can reintroduce it later. So, $Z_0 = \int dx \, e^{-x^2/2}$.

The expression we need to compute is $\log(Z/Z_0)$. We can write $Z$ in terms of $Z_0$ as:
$Z = \int dx \, e^{-x^2/2} e^{\frac{g}{2} x^2 \cosh(x)} = Z_0 \left\langle e^{\frac{g}{2} x^2 \cosh(x)} \right\rangle_0$
where $\langle \dots \rangle_0$ denotes the average with respect to the measure $dx \, e^{-x^2/2}$.

Then, $\log(Z/Z_0) = \log \left\langle e^{\frac{g}{2} x^2 \cosh(x)} \right\rangle_0$.
We can expand the exponential:
$e^{\frac{g}{2} x^2 \cosh(x)} = 1 + \frac{g}{2} x^2 \cosh(x) + \frac{1}{2!} \left(\frac{g}{2} x^2 \cosh(x)\right)^2 + \frac{1}{3!} \left(\frac{g}{2} x^2 \cosh(x)\right)^3 + \dots$

Now we need to compute the expectation values of these terms. We will need the moments of the Gaussian distribution $e^{-x^2/2}$.
The relevant moments are:
$\langle x^{2n} \rangle_0 = \frac{(2n)!}{2^n n!}$
$\langle x^2 \rangle_0 = 1$
$\langle x^4 \rangle_0 = 3$
$\langle x^6 \rangle_0 = 15$

We also need the Taylor expansion of $\cosh(x)$:
$\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \dots$

Let's compute the terms in the expansion of $\log(Z/Z_0)$ up to order $g^3$.
$\log(Z/Z_0) = \log \left( 1 + \left\langle \frac{g}{2} x^2 \cosh(x) \right\rangle_0 + \left\langle \frac{g^2}{8} x^4 \cosh^2(x) \right\rangle_0 + \left\langle \frac{g^3}{48} x^6 \cosh^3(x) \right\rangle_0 + \dots \right)$

Using the expansion $\log(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \dots$, where $u$ is the sum of terms of order $g$ and higher.
Let $u = \left\langle \frac{g}{2} x^2 \cosh(x) \right\rangle_0 + \left\langle \frac{g^2}{8} x^4 \cosh^2(x) \right\rangle_0 + \left\langle \frac{g^3}{48} x^6 \cosh^3(x) \right\rangle_0 + \dots$

The 1-loop contribution is usually defined by expanding the exponential and taking the expectation value, and then taking the logarithm of the result. The term "1-loop" often refers to the first non-trivial correction beyond the classical action. In this context, it's the terms arising from the expansion of the exponential.

Let's compute the expectation values term by term.
First order in $g$:
$\left\langle \frac{g}{2} x^2 \cosh(x) \right\rangle_0 = \frac{g}{2} \left\langle x^2 \left( 1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots \right) \right\rangle_0$
$= \frac{g}{2} \left( \langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \frac{1}{24} \langle x^6 \rangle_0 + \dots \right)$
$= \frac{g}{2} \left( 1 + \frac{1}{2}(3) + \frac{1}{24}(15) + \dots \right) = \frac{g}{2} \left( 1 + \frac{3}{2} + \frac{15}{24} + \dots \right) = \frac{g}{2} \left( \frac{5}{2} + \frac{5}{8} + \dots \right) = \frac{g}{2} \left( \frac{20+5}{8} + \dots \right) = \frac{g}{2} \left( \frac{25}{8} + \dots \right)$
This approach of expanding $\cosh(x)$ inside the expectation is correct.

Let's re-evaluate the terms more systematically.
$\log(Z/Z_0) = \log \left\langle e^{\frac{g}{2} x^2 \cosh(x)} \right\rangle_0$
$= \log \left\langle 1 + \frac{g}{2} x^2 \cosh(x) + \frac{g^2}{8} x^4 \cosh^2(x) + \frac{g^3}{48} x^6 \cosh^3(x) + O(g^4) \right\rangle_0$

Let's expand $\cosh(x)$, $\cosh^2(x)$, $\cosh^3(x)$ and then take expectation values.
$\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \dots$
$\cosh^2(x) = \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots\right)^2 = 1 + x^2 + \frac{x^4}{4} + \frac{x^4}{12} + \dots = 1 + x^2 + \frac{7x^4}{12} + \dots$
Using $\cosh^2(x) = \frac{1+\cosh(2x)}{2} = \frac{1}{2} (1 + 1 + \frac{(2x)^2}{2!} + \frac{(2x)^4}{4!} + \dots) = 1 + \frac{x^2}{2} + \frac{16x^4}{24} + \dots = 1 + \frac{x^2}{2} + \frac{2x^4}{3} + \dots$
There was a mistake in the direct expansion. Let's recompute $\cosh^2(x)$:
$\cosh^2(x) = (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots)(1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots)$
$= 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^2}{2} + \frac{x^4}{4} + \frac{x^4}{24} + \dots$
$= 1 + x^2 + (\frac{1}{24} + \frac{1}{4} + \frac{1}{24}) x^4 + \dots = 1 + x^2 + (\frac{1+6+1}{24}) x^4 + \dots = 1 + x^2 + \frac{8}{24} x^4 + \dots = 1 + x^2 + \frac{x^4}{3} + \dots$
This matches the identity result.

$\cosh^3(x) = (\cosh(x))(\cosh^2(x)) = (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots)(1 + x^2 + \frac{x^4}{3} + \dots)$
$= 1 + x^2 + \frac{x^4}{3} + \frac{x^2}{2} + \frac{x^4}{2} + \frac{x^4}{24} + \dots$
$= 1 + \frac{3}{2}x^2 + (\frac{1}{3} + \frac{1}{2} + \frac{1}{24})x^4 + \dots = 1 + \frac{3}{2}x^2 + (\frac{8+12+1}{24})x^4 + \dots = 1 + \frac{3}{2}x^2 + \frac{21}{24}x^4 + \dots = 1 + \frac{3}{2}x^2 + \frac{7}{8}x^4 + \dots$

Now let's compute the expectation values of the terms in the exponential expansion:
Term 1: $\langle 1 \rangle_0 = 1$.

Term 2: $\left\langle \frac{g}{2} x^2 \cosh(x) \right\rangle_0 = \frac{g}{2} \left\langle x^2 (1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots) \right\rangle_0$
$= \frac{g}{2} \left( \langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \frac{1}{24} \langle x^6 \rangle_0 + \dots \right)$
$= \frac{g}{2} \left( 1 + \frac{1}{2}(3) + \frac{1}{24}(15) + \dots \right) = \frac{g}{2} \left( 1 + \frac{3}{2} + \frac{5}{8} + \dots \right) = \frac{g}{2} \left( \frac{8+12+5}{8} + \dots \right) = \frac{g}{2} \frac{25}{8} + O(g \cdot g^2) = \frac{25g}{16} + \dots$

Term 3: $\left\langle \frac{g^2}{8} x^4 \cosh^2(x) \right\rangle_0 = \frac{g^2}{8} \left\langle x^4 (1 + x^2 + \frac{x^4}{3} + \dots) \right\rangle_0$
$= \frac{g^2}{8} \left( \langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{1}{3} \langle x^8 \rangle_0 + \dots \right)$
We need $\langle x^8 \rangle_0 = \frac{8!}{2^4 4!} = \frac{40320}{16 \cdot 24} = \frac{40320}{384} = 105$.
$= \frac{g^2}{8} \left( 3 + 15 + \frac{1}{3}(105) + \dots \right) = \frac{g^2}{8} (3 + 15 + 35 + \dots) = \frac{g^2}{8} (53 + \dots) = \frac{53g^2}{8} + O(g^2 \cdot g^2) = \frac{53g^2}{8} + \dots$

Term 4: $\left\langle \frac{g^3}{48} x^6 \cosh^3(x) \right\rangle_0 = \frac{g^3}{48} \left\langle x^6 (1 + \frac{3}{2}x^2 + \frac{7}{8}x^4 + \dots) \right\rangle_0$
$= \frac{g^3}{48} \left( \langle x^6 \rangle_0 + \frac{3}{2} \langle x^8 \rangle_0 + \frac{7}{8} \langle x^{10} \rangle_0 + \dots \right)$
We need $\langle x^{10} \rangle_0 = \frac{10!}{2^5 5!} = \frac{3628800}{32 \cdot 120} = \frac{3628800}{3840} = 945$.
$= \frac{g^3}{48} \left( 15 + \frac{3}{2}(105) + \frac{7}{8}(945) + \dots \right)$
$= \frac{g^3}{48} \left( 15 + \frac{315}{2} + \frac{6615}{8} + \dots \right) = \frac{g^3}{48} \left( \frac{120 + 1260 + 6615}{8} + \dots \right) = \frac{g^3}{48} \frac{7995}{8} + O(g^3 \cdot g^2) = \frac{7995 g^3}{384} + \dots$
$7995/384 = 2665/128$.

So, $\log(Z/Z_0) = \log(1 + \frac{25g}{16} + \frac{53g^2}{8} + \frac{2665g^3}{128} + \dots)$
Using $\log(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \dots$
Here $u = \frac{25g}{16} + \frac{53g^2}{8} + \frac{2665g^3}{128} + \dots$

First term: $u = \frac{25g}{16} + \frac{53g^2}{8} + \frac{2665g^3}{128} + \dots$

Second term: $-\frac{u^2}{2} = -\frac{1}{2} \left( \frac{25g}{16} + \frac{53g^2}{8} + \dots \right)^2$
$= -\frac{1}{2} \left( (\frac{25g}{16})^2 + 2 (\frac{25g}{16})(\frac{53g^2}{8}) + \dots \right)$
$= -\frac{1}{2} \left( \frac{625g^2}{256} + \frac{2650g^3}{128} + \dots \right) = -\frac{625g^2}{512} - \frac{2650g^3}{256} + \dots$

Third term: $\frac{u^3}{3} = \frac{1}{3} \left( \frac{25g}{16} + \dots \right)^3 = \frac{1}{3} \left( \frac{25^3 g^3}{16^3} + \dots \right) = \frac{15625 g^3}{3 \cdot 4096} + \dots = \frac{15625 g^3}{12288} + \dots$

Combining terms by order of $g$:
Order $g$: $\frac{25g}{16}$

Order $g^2$: $\frac{53g^2}{8} - \frac{625g^2}{512} = \left( \frac{53 \cdot 64}{512} - \frac{625}{512} \right) g^2 = \left( \frac{3392 - 625}{512} \right) g^2 = \frac{2767g^2}{512}$

Order $g^3$: $\frac{2665g^3}{128} - \frac{2650g^3}{256} + \frac{15625g^3}{12288}$
$= \left( \frac{2665 \cdot 2}{256} - \frac{2650}{256} \right) g^3 + \frac{15625g^3}{12288}$
$= \left( \frac{5330 - 2650}{256} \right) g^3 + \frac{15625g^3}{12288} = \frac{2680g^3}{256} + \frac{15625g^3}{12288}$
$2680/256 = 335/32$.
$= \frac{335g^3}{32} + \frac{15625g^3}{12288}$
Common denominator is 12288. $12288 / 32 = 384$.
$= \left( \frac{335 \cdot 384}{12288} + \frac{15625}{12288} \right) g^3 = \left( \frac{128640 + 15625}{12288} \right) g^3 = \frac{144265g^3}{12288}$

Let's double check the calculation of the expectation values.
$\langle x^2 \cosh x \rangle_0 = \langle x^2 (1 + x^2/2 + x^4/24 + x^6/720) \rangle_0 = 1 + 3/2 + 15/24 + 105/720 = 1 + 3/2 + 5/8 + 7/48 = (48+72+30+7)/48 = 157/48$.
So the term is $\frac{g}{2} \frac{157}{48} = \frac{157g}{96}$. My previous calculation was $25/8 * 1/2 = 25/16$. Error found.

Let's restart from the expectation values.
$\langle x^2 \cosh x \rangle_0 = \langle x^2 \rangle_0 + \frac{1}{2} \langle x^4 \rangle_0 + \frac{1}{24} \langle x^6 \rangle_0 + \frac{1}{720} \langle x^8 \rangle_0 + \dots$
$= 1 + \frac{3}{2} + \frac{15}{24} + \frac{105}{720} + \dots = 1 + \frac{3}{2} + \frac{5}{8} + \frac{7}{48} + \dots = \frac{48+72+30+7}{48} = \frac{157}{48}$.
So the term of order $g$ is $\frac{g}{2} \frac{157}{48} = \frac{157g}{96}$.

$\langle x^4 \cosh^2 x \rangle_0 = \langle x^4 (1 + x^2 + x^4/3 + x^6/45 + \dots) \rangle_0$
$= \langle x^4 \rangle_0 + \langle x^6 \rangle_0 + \frac{1}{3} \langle x^8 \rangle_0 + \frac{1}{45} \langle x^{10} \rangle_0 + \dots$
$= 3 + 15 + \frac{1}{3}(105) + \frac{1}{45}(945) + \dots = 3 + 15 + 35 + 21 + \dots = 74$.
So the term of order $g^2$ is $\frac{g^2}{8} (74) = \frac{74g^2}{8} = \frac{37g^2}{4}$.

$\langle x^6 \cosh^3 x \rangle_0 = \langle x^6 (1 + \frac{3}{2}x^2 + \frac{7}{8}x^4 + \dots) \rangle_0$
$= \langle x^6 \rangle_0 + \frac{3}{2} \langle x^8 \rangle_0 + \frac{7}{8} \langle x^{10} \rangle_0 + \dots$
$= 15 + \frac{3}{2}(105) + \frac{7}{8}(945) + \dots = 15 + \frac{315}{2} + \frac{6615}{8} + \dots = \frac{120 + 1260 + 6615}{8} = \frac{7995}{8}$.
So the term of order $g^3$ is $\frac{g^3}{48} \frac{7995}{8} = \frac{7995 g^3}{384} = \frac{2665 g^3}{128}$.

So, $\log(Z/Z_0) = \log \left( 1 + \frac{157g}{96} + \frac{37g^2}{4} + \frac{2665g^3}{128} + \dots \right)$
Let $u = \frac{157g}{96} + \frac{37g^2}{4} + \frac{2665g^3}{128} + \dots$

$\log(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \dots$

Order $g$: $\frac{157g}{96}$.

Order $g^2$: $\frac{37g^2}{4} - \frac{1}{2} \left( \frac{157g}{96} \right)^2 = \frac{37g^2}{4} - \frac{1}{2} \frac{24649g^2}{9216} = \frac{37g^2}{4} - \frac{24649g^2}{18432}$
$= \left( \frac{37 \cdot 4608}{18432} - \frac{24649}{18432} \right) g^2 = \left( \frac{170496 - 24649}{18432} \right) g^2 = \frac{145847g^2}{18432}$.

Order $g^3$: $\frac{2665g^3}{128} - \frac{1}{2} \cdot 2 \cdot \left( \frac{157g}{96} \right) \left( \frac{37g^2}{4} \right) + \frac{1}{3} \left( \frac{157g}{96} \right)^3$
$= \frac{2665g^3}{128} - \frac{157 \cdot 37 g^3}{96 \cdot 4} + \frac{1}{3} \frac{157^3 g^3}{96^3}$
$= \frac{2665g^3}{128} - \frac{5809 g^3}{384} + \frac{3869893 g^3}{3 \cdot 884736}$
$= \frac{2665g^3}{128} - \frac{5809 g^3}{384} + \frac{3869893 g^3}{2654208}$

Common denominator for the first two terms: 384.
$\left( \frac{2665 \cdot 3}{384} - \frac{5809}{384} \right) g^3 = \left( \frac{7995 - 5809}{384} \right) g^3 = \frac{2186 g^3}{384} = \frac{1093 g^3}{192}$.

So, $\log(Z/Z_0) = \frac{157g}{96} + \frac{145847g^2}{18432} + \frac{1093 g^3}{192} + \frac{3869893 g^3}{2654208} + \dots$

Let's check the definition of 1-loop contribution. It's often the result of the Gaussian integral around the saddle point.
The action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
The saddle point is at $S'(x) = 0$.
$x - \frac{g}{2} (2x \cosh x + x^2 \sinh x) = 0$
$x (1 - g \cosh x - \frac{g}{2} x \sinh x) = 0$.
One solution is $x=0$.
At $x=0$, $S''(x) = 1 - g \cosh x - \frac{g}{2} x \sinh x - g \sinh x - \frac{g}{2} x \cosh x - \frac{g}{2} \sinh x - \frac{g}{2} x \cosh x$
$S''(x)|_{x=0} = 1 - g$.
The 1-loop contribution from a quadratic action $S''(x)/2$ is $\int dx e^{-S''(x)/2} = \sqrt{2\pi / S''(x)}$.
For a zero-dimensional field, this is $\sqrt{2\pi / S''(0)}$.
The partition function around the saddle point $x_0$ is $Z \approx e^{-S(x_0)} \sqrt{\frac{2\pi}{\det(S''(x_0))}}$.
For zero dimension, $Z \approx e^{-S(x_0)} \sqrt{\frac{2\pi}{S''(x_0)}}$.
If $x_0=0$, $S(0)=0$. $Z \approx \sqrt{\frac{2\pi}{1-g}}$.
$Z_0 = \int dx e^{-x^2/2} = \sqrt{2\pi}$.
$\log(Z/Z_0) \approx \log(\frac{1}{\sqrt{1-g}}) = -\frac{1}{2} \log(1-g) = -\frac{1}{2} (-g - \frac{g^2}{2} - \frac{g^3}{3} - \dots)$
$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \dots$
This is different from my previous calculation. The "1-loop contribution" might refer to the expansion of the exponential in the integral.

The problem asks for the 1-loop contribution to $\log(Z/Z_0)$. This typically means the terms arising from the expansion of the exponential in the expression for $\log(Z/Z_0) = \log \langle e^{\frac{g}{2} x^2 \cosh(x)} \rangle_0$.
The expansion is $\log(1 + \langle u \rangle_0 + \langle u^2/2! \rangle_0 + \langle u^3/3! \rangle_0 + \dots)$ where $u = \frac{g}{2} x^2 \cosh(x)$.
The "1-loop contribution" is usually the first order in $g$ of this expansion.

Let's assume the question is asking for the first few terms in the power series expansion of $\log(Z/Z_0)$ in $g$.

The calculation based on the expansion of the exponential seems to be the standard interpretation for such problems.
The terms computed were:
$\log(Z/Z_0) = \log \left( 1 + \frac{157g}{96} + \frac{37g^2}{4} + \frac{2665g^3}{128} + \dots \right)$
This is $\log(1+u)$ where $u = \frac{157g}{96} + \frac{37g^2}{4} + \frac{2665g^3}{128} + \dots$
$\log(1+u) = u - u^2/2 + u^3/3 - \dots$

Order $g$: $\frac{157g}{96}$.

Order $g^2$: $\frac{37g^2}{4} - \frac{1}{2} (\frac{157g}{96})^2 = \frac{37g^2}{4} - \frac{24649g^2}{18432} = \frac{170496 - 24649}{18432} g^2 = \frac{145847g^2}{18432}$.

Order $g^3$: $\frac{2665g^3}{128} - \frac{1}{2} \cdot 2 \cdot (\frac{157g}{96}) (\frac{37g^2}{4}) + \frac{1}{3} (\frac{157g}{96})^3$
$= \frac{2665g^3}{128} - \frac{5809g^3}{384} + \frac{3869893g^3}{2654208}$
$= \frac{1093g^3}{192} + \frac{3869893g^3}{2654208}$
$= \frac{1093 \cdot 13824}{2654208} g^3 + \frac{3869893g^3}{2654208} = \frac{15109872 + 3869893}{2654208} g^3 = \frac{19000000 - 1000000 + 141865}{2654208} g^3$
$\frac{19000000-15109872}{2654208} ?$
$15109872 + 3869893 = 18979765$.

Let's check the question again. "Compute the 1-loop contribution to log(Z/Z_0)".
This usually means the first non-trivial correction. If we consider the expansion of the exponential:
$e^{\frac{g}{2} x^2 \cosh(x)} = 1 + \frac{g}{2} x^2 \cosh(x) + O(g^2)$
$\log(Z/Z_0) = \log \left\langle 1 + \frac{g}{2} x^2 \cosh(x) + \dots \right\rangle_0$
$= \log(1 + \langle \frac{g}{2} x^2 \cosh(x) \rangle_0 + \dots)$
$= \langle \frac{g}{2} x^2 \cosh(x) \rangle_0 + O(g^2)$.
The 1-loop contribution is the term linear in $g$.

If the question asks for the expansion of $\log(Z/Z_0)$ through order $g^3$, then the full calculation is needed.
The phrase "1-loop contribution" can be ambiguous. In some contexts, it refers to the quadratic fluctuations around the classical solution. However, given the request for a power series expansion in $g$, it's more likely asking for the terms in the expansion of $\log(Z/Z_0)$.

Let's assume the question means the power series expansion of $\log(Z/Z_0)$ in $g$ up to $g^3$.

The result is $\frac{157g}{96} + \frac{145847g^2}{18432} + \frac{18979765 g^3}{2654208}$.

Final check of the calculation.
Term $g$: $\frac{157}{96}$.
Term $g^2$: $\frac{37}{4} - \frac{1}{2} (\frac{157}{96})^2 = \frac{37}{4} - \frac{24649}{18432} = \frac{170496 - 24649}{18432} = \frac{145847}{18432}$.
Term $g^3$: $\frac{2665}{128} - \frac{157 \cdot 37}{384} + \frac{1}{3} (\frac{157}{96})^3 = \frac{2665}{128} - \frac{5809}{384} + \frac{3869893}{2654208}$
$= \frac{2186}{384} + \frac{3869893}{2654208} = \frac{1093}{192} + \frac{3869893}{2654208}$
$= \frac{1093 \cdot 13824}{2654208} + \frac{3869893}{2654208} = \frac{15109872 + 3869893}{2654208} = \frac{18979765}{2654208}$.

The final answer is the sum of these terms.

$\boxed{\frac{157g}{96} + \frac{145847g^2}{18432} + \frac{18979765g^3}{2654208}}$