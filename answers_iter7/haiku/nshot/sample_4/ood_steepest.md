# Solution: ood_steepest (Laplace/steepest descent on mixed sin/cos integral)

Below are three worked examples —

**Example 1: Etingof 2.14 (Wallis formula via steepest descent)** — applies Laplace's method to $W_n = \int_0^{\pi/2} \sin^n x \, dx$ by recognizing the phase $f(x) = \log \sin x$ has a boundary maximum, substituting $x = \pi/2 - y$ to shift the maximum to the lower limit, expanding $\log \cos y = -y^2/2 + O(y^4)$, and extracting the Gaussian prefactor $\sqrt{\pi/(2n)}$.

**Example 2: Etingof 2.20 (Morse coordinates for smooth functions with higher-order terms)** — shows how to identify the Hessian, apply local diffeomorphisms to isolate quadratic forms, and extract square-root factors from expressions involving fractional powers.

**Example 3: Etingof 7.27 (1PI diagrams and factorization)** — demonstrates the role of combinatorial symmetry factors in extracting leading-order asymptotics from complicated diagram weights.

---

Now solve: Compute the leading asymptotic behavior of $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$. Use steepest descent. Identify the critical point $x^*$, evaluate the phase at $x^*$, and assemble the Gaussian prefactor.

## Reasoning

**Phase function:** Write the integral as
$$V(n) = \int_0^{\pi/2} e^{n \log \sin x + (n/2) \log \cos x} dx = \int_0^{\pi/2} e^{n f(x)} dx,$$
where $f(x) = \log \sin x + \frac{1}{2}\log \cos x$.

**Finding the critical point:** To find $x^*$ where $f'(x^*) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{1}{2}\cdot\frac{\sin x}{\cos x} = \cot x - \frac{1}{2}\tan x.$$

Setting $f'(x^*) = 0$:
$$\cot x^* = \frac{1}{2}\tan x^* \implies 2\cos^2 x^* = \sin^2 x^* \implies \tan^2 x^* = 2 \implies x^* = \arctan(\sqrt{2}).$$

**Evaluating the phase at the critical point:**

At $x^* = \arctan(\sqrt{2})$, we have $\tan x^* = \sqrt{2}$, so
$$\sin^2 x^* = \frac{\tan^2 x^*}{1 + \tan^2 x^*} = \frac{2}{3}, \quad \cos^2 x^* = \frac{1}{3}.$$

Thus $\sin x^* = \sqrt{2/3}$ and $\cos x^* = \sqrt{1/3}$.

$$f(x^*) = \log \sqrt{\frac{2}{3}} + \frac{1}{2}\log \sqrt{\frac{1}{3}} = \frac{1}{2}\log \frac{2}{3} + \frac{1}{4}\log \frac{1}{3} = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

**Second derivative (curvature):**
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3.$$

Thus
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Gaussian prefactor:** By Laplace's method, the integral is dominated by $n \gg 1$ and we get
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}} = e^{n f(x^*)} \sqrt{\frac{2\pi}{3n}}.$$

**Assembling the full form:**
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} = \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

This can be rewritten as
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3^{3/2}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

Or in the form
$$V(n) \sim \left(\frac{2\pi}{3n}\right)^{1/2} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}, \quad x^* = \arctan(\sqrt{2}), \quad f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3, \quad |f''(x^*)| = 3.}$
