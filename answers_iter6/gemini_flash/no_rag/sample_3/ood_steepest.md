The problem asks us to compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$ using the Laplace (or steepest descent) method.

The Laplace method is used for integrals of the form $\int_a^b e^{n f(x)} dx$. The dominant contribution to the integral as $n \to \infty$ comes from the neighborhood of the maximum of $f(x)$ within the integration interval.

**1. Identify the phase function $g(x)$**

First, we rewrite the integrand in the form $e^{n g(x)}$:
$V(n) = \int_0^{\pi/2} e^{\ln((\sin x)^n)} e^{\ln((\cos x)^{n/2})} dx$
$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} dx$
$V(n) = \int_0^{\pi/2} e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)} dx$

Thus, our phase function is $g(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
The integration interval is $[0, \pi/2]$. At the endpoints, $\sin x \to 0$ at $x=0$ and $\cos x \to 0$ at $x=\pi/2$. This means $g(x) \to -\infty$ at both boundaries, implying that the maximum of $g(x)$ must be in the interior of the interval $(0, \pi/2)$.

**2. Locate the critical point $x^*$**

To find the critical point $x^*$, we set the first derivative of $g(x)$ to zero:
$g'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$g'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$g'(x) = \cot x - \frac{1}{2} \tan x$

Setting $g'(x^*) = 0$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\cot x^* = \frac{1}{2} \tan x^*$
Using $\cot x = 1/\tan x$:
$\frac{1}{\tan x^*} = \frac{1}{2} \tan x^*$
$2 = \tan^2 x^*$
$\tan x^* = \pm \sqrt{2}$

Since $x^*$ must be in $(0, \pi/2)$, $\tan x^*$ must be positive. Therefore, the critical point is:
$x^* = \arctan(\sqrt{2})$

**3. Evaluate the phase function at $x^*$**

To evaluate $g(x^*)$, we need $\sin x^*$ and $\cos x^*$. If $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

Now, substitute these values into $g(x^*)$:
$g(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$g(x^*) = \left(\ln(\sqrt{2}) - \ln(\sqrt{3})\right) + \frac{1}{2} (-\ln(\sqrt{3}))$
$g(x^*) = \frac{1}{2}\ln 2 - \frac{1}{2}\ln 3 - \frac{1}{4}\ln 3$
$g(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$

This value will be part of the exponential factor $e^{n g(x^*)} = e^{n(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3)} = e^{\ln(2^{n/2})} e^{\ln(3^{-3n/4})} = \frac{2^{n/2}}{3^{3n/4}}$.

**4. Evaluate the second derivative of the phase function at $x^*$**

Next, we compute the second derivative $g''(x)$:
$g'(x) = \cot x - \frac{1}{2} \tan x$
$g''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Now, substitute $x^*$ into $g''(x)$. We have $\csc x^* = \frac{1}{\sin x^*} = \frac{\sqrt{3}}{\sqrt{2}}$ and $\sec x^* = \frac{1}{\cos x^*} = \sqrt{3}$.
$g''(x^*) = -\left(\frac{\sqrt{3}}{\sqrt{2}}\right)^2 - \frac{1}{2} (\sqrt{3})^2$
$g''(x^*) = -\frac{3}{2} - \frac{1}{2}(3)$
$g''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$

Since $g''(x^*) < 0$, $x^*$ is indeed a maximum, confirming it's the dominant contribution point.

**5. Assemble the Gaussian-fluctuation prefactor and the final asymptotic behavior**

The leading asymptotic behavior for an integral of the form $\int_a^b e^{n g(x)} dx$ with a single interior maximum at $x^*$ is given by the Laplace method formula:
$V(n) \sim \sqrt{\frac{2\pi}{n|g''(x^*)|}} e^{n g(x^*)}$ as $n \to \infty$.

Substitute the calculated values:
$|g''(x^*)| = |-3| = 3$
$e^{n g(x^*)} = \frac{2^{n/2}}{3^{3n/4}}$

Therefore, the leading asymptotic behavior of $V(n)$ is:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}$

This can also be written as:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left( \frac{\sqrt{2}}{3^{3/4}} \right)^n$

The final answer is $\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}}$