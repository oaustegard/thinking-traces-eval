To compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$, we will use the Laplace method (a specific case of the steepest descent method for real integrals).

**1. Rewrite the integrand in the form $e^{n \phi(x)}$:**
The integral can be written as:
$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x)} e^{\frac{n}{2} \ln(\cos x)} dx$
$V(n) = \int_0^{\pi/2} e^{n \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)} dx$
So, the phase function is $\phi(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.

**2. Identify the location $x^*$ of the critical point of the phase function:**
The critical point $x^*$ is where $\phi'(x^*) = 0$.
First, compute the first derivative of $\phi(x)$:
$\phi'(x) = \frac{d}{dx} \left( \ln(\sin x) + \frac{1}{2} \ln(\cos x) \right)$
$\phi'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$\phi'(x) = \cot x - \frac{1}{2} \tan x$

Set $\phi'(x^*) = 0$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\cot x^* = \frac{1}{2} \tan x^*$
$\frac{1}{\tan x^*} = \frac{1}{2} \tan x^*$
$2 = (\tan x^*)^2$
$\tan x^* = \pm \sqrt{2}$

Since the integration range is $x \in [0, \pi/2]$, both $\sin x$ and $\cos x$ are positive, meaning $\tan x$ must be positive.
Therefore, $\tan x^* = \sqrt{2}$.
This implies $x^* = \arctan(\sqrt{2})$. This critical point is in the interval $(0, \pi/2)$.

**3. Evaluate the phase at $x^*$ and the second derivative at $x^*$:**
To confirm $x^*$ is a maximum and to assemble the prefactor, we need $\phi(x^*)$ and $\phi''(x^*)$.

From $\tan x^* = \sqrt{2}$, we can construct a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$. The hypotenuse is $\sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{3}$.
So, $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$.

Now, evaluate $\phi(x^*)$:
$\phi(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$\phi(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$\phi(x^*) = \left(\frac{1}{2}\ln 2 - \frac{1}{2}\ln 3\right) + \frac{1}{2} \left(-\frac{1}{2}\ln 3\right)$
$\phi(x^*) = \frac{1}{2}\ln 2 - \frac{1}{2}\ln 3 - \frac{1}{4}\ln 3$
$\phi(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$

Next, compute the second derivative $\phi''(x)$:
$\phi''(x) = \frac{d}{dx} (\cot x - \frac{1}{2} \tan x)$
$\phi''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Evaluate $\phi''(x^*)$:
From $\tan x^* = \sqrt{2}$:
$\sec^2 x^* = 1 + \tan^2 x^* = 1 + (\sqrt{2})^2 = 1 + 2 = 3$.
$\csc^2 x^* = 1 + \cot^2 x^* = 1 + (1/\sqrt{2})^2 = 1 + 1/2 = 3/2$.
So, $\phi''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$.
Since $\phi''(x^*) = -3 < 0$, $x^*$ is indeed a maximum, which is necessary for the Laplace method.

**4. Assemble the Gaussian-fluctuation prefactor and the leading asymptotic behavior:**
The leading asymptotic behavior of an integral of the form $\int_a^b e^{n \phi(x)} dx$ with a single interior maximum $x^*$ is given by Laplace's formula:
$V(n) \sim e^{n \phi(x^*)} \sqrt{\frac{2\pi}{n |\phi''(x^*)|}}$ as $n \to \infty$.

Substitute the values we found:
$V(n) \sim e^{n \left(\frac{1}{2}\ln 2 - \frac{3}{4}\ln 3\right)} \sqrt{\frac{2\pi}{n |-3|}}$
$V(n) \sim e^{n \ln(2^{1/2})} e^{n \ln(3^{-3/4})} \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim (2^{1/2})^n (3^{-3/4})^n \sqrt{\frac{2\pi}{3n}}$
$V(n) \sim \frac{2^{n/2}}{3^{3n/4}} \sqrt{\frac{2\pi}{3n}}$

This can be further simplified:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2^{1/2}}{3^{3/4}}\right)^n$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{\sqrt[4]{27}}\right)^n$

The location of the critical point is $x^* = \arctan(\sqrt{2})$.
The phase at the critical point is $\phi(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4}\ln 3$.
The Gaussian-fluctuation prefactor is $\sqrt{\frac{2\pi}{n |\phi''(x^*)|}} = \sqrt{\frac{2\pi}{3n}}$.

The leading asymptotic behavior is:
$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{\sqrt[4]{27}}\right)^n}$