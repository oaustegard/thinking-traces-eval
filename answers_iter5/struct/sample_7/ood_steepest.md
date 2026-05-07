# Solution: Steepest Descent for Mixed Trigonometric Integral

## Relevance Assessment

**Retrieved examples:**
1. **ex_2_14_wallis** (relevance 0.32): Steepest descent applied to $\int_0^{\pi/2} \sin^n x\, dx$ with phase function $f(x) = \log\sin x$ achieving maximum at the boundary.
2. **ex_2_20_morse** (relevance 0.058): Morse lemma and local coordinates—not directly applicable to this integral problem.
3. **ex_7_27_quartic_1pi** (relevance 0.019): Perturbative QFT 2-point function—not relevant.

**Key difference from Wallis:** The target problem $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ has an **interior critical point**, not a boundary maximum. The mixed exponents create a new phase function $f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$. Wallis treated only $\sin x$ terms; we must handle coupled competition between sine and cosine factors.

---

## Solution

### Step 1: Identify the Phase Function

Rewrite the integral in exponential form:
$$V(n) = \int_0^{\pi/2} e^{n f(x)} dx, \quad f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$$

This is distinct from Wallis, where only $\log(\sin x)$ appeared.

### Step 2: Locate the Critical Point

Compute the derivative of the phase:
$$f'(x) = \cot x - \frac{1}{2}\tan x = \frac{\cos^2 x}{\sin x} - \frac{\sin x}{2\cos x}$$

Setting $f'(x) = 0$:
$$\frac{\cos^2 x}{\sin x} = \frac{\sin x}{2\cos x}$$
$$2\cos^3 x = \sin^2 x$$
$$2\cos^3 x = 1 - \cos^2 x$$
$$2\cos^3 x + \cos^2 x - 1 = 0$$

Alternatively, multiply $\cot x = \frac{1}{2}\tan x$ by $\sin x \cos x$:
$$\cos^2 x = \frac{1}{2}\sin^2 x$$
$$\tan^2 x = 2$$

Thus $x^* = \arctan(\sqrt{2})$, which lies in $(0, \pi/2)$—a genuine interior critical point, **unlike Wallis**.

### Step 3: Evaluate Phase and Its Second Derivative at $x^*$

From $\tan x^* = \sqrt{2}$:
- $\sin^2 x^* = \frac{2}{3}$, so $\sin x^* = \sqrt{2/3}$
- $\cos^2 x^* = \frac{1}{3}$, so $\cos x^* = \sqrt{1/3}$

Phase value:
$$f(x^*) = \log\sqrt{2/3} + \frac{1}{2}\log\sqrt{1/3} = \frac{1}{2}\log(2/3) + \frac{1}{4}\log(1/3)$$
$$= \frac{1}{2}(\log 2 - \log 3) + \frac{1}{4}(-\log 3) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

Equivalently, $f(x^*) = \frac{1}{2}\log(2/3^{3/2})$.

Second derivative:
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x^*$:
- $\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}$
- $\sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$

Thus:
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

### Step 4: Assemble the Gaussian Prefactor

By Laplace's method, the leading asymptotic is:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}}$$

Substituting $f(x^*)$:
$$V(n) \sim \exp\left[n\left(\frac{1}{2}\log 2 - \frac{3}{4}\log 3\right)\right] \sqrt{\frac{2\pi}{3n}}$$
$$= 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}$$

Rewrite the exponent:
$$2^{n/2} \cdot 3^{-3n/4} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

### Step 5: Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Alternatively:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

**Verification checklist:**
- ✓ Interior critical point identified: $\tan^2 x^* = 2$
- ✓ Phase value computed: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$
- ✓ Second derivative magnitude: $|f''(x^*)| = 3$
- ✓ Gaussian prefactor assembled: $\sqrt{2\pi/(3n)}$

---

## Key Distinction from Retrieved Examples

The Wallis example (ex_2_14) maximized the phase at the boundary ($x = \pi/2$); this problem features an **interior saddle point** due to the competing $\sin^n$ and $\cos^{n/2}$ factors. The method is identical (Laplace asymptotic), but the geometry is fundamentally different—a critical point rather than boundary behavior.
