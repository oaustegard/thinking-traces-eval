# OOD Steepest Descent: Mixed Powers Integral

## Relevance Assessment

The retrieved examples share the *technique* of steepest descent (Laplace asymptotics) but diverge significantly in setup:

1. **ex_2_14_wallis (relevance 0.3246):** Classic Wallis integral $\int_0^{\pi/2} \sin^n x\, dx$ uses steepest descent at the *boundary* $x = \pi/2$. The phase function $f(x) = \log\sin x$ has its maximum at the boundary, requiring coordinate substitution $x = \pi/2 - y$ to linearize near the maximum. **Difference:** Wallis has a single integrand power; our problem has mixed powers $\sin^n x \cdot \cos^{n/2} x$, and the maximum lies in the interior (not boundary). This requires interior critical-point analysis.

2. **ex_2_20_morse (relevance 0.0576):** Morse lemma for coordinate transforms near non-degenerate critical points. While Morse theory underpins steepest descent, this example focuses on explicit coordinate changes for multivariable functions. **Difference:** Our phase is univariate; the critical-point structure is simpler.

3. **ex_7_27_quartic_1pi (relevance 0.0186):** Likely a different integral approximation problem with minimal relevance.

**Takeaway:** ex_2_14 is the closest guide (steepest descent mechanics), but its *boundary* maximum contrasts with our *interior* critical point. Use the Wallis framework (identify $f(x)$, find maximum, expand) but adapt to interior criticality.

---

## Solution

### Step 1: Identify the phase function

Rewrite the integral as:
$$V(n) = \int_0^{\pi/2} e^{n\log\sin x + \frac{n}{2}\log\cos x} dx = \int_0^{\pi/2} e^{n f(x)} dx$$

where the phase function is:
$$f(x) = \log\sin x + \frac{1}{2}\log\cos x$$

### Step 2: Locate the interior critical point

For steepest descent, find where $f'(x) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2}\tan x$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x$$

Multiply both sides by $\sin x \cos x$:
$$\cos^2 x = \frac{1}{2}\sin^2 x$$
$$2\cos^2 x = \sin^2 x$$
$$\tan^2 x = 2$$

Since $x \in (0, \pi/2)$, we have $\tan x > 0$, so:
$$x^* = \arctan(\sqrt{2})$$

From $\tan x^* = \sqrt{2}$, we deduce:
$$\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}, \quad \cos x^* = \frac{1}{\sqrt{3}}$$

### Step 3: Evaluate the phase at the critical point

$$f(x^*) = \log\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2}\log\left(\frac{1}{\sqrt{3}}\right)$$
$$= \frac{1}{2}\log\left(\frac{2}{3}\right) + \frac{1}{4}\log\left(\frac{1}{3}\right)$$
$$= \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3$$
$$= \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

Equivalently:
$$f(x^*) = \frac{1}{2}\log\left(\frac{2}{3^{3/2}}\right) = \frac{1}{2}\log\left(\frac{2}{3\sqrt{3}}\right)$$

### Step 4: Compute the second derivative

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$$
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2} \cdot 3 = -\frac{3}{2} - \frac{3}{2} = -3$$

### Step 5: Assemble the Gaussian prefactor and leading asymptotic

By Laplace's method:
$$V(n) \sim e^{nf(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{nf(x^*)} \sqrt{\frac{2\pi}{3n}}$$

Substitute $f(x^*)$:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \exp\left[n \left(\frac{1}{2}\log 2 - \frac{3}{4}\log 3\right)\right]$$
$$= \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}$$
$$= \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3^{3/2}}\right)^{n/2}$$
$$= \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

---

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

**Key differences from Wallis:** (1) Interior rather than boundary maximum requires solving $f'(x) = 0$ directly. (2) Mixed powers lead to a two-term phase function, not a single logarithm. (3) The critical point $x^* = \arctan(\sqrt{2})$ is transcendental, not a simple angle. (4) The prefactor $\sqrt{2\pi/(3n)}$ arises from the second derivative $|f''(x^*)| = 3$, distinct from Wallis's simpler geometry.
