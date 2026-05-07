# Solution: ood_steepest (Steepest descent for mixed sin/cos integral)

## Problem
Compute the leading asymptotic behavior of 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$$
as $n \to \infty$ using the steepest descent method.

## Solution

### Phase function and critical point

Rewrite the integral in exponential form:
$$V(n) = \int_0^{\pi/2} e^{n \log(\sin x) + (n/2) \log(\cos x)} dx = \int_0^{\pi/2} e^{n f(x)} dx,$$
where the phase function is:
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x).$$

**Finding the critical point:** Compute $f'(x)$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{1}{2} \cdot \frac{\sin x}{\cos x} = \cot x - \frac{1}{2}\tan x.$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x \quad \Rightarrow \quad \frac{\cos^2 x}{\sin^2 x} = \frac{1}{2} \quad \Rightarrow \quad 2\cos^2 x = \sin^2 x.$$

Using $\sin^2 x + \cos^2 x = 1$:
$$2\cos^2 x = 1 - \cos^2 x \quad \Rightarrow \quad 3\cos^2 x = 1 \quad \Rightarrow \quad \cos x = \frac{1}{\sqrt{3}}.$$

Thus $\sin x = \sqrt{1 - 1/3} = \sqrt{2/3}$, and $\tan^2 x = 2$. The critical point is:
$$x^* = \arctan(\sqrt{2}).$$

### Phase value and second derivative

**Phase at the critical point:**
$$f(x^*) = \log(\sqrt{2/3}) + \frac{1}{2}\log(\sqrt{1/3}) = \frac{1}{2}\log(2/3) + \frac{1}{4}\log(1/3).$$

Simplify:
$$f(x^*) = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 + \frac{1}{4}(0 - \log 3) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3 = \frac{1}{2}\log\left(\frac{2}{3^{3/2}}\right).$$

**Second derivative:**
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$:
- $\csc^2 x^* = 1/\sin^2(x^*) = 1/(2/3) = 3/2$
- $\sec^2 x^* = 1/\cos^2(x^*) = 1/(1/3) = 3$

Thus:
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3.$$

### Laplace / steepest descent formula

For an integral $\int e^{n f(x)} dx$ with a critical point at $x^*$ in the interior:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}.$$

Substitute our values:
$$V(n) \sim \exp\left[\frac{n}{2}\log\left(\frac{2}{3^{3/2}}\right)\right] \sqrt{\frac{2\pi}{3n}}.$$

Simplify the exponential:
$$e^{n f(x^*)} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2} = 2^{n/2} \cdot 3^{-3n/4}.$$

### Final answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2}.}$$

Equivalently:
$$V(n) \sim \left(\sqrt{\frac{2}{3\sqrt{3}}}\right)^n \sqrt{\frac{2\pi}{3n}}.$$

**Verification of critical components:**
- Critical point: $\tan^2 x^* = 2$ ✓
- Phase value: $f(x^*) = \frac{1}{2}\log(2/(3\sqrt{3}))$ ✓
- Second derivative magnitude: $|f''(x^*)| = 3$ ✓
- Gaussian prefactor: $\sqrt{2\pi/(3n)}$ ✓
