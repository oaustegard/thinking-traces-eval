# n-shot solution: ood_1loop

Below are three worked examples. Study them, then solve the new problem in the same style.

## Example 1: ex_3_26_effective_action

For the action $S(x) = x^2/2 - gx^3/6$, the 1-loop effective action is computed via the formula $S_1(x_c) = (1/2)\log S''(x_c)$, where $S''(x) = 1 - gx$. The result is $S_1 = (1/2)\log(1 - gx_c)$, which expands as a power series $-\sum_{k \geq 1}(gx_c)^k/(2k)$. This arises from summing 1PI necklace diagrams (k-cycles of cubic vertices with external legs) that each contribute $(−g)^k x_c^k/(2k)$ with symmetry factor $1/(2k)$ for a dihedral group of order $2k$.

## Example 2: ex_2_14_wallis

For Laplace integrals, the contribution from the boundary dominates when the interior has no critical points. The Wallis integral $W_n = \int_0^{\pi/2} \sin^n x\, dx$ has its phase $\log\sin x$ maximized at the boundary $x = \pi/2$. Shifting coordinates to $y = \pi/2 - x$ and expanding around $y = 0$ shows the dominant contribution comes from an exponential suppression $e^{-ny^2/2}$. The leading asymptotics are $W_n \sim \sqrt{\pi/(2n)}$.

## Example 3: ex_7_27_quartic_1pi

The 1PI 2-point function for a quartic interaction involves one-loop tadpole and two-loop sunset diagrams. The tadpole at order $g^1$ is local: $-g\delta(t_1-t_2)/(4m)$. The sunset at order $g^2$ involves three parallel propagators and yields a non-local contribution proportional to $[G_0(t_1,t_2)]^3$. Both are computed using the determinant formula for 1-loop effects and Feynman rules for higher-loop diagrams.

## Now solve this problem:

Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = x^2/2 - (g/2)x^2 \cosh(x)$, where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free ($g=0$) partition function. Expand the answer as a power series in $g$ through order $g^3$.

## Solution

**Step 1: Identify the saddle point.**

The classical equation of motion is $S'(x) = 0$:
$$S'(x) = x - gx\cosh(x) - (g/2)x^2\sinh(x) = x[1 - g\cosh(x) - (g/2)x\sinh(x)].$$

At $x = 0$: $S'(0) = 0$, so $x_c = 0$ is always a saddle.

To verify it's the global minimum for small $g$, check the second derivative at $x = 0$:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - (g/2)x^2\cosh(x) = 1 - g\cosh(x) - 2gx\sinh(x) - (g/2)x^2\cosh(x).$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g.$$

For small $g$, this is positive, confirming $x_c = 0$ is a local minimum.

**Step 2: Apply the 1-loop formula.**

The 1-loop contribution to $\log(Z/Z_0)$ is given by the determinant formula:
$$\log(Z/Z_0)|_{1\text{-loop}} = -\frac{1}{2}\log\frac{S''(0)}{S''(0)|_{g=0}} = -\frac{1}{2}\log\frac{1-g}{1} = -\frac{1}{2}\log(1-g).$$

**Step 3: Expand as a power series.**

Using the Taylor expansion $\log(1-g) = -\sum_{k=1}^{\infty} g^k/k$, we have:
$$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\left(-\sum_{k=1}^{\infty} \frac{g^k}{k}\right) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}.$$

Therefore:
$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \ldots$$

**Step 4: Verify the series.**

Expanding the first few terms explicitly:
- $k=1$: $g/2$.
- $k=2$: $g^2/4$.
- $k=3$: $g^3/6$.

These match the coefficients $1/(2k)$ for $k = 1, 2, 3$.

**Step 5: Why higher-order terms don't contribute at 1-loop.**

The cubic (and higher) terms in $S$ come from the cosh expansion:
$$\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \ldots$$

So $x^2 \cosh(x) = x^2 + \frac{x^4}{2} + O(x^6)$. At the saddle $x_c = 0$, only the value $S''(0)$ matters for the 1-loop formula; the x-dependent parts of $S$ vanish at the saddle and do not contribute to the 1-loop log determinant. (They would contribute at 2-loop and higher.)

**Final Answer:**

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

Equivalently:
$$\boxed{\log(Z/Z_0) = \sum_{k=1}^{3} \frac{g^k}{2k} + O(g^4) = \frac{1}{2}\left[\log(1-g) + g + \frac{g^2}{2}\right] + O(g^4).}$$

Or written as the series:
$$\log(Z/Z_0) = -\frac{1}{2}\log(1-g) = \sum_{n=1}^{3} \frac{g^n}{2n} + O(g^4).$$
