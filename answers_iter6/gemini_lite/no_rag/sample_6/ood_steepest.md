We want to compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$. We will use the method of steepest descent, also known as Laplace's method.

First, we rewrite the integrand in the form $e^{n f(x)}$.
Let $g(x) = (\sin x)^n (\cos x)^{n/2}$.
Taking the natural logarithm, we get:
$\ln g(x) = n \ln(\sin x) + \frac{n}{2} \ln(\cos x)$
So, $g(x) = e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)}$.
The phase function is $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

We need to find the maximum of $f(x)$ in the interval $[0, \pi/2]$. We do this by finding the critical points, i.e., where $f'(x) = 0$.
$f'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$f'(x) = \cot x - \frac{1}{2} \tan x$

Set $f'(x) = 0$:
$\cot x - \frac{1}{2} \tan x = 0$
$\cot x = \frac{1}{2} \tan x$
$\frac{1}{\tan x} = \frac{1}{2} \tan x$
$\tan^2 x = 2$
$\tan x = \sqrt{2}$ (Since $x \in [0, \pi/2]$, $\tan x \ge 0$).

Let $x^*$ be the value of $x$ such that $\tan x^* = \sqrt{2}$. This value $x^*$ is in the interval $(0, \pi/2)$.
We can find $\sin x^*$ and $\cos x^*$. If $\tan x^* = \sqrt{2}$, we can imagine a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse would be $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{2+1} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

The maximum of $f(x)$ occurs at $x^*$. Let's evaluate $f(x^*)$:
$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$f(x^*) = \ln(\sqrt{2}) - \ln(\sqrt{3}) + \frac{1}{2} (\ln(1) - \ln(\sqrt{3}))$
$f(x^*) = \frac{1}{2} \ln(2) - \frac{1}{2} \ln(3) - \frac{1}{2} \ln(3)$
$f(x^*) = \frac{1}{2} \ln(2) - \ln(3) = \ln\left(\frac{\sqrt{2}}{3}\right)$.

Now we need to compute the second derivative of $f(x)$ at $x^*$, $f''(x^*)$, to determine the Gaussian-fluctuation prefactor.
$f'(x) = \cot x - \frac{1}{2} \tan x$
$f''(x) = \frac{d}{dx}(\cot x) - \frac{1}{2} \frac{d}{dx}(\tan x)$
$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Now evaluate $f''(x^*)$:
$\sin x^* = \frac{\sqrt{2}}{\sqrt{3}} \implies \csc x^* = \frac{\sqrt{3}}{\sqrt{2}} \implies \csc^2 x^* = \frac{3}{2}$
$\cos x^* = \frac{1}{\sqrt{3}} \implies \sec x^* = \sqrt{3} \implies \sec^2 x^* = 3$

$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$.

According to Laplace's method, the asymptotic behavior of the integral is given by:
$V(n) \sim \sqrt{\frac{2\pi}{-n f''(x^*)}} e^{n f(x^*)}$

Substituting the values we found:
$V(n) \sim \sqrt{\frac{2\pi}{-n (-3)}} e^{n \ln(\frac{\sqrt{2}}{3})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3}\right)^n$

Let's double check the original integral form. The integrand is $(\sin x)^n (\cos x)^{n/2}$.
The general form for Laplace's method for an integral $\int_a^b e^{M h(x)} dx$ where $M$ is large is $\sqrt{\frac{2\pi}{M (-h''(x^*))}} e^{M h(x^*)}$ if the maximum is at $x^*$.
In our case, the exponent is $n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$. So $M=n$ and $h(x) = f(x)$.

The location of the critical point is $x^*$ such that $\tan x^* = \sqrt{2}$.
The value of the phase function at the critical point is $f(x^*) = \ln\left(\frac{\sqrt{2}}{3}\right)$.
The second derivative of the phase function at the critical point is $f''(x^*) = -3$.

Therefore, the leading asymptotic behavior is:
$V(n) \sim \sqrt{\frac{2\pi}{n (-f''(x^*))}} e^{n f(x^*)}$
$V(n) \sim \sqrt{\frac{2\pi}{n (-(-3))}} e^{n \ln(\frac{\sqrt{2}}{3})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3}\right)^n$

The final answer is $\boxed{\sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3}\right)^n}$.