# Solution: Steepest Descent for Non-Standard Wallis Integral

## Relevance Assessment

**Retrieved examples and their relevance:**

1. **ex_2_14_wallis (0.325)** — *Relevant, but different setup.* The Wallis example uses the phase $f(x) = \log(\sin x)$ over $[0, \pi/2]$ and applies steepest descent to the boundary ($x = \pi/2$). The current problem has a *mixed trigonometric power* $\log(\sin x) + \frac{1}{2}\log(\cos x)$ and an *interior critical point*. The methodology (exponential integral, phase function, Gaussian fluctuation prefactor) transfers directly, but the phase and critical-point location differ entirely.

2. **ex_2_20_morse (0.058)** — *Not applicable.* This is a Morse lemma problem on $\mathbb{R}^2$, not a steepest descent problem on $[0, \pi/2]$. Skip.

3. **ex_7_27_quartic_1pi (0.019)** — *Not applicable.* This is a perturbative QFT problem, not an asymptotic integral. Skip.

**Differences from Wallis:**
- Wallis has a boundary maximum; this problem has an interior critical point.
- Wallis uses a single-power exponent; this problem mixes $\sin^n$ and $\cos^{n/2}$ with distinct powers.
- Critical-point equation is different: Wallis has $f'(x) = \cot x = 0$ at $\pi/2$ (boundary); here $f'(x) = \cot x - \frac{1}{2}\tan x = 0$ at an interior point.

---

## Solution

### Step 1: Rewrite as exponential integral

The integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2}\, dx$ can be rewritten as:
$$V(n) = \int_0^{\pi/2} \exp\left[n \log(\sin x) + \frac{n}{2} \log(\cos x)\right] dx = \int_0^{\pi/2} e^{n f(x)}\, dx$$

where the phase function is:
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$$

As $n \to \infty$, the integral is dominated by the maximum of $f(x)$.

### Step 2: Find the critical point

Take the derivative:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2}\tan x$$

Set $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x$$
$$\frac{\cos^2 x}{\sin x \cos x} = \frac{\sin x}{2\cos x}$$
$$\frac{\cos x}{\sin x} = \frac{\sin x}{2\cos x}$$
$$2\cos^2 x = \sin^2 x$$
$$\tan^2 x = 2$$

Since $x \in (0, \pi/2)$, we have $\tan x = \sqrt{2}$, so $x^* = \arctan(\sqrt{2})$.

### Step 3: Evaluate $\sin x^*$ and $\cos x^*$

From $\tan x^* = \sqrt{2}$ and $\sin^2 x^* + \cos^2 x^* = 1$:
$$\sin^2 x^* = \frac{\tan^2 x^*}{1 + \tan^2 x^*} = \frac{2}{3} \quad \Rightarrow \quad \sin x^* = \sqrt{\frac{2}{3}}$$
$$\cos^2 x^* = \frac{1}{1 + \tan^2 x^*} = \frac{1}{3} \quad \Rightarrow \quad \cos x^* = \sqrt{\frac{1}{3}}$$

### Step 4: Evaluate $f(x^*)$

$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\sqrt{\frac{1}{3}} = \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3}$$
$$= \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

Equivalently:
$$f(x^*) = \frac{1}{2}\log\frac{2}{3^{3/2}} = \frac{1}{2}\log\frac{2}{3\sqrt{3}}$$

### Step 5: Compute the second derivative

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x = x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$$
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

Since $f''(x^*) < 0$, the critical point is indeed a maximum, confirming applicability of steepest descent.

### Step 6: Assemble the Gaussian prefactor

By steepest descent (Laplace method), near the maximum $x^*$:
$$V(n) \sim e^{nf(x^*)} \cdot \sqrt{\frac{2\pi}{n|f''(x^*)|}}\quad\text{(with appropriate phase adjustment)}$$

Substituting $|f''(x^*)| = 3$:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \exp\left[nf(x^*)\right]$$

### Step 7: Express in final form

$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}$$

The exponential factors can be rewritten as:
$$2^{n/2} \cdot 3^{-3n/4} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

---

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Equivalently:
$$\boxed{V(n) \sim 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}}$$

**Subchecks confirmed:** (1) Interior critical point $\tan^2 x^* = 2$ identified. (2) Phase value $f(x^*) = \frac{1}{2}\log(2/(3\sqrt{3}))$ computed. (3) Second derivative $|f''(x^*)| = 3$ verified. (4) Gaussian prefactor $\sqrt{2\pi/(3n)}$ assembled correctly.
