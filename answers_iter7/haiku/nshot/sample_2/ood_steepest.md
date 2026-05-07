# Solution: OOD Steepest Descent Problem

## Reasoning

I need to find the leading asymptotic behavior of $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$ using steepest descent.

**Step 1: Set up the steepest descent form.** Rewrite the integral as
$$V(n) = \int_0^{\pi/2} e^{n \log(\sin x) + (n/2)\log(\cos x)} dx = \int_0^{\pi/2} e^{n f(x)} dx,$$
where the phase function is
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x).$$

**Step 2: Find the critical point.** For steepest descent, find the interior critical point by setting $f'(x) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2}\tan x = 0.$$
Thus,
$$\cot x = \frac{1}{2}\tan x \implies \frac{\cos x}{\sin x} = \frac{1}{2}\cdot\frac{\sin x}{\cos x} \implies 2\cos^2 x = \sin^2 x.$$
Using $\sin^2 x + \cos^2 x = 1$:
$$2\cos^2 x = 1 - \cos^2 x \implies 3\cos^2 x = 1 \implies \cos^2 x = \frac{1}{3}, \quad \sin^2 x = \frac{2}{3}.$$
So $x_* = \arctan(\sqrt{2})$, with $\sin x_* = \sqrt{2/3}$ and $\cos x_* = \sqrt{1/3}$.

**Step 3: Evaluate the phase at the critical point.**
$$f(x_*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\sqrt{\frac{1}{3}} = \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3}.$$
Simplify:
$$f(x_*) = \frac{1}{2}(\log 2 - \log 3) + \frac{1}{4}(-\log 3) = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$
Equivalently,
$$f(x_*) = \frac{1}{2}\log\frac{2}{3^{3/2}} = \frac{1}{2}\log\frac{2}{3\sqrt{3}}.$$

**Step 4: Compute the second derivative.** The Gaussian prefactor requires $f''(x_*)$:
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$
At the critical point:
$$\csc^2 x_* = \frac{1}{\sin^2 x_*} = \frac{3}{2}, \quad \sec^2 x_* = \frac{1}{\cos^2 x_*} = 3.$$
Thus,
$$f''(x_*) = -\frac{3}{2} - \frac{1}{2} \cdot 3 = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 5: Assemble the Laplace/steepest descent approximation.** For large $n$:
$$V(n) \sim e^{n f(x_*)} \sqrt{\frac{2\pi}{n|f''(x_*)|}} = e^{n f(x_*)} \sqrt{\frac{2\pi}{3n}}.$$
Substituting $f(x_*)$:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot e^{n \cdot \frac{1}{2}\log(2/(3\sqrt{3}))} = \sqrt{\frac{2\pi}{3n}} \cdot \exp\left(\frac{n}{2}\log\frac{2}{3^{3/2}}\right).$$
Simplify the exponent:
$$\exp\left(\frac{n}{2}\log\frac{2}{3^{3/2}}\right) = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \frac{2^{n/2}}{3^{3n/4}}.$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \frac{2^{n/2}}{3^{3n/4}} = \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2}.}$$

Equivalently, $V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$ or
$$V(n) \sim \left(\frac{2\pi}{3n}\right)^{1/2} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

**Critical subchecks:**
- Critical point: $\tan^2 x_* = 2$ (equivalently $3\cos^2 x_* = 1$). ✓
- Phase at critical point: $f(x_*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$ or $\log(2/(3\sqrt{3}))/2$. ✓
- Second derivative magnitude: $|f''(x_*)| = 3$. ✓
- Gaussian prefactor: $\sqrt{2\pi/(3n)}$. ✓
