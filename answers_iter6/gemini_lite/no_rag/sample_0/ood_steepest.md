We are asked to compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, using the steepest descent/Laplace method.

The integral is of the form $\int_a^b e^{n \phi(x)} dx$. To apply the steepest descent method, we need to rewrite the integrand in this exponential form.
Let $f(x) = (\sin x)^n (\cos x)^{n/2}$.
We can write $f(x) = e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} = e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)}$.
So, the phase function is $\phi(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

The steepest descent method is applicable when the integrand has a dominant maximum. We need to find the critical points of $\phi(x)$ in the interval $[0, \pi/2]$. These are the points where $\phi'(x) = 0$.

First, let's compute the derivative of $\phi(x)$:
$\phi'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$\phi'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$\phi'(x) = \cot x - \frac{1}{2} \tan x$

Now, we set $\phi'(x) = 0$ to find the critical points:
$\cot x - \frac{1}{2} \tan x = 0$
$\cot x = \frac{1}{2} \tan x$
$\frac{\cos x}{\sin x} = \frac{1}{2} \frac{\sin x}{\cos x}$
$2 \cos^2 x = \sin^2 x$

We know that $\sin^2 x + \cos^2 x = 1$. Substituting $\sin^2 x = 1 - \cos^2 x$ into the equation:
$2 \cos^2 x = 1 - \cos^2 x$
$3 \cos^2 x = 1$
$\cos^2 x = \frac{1}{3}$

Since $x \in [0, \pi/2]$, $\cos x \ge 0$. Thus, $\cos x = \frac{1}{\sqrt{3}}$.
This gives us the location of the critical point, $x^*$, such that $\cos(x^*) = \frac{1}{\sqrt{3}}$.
From $\cos^2 x = 1/3$, we also get $\sin^2 x = 1 - 1/3 = 2/3$. Since $x \in [0, \pi/2]$, $\sin x = \sqrt{2/3}$.
So, the critical point is $x^* = \arccos(1/\sqrt{3}) = \arcsin(\sqrt{2/3})$.

Next, we need to evaluate the phase function $\phi(x^*)$ at the critical point.
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\phi(x^*) = \ln\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{2} \left( \ln(1) - \ln(\sqrt{3}) \right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) - \frac{1}{2} \ln(\sqrt{3})$
$\phi(x^*) = \frac{1}{2} \left( \ln\left(\frac{2}{3}\right) - \ln\left(3^{1/2}\right) \right)$
$\phi(x^*) = \frac{1}{2} \left( \ln\left(\frac{2}{3}\right) - \frac{1}{2} \ln(3) \right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) - \frac{1}{4} \ln(3)$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$
$\phi(x^*) = \ln(2^{1/2}) - \ln(3^{3/4})$
$\phi(x^*) = \ln\left(\frac{\sqrt{2}}{3^{3/4}}\right)$

The Laplace method states that the asymptotic behavior is given by:
$V(n) \sim e^{n \phi(x^*)} \sqrt{\frac{2\pi}{-n \phi''(x^*)}}$

We need to compute the second derivative of $\phi(x)$.
$\phi'(x) = \cot x - \frac{1}{2} \tan x$
$\phi''(x) = \frac{d}{dx} \left( \cot x - \frac{1}{2} \tan x \right)$
$\phi''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Now, we evaluate $\phi''(x^*)$:
$\cos(x^*) = \frac{1}{\sqrt{3}}$, so $\sec(x^*) = \sqrt{3}$, and $\sec^2(x^*) = 3$.
$\sin(x^*) = \sqrt{\frac{2}{3}}$, so $\csc(x^*) = \sqrt{\frac{3}{2}}$, and $\csc^2(x^*) = \frac{3}{2}$.

$\phi''(x^*) = -\frac{3}{2} - \frac{1}{2} (3)$
$\phi''(x^*) = -\frac{3}{2} - \frac{3}{2}$
$\phi''(x^*) = -3$

Now we can assemble the Gaussian-fluctuation prefactor:
$\sqrt{\frac{2\pi}{-n \phi''(x^*)}} = \sqrt{\frac{2\pi}{-n (-3)}} = \sqrt{\frac{2\pi}{3n}}$

The leading asymptotic behavior is:
$V(n) \sim e^{n \phi(x^*)} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} \left(\frac{2\pi}{3n}\right)^{1/2}$
$V(n) \sim e^{\ln(2^{n/2})} e^{\ln(3^{-3n/4})} \left(\frac{2\pi}{3n}\right)^{1/2}$
$V(n) \sim 2^{n/2} 3^{-3n/4} \left(\frac{2\pi}{3n}\right)^{1/2}$
$V(n) \sim \frac{\sqrt{2\pi}}{\sqrt{3n}} \frac{2^{n/2}}{3^{3n/4}}$

Let's double check the calculation of $\phi(x^*)$:
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\sin x^* = \sqrt{2/3}$, $\cos x^* = 1/\sqrt{3}$
$\phi(x^*) = \ln(\sqrt{2/3}) + \frac{1}{2} \ln(1/\sqrt{3})$
$\phi(x^*) = \frac{1}{2} \ln(2/3) + \frac{1}{2} (\ln 1 - \ln \sqrt{3})$
$\phi(x^*) = \frac{1}{2} \ln(2/3) - \frac{1}{2} \ln(3^{1/2})$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$
This seems correct.

The integral can be rewritten as:
$V(n) = \int_0^{\pi/2} e^{n(\ln(\sin x) + \frac{1}{2}\ln(\cos x))} dx$

The critical point is $x^*$ where $\cos x^* = 1/\sqrt{3}$ and $\sin x^* = \sqrt{2/3}$.
The value of the phase at the critical point is $n \phi(x^*) = n(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3)$.
The second derivative of the phase is $\phi''(x^*) = -3$.

The asymptotic behavior is given by:
$V(n) \sim e^{n \phi(x^*)} \sqrt{\frac{2\pi}{-n \phi''(x^*)}}$
$V(n) \sim e^{n(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3)} \sqrt{\frac{2\pi}{-n(-3)}}$
$V(n) \sim e^{\ln(2^{n/2})} e^{\ln(3^{-3n/4})} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim 2^{n/2} 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim \frac{\sqrt{2\pi}}{\sqrt{3n}} \frac{2^{n/2}}{3^{3n/4}}$

Final check on the form of the answer.
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left( \frac{2^{1/2}}{3^{3/4}} \right)^n$

The location $x^*$ of the critical point is given by $\cos x^* = 1/\sqrt{3}$.
The phase at $x^*$ is $\phi(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{-n \phi''(x^*)}} = \sqrt{\frac{2\pi}{3n}}$.

Combining these gives the leading asymptotic behavior.

The final answer is $\boxed{\sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n}$.