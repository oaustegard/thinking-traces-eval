The problem asks for the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, using the steepest descent / Laplace method.

**1. Identify the Phase Function**
First, we rewrite the integrand in the form $e^{n g(x)}$.
The integrand is $(\sin x)^n (\cos x)^{n/2}$.
$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} dx$
$V(n) = \int_0^{\pi/2} e^{n \left(\ln(\sin x) + \frac{1}{2} \ln(\cos x)\right)} dx$
So, the phase function is $g(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

**2. Locate the Critical Point $x^*$**
The critical point $x^*$ is where the first derivative of the phase function is zero, i.e., $g'(x^*) = 0$.
$g'(x) = \frac{d}{dx} \left(\ln(\sin x) + \frac{1}{2} \ln(\cos x)\right)$
$g'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$g'(x) = \cot x - \frac{1}{2} \tan x$

Set $g'(x) = 0$:
$\cot x - \frac{1}{2} \tan x = 0$
$\cot x = \frac{1}{2} \tan x$
$\frac{1}{\tan x} = \frac{1}{2} \tan x$
$2 = \tan^2 x$
Since $x \in (0, \pi/2)$, $\tan x$ must be positive. Therefore, $\tan x^* = \sqrt{2}$.
The critical point is $x^* = \arctan(\sqrt{2})$. This point lies within the integration interval $(0, \pi/2)$.

**3. Evaluate the Phase Function at $x^*$, $g(x^*)$**
To evaluate $g(x^*)$, we need $\sin x^*$ and $\cos x^*$. From $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{2+1} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

Now substitute these into $g(x)$:
$g(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$g(x^*) = \ln(\sqrt{2}) - \ln(\sqrt{3}) + \frac{1}{2} (-\ln(\sqrt{3}))$
$g(x^*) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$
$g(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$

**4. Evaluate the Second Derivative of the Phase Function at $x^*$, $g''(x^*)$**
We need to calculate $g''(x)$ to determine if $x^*$ is a maximum and to get the prefactor.
$g''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
$g''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Substitute $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{(\sqrt{2}/\sqrt{3})^2} = \frac{1}{2/3} = \frac{3}{2}$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{(1/\sqrt{3})^2} = \frac{1}{1/3} = 3$

$g''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$.
Since $g''(x^*) = -3 < 0$, $x^*$ is indeed a maximum.

**5. Assemble the Gaussian-Fluctuation Prefactor and Leading Asymptotic Behavior**
The leading asymptotic behavior of an integral of the form $\int_a^b e^{n g(x)} dx$ with a single interior maximum at $x^*$ is given by the Laplace method formula:
$V(n) \sim e^{n g(x^*)} \sqrt{\frac{2\pi}{n |g''(x^*)|}}$ as $n \to \infty$.

Substitute the values we found:
$e^{n g(x^*)} = e^{n (\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3)} = e^{\ln(2^{n/2})} e^{\ln(3^{-3n/4})} = 2^{n/2} 3^{-3n/4} = \left(\frac{2^{1/2}}{3^{3/4}}\right)^n = \left(\frac{\sqrt{2}}{\sqrt[4]{27}}\right)^n$.
The prefactor term is $\sqrt{\frac{2\pi}{n |g''(x^*)|}} = \sqrt{\frac{2\pi}{n \cdot 3}} = \sqrt{\frac{2\pi}{3n}}$.

Combining these, we get:
$V(n) \sim \left(\frac{\sqrt{2}}{\sqrt[4]{27}}\right)^n \sqrt{\frac{2\pi}{3n}}$
This can also be written as:
$V(n) \sim \left(\frac{2^{1/2}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim \left(\frac{2^{2/4}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim \left(\left(\frac{4}{27}\right)^{1/4}\right)^n \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim \left(\frac{4}{27}\right)^{n/4} \sqrt{\frac{2\pi}{3n}}$

The final answer is $\boxed{V(n) \sim \left(\frac{4}{27}\right)^{n/4} \sqrt{\frac{2\pi}{3n}}}$