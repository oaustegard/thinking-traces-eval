# Solution: Steepest Descent Applied to V(n)

## Problem Statement
Compute the leading asymptotic behavior of:
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$ using steepest descent/Laplace method. Find the critical point $x^*$, evaluate the phase function, and construct the Gaussian prefactor.

## Solution

### Step 1: Identify the Phase Function
For large $n$, the integral is dominated by the maximum of the integrand. We rewrite:
$$V(n) = \int_0^{\pi/2} \exp[n \log(\sin x) + \frac{n}{2} \log(\cos x)] \, dx = \int_0^{\pi/2} e^{n f(x)} \, dx$$

where the phase function is:
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$$

### Step 2: Find the Critical Point
The critical point $x^*$ satisfies $f'(x) = 0$:
$$f'(x) = \cot x - \frac{1}{2}\tan x = 0$$

$$\cot x = \frac{1}{2}\tan x$$

$$\frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x}$$

$$2\cos^2 x = \sin^2 x$$

$$\tan^2 x = 2$$

Thus $\tan x^* = \sqrt{2}$ (taking the positive root in $(0, \pi/2)$).

From $\tan x^* = \sqrt{2}$:
- $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}} = \sqrt{\frac{2}{3}}$
- $\cos x^* = \frac{1}{\sqrt{3}} = \sqrt{\frac{1}{3}}$

### Step 3: Evaluate the Phase at the Critical Point
$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\sqrt{\frac{1}{3}}$$

$$= \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3}$$

$$= \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3$$

$$= \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

Equivalently: $f(x^*) = \frac{1}{2}\log\left(\frac{2}{3^{3/2}}\right) = \frac{1}{2}\log\left(\frac{2}{3\sqrt{3}}\right)$

### Step 4: Compute the Second Derivative
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x = x^*$:
- $\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{2/3} = \frac{3}{2}$
- $\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{1/3} = 3$

$$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$$

Thus $|f''(x^*)| = 3$.

### Step 5: Apply Laplace's Method
The leading asymptotic contribution is:
$$V(n) \sim e^{nf(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}}$$

$$= e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} \sqrt{\frac{2\pi}{3n}}$$

$$= 2^{n/2} \cdot 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}$$

$$= \left(\frac{2}{3^{3/2}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

Equivalently:
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

**Key values:**
- Critical point: $x^* = \arctan(\sqrt{2})$
- Phase value: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$
- Second derivative: $f''(x^*) = -3$
- Gaussian prefactor: $\sqrt{\frac{2\pi}{3n}}$
