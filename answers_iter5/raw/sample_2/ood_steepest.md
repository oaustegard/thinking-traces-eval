# Raw-Trace RAG Answer: ood_steepest

**Problem.** Compute the leading asymptotic behavior of $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2}\,dx$ as $n\to\infty$ using steepest descent/Laplace method. Identify the critical point $x^*$, phase at $x^*$, and Gaussian-fluctuation prefactor.

## Relevance and Differences: Retrieved Traces

**Trace 1 (ex_2_14_wallis, relevance 0.3246):** Most relevant. Wallis integral $W_n = \int_0^{\pi/2}\sin^n x\,dx$ also uses steepest descent on a phase $f(x) = \log\sin x$. The method — rewriting as $e^{nf(x)}$, finding the critical point, evaluating phase and second derivative, assembling the Gaussian prefactor — is directly applicable. **Key difference:** Wallis has a boundary maximum at $x=\pi/2$, not an interior critical point. Our OOD problem has mixed powers $\sin^n \times \cos^{n/2}$, creating an interior critical point (tan$^2 x^* = 2$) distinct from Wallis.

**Trace 2 (ex_2_20_morse, relevance 0.0576):** Morse lemma on $f(x,y)$ near a critical point; constructs local coordinates. Low relevance — Morse theory is about local change-of-variables, not asymptotics of integrals. Not directly helpful.

**Trace 3 (ex_7_27_quartic_1pi, relevance 0.0186):** 1PI 2-point function via Feynman diagrams; focuses on perturbative expansion and symmetry factors. Nearly irrelevant to steepest descent on a classical integral. Ignore.

## Solution

**Step 1: Rewrite as an exponential integral.**

$$V(n) = \int_0^{\pi/2} e^{n\log\sin x + (n/2)\log\cos x}\,dx = \int_0^{\pi/2} e^{n f(x)}\,dx$$

where
$$f(x) = \log\sin x + \tfrac{1}{2}\log\cos x.$$

**Step 2: Find the interior critical point.**

$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \tfrac{1}{2}\tan x.$$

Setting $f'(x^*) = 0$:
$$\cot x^* = \tfrac{1}{2}\tan x^* \implies \frac{\cos x^*}{\sin x^*} = \tfrac{1}{2} \cdot \frac{\sin x^*}{\cos x^*}.$$

Multiply both sides by $\sin x^* \cos x^*$:
$$\cos^2 x^* = \tfrac{1}{2}\sin^2 x^* \implies 2\cos^2 x^* = \sin^2 x^* \implies \tan^2 x^* = 2.$$

Thus $\tan x^* = \sqrt{2}$ (taking the positive root in $(0, \pi/2)$).

From the identity $\sec^2 x = 1 + \tan^2 x$:
$$\cos^2 x^* = \frac{1}{1+\tan^2 x^*} = \frac{1}{3} \implies \cos x^* = \frac{1}{\sqrt{3}}.$$

And
$$\sin^2 x^* = 1 - \cos^2 x^* = \frac{2}{3} \implies \sin x^* = \sqrt{\frac{2}{3}}.$$

**Step 3: Evaluate phase at the critical point.**

$$f(x^*) = \log\sqrt{\tfrac{2}{3}} + \tfrac{1}{2}\log\tfrac{1}{\sqrt{3}} = \tfrac{1}{2}\log\tfrac{2}{3} - \tfrac{1}{4}\log 3 = \tfrac{1}{2}\log 2 - \tfrac{3}{4}\log 3.$$

Equivalently, $f(x^*) = \tfrac{1}{2}\log\bigl(\tfrac{2}{3^{3/2}}\bigr) = \tfrac{1}{2}\log\bigl(\tfrac{2}{3\sqrt{3}}\bigr)$.

**Step 4: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \tfrac{1}{2}\sec^2 x.$$

At $x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3.$$

Therefore
$$f''(x^*) = -\tfrac{3}{2} - \tfrac{3}{2} = -3.$$

**Step 5: Apply steepest descent.**

$$V(n) \sim e^{nf(x^*)}\sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)}\sqrt{\frac{2\pi}{3n}}.$$

Simplify the exponential:
$$e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} = 2^{n/2} \cdot 3^{-3n/4} = \left(\frac{2}{3^{3/2}}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

Combine:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

Equivalently, with the Gaussian factor written as $(2\pi/(3n))^{1/2}$:

$$\boxed{V(n) \sim \left(\frac{2\pi}{3n}\right)^{1/2} \cdot 2^{n/2} \cdot 3^{-3n/4}, \quad\text{or}\quad V(n) \sim \sqrt{\frac{2\pi}{3n}}\, \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.}$$

---

**Key subchecks satisfied:**
1. ✓ Identified $\tan^2 x^* = 2$ (equivalent to $2\cos^2 x^* = \sin^2 x^*$).
2. ✓ Computed $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$ (equivalently $\frac{1}{2}\log\bigl(\frac{2}{3\sqrt{3}}\bigr)$).
3. ✓ Computed $|f''(x^*)| = 3$.
4. ✓ Assembled Gaussian prefactor $\sqrt{2\pi/(3n)}$.
