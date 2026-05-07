To compute the leading asymptotic behavior of the integral $V(n)$ as $n \to \infty$, we will use the Laplace (or steepest descent) method. The integral is given by:
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$$

First, we rewrite the integrand in the form $e^{n f(x)}$:
$$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} dx = \int_0^{\pi/2} e^{n \left(\ln(\sin x) + \frac{1}{2} \ln(\cos x)\right)} dx$$
The phase function is $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

**1. Locate the critical point $x^*$**
The critical point $x^*$ is where the first derivative of the phase function is zero: $f'(x^*) = 0$.
$$f'(x) = \frac{d}{dx} \left(\ln(\sin x) + \frac{1}{2} \ln(\cos x)\right)$$
$$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x} = \cot x - \frac{1}{2} \tan x$$
Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2} \tan x$$
$$\frac{1}{\tan x} = \frac{1}{2} \tan x$$
$$\tan^2 x = 2$$
Since $x \in (0, \pi/2)$, $\tan x$ must be positive. Therefore, $\tan x = \sqrt{2}$.
The location of the critical point is $x^* = \arctan(\sqrt{2})$.

**2. Evaluate the phase at the critical point $x^*$**
To evaluate $f(x^*)$, we need $\sin x^*$ and $\cos x^*$. From $\tan x^* = \sqrt{2}$:
$\sin x^* = \frac{\sqrt{2}}{\sqrt{1^2 + (\sqrt{2})^2}} = \frac{\sqrt{2}}{\sqrt{3}}$
$\cos x^* = \frac{1}{\sqrt{1^2 + (\sqrt{2})^2}} = \frac{1}{\sqrt{3}}$
Now, substitute these into $f(x)$:
$$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$$
$$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$$
$$f(x^*) = \frac{1}{2}\ln\left(\frac{2}{3}\right) + \frac{1}{2} \cdot \frac{1}{2}\ln\left(\frac{1}{3}\right)$$
$$f(x^*) = \frac{1}{2}(\ln 2 - \ln 3) + \frac{1}{4}(-\ln 3)$$
$$f(x^*) = \frac{1}{2}\ln 2 - \frac{1}{2}\ln 3 - \frac{1}{4}\ln 3$$
$$f(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$$
This can be written as $f(x^*) = \ln(2^{1/2} \cdot 3^{-3/4})$.

**3. Evaluate the second derivative of the phase at $x^*$**
We need $f''(x^*)$ to determine if $x^*$ is a maximum and to compute the Gaussian prefactor.
$$f''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$$
$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$$
At $x^*$, we use $\sin^2 x^* = (\sqrt{2}/\sqrt{3})^2 = 2/3$ and $\cos^2 x^* = (1/\sqrt{3})^2 = 1/3$:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{2/3} = 3/2$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{1/3} = 3$
Substitute these values into $f''(x)$:
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$$
Since $f''(x^*) = -3 < 0$, $x^*$ is indeed a maximum, which is required for the Laplace method.

**4. Assemble the Gaussian-fluctuation prefactor and the leading asymptotic behavior**
The Laplace method states that for an integral of the form $\int_a^b e^{n f(x)} dx$, the leading asymptotic behavior as $n \to \infty$ is given by:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{-n f''(x^*)}}$$
Substitute the values we found for $f(x^*)$ and $f''(x^*)$:
$$V(n) \sim e^{n \left(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3\right)} \sqrt{\frac{2\pi}{-n(-3)}}$$
$$V(n) \sim e^{\ln(2^{1/2} 3^{-3/4})^n} \sqrt{\frac{2\pi}{3n}}$$
$$V(n) \sim \left(2^{1/2} 3^{-3/4}\right)^n \sqrt{\frac{2\pi}{3n}}$$
$$V(n) \sim \frac{2^{n/2}}{3^{3n/4}} \sqrt{\frac{2\pi}{3n}}$$

The location of the critical point is $x^* = \arctan(\sqrt{2})$.
The value of the phase function at the critical point is $f(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{3n}}$.

The final answer is $\boxed{V(n) \sim \frac{2^{n/2}}{3^{3n/4}} \sqrt{\frac{2\pi}{3n}}}$