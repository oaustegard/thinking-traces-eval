To compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, we will use the Laplace method.

**1. Rewrite the integrand in the form $e^{n f(x)}$:**
The integrand can be expressed as an exponential function:
$(\sin x)^n (\cos x)^{n/2} = e^{\ln((\sin x)^n (\cos x)^{n/2})}$
$= e^{n \ln(\sin x) + \frac{n}{2} \ln(\cos x)}$
$= e^{n \left(\ln(\sin x) + \frac{1}{2} \ln(\cos x)\right)}$

Thus, we identify the phase function (or action) as $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
The integral is $V(n) = \int_0^{\pi/2} e^{n f(x)} dx$.

**2. Locate the critical point $x^*$:**
The Laplace method states that for large $n$, the integral is dominated by the maximum of $f(x)$. We find this maximum by setting the first derivative of $f(x)$ to zero.
$f'(x) = \frac{d}{dx} \left(\ln(\sin x) + \frac{1}{2} \ln(\cos x)\right)$
$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$f'(x) = \cot x - \frac{1}{2} \tan x$

Set $f'(x) = 0$ to find the critical point $x^*$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\cot x^* = \frac{1}{2} \tan x^*$
$\frac{1}{\tan x^*} = \frac{1}{2} \tan x^*$
$2 = \tan^2 x^*$
$\tan x^* = \pm \sqrt{2}$

Since the integration interval is $x \in [0, \pi/2]$, $\tan x$ must be positive. Therefore, the unique critical point in this interval is:
$x^* = \arctan(\sqrt{2})$

To evaluate $f(x^*)$ and $f''(x^*)$, we need the values of $\sin x^*$ and $\cos x^*$. If $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{2+1} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

**3. Evaluate the phase at the critical point $x^*$:**
$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$f(x^*) = \left(\ln(\sqrt{2}) - \ln(\sqrt{3})\right) + \frac{1}{2} \left(\ln(1) - \ln(\sqrt{3})\right)$
$f(x^*) = \left(\frac{1}{2}\ln 2 - \frac{1}{2}\ln 3\right) + \frac{1}{2} \left(0 - \frac{1}{2}\ln 3\right)$
$f(x^*) = \frac{1}{2}\ln 2 - \frac{1}{2}\ln 3 - \frac{1}{4}\ln 3$
$f(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$
This can also be written as $f(x^*) = \ln\left(2^{1/2}\right) - \ln\left(3^{3/4}\right) = \ln\left(\frac{\sqrt{2}}{3^{3/4}}\right)$.

**4. Evaluate the second derivative of the phase at the critical point $x^*$:**
$f''(x) = \frac{d}{dx} \left(\cot x - \frac{1}{2} \tan x\right)$
$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$
This expression is always negative for $x \in (0, \pi/2)$, confirming that $x^*$ is a maximum.

Now, substitute $x^*$ values:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{(\sqrt{2}/\sqrt{3})^2} = \frac{1}{2/3} = \frac{3}{2}$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{(1/\sqrt{3})^2} = \frac{1}{1/3} = 3$

$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3)$
$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$

**5. Assemble the Gaussian-fluctuation prefactor and the final asymptotic behavior:**
The Laplace approximation formula for an integral of the form $\int_a^b e^{n f(x)} dx$ with a single maximum at $x^*$ is:
$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}$ as $n \to \infty$.

Substitute the values of $f(x^*)$ and $f''(x^*)$:
$V(n) \sim e^{n \left(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3\right)} \sqrt{\frac{2\pi}{n |-3|}}$
$V(n) \sim e^{n \ln(2^{1/2})} e^{n \ln(3^{-3/4})} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim (2^{1/2})^n (3^{-3/4})^n \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim \left(\frac{2^{1/2}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}$

The term $2^{1/2}$ is $\sqrt{2}$, and $3^{3/4}$ is $\sqrt[4]{27}$.
$V(n) \sim \left(\frac{\sqrt{2}}{\sqrt[4]{27}}\right)^n \sqrt{\frac{2\pi}{3n}}$

The final answer is $\boxed{V(n) \sim \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}}$