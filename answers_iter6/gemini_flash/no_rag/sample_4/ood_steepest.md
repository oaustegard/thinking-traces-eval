To compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, we will use the Laplace method (often referred to as steepest descent when generalized to the complex plane). The core idea is that as $n$ becomes large, the integrand is dominated by the region where the exponent is maximized.

First, we rewrite the integrand in the form $e^{n f(x)}$:
$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} dx = \int_0^{\pi/2} e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)} dx$

The phase function (or exponent function) is $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$. The prefactor $h(x)$ is 1 in this case.

**1. Locate the critical point $x^*$**
The critical point $x^*$ is where the first derivative of $f(x)$ is zero: $f'(x^*) = 0$.
$f'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$f'(x) = \cot x - \frac{1}{2} \tan x$

Setting $f'(x) = 0$:
$\cot x - \frac{1}{2} \tan x = 0$
$\frac{1}{\tan x} = \frac{1}{2} \tan x$
$2 = \tan^2 x$
$\tan x = \pm \sqrt{2}$

Since the integration interval is $x \in [0, \pi/2]$, $\sin x > 0$ and $\cos x > 0$, which implies $\tan x$ must be positive.
Therefore, the critical point is $x^* = \arctan(\sqrt{2})$.
This point lies within the interval $(0, \pi/2)$. We note that at the boundaries, $\sin x \to 0$ or $\cos x \to 0$, making $f(x) \to -\infty$, so the maximum must be in the interior.

**2. Evaluate $f(x^*)$**
To evaluate $f(x^*)$, we need the values of $\sin x^*$ and $\cos x^*$.
From $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

Substitute these into $f(x^*)$:
$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
Using logarithm properties $\ln(a/b) = \ln a - \ln b$ and $\ln(a^k) = k \ln a$:
$f(x^*) = \left(\ln(\sqrt{2}) - \ln(\sqrt{3})\right) + \frac{1}{2} \left(\ln(1) - \ln(\sqrt{3})\right)$
$f(x^*) = \left(\frac{1}{2}\ln 2 - \frac{1}{2}\ln 3\right) + \frac{1}{2} \left(0 - \frac{1}{2}\ln 3\right)$
$f(x^*) = \frac{1}{2}\ln 2 - \frac{1}{2}\ln 3 - \frac{1}{4}\ln 3$
$f(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$

**3. Evaluate the second derivative $f''(x^*)$**
First, compute the second derivative of $f(x)$:
$f'(x) = \cot x - \frac{1}{2} \tan x$
$f''(x) = \frac{d}{dx} (\cot x) - \frac{1}{2} \frac{d}{dx} (\tan x)$
$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Since $\csc^2 x > 0$ and $\sec^2 x > 0$ for $x \in (0, \pi/2)$, $f''(x)$ is always negative, confirming that $x^*$ is indeed a maximum.

Now, substitute the values of $\sin x^*$ and $\cos x^*$:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{(\sqrt{2}/\sqrt{3})^2} = \frac{1}{2/3} = \frac{3}{2}$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{(1/\sqrt{3})^2} = \frac{1}{1/3} = 3$

$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$

**4. Assemble the Gaussian-fluctuation prefactor and the asymptotic behavior**
The leading asymptotic behavior of an integral of the form $\int_a^b h(x) e^{n f(x)} dx$ with a single maximum at $x^*$ in $(a,b)$ is given by:
$V(n) \sim h(x^*) \sqrt{\frac{2\pi}{n|f''(x^*)|}} e^{n f(x^*)}$

In our case, $h(x) = 1$. Substituting the values we found:
$V(n) \sim 1 \cdot \sqrt{\frac{2\pi}{n|-3|}} e^{n \left(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3\right)}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} e^{n \ln(2^{1/2})} e^{n \ln(3^{-3/4})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} (2^{1/2})^n (3^{-3/4})^n$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}$

This expression represents the leading asymptotic behavior of $V(n)$ as $n \to \infty$.

The final answer is $\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}}$