# OOD Steepest Descent: Mixed Trigonometric Integral

## Relevance and Differences

**Retrieved Example 1 (ex_2_14_wallis, relevance 0.32):** Applies steepest descent to $\int_0^{\pi/2} \sin^n x\, dx$, with phase function $f(x) = n\log\sin x$. The critical point lies at the boundary ($x = \pi/2$), requiring a change of variables $x = \pi/2 - y$ to move the maximum to the origin. The asymptotic formula uses a Gaussian integral with prefactor $\sqrt{\pi/(2n)}$.

*Key difference:* The current problem has a mixed power structure $\sin^n x \cdot \cos^{n/2} x$ with two independent exponents, so the phase function is $f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$ — no longer a single power of sine. The critical point will be interior (not at a boundary) and requires solving $f'(x) = 0$.

**Retrieved Example 2 (ex_2_20_morse, relevance 0.06):** Treats Morse theory and coordinate transformations for multivariable functions, emphasizing Hessian positivity and local diffeomorphism. While it demonstrates rigorous analysis of critical behavior, it addresses a different problem class (polynomial function on $\mathbb{R}^2$ rather than integral asymptotics).

*Difference:* Not directly applicable; included for completeness of method coverage.

**Retrieved Example 3 (ex_7_27_quartic_1pi, relevance 0.02):** A quantum field theory diagram calculation unrelated to classical asymptotics.

*Difference:* Irrelevant to this problem.

## Solution

The integral is
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2}\, dx.$$

**Step 1: Rewrite as exponential integral and identify phase.**

$$V(n) = \int_0^{\pi/2} \exp\left[n\log(\sin x) + \frac{n}{2}\log(\cos x)\right] dx = \int_0^{\pi/2} \exp[n \cdot f(x)]\, dx,$$

where
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x) = \log\bigl[\sin x \cdot (\cos x)^{1/2}\bigr].$$

**Step 2: Find the critical point.**

Differentiate:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2}\tan x.$$

Set $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x \implies \frac{\cos x}{\sin x} = \frac{\sin x}{2\cos x} \implies 2\cos^2 x = \sin^2 x.$$

Since $\sin^2 x + \cos^2 x = 1$:
$$2\cos^2 x = 1 - \cos^2 x \implies 3\cos^2 x = 1 \implies \cos x = \frac{1}{\sqrt{3}}, \quad \sin x = \sqrt{\frac{2}{3}}.$$

Thus $x^* = \arctan(\sqrt{2})$.

**Step 3: Evaluate phase and second derivative at the critical point.**

$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\frac{1}{3} = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{2}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

Alternatively: $f(x^*) = \frac{1}{2}\log\left(\frac{2}{3\sqrt{3}}\right) = \frac{1}{2}\log(2 \cdot 3^{-3/2})$.

For the second derivative:
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$ where $\sin^2 x^* = 2/3$ and $\cos^2 x^* = 1/3$:
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2} \cdot 3 = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 4: Assemble the Laplace asymptotic expansion.**

The standard formula gives:
$$V(n) \sim e^{n \cdot f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = \exp\left[n\left(\frac{1}{2}\log 2 - \frac{3}{4}\log 3\right)\right] \cdot \sqrt{\frac{2\pi}{3n}}.$$

Simplify the exponential:
$$\exp\left[\frac{n}{2}\log 2 - \frac{3n}{4}\log 3\right] = 2^{n/2} \cdot 3^{-3n/4} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

**Step 5: Final answer.**

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

Equivalently: $V(n) \sim \left(\frac{2\pi}{3n}\right)^{1/2} (2 \cdot 3^{-3/2})^{n/2}$.

The critical subchecks: (1) ✓ $\tan^2 x^* = 2$; (2) ✓ $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$; (3) ✓ $|f''(x^*)| = 3$; (4) ✓ Gaussian prefactor $\sqrt{2\pi/(3n)}$ correctly positioned.
