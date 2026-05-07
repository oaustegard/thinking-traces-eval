# OOD Steepest Descent: Asymptotic of Mixed sin/cos Integral

## Problem
Compute the leading asymptotic behavior of 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$$
as $n \to \infty$ using steepest descent (Laplace's method).

## Solution

### Step 1: Reformulate as Exponential Integral
Rewrite the integral by extracting the exponential:
$$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x) + (n/2) \ln(\cos x)} dx = \int_0^{\pi/2} e^{n f(x)} dx$$

where the phase function is:
$$f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$$

### Step 2: Find the Critical Point
For large $n$, the integral is dominated by the maximum of $f(x)$. Compute:
$$f'(x) = \cot x - \frac{1}{2} \tan x$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2} \tan x$$
$$\frac{\cos x}{\sin x} = \frac{1}{2} \frac{\sin x}{\cos x}$$
$$2 \cos^2 x = \sin^2 x$$
$$\tan^2 x = 2$$

Thus $\tan x^* = \sqrt{2}$, giving:
$$\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}, \quad \cos x^* = \frac{1}{\sqrt{3}}$$

### Step 3: Evaluate the Phase at the Critical Point
$$f(x^*) = \ln\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \ln\left(\sqrt{\frac{1}{3}}\right)$$
$$= \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{4} \ln\left(\frac{1}{3}\right)$$
$$= \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$$
$$= \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$$

### Step 4: Compute the Second Derivative
$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$$

At $x^*$ with $\sin^2 x^* = 2/3$ and $\cos^2 x^* = 1/3$:
$$\csc^2 x^* = \frac{3}{2}, \quad \sec^2 x^* = 3$$
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

### Step 5: Apply Laplace's Method
The asymptotic expansion is:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}$$
$$= e^{n(1/2 \ln 2 - 3/4 \ln 3)} \sqrt{\frac{2\pi}{3n}}$$
$$= 2^{n/2} \cdot 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}$$

This can be rewritten as:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

## Critical Subchecks

1. ✓ Critical point equation: $\tan^2 x^* = 2$
2. ✓ Phase value: $f(x^*) = \frac{1}{2}\ln 2 - \frac{3}{4} \ln 3$
3. ✓ Second derivative: $|f''(x^*)| = 3$
4. ✓ Gaussian prefactor: $\sqrt{\frac{2\pi}{3n}}$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

Or equivalently:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$
