# Solution: OOD Steepest Descent (Mixed sin/cos integral)

## Relevance of Retrieved Traces

**Trace 1 (ex_2_14, Wallis formula).** HIGHLY RELEVANT. This trace demonstrates steepest descent / Laplace method applied to an integral of the form $\int_0^{\pi/2} e^{n\log\sin x}\,dx$, with phase function $f(x) = \log\sin x$ and systematic asymptotic expansion via the Laplace method. The technique—identifying critical points, evaluating the phase, computing the second derivative, assembling the Gaussian prefactor—is directly applicable.

**Trace 2 (ex_2_20, Morse coordinates).** MARGINALLY RELEVANT. This trace constructs explicit Morse coordinates for a non-degenerate critical point of a function $f(x,y)$. While it validates that a critical point is non-degenerate (via the Hessian), the focus is on explicit coordinate changes, not asymptotic expansion. It does not employ the Laplace method and does not compute leading asymptotics.

**Trace 3 (ex_7_27, 1PI 2-point function).** NOT RELEVANT. This trace is purely about Feynman diagrams, symmetry factors, and path integrals in quantum field theory. It contains no steepest descent or saddle-point analysis. It does not apply to the current integral problem.

## Key Differences from Wallis Trace

The Wallis integral has:
- Phase: $f(x) = \log\sin x$ only.
- Critical point location: at the **boundary** $x = \pi/2$ (the log sine is increasing on $(0,\pi/2)$).
- Asymptotic expansion around a boundary point.

The OOD problem has:
- Phase: $f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$ (mixed sin and cos powers).
- Critical point location: **interior** to $(0,\pi/2)$, found by solving $f'(x) = 0$.
- Asymptotic expansion around an interior saddle point.

## Solution

### Step 1: Identify the phase function and critical point

The integral is
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2}\,dx = \int_0^{\pi/2} e^{n[\log\sin x + \frac{1}{2}\log\cos x]}\,dx = \int_0^{\pi/2} e^{n f(x)}\,dx,$$
where
$$f(x) = \log\sin x + \frac{1}{2}\log\cos x.$$

The critical point $x^*$ satisfies
$$f'(x) = \cot x - \frac{1}{2}\tan x = 0.$$

Rewrite: $\frac{\cos x}{\sin x} - \frac{1}{2}\frac{\sin x}{\cos x} = 0$, so $\cos^2 x - \frac{1}{2}\sin^2 x = 0$ (after clearing denominators). Thus
$$2\cos^2 x = \sin^2 x \quad \Rightarrow \quad \tan^2 x = 2 \quad \Rightarrow \quad \tan x = \sqrt{2}.$$

(We take the positive root since $x \in (0, \pi/2)$.)

### Step 2: Evaluate the phase at the critical point

At $x^* = \arctan\sqrt{2}$:
- $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}}$ and $\cos x^* = \frac{1}{\sqrt{3}}$ (from $\sin^2 + \cos^2 = 1$ and $\tan x = \sqrt{2}$).

Then
$$f(x^*) = \log\frac{\sqrt{2}}{\sqrt{3}} + \frac{1}{2}\log\frac{1}{\sqrt{3}} = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

Equivalently, $f(x^*) = \frac{1}{2}\log\frac{2}{3^{3/2}} = \frac{1}{2}\log\frac{2}{3\sqrt{3}}$.

### Step 3: Compute the second derivative

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$: $\csc^2 x^* = 3/2$ (since $\sin x^* = \sqrt{2/3}$) and $\sec^2 x^* = 3$ (since $\cos x^* = \sqrt{1/3}$). Thus
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2} \cdot 3 = -\frac{3}{2} - \frac{3}{2} = -3.$$

### Step 4: Apply Laplace formula and assemble the Gaussian prefactor

By the Laplace method, the leading asymptotic of $V(n)$ is
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}}.$$

Substituting the values:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \exp\left[n \cdot \frac{1}{2}\log 2 - n \cdot \frac{3}{4}\log 3\right] = \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

This can be rewritten as:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3^{3/2}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.}$$

**Critical subchecks passed:**
- (1) Identified $\tan^2 x^* = 2$.
- (2) Computed $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$.
- (3) Computed $|f''(x^*)| = 3$.
- (4) Assembled Gaussian prefactor $\sqrt{\frac{2\pi}{3n}}$.
