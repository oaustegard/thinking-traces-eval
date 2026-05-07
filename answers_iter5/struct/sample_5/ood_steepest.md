# OOD Steepest Descent: Mixed Sin/Cos Powers

## Relevance and Differences

**Retrieved Example 1:** Wallis formula (ex_2_14) – relevance 0.325  
The retrieved example uses pure $\sin^n x$ over $[0, \pi/2]$ with steepest descent applied at the **boundary** ($x = \pi/2$), where the phase $\log \sin x$ achieves its maximum. This is a classic case: substitute $x = \pi/2 - y$, expand near $y=0$, and extract $\sqrt{\pi/(2n)}$ behavior.

**The target problem differs fundamentally:**
- Integrand has **mixed powers**: $(\sin x)^n (\cos x)^{n/2}$, not a single power of one function.
- The phase function $f(x) = n \log \sin x + (n/2) \log \cos x$ has an **interior critical point**, not a boundary maximum.
- The problem explicitly asks for the critical point location $x^*$, the phase value $f(x^*)$, and the Hessian determinant $f''(x^*)$ — structural elements that Wallis bypasses by virtue of boundary behavior.

**Retrieved Examples 2 & 3** (Morse, Quartic-1PI) have much lower relevance (0.06, 0.02) and are not applicable here.

The Wallis example teaches the **method**: rewrite as exponential, find extrema of the phase, apply Gaussian asymptotics near the extremum. But the **setup** and **critical-point algebra** must be adapted to the interior critical point of the mixed-power integrand.

---

## Solution

### Step 1: Rewrite as exponential integral

$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx = \int_0^{\pi/2} \exp\bigl[n \log \sin x + \tfrac{n}{2} \log \cos x\bigr] dx$$

Define the **phase function**:
$$f(x) = \log \sin x + \tfrac{1}{2} \log \cos x$$

Then $V(n) = \int_0^{\pi/2} e^{n f(x)} \, dx$.

### Step 2: Locate the critical point

The integrand is largest where $f'(x) = 0$:
$$f'(x) = \cot x - \tfrac{1}{2} \tan x = \frac{\cos x}{\sin x} - \tfrac{1}{2} \frac{\sin x}{\cos x}$$

Set equal to zero:
$$\frac{\cos x}{\sin x} = \tfrac{1}{2} \frac{\sin x}{\cos x} \quad \Rightarrow \quad \frac{\cos^2 x}{\sin x \cos x} = \frac{\sin x}{2 \cos x}$$

Multiply both sides by $\sin x \cos x$:
$$\cos^2 x = \tfrac{1}{2} \sin^2 x \quad \Rightarrow \quad 2 \cos^2 x = \sin^2 x \quad \Rightarrow \quad \tan^2 x = 2$$

Thus $\tan x^* = \sqrt{2}$ (taking the positive root for $x^* \in (0, \pi/2)$).

**Find $\sin x^*$ and $\cos x^*$:**

From $\tan x^* = \sqrt{2}$, we have $\sin x^* / \cos x^* = \sqrt{2}$, so $\sin x^* = \sqrt{2} \cos x^*$.  
Using $\sin^2 x^* + \cos^2 x^* = 1$:
$$2 \cos^2 x^* + \cos^2 x^* = 1 \quad \Rightarrow \quad 3 \cos^2 x^* = 1 \quad \Rightarrow \quad \cos x^* = \frac{1}{\sqrt{3}}$$

$$\sin x^* = \sqrt{2} \cdot \frac{1}{\sqrt{3}} = \sqrt{\frac{2}{3}}$$

### Step 3: Evaluate the phase at the critical point

$$f(x^*) = \log \sqrt{\frac{2}{3}} + \tfrac{1}{2} \log \frac{1}{\sqrt{3}}$$
$$= \tfrac{1}{2} \log \frac{2}{3} - \tfrac{1}{4} \log 3$$
$$= \tfrac{1}{2} (\log 2 - \log 3) - \tfrac{1}{4} \log 3$$
$$= \tfrac{1}{2} \log 2 - \tfrac{1}{2} \log 3 - \tfrac{1}{4} \log 3$$
$$= \tfrac{1}{2} \log 2 - \tfrac{3}{4} \log 3$$

Alternatively, write as:
$$f(x^*) = \log \left(\frac{2}{3^{3/2}}\right)^{1/2} = \tfrac{1}{2} \log \frac{2}{3\sqrt{3}}$$

### Step 4: Compute the second derivative

$$f''(x) = \frac{d}{dx}\left(\cot x - \tfrac{1}{2}\tan x\right) = -\csc^2 x - \tfrac{1}{2} \sec^2 x$$

At $x = x^*$:
- $\sin x^* = \sqrt{2/3}$, so $\csc^2 x^* = 3/2$
- $\cos x^* = 1/\sqrt{3}$, so $\sec^2 x^* = 3$

$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

(Negative, confirming $x^*$ is a maximum.)

### Step 5: Apply Laplace/Gaussian asymptotics

Near $x = x^*$, the phase expands as:
$$n f(x) \approx n f(x^*) + \tfrac{1}{2} n f''(x^*) (x - x^*)^2 = n f(x^*) - \tfrac{3n}{2} (x - x^*)^2$$

The integral becomes:
$$V(n) \sim e^{n f(x^*)} \int_{-\infty}^{\infty} e^{-3n(x-x^*)^2/2} \, dx$$

Substitute $u = \sqrt{3n/2} \, (x - x^*)$:
$$\int e^{-u^2} \frac{du}{\sqrt{3n/2}} = \sqrt{\frac{\pi}{3n/2}} = \sqrt{\frac{2\pi}{3n}}$$

Therefore:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}}$$

### Step 6: Rewrite the exponential

$$e^{n f(x^*)} = e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} = e^{n \cdot \frac{1}{2}(\log 2 - \frac{3}{2}\log 3)}$$
$$= \left(e^{\log 2 - \frac{3}{2}\log 3}\right)^{n/2} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

---

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

**Key subchecks verified:**
1. ✓ Critical point: $\tan^2 x^* = 2$, giving $x^* = \arctan(\sqrt{2})$
2. ✓ Phase value: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$
3. ✓ Hessian: $|f''(x^*)| = 3$
4. ✓ Gaussian prefactor: $\sqrt{2\pi/(3n)}$
