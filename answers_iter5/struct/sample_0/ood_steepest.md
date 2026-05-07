# Steepest Descent: Mixed sin/cos Power Integral

## Problem
Compute the leading asymptotic behavior of the integral 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$, using steepest descent / Laplace method. Identify the critical point $x^*$ of the phase function, evaluate the phase at $x^*$, and assemble the Gaussian-fluctuation prefactor.

## Retrieved Examples and Relevance

**Example 1 (ex_2_14_wallis)**: Wallis integral with $\sin^n x$ only. This is relevant because it uses steepest descent on a single-power trigonometric integral and demonstrates boundary-maximum identification, change of variables to shift the maximum to the origin, and Gaussian approximation. *Key difference*: Wallis has the maximum at the boundary $x = \pi/2$; our mixed integral may have an interior critical point, requiring different analysis.

**Example 2 (ex_2_20_morse)**: Morse lemma for a cubic polynomial with two variables. This is partially relevant in that it uses implicit-function techniques to extract local coordinates near a critical point, but it applies to smooth potentials in $\mathbb{R}^2$, not trigonometric integrals on a bounded interval. *Key difference*: We deal with a one-dimensional integral on $[0, \pi/2]$ with transcendental functions.

**Example 3 (ex_7_27_quartic_1pi)**: Quantum-field-theory 2-point function with a quartic potential. This is only marginally relevant; it demonstrates Feynman diagram summing but not the specific machinery of steepest descent for trigonometric integrals. *Key difference*: Entirely different domain and method (path integrals vs. real analysis).

The most useful example is **Example 1** (Wallis), which teaches the phase-function approach, but our problem is genuinely non-standard: we have a mixed $(\sin x)^n (\cos x)^{n/2}$ that creates an *interior* critical point, not a boundary maximum.

## Solution

**Step 1: Identify the phase function.**

Write 
$$V(n) = \int_0^{\pi/2} e^{n \log \sin x + (n/2) \log \cos x} \, dx = \int_0^{\pi/2} e^{n f(x)} \, dx,$$
where the phase (exponent per $n$) is 
$$f(x) = \log \sin x + \frac{1}{2} \log \cos x.$$

**Step 2: Find the critical point.**

Set $f'(x) = 0$:
$$f'(x) = \cot x - \frac{1}{2} \tan x = \frac{\cos x}{\sin x} - \frac{1}{2} \frac{\sin x}{\cos x} = 0.$$

Multiply by $\sin x \cos x$:
$$\cos^2 x - \frac{1}{2} \sin^2 x = 0 \implies \cos^2 x = \frac{1}{2} \sin^2 x \implies 2 \cos^2 x = \sin^2 x.$$

Using $\sin^2 x + \cos^2 x = 1$, substitute $\sin^2 x = 2 \cos^2 x$:
$$2 \cos^2 x + \cos^2 x = 1 \implies \cos^2 x = \frac{1}{3}, \quad \sin^2 x = \frac{2}{3}.$$

Therefore $\tan^2 x^* = 2$, and 
$$x^* = \arctan(\sqrt{2}), \quad \sin x^* = \sqrt{2/3}, \quad \cos x^* = \sqrt{1/3}.$$

**Step 3: Evaluate the phase at the critical point.**

$$f(x^*) = \log \sqrt{2/3} + \frac{1}{2} \log \sqrt{1/3} = \frac{1}{2} \log(2/3) + \frac{1}{4} \log(1/3).$$

Simplify:
$$f(x^*) = \frac{1}{2} \log 2 - \frac{1}{2} \log 3 + \frac{1}{4} \log 1 - \frac{1}{4} \log 3 = \frac{1}{2} \log 2 - \frac{3}{4} \log 3.$$

Equivalently,
$$e^{f(x^*)} = 2^{1/2} \cdot 3^{-3/4} = \sqrt{2} / (3\sqrt{3}) = \sqrt{2/27}.$$

**Step 4: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x.$$

At $x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3.$$

Therefore,
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 5: Apply Laplace's formula.**

For $\int_a^b e^{n f(x)} \, dx$ with an interior critical point $x^* \in (a,b)$ and $f''(x^*) < 0$ (confirming a maximum),
$$\int_a^b e^{n f(x)} \, dx \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}} \quad \text{as } n \to \infty.$$

Substitute:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}} = 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}.$$

Rewrite the exponential factors as a single base:
$$2^{n/2} \cdot 3^{-3n/4} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Equivalently, in component form:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.}$$

The critical checks are satisfied: 
1. $\tan^2 x^* = 2$ ✓
2. $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4} \log 3$ ✓
3. $|f''(x^*)| = 3$ ✓
4. Gaussian prefactor $\sqrt{2\pi/(3n)}$ ✓
