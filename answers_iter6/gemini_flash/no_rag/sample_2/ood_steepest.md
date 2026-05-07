To compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, we will employ the Laplace method (also known as the method of steepest descent for real integrals). This method relies on the observation that for large $n$, the integral is dominated by the region around the maximum of the integrand.

**1. Rewrite the Integral in Standard Form**
First, we express the integrand in the form $e^{n f(x)}$.
The integrand is $(\sin x)^n (\cos x)^{n/2}$.
We can write this as:
$(\sin x)^n (\cos x)^{n/2} = e^{\ln((\sin x)^n (\cos x)^{n/2})}$
$= e^{n \ln(\sin x) + \frac{n}{2} \ln(\cos x)}$
$= e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)}$

Thus, the phase function is $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
The integral becomes $V(n) = \int_0^{\pi/2} e^{n f(x)} dx$.

**2. Locate the Critical Point $x^*$}
The leading asymptotic behavior is determined by the maximum of $f(x)$. We find the critical point(s) $x^*$ by setting the first derivative of $f(x)$ to zero: $f'(x) = 0$.

$f'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$f'(x) = \cot x - \frac{1}{2} \tan x$

Set $f'(x) = 0$:
$\cot x - \frac{1}{2} \tan x = 0$
$\cot x = \frac{1}{2} \tan x$
Since $\cot x = 1/\tan x$:
$\frac{1}{\tan x} = \frac{1}{2} \tan x$
$2 = \tan^2 x$
$\tan x = \pm \sqrt{2}$

Given the integration limits $x \in (0, \pi/2)$, both $\sin x$ and $\cos x$ must be positive, which implies $\tan x$ must be positive. Therefore, we choose the positive root:
$\tan x^* = \sqrt{2}$

This defines the location of our critical point $x^*$. We can write $x^* = \arctan(\sqrt{2})$.

**3. Evaluate $f(x^*)$ and $f''(x^*)$**
To evaluate $f(x^*)$ and $f''(x^*)$, we need the values of $\sin x^*$ and $\cos x^*$. If $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{2+1} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

Now, substitute these into $f(x)$:
$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$f(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{2} \left(-\frac{1}{2} \ln 3\right)$
$f(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$f(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$f(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$

Next, we need the second derivative, $f''(x)$:
$f''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Now, substitute $x^*$ into $f''(x)$:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{(\sqrt{2}/\sqrt{3})^2} = \frac{3}{2}$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{(1/\sqrt{3})^2} = 3$
$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3)$
$f''(x^*) = -\frac{3}{2} - \frac{3}{2}$
$f''(x^*) = -3$

Since $f''(x^*) < 0$, this confirms that $x^*$ is a maximum, as required for the Laplace method.

**4. Assemble the Gaussian-Fluctuation Prefactor and Final Asymptotic Behavior**
The leading asymptotic behavior for an integral of the form $\int_a^b e^{n f(x)} dx$ with a unique maximum at $x^*$ within the interval is given by the Laplace formula:
$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}$ as $n \to \infty$.

Substitute the values we found:
$f(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$
$|f''(x^*)| = |-3| = 3$

$V(n) \sim e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} \sqrt{\frac{2\pi}{n \cdot 3}}$

We can rewrite the exponential term:
$e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} = e^{n \ln(2^{1/2})} e^{n \ln(3^{-3/4})} = (2^{1/2})^n (3^{-3/4})^n = \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n$

The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{3n}}$.

Combining these parts, the leading asymptotic behavior is:
$V(n) \sim \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}$

The location of the critical point is $x^* = \arctan(\sqrt{2})$.
The value of the phase function at the critical point is $f(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{3n}}$.

The final answer is $\boxed{V(n) \sim \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}}$.