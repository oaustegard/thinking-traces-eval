Let the integral be $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$. We want to find the leading asymptotic behavior as $n \to \infty$. We will use the steepest descent method (also known as Laplace's method).

First, we rewrite the integrand in the form $e^{n f(x)}$.
Let $g(x) = (\sin x)^n (\cos x)^{n/2}$.
Then $\ln g(x) = n \ln(\sin x) + \frac{n}{2} \ln(\cos x)$.
So, $V(n) = \int_0^{\pi/2} e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)} dx$.
The phase function is $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

To apply the steepest descent method, we need to find the maximum of $f(x)$ in the interval $[0, \pi/2]$. We do this by finding the critical points, where $f'(x) = 0$.

$f'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$f'(x) = \cot x - \frac{1}{2} \tan x$

Set $f'(x) = 0$:
$\cot x - \frac{1}{2} \tan x = 0$
$\cot x = \frac{1}{2} \tan x$
$\frac{1}{\tan x} = \frac{1}{2} \tan x$
$\tan^2 x = 2$
$\tan x = \sqrt{2}$ (since $x \in [0, \pi/2]$, $\tan x \ge 0$).

The location of the critical point $x^*$ is such that $\tan x^* = \sqrt{2}$.
From $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{2+1} = \sqrt{3}$.
Therefore, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

Now, we evaluate the phase function $f(x)$ at the critical point $x^*$:
$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$f(x^*) = \ln(2^{1/2} 3^{-1/2}) + \frac{1}{2} \ln(3^{-1/2})$
$f(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$f(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$
$f(x^*) = \ln(2^{1/2}) - \ln(3^{3/4}) = \ln\left(\frac{\sqrt{2}}{3^{3/4}}\right)$.

The contribution to the integral from the vicinity of $x^*$ is approximately $e^{n f(x^*)} \sqrt{\frac{2\pi}{-n f''(x^*)}}$. We need to compute the second derivative of $f(x)$.

$f'(x) = \cot x - \frac{1}{2} \tan x$
$f''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Now, we evaluate $f''(x^*)$ using $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{(\sqrt{2}/\sqrt{3})^2} = \frac{1}{2/3} = \frac{3}{2}$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{(1/\sqrt{3})^2} = \frac{1}{1/3} = 3$

$f''(x^*) = -\frac{3}{2} - \frac{1}{2} (3) = -\frac{3}{2} - \frac{3}{2} = -3$.

The asymptotic behavior of the integral is given by:
$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{-n f''(x^*)}} \quad \text{as } n \to \infty$.

Substitute the values of $f(x^*)$ and $f''(x^*)$:
$V(n) \sim e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} \sqrt{\frac{2\pi}{-n (-3)}}$
$V(n) \sim e^{n \ln(2^{1/2})} e^{-n \ln(3^{3/4})} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim (2^{1/2})^n (3^{-3/4})^n \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim 2^{n/2} 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}$

We can also write $f(x^*)$ as:
$f(x^*) = \ln\left(\frac{(\sin x^*)^1 (\cos x^*)^{1/2}}{1}\right) = \ln\left( \left(\frac{\sqrt{2}}{\sqrt{3}}\right)^1 \left(\frac{1}{\sqrt{3}}\right)^{1/2} \right) = \ln\left( \frac{2^{1/2}}{3^{1/2}} \frac{1}{3^{1/4}} \right) = \ln\left( \frac{2^{1/2}}{3^{3/4}} \right)$.
So $e^{n f(x^*)} = \left(\frac{2^{1/2}}{3^{3/4}}\right)^n = \frac{2^{n/2}}{3^{3n/4}}$.

The prefactor is $\sqrt{\frac{2\pi}{3n}}$.

The leading asymptotic behavior of the integral is:
$V(n) \sim \frac{2^{n/2}}{3^{3n/4}} \sqrt{\frac{2\pi}{3n}}$.

The critical point is $x^* = \arctan(\sqrt{2})$.
The value of the phase at the critical point is $f(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{-n f''(x^*)}} = \sqrt{\frac{2\pi}{3n}}$.

Putting it all together:
$V(n) \sim e^{n(\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim 2^{n/2} 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}$

The final answer is $\boxed{2^{n/2} 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}}$.