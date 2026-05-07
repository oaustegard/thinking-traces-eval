# Solution: ood_steepest (Asymptotic of V(n) via steepest descent)

## Examples from retrieved traces

**Example 1: ex_2_14_wallis.md** — Computing W_n = ∫₀^{π/2} sin^n x dx using steepest descent by rewriting as ∫ e^{n log sin x} dx. Locates the maximum at the boundary x = π/2, substitutes x = π/2 - y to move the maximum to y = 0, expands log cos y near y = 0, and extracts the Gaussian leading asymptotic √(π/(2n)).

**Example 2: ex_2_20_morse.md** — Solving via explicit factorization and smooth square-root constructions. Demonstrates how to identify structure (here, products of smooth factors), apply Taylor expansion with integral remainder, and verify smoothness of derived functions.

**Example 3: ex_7_27_quartic_1pi.md** — Computing contributions order-by-order via Feynman diagrams, then combining them systematically. Shows careful tracking of exponents, prefactors, and symmetry factors in increasingly complex expressions.

## Solution

We compute the asymptotic behavior of V(n) = ∫₀^{π/2} (sin x)^n (cos x)^{n/2} dx as n → ∞.

**Step 1: Rewrite as Laplace integral.** Write
$$V(n) = \int_0^{\pi/2} e^{n \log(\sin x) + (n/2) \log(\cos x)} \, dx = \int_0^{\pi/2} e^{n f(x)} \, dx,$$
where $f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$.

**Step 2: Find the critical point.** Compute $f'(x) = \cot x - \frac{1}{2}\tan x$. Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x \implies \frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x} \implies 2\cos^2 x = \sin^2 x.$$

Thus $\tan^2 x = 2$, so $x^* = \arctan(\sqrt{2})$.

At this point: $\sin^2 x^* = 2/3$ and $\cos^2 x^* = 1/3$, giving $\sin x^* = \sqrt{2/3}$ and $\cos x^* = \sqrt{1/3}$.

**Step 3: Evaluate the phase at x\*.** 
$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\sqrt{\frac{1}{3}} = \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3} = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

Equivalently, $f(x^*) = \frac{1}{2}\log\frac{2}{3^{3/2}} = \frac{1}{2}\log\frac{2}{3\sqrt{3}}$.

**Step 4: Compute the second derivative.** 
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$: $\sin^2 x^* = 2/3 \implies \csc^2 x^* = 3/2$, and $\cos^2 x^* = 1/3 \implies \sec^2 x^* = 3$.

Thus $f''(x^*) = -3/2 - 3/2 = -3$.

**Step 5: Apply steepest descent formula.** For a Laplace integral with critical point x*, the leading asymptotic is
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}}.$$

Substitute $f(x^*) = \frac{1}{2}\log(2/3\sqrt{3})$:
$$e^{n f(x^*)} = e^{(n/2)\log(2/(3\sqrt{3}))} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2} = \left(\frac{2}{3^{3/2}}\right)^{n/2}.$$

**Step 6: Final assembly.**
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.}$$

Equivalently, grouping the exponents:
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}.$$

Or in fully simplified form:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot (2 \cdot 3^{-3/2})^{n/2} = \left(\frac{2\pi}{3n}\right)^{1/2} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$
