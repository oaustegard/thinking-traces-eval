To compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, we will use the Laplace method (a specific case of the steepest descent method for real exponents).

First, we rewrite the integrand in the form $e^{n f(x)}$:
$V(n) = \int_0^{\pi/2} \exp\left( \ln\left((\sin x)^n (\cos x)^{n/2}\right) \right) dx$
$V(n) = \int_0^{\pi/2} \exp\left( n \ln(\sin x) + \frac{n}{2} \ln(\cos x) \right) dx$
Thus, the phase function is $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

The Laplace method states that the leading asymptotic behavior of an integral of the form $\int_a^b e^{n f(x)} dx$ as $n \to \infty$ is dominated by the maximum of $f(x)$. If $f(x)$ has a unique global maximum at $x^*$ within the interval $(a,b)$, and $f''(x^*) < 0$, then:
$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}}$

We proceed with the following steps:

1.  **Find the critical point $x^*$**:
    We need to find $x^*$ such that $f'(x^*) = 0$.
    $f'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
    $f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
    $f'(x) = \cot x - \frac{1}{2} \tan x$

    Setting $f'(x^*) = 0$:
    $\cot x^* - \frac{1}{2} \tan x^* = 0$
    $\cot x^* = \frac{1}{2} \tan x^*$
    $\frac{1}{\tan x^*} = \frac{1}{2} \tan x^*$
    $2 = (\tan x^*)^2$
    $\tan x^* = \pm \sqrt{2}$

    Since the integration interval is $x \in [0, \pi/2]$, $\sin x > 0$ and $\cos x > 0$, implying $\tan x > 0$. Therefore, we choose the positive root:
    $\tan x^* = \sqrt{2}$
    The location of the critical point is $x^* = \arctan(\sqrt{2})$. This point is within the interval $(0, \pi/2)$.

2.  **Evaluate the phase function at $x^*$**:
    To evaluate $f(x^*)$, we need $\sin x^*$ and $\cos x^*$. From $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{3}$.
    So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

    Now, substitute these into $f(x^*)$:
    $f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
    $f(x^*) = \left(\frac{1}{2}\ln 2 - \frac{1}{2}\ln 3\right) + \frac{1}{2} \left(-\frac{1}{2}\ln 3\right)$
    $f(x^*) = \frac{1}{2}\ln 2 - \frac{1}{2}\ln 3 - \frac{1}{4}\ln 3$
    $f(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$

3.  **Compute the second derivative $f''(x^*)$**:
    $f''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
    $f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

    Evaluate at $x^*$:
    $\csc^2 x^* = \left(\frac{\sqrt{3}}{\sqrt{2}}\right)^2 = \frac{3}{2}$
    $\sec^2 x^* = \left(\frac{\sqrt{3}}{1}\right)^2 = 3$
    $f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3)$
    $f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$

    Since $f''(x^*) = -3 < 0$, $x^*$ is indeed a maximum.

4.  **Assemble the Gaussian-fluctuation prefactor and the final asymptotic behavior**:
    Using the Laplace method formula:
    $V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}}$
    $V(n) \sim \exp\left( n \left(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3\right) \right) \sqrt{\frac{2\pi}{n|-3|}}$
    $V(n) \sim \exp\left( \ln\left(2^{n/2}\right) - \ln\left(3^{3n/4}\right) \right) \sqrt{\frac{2\pi}{3n}}$
    $V(n) \sim \frac{2^{n/2}}{3^{3n/4}} \sqrt{\frac{2\pi}{3n}}$

This is the leading asymptotic behavior of the integral.

The final answer is $\boxed{V(n) \sim \frac{2^{n/2}}{3^{3n/4}} \sqrt{\frac{2\pi}{3n}}}$