We are asked to compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, using the steepest descent/Laplace method.

The integral is of the form $\int_a^b e^{n \phi(x)} dx$, where $n$ is a large parameter. To apply the steepest descent method, we need to rewrite the integrand in this exponential form.
Let $f(x) = (\sin x)^n (\cos x)^{n/2}$. We can write this as $e^{n \ln(\sin x) + \frac{n}{2} \ln(\cos x)}$.
So, the phase function is $\phi(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
The integral can be written as $V(n) = \int_0^{\pi/2} e^{n \phi(x)} dx$.

The steepest descent method requires finding the critical points of the phase function $\phi(x)$ within the interval of integration. We need to find $x^*$ such that $\phi'(x^*) = 0$.
First, let's compute the derivative of $\phi(x)$:
$\phi'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$\phi'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$\phi'(x) = \cot x - \frac{1}{2} \tan x$

Now, we set $\phi'(x^*) = 0$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\cot x^* = \frac{1}{2} \tan x^*$
$\frac{\cos x^*}{\sin x^*} = \frac{1}{2} \frac{\sin x^*}{\cos x^*}$
$2 \cos^2 x^* = \sin^2 x^*$

We know that $\sin^2 x^* + \cos^2 x^* = 1$. Substituting $\sin^2 x^* = 2 \cos^2 x^*$, we get:
$2 \cos^2 x^* + \cos^2 x^* = 1$
$3 \cos^2 x^* = 1$
$\cos^2 x^* = \frac{1}{3}$

Since $x$ is in the interval $[0, \pi/2]$, $\cos x^*$ must be positive.
So, $\cos x^* = \frac{1}{\sqrt{3}}$.
Then, $\sin^2 x^* = 1 - \cos^2 x^* = 1 - \frac{1}{3} = \frac{2}{3}$.
Since $x$ is in $[0, \pi/2]$, $\sin x^*$ is also positive, so $\sin x^* = \sqrt{\frac{2}{3}}$.

The critical point $x^*$ is such that $\cos x^* = 1/\sqrt{3}$ and $\sin x^* = \sqrt{2/3}$. This point lies within the interval $(0, \pi/2)$, as $\cos(\pi/2) = 0$ and $\cos(0) = 1$.

Next, we need to evaluate the phase at the critical point, $\phi(x^*)$:
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\phi(x^*) = \ln\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{2} \left(-\frac{1}{2} \ln 3\right)$
$\phi(x^*) = \frac{1}{2} \ln\left(\frac{2}{3}\right) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} (\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$
$\phi(x^*) = \ln(2^{1/2}) - \ln(3^{3/4}) = \ln\left(\frac{\sqrt{2}}{3^{3/4}}\right)$

Now, we need to compute the second derivative of $\phi(x)$ to determine the Gaussian-fluctuation prefactor.
$\phi'(x) = \cot x - \frac{1}{2} \tan x$
$\phi''(x) = \frac{d}{dx} (\cot x) - \frac{1}{2} \frac{d}{dx} (\tan x)$
$\phi''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Evaluate $\phi''(x^*)$:
$\phi''(x^*) = -\csc^2 x^* - \frac{1}{2} \sec^2 x^*$
We have $\sin x^* = \sqrt{2/3}$, so $\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{2/3} = \frac{3}{2}$.
We have $\cos x^* = 1/\sqrt{3}$, so $\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{1/3} = 3$.

$\phi''(x^*) = -\frac{3}{2} - \frac{1}{2} (3) = -\frac{3}{2} - \frac{3}{2} = -3$.

The leading asymptotic behavior of the integral is given by Laplace's method as:
$V(n) \sim \sqrt{\frac{2\pi}{n | \phi''(x^*) |}} e^{n \phi(x^*)}$

Substituting the values we found:
$V(n) \sim \sqrt{\frac{2\pi}{n |-3|}} e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} e^{n \ln(2^{1/2} 3^{-3/4})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(2^{1/2} 3^{-3/4}\right)^n$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}$

Let's check the value of $\phi(x^*)$ again.
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\sin x^* = \sqrt{2/3}$, $\cos x^* = 1/\sqrt{3}$
$\phi(x^*) = \ln(\sqrt{2/3}) + \frac{1}{2} \ln(1/\sqrt{3})$
$\phi(x^*) = \frac{1}{2} \ln(2/3) - \frac{1}{4} \ln(3)$
$\phi(x^*) = \frac{1}{2}(\ln 2 - \ln 3) - \frac{1}{4} \ln 3$
$\phi(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$

The asymptotic behavior is $e^{n \phi(x^*)} = e^{n(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3)} = (2^{1/2} 3^{-3/4})^n = 2^{n/2} 3^{-3n/4}$.

The full result is:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}$

We can rewrite $3^{-3n/4}$ as $(3^{-3/4})^n$.

Final check of calculations:
Phase function: $\phi(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
Derivative: $\phi'(x) = \cot x - \frac{1}{2} \tan x$.
Critical point: $\cot x^* = \frac{1}{2} \tan x^* \implies 2 \cos^2 x^* = \sin^2 x^*$.
$3 \cos^2 x^* = 1 \implies \cos x^* = 1/\sqrt{3}$, $\sin x^* = \sqrt{2/3}$.
Phase at critical point: $\phi(x^*) = \ln(\sqrt{2/3}) + \frac{1}{2} \ln(1/\sqrt{3}) = \frac{1}{2}\ln(2/3) - \frac{1}{4}\ln(3) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$.
Second derivative: $\phi''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$.
$\phi''(x^*) = -3/2 - \frac{1}{2}(3) = -3$.

The formula for Laplace's method is indeed $\sqrt{\frac{2\pi}{n | \phi''(x^*) |}} e^{n \phi(x^*)}$.

$V(n) \sim \sqrt{\frac{2\pi}{n |-3|}} e^{n (\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3)}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} e^{\ln(2^{n/2})} e^{\ln(3^{-3n/4})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}$

The location of the critical point is $x^* = \arccos(1/\sqrt{3})$.
The phase at $x^*$ is $\phi(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{n |\phi''(x^*)|}} = \sqrt{\frac{2\pi}{3n}}$.

The final answer is $\boxed{\sqrt{\frac{2\pi}{3n}} 2^{n/2} 3^{-3n/4}}$.