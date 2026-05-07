# n-shot solution: ood_steepest

Below are three worked examples. Study them, then solve the new problem in the same style.

## Example 1: ex_2_14_wallis

The integral $W_n = \int_0^{\pi/2} \sin^n x\, dx$ can be analyzed asymptotically by rewriting it as $\int_0^{\pi/2} e^{n\log\sin x} dx$. The phase $f(x) = \log\sin x$ achieves its maximum at the boundary $x = \pi/2$ (where $f = 0$). Shifting to $y = \pi/2 - x$ and using the expansion $\log\cos y = -y^2/2 - y^4/12 - \ldots$ shows that the integral is dominated by the $y \approx 0$ region. The leading Laplace-method approximation is $W_n \sim \sqrt{\pi/(2n)}$, which matches the exact recursion formula when properly normalized.

## Example 2: ex_2_20_morse

For a smooth function with specific vanishing properties, explicit local Morse coordinates can be constructed by identifying how the function decomposes into independent quadratic and higher-order terms. The key insight is to factor the x-dependence and the y-dependence separately: if $f = [x\sqrt{c(y) + d(y)x}]^2 + [y\sqrt{a(y)/y^2 + b(y)x/y^2}]^2$, then the Jacobian determinant shows that the map is a local diffeomorphism near the origin.

## Example 3: ex_7_27_quartic_1pi

Steepest descent and saddle-point methods depend on the location and structure of critical points. For the 1PI 2-point function, Feynman diagrams are evaluated in momentum (or in this case, time-domain) space by identifying the poles and endpoints where the phase achieves its extremum. The free propagator $G_0(t_1, t_2) = e^{-m|t_1-t_2|}/(2m)$ encodes the mass scale; when multiple propagators appear in series, as in the sunset diagram with three internal lines, the exponential factor becomes $e^{-3m|t_1-t_2|}$, showing that the effective mass is tripled.

## Now solve this problem:

Compute the leading asymptotic behavior of the integral $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$ using steepest descent / Laplace method. Identify the location $x^*$ of the critical point of the phase function, evaluate the phase at $x^*$, and assemble the Gaussian-fluctuation prefactor.

## Solution

**Step 1: Rewrite as a Laplace integral.**

We write the integrand in exponential form:
$$V(n) = \int_0^{\pi/2} e^{n\log\sin x + (n/2)\log\cos x} dx = \int_0^{\pi/2} e^{n f(x)} dx$$
where the "phase" (actually an action, since we have the large parameter $n$) is:
$$f(x) = \log\sin x + \frac{1}{2}\log\cos x.$$

**Step 2: Find the critical point.**

The critical point satisfies $f'(x) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2}\tan x.$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2}\tan x \implies \frac{\cos^2 x}{\sin^2 x} = \frac{\sin x}{2\cos x} \implies 2\cos^3 x = \sin^3 x.$$

Dividing: $\tan^3 x = 2$, so $\tan x = 2^{1/3}$. Wait, that's not the standard form. Let me recompute.

From $\cot x = \frac{1}{2}\tan x$:
$$\frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x} \implies 2\cos^2 x = \sin^2 x \implies \tan^2 x = 2.$$

So $\tan x^* = \sqrt{2}$, which means $x^* = \arctan(\sqrt{2})$.

**Step 3: Evaluate $f(x^*)$ and geometric quantities.**

From $\tan x^* = \sqrt{2}$, we can construct a right triangle: opposite $= \sqrt{2}$, adjacent $= 1$, hypotenuse $= \sqrt{3}$. Thus:
$$\sin x^* = \frac{\sqrt{2}}{\sqrt{3}} = \sqrt{\frac{2}{3}}, \quad \cos x^* = \frac{1}{\sqrt{3}} = \sqrt{\frac{1}{3}}.$$

Evaluating the phase:
$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\sqrt{\frac{1}{3}} = \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3}.$$

Simplifying:
$$f(x^*) = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3 = \log\frac{2^{1/2}}{3^{3/4}}.$$

Or in exponential form: $e^{f(x^*)} = \frac{\sqrt{2}}{3^{3/4}} = \frac{2^{1/2}}{3^{3/4}}$.

**Step 4: Compute the second derivative.**

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x = x^*$:
- $\csc^2 x^* = 1/\sin^2 x^* = 1/(2/3) = 3/2$.
- $\sec^2 x^* = 1/\cos^2 x^* = 1/(1/3) = 3$.

Thus:
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2} \cdot 3 = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 5: Laplace approximation.**

The leading asymptotic behavior is:
$$V(n) \sim e^{nf(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{nf(x^*)} \sqrt{\frac{2\pi}{3n}}.$$

Substituting the numerical values:
$$V(n) \sim \frac{2^{1/2}}{3^{3/4}} \cdot \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2^{1/2}}{3^{3/4}}\right)^n = \left(\frac{2^{1/2}}{3^{3/4}}\right)^n \sqrt{\frac{2\pi}{3n}}.$$

This can also be written as:
$$\boxed{V(n) \sim \frac{\sqrt{2\pi}}{(3n)^{1/2}} \cdot \left(\frac{2}{3^{3/2}}\right)^{n/2}.}$$

Or equivalently:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n.}$$

The critical point is $x^* = \arctan(\sqrt{2})$, the phase value is $f(x^*) = (1/2)\log(2/3^{3/2})$, and the Gaussian prefactor is $\sqrt{2\pi/(3n)}$.
