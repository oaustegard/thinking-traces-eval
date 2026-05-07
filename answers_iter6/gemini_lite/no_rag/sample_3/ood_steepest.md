We are asked to compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, using the steepest descent/Laplace method.

The integral is of the form $\int_a^b e^{n \phi(x)} dx$. To apply the steepest descent method, we first rewrite the integrand in this exponential form.
Let $f(x) = (\sin x)^n (\cos x)^{n/2}$.
We can write this as $f(x) = e^{n \ln(\sin x) + (n/2) \ln(\cos x)}$.
So, the integral is $V(n) = \int_0^{\pi/2} e^{n \left[ \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right]} dx$.

The phase function is $\phi(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
We need to find the critical point of $\phi(x)$ in the interval $[0, \pi/2]$. The critical point $x^*$ is where $\phi'(x^*) = 0$.

First, let's compute the derivative of $\phi(x)$:
$\phi'(x) = \frac{d}{dx} (\ln(\sin x) + \frac{1}{2} \ln(\cos x))$
$\phi'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$\phi'(x) = \cot x - \frac{1}{2} \tan x$.

Now, we set $\phi'(x^*) = 0$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\cot x^* = \frac{1}{2} \tan x^*$
$\frac{\cos x^*}{\sin x^*} = \frac{1}{2} \frac{\sin x^*}{\cos x^*}$
$2 \cos^2 x^* = \sin^2 x^*$.

We know that $\sin^2 x^* + \cos^2 x^* = 1$. Substituting $\sin^2 x^* = 2 \cos^2 x^*$:
$2 \cos^2 x^* + \cos^2 x^* = 1$
$3 \cos^2 x^* = 1$
$\cos^2 x^* = \frac{1}{3}$.

Since $x^*$ is in the interval $[0, \pi/2]$, $\cos x^* > 0$, so $\cos x^* = \frac{1}{\sqrt{3}}$.
Then $\sin^2 x^* = 1 - \cos^2 x^* = 1 - \frac{1}{3} = \frac{2}{3}$.
Since $x^*$ is in $[0, \pi/2]$, $\sin x^* > 0$, so $\sin x^* = \sqrt{\frac{2}{3}}$.

The location of the critical point is $x^* = \arccos\left(\frac{1}{\sqrt{3}}\right) = \arcsin\left(\sqrt{\frac{2}{3}}\right)$.
We need to check if this critical point is within the interval $[0, \pi/2]$. Since $\frac{1}{\sqrt{3}}$ is between 0 and 1, $x^*$ is indeed in $[0, \pi/2]$.

Next, we need to evaluate the phase function $\phi(x^*)$ at the critical point.
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\phi(x^*) = \ln\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{2} \left(-\frac{1}{2} \ln 3\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$.

Alternatively, using $\cos^2 x^* = 1/3$ and $\sin^2 x^* = 2/3$:
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\phi(x^*) = \frac{1}{2} \ln(\sin^2 x^*) + \frac{1}{4} \ln(\cos^2 x^*)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{4} \ln\left(\frac{1}{3}\right)$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) + \frac{1}{4} (-\ln 3)$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3 = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$.

The contribution from the phase at the critical point is $e^{n \phi(x^*)} = e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} = \left(\frac{2^{1/2}}{3^{3/4}}\right)^n$.

Now, we need to compute the second derivative of $\phi(x)$ to determine the Gaussian fluctuation prefactor.
$\phi'(x) = \cot x - \frac{1}{2} \tan x$.
$\phi''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
$\phi''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$.

Now evaluate $\phi''(x^*)$:
$\cos^2 x^* = 1/3 \implies \sec^2 x^* = 3$.
$\sin^2 x^* = 2/3 \implies \csc^2 x^* = 3/2$.

$\phi''(x^*) = -\frac{3}{2} - \frac{1}{2} (3) = -\frac{3}{2} - \frac{3}{2} = -3$.

The steepest descent approximation for the integral $V(n)$ is given by:
$V(n) \sim \sqrt{\frac{2\pi}{n |\phi''(x^*)|}} e^{n \phi(x^*)}$ as $n \to \infty$.

Substituting the values we found:
$V(n) \sim \sqrt{\frac{2\pi}{n |-3|}} e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(e^{\ln 2^{n/2}} e^{\ln 3^{-3n/4}}\right)$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}$.

Let's re-check the phase calculation.
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$.
$\sin x^* = \sqrt{2/3}$, $\cos x^* = 1/\sqrt{3}$.
$\phi(x^*) = \ln(\sqrt{2/3}) + \frac{1}{2} \ln(1/\sqrt{3})$
$\phi(x^*) = \frac{1}{2} \ln(2/3) + \frac{1}{2} (-\frac{1}{2} \ln 3)$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$. This is correct.

The prefactor is $\sqrt{\frac{2\pi}{n |\phi''(x^*)|}} = \sqrt{\frac{2\pi}{3n}}$.

So, the leading asymptotic behavior is:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2^{1/2}}{3^{3/4}}\right)^n$.

Final check of the question requirements:
- Location $x^*$ of the critical point: $\cos^2 x^* = 1/3$, $\sin^2 x^* = 2/3$.
- Evaluate the phase at $x^*$: $\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$.
- Assemble the Gaussian-fluctuation prefactor: $\sqrt{\frac{2\pi}{n |\phi''(x^*)|}} = \sqrt{\frac{2\pi}{3n}}$.

The integral can be written as $\int_0^{\pi/2} e^{n \phi(x)} dx$.
The dominant contribution comes from the maximum of $\phi(x)$. We found a maximum because $\phi''(x^*) < 0$.
The approximation is $\sqrt{\frac{2\pi}{n |\phi''(x^*)|}} e^{n \phi(x^*)}$.

$V(n) \sim \sqrt{\frac{2\pi}{3n}} e^{n(\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} e^{\ln(2^{n/2})} e^{\ln(3^{-3n/4})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}$.

The final answer is $\boxed{\sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}}$.