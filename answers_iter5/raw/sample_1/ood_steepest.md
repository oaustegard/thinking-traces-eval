# Raw-trace RAG: OOD Steepest Descent Problem

## Relevance Assessment

**Trace 1 (ex_2_14_wallis):** Relevant with strong caveats. The Wallis integral $W_n = \int_0^{\pi/2} \sin^n x \, dx$ is transformed into exponential form $\int_0^{\pi/2} e^{n\log\sin x} dx$ and solved via steepest descent. The *method* — rewriting the integral exponentially, identifying the phase function, locating the critical point, computing the second derivative, and assembling the Gaussian prefactor — is directly applicable. **However,** the Wallis phase $f(x) = \log\sin x$ has its maximum at the *boundary* $x = \pi/2$, not an interior critical point, which makes the asymptotics different from the OOD problem.

**Trace 2 (ex_2_20_morse):** Irrelevant. This is a local coordinate transformation problem for a cubic potential $f(x,y) = a(y) + b(y)x + c(y)x^2 + d(y)x^3$, aimed at diagonalizing via Morse lemma. It uses no asymptotic analysis or saddle-point methods. The cubic is a structural element, not a phase function.

**Trace 3 (ex_7_27_quartic):** Irrelevant. This is a Feynman-diagram computation of 1-loop and 2-loop self-energy diagrams for a quartic oscillator. While it involves expansions in the coupling $g$ and perturbative orders, it is field-theoretic and diagram-combinatorial, not asymptotic analysis of integrals.

## Differences from Trace 1

The retrieved Wallis example exhibits these critical differences from the OOD problem:

1. **Phase function location:** Wallis has $f(x) = \log\sin x$ with maximum at the *boundary* $x = \pi/2$. The OOD problem has $f(x) = \log(\sin x) + \tfrac{1}{2}\log(\cos x)$ with maximum at an *interior critical point* where $f'(x) = 0$.

2. **Critical point structure:** In Wallis, steepest descent becomes a boundary-layer analysis. In the OOD problem, the critical point is interior and the Laplace approximation applies classically.

3. **Mixed powers:** The OOD integral involves both $(\sin x)^n$ and $(\cos x)^{n/2}$ — a non-standard mixed power. Wallis uses only $(\sin x)^n$, corresponding to a single logarithmic term in the phase.

4. **Asymptotic form:** Wallis concludes with $W_n \sim \sqrt{\pi/(2n)}$ (pure Gaussian, no exponential prefactor). The OOD problem asks for the full leading asymptotic including the exponential factor from the phase evaluated at the critical point.

## Solution

**Phase function and critical point.**

The integrand is $(sin x)^n (\cos x)^{n/2}$. Write:
$$V(n) = \int_0^{\pi/2} e^{n[\log\sin x + \tfrac{1}{2}\log\cos x]} dx = \int_0^{\pi/2} e^{n f(x)} dx,$$
where $f(x) = \log(\sin x) + \tfrac{1}{2}\log(\cos x)$.

Setting $f'(x) = 0$:
$$f'(x) = \cot x - \tfrac{1}{2}\tan x = 0 \implies \cot x = \tfrac{1}{2}\tan x.$$

Multiply by $\sin x \cos x$:
$$\cos^2 x = \tfrac{1}{2}\sin^2 x \implies 2\cos^2 x = \sin^2 x \implies \tan^2 x = 2.$$

So $\tan x_* = \sqrt{2}$, giving:
$$\sin x_* = \frac{\sqrt{2}}{\sqrt{3}}, \quad \cos x_* = \frac{1}{\sqrt{3}}.$$

(From $\sin^2 x + \cos^2 x = 1$ and $\sin^2 x = 2\cos^2 x$, we get $3\cos^2 x = 1$, so $\cos x_* = 1/\sqrt{3}$ and $\sin x_* = \sqrt{2/3}$.)

**Phase at critical point.**

$$f(x_*) = \log(\sqrt{2/3}) + \tfrac{1}{2}\log(1/\sqrt{3}) = \tfrac{1}{2}\log(2/3) - \tfrac{1}{4}\log 3 = \tfrac{1}{2}[\log 2 - \log 3 - \tfrac{1}{2}\log 3] = \tfrac{1}{2}[\log 2 - \tfrac{3}{2}\log 3].$$

Equivalently, $f(x_*) = \tfrac{1}{2}\log(2/3^{3/2}) = \tfrac{1}{2}\log(2/(3\sqrt{3}))$.

**Second derivative.**

$$f''(x) = -\csc^2 x - \tfrac{1}{2}\sec^2 x.$$

At $x_*$ where $\sin x_* = \sqrt{2/3}$ and $\cos x_* = 1/\sqrt{3}$:
$$\csc^2 x_* = \frac{3}{2}, \quad \sec^2 x_* = 3.$$

Thus:
$$f''(x_*) = -\tfrac{3}{2} - \tfrac{3}{2} = -3.$$

**Laplace approximation.**

$$V(n) \sim e^{n f(x_*)} \sqrt{\frac{2\pi}{n|f''(x_*)|}} = e^{n \cdot \tfrac{1}{2}\log(2/(3\sqrt{3}))} \sqrt{\frac{2\pi}{3n}}.$$

Simplify the exponential:
$$e^{n \cdot \tfrac{1}{2}\log(2/(3\sqrt{3}))} = (2/(3\sqrt{3}))^{n/2} = 2^{n/2} / (3\sqrt{3})^{n/2} = 2^{n/2} \cdot 3^{-n/2} \cdot 3^{-n/4} = (2/3)^{n/2} \cdot 3^{-n/4}.$$

Wait: $3\sqrt{3} = 3^{3/2}$, so $(3^{3/2})^{n/2} = 3^{3n/4}$. Thus:
$$e^{n f(x_*)} = 2^{n/2} / 3^{3n/4}.$$

**Final asymptotic.**

$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2}.$$

Or in the form requested by the rubric:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

with critical checks: (1) $\tan^2 x_* = 2$ ✓, (2) $f(x_*) = \tfrac{1}{2}\log(2/(3\sqrt{3}))$ ✓, (3) $|f''(x_*)| = 3$ ✓, (4) Gaussian prefactor $\sqrt{2\pi/(3n)}$ ✓.
