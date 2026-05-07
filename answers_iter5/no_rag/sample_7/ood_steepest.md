# OOD Steepest Descent: Asymptotic Expansion of V(n)

## Problem Statement
Compute the leading asymptotic behavior of 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$$
as $n \to \infty$ using the steepest descent (Laplace) method. Identify the critical point, evaluate the phase function, and compute the Gaussian prefactor.

## Solution

### Step 1: Rewrite the Integral in Exponential Form

To apply Laplace's method, we express the integrand in exponential form:
$$V(n) = \int_0^{\pi/2} \exp[n \log(\sin x) + \frac{n}{2} \log(\cos x)] dx = \int_0^{\pi/2} \exp[n f(x)] dx$$

where the phase function is:
$$f(x) = \log(\sin x) + \frac{1}{2} \log(\cos x)$$

### Step 2: Find the Critical Point

To locate the saddle point, compute $f'(x) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{1}{2} \cdot \frac{\sin x}{\cos x} = \cot x - \frac{1}{2}\tan x$$

Setting this equal to zero:
$$\cot x = \frac{1}{2}\tan x$$
$$\frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x}$$
$$2\cos^2 x = \sin^2 x$$
$$\tan^2 x = 2$$

Since $x \in (0, \pi/2)$, we have $\tan x = \sqrt{2}$, so:
$$x^* = \arctan(\sqrt{2})$$

### Step 3: Compute Values at the Critical Point

From $\tan x^* = \sqrt{2}$, we construct the unit circle relation:
- $\sin^2 x^* = \frac{\tan^2 x^*}{1 + \tan^2 x^*} = \frac{2}{3}$, so $\sin x^* = \sqrt{2/3}$
- $\cos^2 x^* = \frac{1}{1 + \tan^2 x^*} = \frac{1}{3}$, so $\cos x^* = \sqrt{1/3}$

Now evaluate $f(x^*)$:
$$f(x^*) = \log(\sqrt{2/3}) + \frac{1}{2}\log(\sqrt{1/3})$$
$$= \frac{1}{2}\log(2/3) + \frac{1}{4}\log(1/3)$$
$$= \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3$$
$$= \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

### Step 4: Compute the Second Derivative

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x = x^*$:
- $\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{2/3} = \frac{3}{2}$
- $\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{1/3} = 3$

Therefore:
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$$

### Step 5: Apply Laplace's Method

The standard Laplace formula for $\int e^{nf(x)} dx$ gives:
$$V(n) \sim e^{nf(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}}$$

Substituting our values:
$$V(n) \sim e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} \sqrt{\frac{2\pi}{3n}}$$

$$= 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}$$

This can be written equivalently as:
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

or factored as:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}}$$

**Critical checks:**
1. Critical point: $\tan^2 x^* = 2$ ✓
2. Phase at critical point: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$ ✓
3. Second derivative: $|f''(x^*)| = 3$ ✓
4. Gaussian prefactor: $\sqrt{\frac{2\pi}{3n}}$ ✓
