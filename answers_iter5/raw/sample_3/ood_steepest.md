# Raw-trace RAG Answer: OOD Steepest Descent

## Relevance Assessment

**Trace 1 (ex_2_14_wallis): Relevance 0.32** — Moderately relevant. This trace applies steepest descent to $W_n = \int_0^{\pi/2} \sin^n x \, dx$ with phase function $f(x) = \log \sin x$. The phase has a boundary maximum (not an interior critical point), requiring a different asymptotic regime than the main problem. However, the *method* (reformulating as exponential, identifying the phase, analyzing critical points or boundary behavior, and assembling the Gaussian approximation) is directly applicable.

**Trace 2 (ex_2_20_morse): Relevance 0.06** — Minimal relevance. This trace concerns Morse coordinates and the Morse lemma (converting a function to sum-of-squares form near a critical point). While it involves critical-point structure, it does not employ steepest descent or asymptotic integration — it is a purely algebraic coordinate transformation. Irrelevant for the main problem.

**Trace 3 (ex_7_27_quartic_1pi): Relevance 0.02** — Negligible. No details provided in this session, but based on title this likely concerns a 1-loop calculation in a quartic theory, not steepest descent on classical integrals. Irrelevant.

**Key differences from Wallis trace:**
- **Phase function:** Wallis uses $f(x) = \log \sin x$, which is monotone increasing on $(0, \pi/2)$ with maximum at the boundary $x = \pi/2$. The main problem uses $f(x) = \log \sin x + \frac{1}{2} \log \cos x$, which is **interior-critical** (vanishing derivative at $x^* = \arctan(\sqrt{2})$ inside the domain).
- **Asymptotic regime:** Wallis boundary-dominates near $x = \pi/2$. The main problem has an interior saddle point, requiring full Laplace/steepest-descent expansion.
- **Coupling:** Wallis has power $n$ on a single function. The main problem couples two powers: $n$ on $\sin^n$ and $n/2$ on $\cos^{n/2}$, creating a mixed exponent in the phase.

---

## Solution

Let $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$. Rewrite as a Laplace integral:
$$V(n) = \int_0^{\pi/2} \exp\left[n \log \sin x + \frac{n}{2} \log \cos x\right] dx = \int_0^{\pi/2} e^{n f(x)} \, dx$$
where $f(x) = \log \sin x + \frac{1}{2} \log \cos x$.

**Step 1: Find the critical point.**

Set $f'(x) = 0$:
$$f'(x) = \cot x - \frac{1}{2} \tan x = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \frac{2\cos^2 x - \sin^2 x}{2 \sin x \cos x}.$$

Numerator zero: $2\cos^2 x = \sin^2 x$, so $\tan^2 x = 2$. Thus $\tan x^* = \sqrt{2}$ (taking the positive root in $(0, \pi/2)$).

From $\tan x^* = \sqrt{2}$, we have $\sin^2 x^* = \frac{2}{3}$ and $\cos^2 x^* = \frac{1}{3}$ (using $\sin^2 + \cos^2 = 1$ and $\tan^2 = \sin^2/\cos^2$). Thus $\sin x^* = \sqrt{2/3}$ and $\cos x^* = \sqrt{1/3}$.

**Step 2: Evaluate the phase at the critical point.**

$$f(x^*) = \log \sqrt{\frac{2}{3}} + \frac{1}{2} \log \sqrt{\frac{1}{3}} = \frac{1}{2} \log \frac{2}{3} + \frac{1}{4} \log \frac{1}{3} = \frac{1}{2} \log 2 - \frac{1}{2} \log 3 + \frac{1}{4} \log 1 - \frac{1}{4} \log 3$$
$$= \frac{1}{2} \log 2 - \frac{3}{4} \log 3 = \frac{1}{2} \log \frac{2}{3^{3/2}} = \frac{1}{2} \log \frac{2}{3\sqrt{3}}.$$

**Step 3: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x.$$

At $x = x^*$:
- $\csc^2 x^* = 1/\sin^2 x^* = 3/2$
- $\sec^2 x^* = 1/\cos^2 x^* = 3$

Thus $f''(x^*) = -3/2 - 3/2 = -3$.

**Step 4: Assemble the Laplace asymptotics.**

The standard form is:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}} = e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}}.$$

Substituting $f(x^*) = \frac{1}{2} \log \frac{2}{3\sqrt{3}}$:
$$e^{n f(x^*)} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2} = \frac{2^{n/2}}{3^{n/2} \cdot 3^{n/4}} = \frac{2^{n/2}}{3^{3n/4}}.$$

Thus:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}.}$$

Equivalently, $V(n) \sim \left(\frac{2}{3^{3/2}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$, or combining the exponential and polynomial prefactors: $V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$.

**Critical subchecks:**
- ✓ Identified $\tan^2 x^* = 2$ from the critical-point equation.
- ✓ Computed $f(x^*) = \frac{1}{2} \log 2 - \frac{3}{4} \log 3$.
- ✓ Computed $|f''(x^*)| = 3$.
- ✓ Assembled the Gaussian prefactor $\sqrt{2\pi / (3n)}$ with correct $n$-scaling.

The Wallis trace showed how to handle boundary-dominated asymptotics; here the interior critical point is the dominant contribution, and the method parallels theirs but with interior-point geometry.
