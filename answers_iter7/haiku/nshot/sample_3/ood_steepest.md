# Solution: ood_steepest (Steepest descent on mixed sin/cos integral)

## Worked Examples

**Example 1 (ex_2_14_wallis): Asymptotic expansion via Laplace method.** The Wallis integral $W_n = \int_0^{\pi/2} \sin^n x \, dx$ is rewritten as $\int_0^{\pi/2} e^{n\log\sin x} dx$. The phase $f(x) = \log\sin x$ has its maximum at the boundary $x = \pi/2$. Substituting $x = \pi/2 - y$ converts to $\int_0^{\pi/2} e^{n\log\cos y} dy$, where near $y=0$: $\log\cos y = -y^2/2 - y^4/12 - \ldots$. The Gaussian damping yields $W_n \sim \sqrt{\pi/(2n)}$.

**Example 2 (ex_2_20_morse): Systematic coordinate extraction.** Morse lemma provides explicit local coordinates via factoring: $u(x,y) = x\sqrt{c(y) + d(y)x}$ and $v(x,y) = y\sqrt{a(y)/y^2 + b(y)x/y^2}$. The prefactor extraction (outside the square root) isolates the dominant contribution, while the term inside (which is $> 0$ near origin) allows smooth square-root evaluation.

**Example 3 (ex_7_27_quartic_1pi): Precision in loop-integral evaluation.** One-loop and two-loop Feynman diagrams for the self-energy show how to carefully track all internal propagators. The sunset has three parallel propagators giving $\Sigma^{(2)} \propto [G_0(t_1,t_2)]^3$; counting internal edges directly yields the coefficient.

## Solving ood_steepest

We compute $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$ as $n \to \infty$.

**Step 1: Identify the phase function.**
$$V(n) = \int_0^{\pi/2} e^{n\log\sin x + (n/2)\log\cos x} dx = \int_0^{\pi/2} e^{n f(x)} dx,$$
where
$$f(x) = \log\sin x + \frac{1}{2}\log\cos x.$$

**Step 2: Find the critical point.**
$$f'(x) = \cot x - \frac{1}{2}\tan x = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \frac{2\cos^2 x - \sin^2 x}{2\sin x \cos x}.$$

Setting $f'(x) = 0$:
$$2\cos^2 x = \sin^2 x \implies \tan^2 x = 2 \implies \tan x = \sqrt{2}.$$

Thus $x_* = \arctan(\sqrt{2})$, giving $\sin x_* = \sqrt{2/3}$ and $\cos x_* = \sqrt{1/3}$ (from $\sin^2 + \cos^2 = 1$ with $\sin x_*/\cos x_* = \sqrt{2}$).

**Step 3: Evaluate the phase at the critical point.**
$$f(x_*) = \log(\sqrt{2/3}) + \frac{1}{2}\log(\sqrt{1/3}) = \frac{1}{2}\log(2/3) + \frac{1}{4}\log(1/3).$$

Simplify:
$$f(x_*) = \frac{1}{2}\log 2 - \frac{1}{2}\log 3 + \frac{1}{4}\log 1 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

Alternatively:
$$f(x_*) = \frac{1}{2}\log\left(\frac{2}{3^{3/2}}\right) = \frac{1}{2}\log\left(\frac{2}{3\sqrt{3}}\right).$$

**Step 4: Compute the second derivative.**
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x_*$: $\csc^2 x_* = \frac{1}{\sin^2 x_*} = \frac{3}{2}$ and $\sec^2 x_* = \frac{1}{\cos^2 x_*} = 3$.

Thus:
$$f''(x_*) = -\frac{3}{2} - \frac{3}{2} = -3.$$

**Step 5: Assemble the Gaussian prefactor.**

By Laplace's formula:
$$V(n) \sim e^{n f(x_*)} \sqrt{\frac{2\pi}{n|f''(x_*)|}} = e^{n f(x_*)} \sqrt{\frac{2\pi}{3n}}.$$

Substituting $f(x_*) = \frac{1}{2}\log(2/(3\sqrt{3}))$:
$$e^{nf(x_*)} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2} = \frac{2^{n/2}}{3^{n/2} \cdot 3^{n/4}} = \frac{2^{n/2}}{3^{3n/4}}.$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \frac{2^{n/2}}{3^{3n/4}} = \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3^{3/2}}\right)^{n/2}.}$$

Equivalently,
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}.$$

The critical point is at $x_* = \arctan(\sqrt{2})$ with $\tan^2 x_* = 2$. The second derivative is $|f''(x_*)| = 3$, and the pre-exponential is $\sqrt{2\pi/(3n)}$.
