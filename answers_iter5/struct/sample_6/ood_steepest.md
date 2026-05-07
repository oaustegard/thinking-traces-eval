# Sample 6: OOD Steepest Descent Problem

## Relevance Assessment

**Retrieved examples:**
1. **ex_2_14_wallis** (relevance: 0.3246) — applies steepest descent to $W_n = \int_0^{\pi/2} \sin^n x\, dx$
2. **ex_2_20_morse** (relevance: 0.0576) — Morse coordinates for cubic critical points (topological, not asymptotics)
3. **ex_7_27_quartic_1pi** (relevance: 0.0186) — 1PI diagrams and loop integrals (field theory, not real analysis)

**Relevance and differences:**

The Wallis example is highly relevant: both involve steepest descent applied to integrals of the form $\int_0^{\pi/2} e^{n f(x)} dx$, and both require finding the critical point of the phase function $f(x) = \log(\text{integrand})$. However, the **target problem differs fundamentally** in structure:

- **Wallis:** $f(x) = \log(\sin x)$ is a single-variable phase with maximum at the boundary $x = \pi/2$.
- **Target:** $f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$ involves a *mixed power* and reaches its maximum at an **interior critical point** (not boundary).

The Morse and quartic examples are nearly irrelevant; Morse treats coordinate changes at critical points (not asymptotics), and the field theory integral is a different context entirely. The target problem requires pure applied analysis: steepest descent, no field theory machinery.

## Solution

The integral is
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx.$$

Rewrite in exponential form:
$$V(n) = \int_0^{\pi/2} e^{n \log(\sin x) + \frac{n}{2} \log(\cos x)} dx = \int_0^{\pi/2} e^{n f(x)} dx,$$

where the **phase function** is
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x).$$

**Step 1: Find the critical point.**

Compute the first derivative:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{1}{2} \cdot \frac{\sin x}{\cos x} = \cot x - \frac{1}{2}\tan x.$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x \implies \frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x} \implies 2\cos^2 x = \sin^2 x.$$

Thus $\tan^2 x = 2$, giving $\tan x = \sqrt{2}$ (since $x \in (0, \pi/2)$).

From $\tan x = \sqrt{2}$:
- $\sin^2 x = \frac{\tan^2 x}{1 + \tan^2 x} = \frac{2}{3}$, so $\sin x = \sqrt{2/3}$
- $\cos^2 x = \frac{1}{1 + \tan^2 x} = \frac{1}{3}$, so $\cos x = \sqrt{1/3}$

Thus $x^* = \arctan(\sqrt{2})$.

**Step 2: Evaluate the phase at the critical point.**

$$f(x^*) = \log(\sqrt{2/3}) + \frac{1}{2}\log(\sqrt{1/3}) = \frac{1}{2}\log(2/3) + \frac{1}{4}\log(1/3).$$

Simplify:
$$f(x^*) = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

Alternatively, write as a single exponent:
$$e^{f(x^*)} = 2^{1/2} \cdot 3^{-3/4} = \sqrt{2} \cdot 3^{-3/4}.$$

**Step 3: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$:
- $\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}$
- $\sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$

Thus
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2} \cdot 3 = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 4: Assemble the Gaussian prefactor and leading asymptotics.**

By Laplace's method, the integral is dominated by the neighborhood of $x^*$:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}.$$

Substitute:
$$V(n) \sim \sqrt{\frac{2\pi}{n \cdot 3}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \cdot (2 \cdot 3^{-3/2})^{n/2}.$$

Simplify the base:
$$2 \cdot 3^{-3/2} = 2 \cdot \frac{1}{3\sqrt{3}} = \frac{2}{3\sqrt{3}}.$$

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Equivalently, in exponential form:
$$V(n) \sim \left(\frac{2\pi}{3n}\right)^{1/2} \cdot e^{\frac{n}{2}(\log 2 - \frac{3}{2}\log 3)}.$$

Both forms capture the critical subchecks: identification of $\tan^2 x^* = 2$, phase value $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$, second derivative magnitude $|f''(x^*)| = 3$, and Gaussian prefactor $\sqrt{2\pi/(3n)}$.
