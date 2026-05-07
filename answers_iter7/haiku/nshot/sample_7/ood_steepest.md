# Solution: ood_steepest (Asymptotic behavior via steepest descent)

## Problem
Compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$. Identify the critical point of the phase function, evaluate the phase there, and assemble the Gaussian-fluctuation prefactor.

## Solution

**Phase function and critical point.** Rewrite the integral in Laplace form:
$$V(n) = \int_0^{\pi/2} e^{f(x)} dx, \quad f(x) = n \log(\sin x) + \frac{n}{2} \log(\cos x)$$

The critical point satisfies $f'(x) = 0$:
$$f'(x) = n\left(\frac{\cos x}{\sin x} - \frac{1}{2}\frac{\sin x}{\cos x}\right) = n\left(\cot x - \frac{1}{2}\tan x\right)$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x \implies \frac{\cos^2 x}{\sin^2 x} = \frac{1}{2}\frac{\sin x}{\cos x}$$

Multiply by $\sin^2 x$:
$$\cos^2 x = \frac{1}{2}\sin x \cdot \sin x / (\cos x \cdot \sin x) = \frac{1}{2}\sin x \cdot (\sin x / \cos x)$$

Actually, let me redo: $\cot x - \frac{1}{2}\tan x = 0 \implies \frac{\cos x}{\sin x} = \frac{1}{2}\frac{\sin x}{\cos x}$.

Cross-multiply: $\cos^2 x = \frac{1}{2}\sin^2 x$, so $\tan^2 x = 2$, giving $\tan x = \sqrt{2}$ (positive in $(0, \pi/2)$).

From $\tan x = \sqrt{2}$:
- $\sin x = \frac{\sqrt{2}}{\sqrt{3}}$
- $\cos x = \frac{1}{\sqrt{3}}$

So $x^* = \arctan(\sqrt{2})$.

**Phase at critical point.**
$$f(x^*) = n \log\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{n}{2}\log\left(\frac{1}{\sqrt{3}}\right)$$
$$= n\left(\frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3\right) = n\left(\frac{1}{2}\log 2 - \frac{3}{4}\log 3\right)$$
$$= \frac{n}{2}\log(2 \cdot 3^{-3/2}) = \frac{n}{2}\log\left(\frac{2}{3\sqrt{3}}\right)$$

**Second derivative.** 
$$f''(x) = n\left(-\csc^2 x - \frac{1}{2}\sec^2 x\right)$$

At $x^*$ where $\sin x^* = \sqrt{2/3}$ and $\cos x^* = 1/\sqrt{3}$:
- $\csc^2 x^* = 3/2$
- $\sec^2 x^* = 3$

Thus:
$$f''(x^*) = n\left(-\frac{3}{2} - \frac{3}{2}\right) = -3n$$

**Laplace asymptotic formula.** For an integral $\int_a^b e^{f(x)} dx$ with $f$ having a critical point $x^*$ in the interior and $f''(x^*) < 0$:
$$\int_a^b e^{f(x)} dx \sim e^{f(x^*)} \sqrt{\frac{2\pi}{|f''(x^*)|}}$$

Applying this:
$$V(n) \sim \exp\left(\frac{n}{2}\log\left(\frac{2}{3\sqrt{3}}\right)\right) \sqrt{\frac{2\pi}{3n}}$$

$$= \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

Rewrite more explicitly. Note $\frac{2}{3\sqrt{3}} = \frac{2}{3^{3/2}} = \frac{2 \cdot 3^{-3/2}}{1}$, and:
$$\left(\frac{2}{3\sqrt{3}}\right)^{n/2} = 2^{n/2} \cdot 3^{-3n/4}$$

Thus:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2}}$$

Equivalently:
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

**Critical checks:**
- Critical point: $\tan^2 x^* = 2$. ✓
- Phase value: $f(x^*) = \frac{n}{2}\log(2/(3\sqrt{3}))$. ✓
- Second derivative: $|f''(x^*)| = 3n$. ✓
- Gaussian prefactor: $\sqrt{2\pi/(3n)}$. ✓
