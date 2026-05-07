# Solution: ood_steepest (Asymptotic of mixed sin/cos power integral)

## Problem
Compute the leading asymptotic behavior of
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$$
as $n \to \infty$ using steepest descent/Laplace method.

## Solution

**Step 1: Rewrite as Laplace integral.**

Write the integrand in exponential form:
$$V(n) = \int_0^{\pi/2} e^{n \log(\sin x) + (n/2)\log(\cos x)} dx = \int_0^{\pi/2} e^{n f(x)} dx$$
where $f(x) = \log(\sin x) + \tfrac{1}{2}\log(\cos x)$.

**Step 2: Find the critical point.**

Take the derivative:
$$f'(x) = \cot x - \tfrac{1}{2}\tan x = \frac{\cos x}{\sin x} - \frac{1}{2}\frac{\sin x}{\cos x} = \frac{\cos^2 x - \frac{1}{2}\sin^2 x}{\sin x \cos x}.$$

Setting $f'(x) = 0$: $\cos^2 x = \tfrac{1}{2}\sin^2 x$, so $\tan^2 x = 2$, giving $x^* = \arctan(\sqrt{2})$.

**Step 3: Evaluate at the critical point.**

At $x^*$: $\tan x^* = \sqrt{2}$, so
$$\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}, \quad \cos x^* = \frac{1}{\sqrt{3}}.$$

The phase function value:
$$f(x^*) = \log\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \tfrac{1}{2}\log\left(\frac{1}{\sqrt{3}}\right) = \tfrac{1}{2}\log 2 - \tfrac{1}{2}\log 3 - \tfrac{1}{4}\log 3 = \tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3.$$

Equivalently: $f(x^*) = \tfrac{1}{2}\log(2/3^{3/2}) = \tfrac{1}{2}\log(2/(3\sqrt{3}))$.

**Step 4: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \tfrac{1}{2}\sec^2 x.$$

At $x^*$: $\csc^2 x^* = 3/2$, $\sec^2 x^* = 3$, so
$$f''(x^*) = -\tfrac{3}{2} - \tfrac{3}{2} = -3.$$

**Step 5: Apply Laplace formula.**

The Laplace/steepest descent formula gives
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n[\tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3]} \sqrt{\frac{2\pi}{3n}}.$$

Simplify the exponential:
$$e^{n[\tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3]} = 2^{n/2} \cdot 3^{-3n/4}.$$

**Step 6: Final form.**

$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

Factor out constant terms:
$$V(n) \sim \sqrt{\frac{2\pi}{3}} \cdot \frac{1}{\sqrt{n}} \cdot \left(\frac{2}{3^{3/2}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

Alternatively, grouping the $n$-dependence:
$$V(n) \sim \frac{1}{\sqrt{3n}} \sqrt{2\pi} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.}$$

**Key features verified:**
- Critical point: $x^* = \arctan(\sqrt{2})$ with $\tan^2 x^* = 2$ ✓
- Phase value: $f(x^*) = \tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3$ ✓
- Second derivative: $|f''(x^*)| = 3$ ✓
- Gaussian prefactor: $\sqrt{2\pi/(3n)}$ ✓
