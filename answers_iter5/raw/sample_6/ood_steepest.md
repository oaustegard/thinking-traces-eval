# Solution: OOD Steepest Descent Integral

## Relevance Assessment

**Retrieved traces:**
1. **ex_2_14_wallis** (relevance 0.32): *Highly relevant.* This trace solves a steepest descent problem for $W_n = \int_0^{\pi/2} \sin^n x\, dx$, establishing the general method of identifying boundary maxima, extracting the phase function, and computing the Gaussian prefactor. The framework (phase function $f(x) = \log(\sin x)$, finding critical points via $f'(x) = 0$, evaluating second derivatives) directly applies.

2. **ex_2_20_morse** (relevance 0.06): *Irrelevant.* This is a local coordinate problem for a Morse critical point of a multivariate function $f(x,y)$. While it involves analyzing critical points and Hessians, it addresses Morse theory and diffeomorphism, not asymptotic integrals.

3. **ex_7_27_quartic_1pi** (relevance 0.02): *Irrelevant.* This is a Feynman-diagram 1PI calculation for a quantum field theory problem with no connection to steepest descent asymptotics.

## Key Differences from Wallis Trace

The retrieved trace addresses $W_n = \int_0^{\pi/2} \sin^n x\, dx$ where the phase $f(x) = \log(\sin x)$ has a **boundary maximum** at $x = \pi/2$. The main problem instead presents:
$$V(n) = \int_0^{\pi/2} \sin^n x \cdot \cos^{n/2} x\, dx$$
with phase function $f(x) = \log(\sin x) + \tfrac{1}{2}\log(\cos x)$. This phase has a different **interior critical point**, not a boundary maximum, requiring direct steepest descent analysis rather than boundary asymptotics.

## Solution

**Step 1: Identify the phase and critical point.**

Write $V(n) = \int_0^{\pi/2} e^{n[\log(\sin x) + \tfrac{1}{2}\log(\cos x)]}\, dx$.

The phase function is:
$$f(x) = \log(\sin x) + \tfrac{1}{2}\log(\cos x).$$

To find the critical point $x^*$, compute:
$$f'(x) = \cot x - \tfrac{1}{2}\tan x = 0.$$

This gives:
$$\cot x = \tfrac{1}{2}\tan x \implies \frac{\cos x}{\sin x} = \tfrac{1}{2}\cdot\frac{\sin x}{\cos x}.$$

Cross-multiplying:
$$2\cos^2 x = \sin^2 x \implies \tan^2 x = 2.$$

Since $x \in (0, \pi/2)$, we have $\tan x = \sqrt{2}$, so:
$$x^* = \arctan(\sqrt{2}).$$

**Step 2: Find $\sin x^*$ and $\cos x^*$.**

From $\tan x^* = \sqrt{2}$:
$$\sin^2 x^* = \frac{2}{1+2} = \frac{2}{3}, \quad \cos^2 x^* = \frac{1}{3}.$$

Thus:
$$\sin x^* = \sqrt{\frac{2}{3}}, \quad \cos x^* = \sqrt{\frac{1}{3}}.$$

**Step 3: Evaluate the phase at the critical point.**

$$f(x^*) = \log\sqrt{\frac{2}{3}} + \tfrac{1}{2}\log\sqrt{\frac{1}{3}} = \tfrac{1}{2}\log\frac{2}{3} + \tfrac{1}{4}\log\frac{1}{3}.$$

Combining:
$$f(x^*) = \tfrac{1}{2}\log 2 - \tfrac{1}{2}\log 3 - \tfrac{1}{4}\log 3 = \tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3.$$

Equivalently:
$$f(x^*) = \tfrac{1}{2}\log\frac{2}{3^{3/2}} = \tfrac{1}{2}\log\frac{2}{3\sqrt{3}}.$$

**Step 4: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \tfrac{1}{2}\sec^2 x.$$

At $x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3.$$

Therefore:
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 5: Assemble the asymptotic expansion.**

By the steepest descent (Laplace) formula:
$$V(n) \sim e^{nf(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n[\tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3]} \sqrt{\frac{2\pi}{3n}}.$$

Simplifying the exponential:
$$e^{n[\tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3]} = 2^{n/2} \cdot 3^{-3n/4} = (2 \cdot 3^{-3/2})^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

**Final answer:**
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Equivalently, in factored form:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.}$$

The critical checks confirm: (1) $\tan^2 x^* = 2$ ✓, (2) $f(x^*) = \tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3$ ✓, (3) $|f''(x^*)| = 3$ ✓, (4) Gaussian prefactor $\sqrt{2\pi/(3n)}$ ✓.
