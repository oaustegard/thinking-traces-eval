We are asked to compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, using the steepest descent/Laplace method.

The integral is of the form $V(n) = \int_a^b e^{n \phi(x)} dx$, where the exponent $n \phi(x)$ is dominant for large $n$.
Let's rewrite the integrand in this form.
$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} dx = \int_0^{\pi/2} e^{n (\ln(\sin x) + \frac{1}{2} \ln(\cos x))} dx$
So, the phase function is $\phi(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
The integration limits are from $a=0$ to $b=\pi/2$.

The Laplace method requires finding the maximum of the phase function $\phi(x)$ in the interval of integration. We first find the critical points by setting the derivative of $\phi(x)$ to zero.
$\phi'(x) = \frac{d}{dx} (\ln(\sin x) + \frac{1}{2} \ln(\cos x))$
$\phi'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x} = \cot x - \frac{1}{2} \tan x$

To find the critical point $x^*$, we set $\phi'(x^*) = 0$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\frac{\cos x^*}{\sin x^*} = \frac{1}{2} \frac{\sin x^*}{\cos x^*}$
$2 \cos^2 x^* = \sin^2 x^*$
Using the identity $\sin^2 x^* = 1 - \cos^2 x^*$:
$2 \cos^2 x^* = 1 - \cos^2 x^*$
$3 \cos^2 x^* = 1$
$\cos^2 x^* = \frac{1}{3}$

Since $x$ is in the interval $[0, \pi/2]$, $\cos x^*$ must be positive.
$\cos x^* = \frac{1}{\sqrt{3}}$
This gives a unique critical point in the interval $(0, \pi/2)$. Let's find $\sin x^*$:
$\sin^2 x^* = 1 - \cos^2 x^* = 1 - \frac{1}{3} = \frac{2}{3}$
Since $x$ is in $(0, \pi/2)$, $\sin x^*$ must be positive.
$\sin x^* = \sqrt{\frac{2}{3}}$

Now we need to check if this critical point is a maximum. We compute the second derivative of $\phi(x)$:
$\phi''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
$\phi''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$
At $x^*$, we have:
$\cos x^* = \frac{1}{\sqrt{3}} \implies \sec x^* = \sqrt{3} \implies \sec^2 x^* = 3$
$\sin x^* = \sqrt{\frac{2}{3}} \implies \csc x^* = \sqrt{\frac{3}{2}} \implies \csc^2 x^* = \frac{3}{2}$
$\phi''(x^*) = -\frac{3}{2} - \frac{1}{2} (3) = -\frac{3}{2} - \frac{3}{2} = -3$
Since $\phi''(x^*) < 0$, the critical point $x^*$ corresponds to a maximum of the phase function.

Now, we evaluate the phase function at $x^*$:
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\phi(x^*) = \ln\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{2} \left(-\frac{1}{2} \ln 3\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$

The Laplace method states that the asymptotic behavior of the integral is given by:
$V(n) \sim \sqrt{\frac{2\pi}{-n \phi''(x^*)}} e^{n \phi(x^*)}$
We have $n \phi(x^*) = n \left(\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3\right) = \ln(2^{n/2}) - \ln(3^{3n/4}) = \ln\left(\frac{2^{n/2}}{3^{3n/4}}\right)$.
So, $e^{n \phi(x^*)} = \frac{2^{n/2}}{3^{3n/4}}$.

The prefactor is $\sqrt{\frac{2\pi}{-n \phi''(x^*)}} = \sqrt{\frac{2\pi}{-n (-3)}} = \sqrt{\frac{2\pi}{3n}}$.

Assembling the Gaussian-fluctuation prefactor and the exponential term:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2^{n/2}}{3^{3n/4}}\right)$

Let's check the endpoints. At $x=0$, $\sin x = 0$, so the integrand is 0. At $x=\pi/2$, $\cos x = 0$, so the integrand is 0. Thus, the endpoints do not contribute to the leading asymptotic behavior.

The leading asymptotic behavior is:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2^{n/2}}{3^{3n/4}}\right)$

We can rewrite this as:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2^{n/2}}{3^{3n/4}}\right) = \sqrt{\frac{2\pi}{3}} n^{-1/2} 2^{n/2} 3^{-3n/4}$

The location of the critical point is $x^* = \arccos(1/\sqrt{3})$.
The value of the phase at $x^*$ is $\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{3n}}$.

The final answer is $\boxed{\sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}}$.