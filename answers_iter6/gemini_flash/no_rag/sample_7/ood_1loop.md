The problem asks for the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$. We need to expand the answer as a power series in $g$ through order $g^3$.

First, let's define $Z$ and $Z_0$:
$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx$
$Z_0 = \int_{-\infty}^{\infty} e^{-S_0(x)/\hbar} dx$, where $S_0(x) = x^2/2$.

The free partition function $Z_0$ is a Gaussian integral:
$Z_0 = \int_{-\infty}^{\infty} e^{-x^2/(2\hbar)} dx = \sqrt{2\pi\hbar}$.

To compute $Z$, we use the semi-classical expansion (or WKB expansion). We expand the action $S(x)$ around its classical minimum. For small $g$, $x_c=0$ is a minimum.
Let's expand $S(x)$ in a Taylor series around $x=0$:
$S(x) = \sum_{n=0}^{\infty} \frac{S^{(n)}(0)}{n!} x^n$.
Since $S(x)$ is an even function, only even powers of $x$ will be present.
$S(x) = x^2/2 - (g/2) x^2 \cosh(x) = x^2/2 - (g/2) x^2 \sum_{k=0}^{\infty} \frac{x^{2k}}{(2k)!}$
$S(x) = x^2/2 - (g/2) \left( x^2 + \frac{x^4}{2!} + \frac{x^6}{4!} + \frac{x^8}{6!} + \dots \right)$
$S(x) = \left( \frac{1}{2} - \frac{g}{2} \right) x^2 - \frac{g}{2 \cdot 2!} x^4 - \frac{g}{2 \cdot 4!} x^6 - \frac{g}{2 \cdot 6!} x^8 - \dots$
$S(x) = \frac{1-g}{2} x^2 - \frac{g}{4} x^4 - \frac{g}{48} x^6 - \frac{g}{1440} x^8 - \dots$

From this expansion, we can identify the derivatives at $x=0$:
$S(0) = 0$
$S''(0) = 1-g$
$S^{(4)}(0) = -g \cdot (4!/4) = -6g$
$S^{(6)}(0) = -g \cdot (6!/48) = -15g$
$S^{(8)}(0) = -g \cdot (8!/1440) = -28g$

Now, we perform the integral $Z = \int dx e^{-S(x)/\hbar}$. It is convenient to scale $x = \sqrt{\hbar}y$:
$S(x)/\hbar = S(\sqrt{\hbar}y)/\hbar = \frac{1-g}{2} y^2 - \frac{g\hbar}{4} y^4 - \frac{g\hbar^2}{48} y^6 - \frac{g\hbar^3}{1440} y^8 - \dots$
$Z = \int \sqrt{\hbar} dy e^{-\left(\frac{1-g}{2} y^2 - \frac{g\hbar}{4} y^4 - \frac{g\hbar^2}{48} y^6 - \dots\right)}$
$Z = \sqrt{\hbar} \int dy e^{-\frac{1-g}{2} y^2} e^{\frac{g\hbar}{4} y^4 + \frac{g\hbar^2}{48} y^6 + \dots}$
We expand the second exponential in powers of $\hbar$:
$e^{\frac{g\hbar}{4} y^4 + \frac{g\hbar^2}{48} y^6 + \dots} = 1 + \left(\frac{g\hbar}{4} y^4 + \frac{g\hbar^2}{48} y^6 + \dots\right) + \frac{1}{2} \left(\frac{g\hbar}{4} y^4\right)^2 + O(\hbar^3)$
$= 1 + \frac{g\hbar}{4} y^4 + \frac{g\hbar^2}{48} y^6 + \frac{g^2\hbar^2}{32} y^8 + O(\hbar^3)$

Substitute this back into the integral for $Z$:
$Z = \sqrt{\hbar} \int dy e^{-\frac{1-g}{2} y^2} \left( 1 + \frac{g\hbar}{4} y^4 + \frac{g\hbar^2}{48} y^6 + \frac{g^2\hbar^2}{32} y^8 + O(\hbar^3) \right)$
Let $A = (1-g)/2$. The integral $\int e^{-Ay^2} dy = \sqrt{\pi/A}$.
We need the Gaussian moments $\langle y^{2n} \rangle_A = \frac{\int y^{2n} e^{-Ay^2} dy}{\int e^{-Ay^2} dy} = \frac{(2n)!}{n!(4A)^n}$.
$4A = 2(1-g)$.
$\langle y^4 \rangle_A = \frac{4!}{2!(2(1-g))^2} = \frac{24}{2 \cdot 4(1-g)^2} = \frac{3}{(1-g)^2}$.
$\langle y^6 \rangle_A = \frac{6!}{3!(2(1-g))^3} = \frac{720}{6 \cdot 8(1-g)^3} = \frac{15}{(1-g)^3}$.
$\langle y^8 \rangle_A = \frac{8!}{4!(2(1-g))^4} = \frac{40320}{24 \cdot 16(1-g)^4} = \frac{105}{(1-g)^4}$.

