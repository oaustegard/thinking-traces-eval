# Solution: ood_1loop (1-loop for non-polynomial cosh interaction)

Below are three worked examples —

**Example 1: Etingof 3.26 (1-loop effective action with cubic)** — derives $S_1(x_c) = \frac{1}{2}\log(1 - gx_c)$ using the determinant formula $S_1 = \frac{1}{2}\log S''(x_c)$, then expands in powers of $g$ to recover the necklace diagram sum $\sum_{k\ge 1} (-1)^k (gx_c)^k/(2k)$.

**Example 2: Etingof 2.14 (Wallis formula)** — shows how to systematically expand log terms: $\log(1-u) = -\sum_{k\ge 1} u^k/k$, extracting coefficients order by order.

**Example 3: Etingof 7.27 (1PI diagrams and loop counting)** — illustrates how to identify the saddle point, compute second derivatives, and apply the one-loop formula via Feynman diagrams.

---

Now solve: Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action $S(x) = x^2/2 - (g/2) x^2 \cosh(x)$, where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free (g=0) partition function. Expand the answer as a power series in $g$ through order $g^3$.

## Reasoning

**Saddle point:** The action is $S(x) = x^2/2 - (g/2)x^2\cosh(x)$. Taking the derivative:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2}x^2\sinh(x) = x\left(1 - g\cosh(x) - \frac{g}{2}x\sinh(x)\right).$$

At $x = 0$: $S'(0) = 0$ always, so $x_c = 0$ is a saddle for all $g$ in a neighborhood of $g = 0$.

**Second derivative at the saddle:**
$$S''(x) = 1 - g\cosh(x) - g x \sinh(x) - \frac{g}{2}x\sinh(x) - \frac{g}{2}x\sinh(x) - \frac{g}{2}x^2\cosh(x)$$
$$= 1 - g\cosh(x) - g x \sinh(x) - g x \sinh(x) - \frac{g}{2}x^2\cosh(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

At $x = 0$ (using $\cosh(0) = 1$, $\sinh(0) = 0$):
$$S''(0) = 1 - g \cdot 1 = 1 - g.$$

**1-loop formula:** The standard 1-loop contribution is
$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{1}{2}\log\frac{S''(0)|_{g=0}}{S''(0)} = \frac{1}{2}\log\frac{1}{1-g} = -\frac{1}{2}\log(1-g).$$

**Power-series expansion:**
$$-\frac{1}{2}\log(1-g) = -\frac{1}{2}\sum_{k\ge 1}\frac{(-1)^k(-g)^k}{k} = -\frac{1}{2}\sum_{k\ge 1}\frac{(-1)^{k+1}g^k}{k} = \frac{1}{2}\sum_{k\ge 1}\frac{(-1)^k g^k}{k}.$$

Wait, let me redo: $\log(1-u) = -\sum_{k\ge 1} u^k/k$, so $\log(1-g) = -\sum_{k\ge 1} g^k/k$. Thus
$$-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k\ge 1}\frac{g^k}{k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

**Verification of formula:** The cosh and sinh terms in $S''(x)$ only affect the higher-order corrections in the expansion of $S''$ around $x_c = 0$, but they do NOT contribute to $S''(0)$ itself — at $x = 0$ only the constant term of the cosh expansion (which is 1) matters, giving $S''(0) = 1 - g$. The cubic terms from expanding $\cosh(x) = 1 + x^2/2 + \cdots$ would contribute at the 3-loop level or modify saddle locations, but at 1-loop the result is simply determined by $S''(0)$.

**Final answer:** The 1-loop contribution through order $g^3$ is

$$\boxed{\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4) = \sum_{k=1}^3 \frac{g^k}{2k}.}$$

The key sub-checks: (1) $x_c = 0$ identified as saddle, (2) $S''(0) = 1 - g$, (3) 1-loop formula $-\frac{1}{2}\log(1-g)$ applied correctly, (4) Taylor expansion yielding coefficients $1/(2k)$ for each $g^k$ term.
