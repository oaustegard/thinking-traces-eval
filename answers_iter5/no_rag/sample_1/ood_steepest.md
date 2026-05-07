# Steepest Descent Analysis of V(n)

## Problem
Compute the leading asymptotic behavior of the integral 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$ using steepest descent / Laplace method.

## Solution

### Step 1: Reformulate as an exponential integral
Write the integrand in exponential form:
$$V(n) = \int_0^{\pi/2} \exp\left[n \log(\sin x) + \frac{n}{2} \log(\cos x)\right] dx$$

The phase function is:
$$f(x) = \log(\sin x) + \frac{1}{2} \log(\cos x)$$

So $V(n) = \int_0^{\pi/2} e^{n f(x)} dx$.

### Step 2: Find the critical point
To apply Laplace's method, find where $f'(x) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{1}{2} \cdot \frac{\sin x}{\cos x} = \cot x - \frac{1}{2}\tan x$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x$$
$$\frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x}$$
$$2\cos^2 x = \sin^2 x$$
$$\tan^2 x = 2$$

Since $x \in [0, \pi/2]$, we have $x^* = \arctan(\sqrt{2})$.

### Step 3: Evaluate sin and cos at x*
From $\tan^2 x^* = 2$:
- $\sec^2 x^* = 1 + \tan^2 x^* = 3 \Rightarrow \cos^2 x^* = 1/3 \Rightarrow \cos x^* = 1/\sqrt{3}$
- $\sin^2 x^* = 1 - 1/3 = 2/3 \Rightarrow \sin x^* = \sqrt{2/3}$

### Step 4: Evaluate the phase at x*
$$f(x^*) = \log(\sqrt{2/3}) + \frac{1}{2}\log(\sqrt{1/3})$$
$$= \frac{1}{2}\log(2/3) + \frac{1}{4}\log(1/3)$$
$$= \frac{1}{2}(\log 2 - \log 3) + \frac{1}{4}(-\log 3)$$
$$= \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

Equivalently: $f(x^*) = \frac{1}{2}\log(2/(3\sqrt{3}))$

### Step 5: Compute the second derivative
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x^*$:
- $\csc^2 x^* = 1/\sin^2 x^* = 3/2$
- $\sec^2 x^* = 3$

Therefore:
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

The magnitude is $|f''(x^*)| = 3$.

### Step 6: Apply Laplace's method
The leading asymptotic is:
$$V(n) \sim \exp[n f(x^*)] \sqrt{\frac{2\pi}{n |f''(x^*)|}}$$

$$V(n) \sim \exp\left[n\left(\frac{1}{2}\log 2 - \frac{3}{4}\log 3\right)\right] \sqrt{\frac{2\pi}{3n}}$$

$$V(n) \sim 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}$$

### Step 7: Simplify the exponential part
$$2^{n/2} \cdot 3^{-3n/4} = \left(2 \cdot 3^{-3/2}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Equivalently: $V(n) \sim (2\pi/(3n))^{1/2} \cdot 2^{n/2} \cdot 3^{-3n/4}$

**Key identifications:**
- Critical point: $x^* = \arctan(\sqrt{2})$ with $\tan^2 x^* = 2$
- Phase at critical point: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$
- Second derivative: $f''(x^*) = -3$, so $|f''(x^*)| = 3$
- Gaussian prefactor: $\sqrt{2\pi/(3n)}$
