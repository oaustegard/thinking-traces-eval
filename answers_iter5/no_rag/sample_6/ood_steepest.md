# Steepest Descent Analysis of V(n)

## Problem Statement
Compute the leading asymptotic behavior of:
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$ using the steepest descent (Laplace) method.

## Solution

### Step 1: Rewrite as an Exponential Integral

Rewrite the integrand in exponential form:
$$V(n) = \int_0^{\pi/2} e^{n \ln(\sin x) + (n/2) \ln(\cos x)} \, dx = \int_0^{\pi/2} e^{n f(x)} \, dx$$

where the phase function is:
$$f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$$

### Step 2: Find the Critical Point

To apply Laplace's method, find where $f'(x) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2 \cos x} = \cot x - \frac{1}{2} \tan x$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2} \tan x$$

$$\frac{\cos x}{\sin x} = \frac{\sin x}{2 \cos x}$$

$$2 \cos^2 x = \sin^2 x$$

$$\tan^2 x = 2$$

Therefore: $x^* = \arctan(\sqrt{2})$.

At this critical point:
- $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}} = \sqrt{\frac{2}{3}}$ (from $\tan x^* = \sqrt{2}$, so $\sin^2 x^* = \frac{2}{3}$)
- $\cos x^* = \frac{1}{\sqrt{3}} = \sqrt{\frac{1}{3}}$

### Step 3: Evaluate the Phase at the Critical Point

$$f(x^*) = \ln\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \ln\left(\sqrt{\frac{1}{3}}\right)$$

$$= \frac{1}{2} \ln\left(\frac{2}{3}\right) + \frac{1}{4} \ln\left(\frac{1}{3}\right)$$

$$= \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 - \frac{1}{4} \ln 3$$

$$= \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3 = \frac{1}{2} \ln\left(\frac{2}{3^{3/2}}\right)$$

### Step 4: Compute the Second Derivative

$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$$

At $x^*$:
- $\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}$
- $\sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$

$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

### Step 5: Apply Laplace's Method

The leading asymptotic for $\int e^{nf(x)} dx$ is:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}$$

$$= \exp\left(n \left[\frac{1}{2} \ln 2 - \frac{3}{4} \ln 3\right]\right) \sqrt{\frac{2\pi}{3n}}$$

$$= \left(2^{1/2} \cdot 3^{-3/4}\right)^n \sqrt{\frac{2\pi}{3n}}$$

This can be rewritten as:
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

Or more explicitly:
$$V(n) \sim 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}$$

## Verification of Key Subchecks

1. **Critical point equation**: $\tan^2 x^* = 2$ ✓
2. **Phase value**: $f(x^*) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3$ ✓
3. **Second derivative**: $|f''(x^*)| = 3$ ✓
4. **Gaussian prefactor**: $\sqrt{\frac{2\pi}{3n}}$ ✓

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

Equivalently:
$$\boxed{V(n) \sim \left(\frac{2}{3^{3/2}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}}$$