Now, evaluate $Z$:
$Z = \sqrt{\hbar} \sqrt{\frac{\pi}{A}} \left( 1 + \frac{g\hbar}{4} \langle y^4 \rangle_A + \frac{g\hbar^2}{48} \langle y^6 \rangle_A + \frac{g^2\hbar^2}{32} \langle y^8 \rangle_A + O(\hbar^3) \right)$
$Z = \sqrt{\hbar} \sqrt{\frac{2\pi}{1-g}} \left( 1 + \frac{g\hbar}{4} \frac{3}{(1-g)^2} + \frac{g\hbar^2}{48} \frac{15}{(1-g)^3} + \frac{g^2\hbar^2}{32} \frac{105}{(1-g)^4} + O(\hbar^3) \right)$
Recognizing $Z_0 = \sqrt{2\pi\hbar}$:
$Z = Z_0 \frac{1}{\sqrt{1-g}} \left( 1 + \frac{3g\hbar}{4(1-g)^2} + \frac{5g\hbar^2}{16(1-g)^3} + \frac{105g^2\hbar^2}{32(1-g)^4} + O(\hbar^3) \right)$

Now we compute $\log(Z/Z_0)$:
$\log(Z/Z_0) = \log\left( \frac{1}{\sqrt{1-g}} \left( 1 + \frac{3g\hbar}{4(1-g)^2} + \frac{5g\hbar^2}{16(1-g)^3} + \frac{105g^2\hbar^2}{32(1-g)^4} + O(\hbar^3) \right) \right)$
$\log(Z/Z_0) = -\frac{1}{2}\log(1-g) + \log\left( 1 + \left( \frac{3g}{4(1-g)^2} \right)\hbar + \left( \frac{5g}{16(1-g)^3} + \frac{105g^2}{32(1-g)^4} \right)\hbar^2 + O(\hbar^3) \right)$
Using the expansion $\log(1+u) = u - u^2/2 + O(u^3)$:
$\log(Z/Z_0) = -\frac{1}{2}\log(1-g) + \left( \frac{3g}{4(1-g)^2} \right)\hbar + \left( \frac{5g}{16(1-g)^3} + \frac{105g^2}{32(1-g)^4} \right)\hbar^2 - \frac{1}{2} \left( \frac{3g}{4(1-g)^2} \right)^2 \hbar^2 + O(\hbar^3)$
$\log(Z/Z_0) = -\frac{1}{2}\log(1-g) + \left( \frac{3g}{4(1-g)^2} \right)\hbar + \left( \frac{5g}{16(1-g)^3} + \frac{105g^2}{32(1-g)^4} - \frac{9g^2}{32(1-g)^4} \right)\hbar^2 + O(\hbar^3)$
$\log(Z/Z_0) = -\frac{1}{2}\log(1-g) + \left( \frac{3g}{4(1-g)^2} \right)\hbar + \left( \frac{5g}{16(1-g)^3} + \frac{96g^2}{32(1-g)^4} \right)\hbar^2 + O(\hbar^3)$

The "1-loop contribution" is conventionally defined as the coefficient of $\hbar^1$ in the semi-classical expansion of $\log(Z/Z_0)$.
So, the 1-loop contribution is $L_1 = \frac{3g}{4(1-g)^2}$.

Now, we need to expand $L_1$ as a power series in $g$ through order $g^3$:
$L_1 = \frac{3g}{4} (1-g)^{-2}$
Using the generalized binomial theorem $(1+x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!} x^2 + \frac{\alpha(\alpha-1)(\alpha-2)}{3!} x^3 + \dots$:
$(1-g)^{-2} = 1 + (-2)(-g) + \frac{(-2)(-3)}{2!}(-g)^2 + \frac{(-2)(-3)(-4)}{3!}(-g)^3 + O(g^4)$
$= 1 + 2g + 3g^2 + 4g^3 + O(g^4)$

Substitute this back into the expression for $L_1$:
$L_1 = \frac{3g}{4} (1 + 2g + 3g^2 + 4g^3 + O(g^4))$
$L_1 = \frac{3}{4}g + \frac{6}{4}g^2 + \frac{9}{4}g^3 + \frac{12}{4}g^4 + O(g^5)$
$L_1 = \frac{3}{4}g + \frac{3}{2}g^2 + \frac{9}{4}g^3 + O(g^4)$

The 1-loop contribution to $\log(Z/Z_0)$, expanded as a power series in $g$ through order $g^3$, is:

$\boxed{\hbar \left( \frac{3}{4}g + \frac{3}{2}g^2 + \frac{9}{4}g^3 \right)}$