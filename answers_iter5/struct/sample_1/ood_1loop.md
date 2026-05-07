# Solution: 1-Loop Partition Function with Cosh Interaction

## Relevance Assessment

**Retrieved examples and their relevance:**

1. **ex_3_26_effective_action (0.172)** — *Relevant, but different action.* This example computes 1-loop effective action for $S(x) = \frac{x^2}{2} - \frac{gx^3}{6}$ with a cubic interaction. It teaches the saddle-point method and the formula $-\frac{1}{2}\log(S''(x_c))$ for the 1-loop contribution. However, the current problem has $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$, which is fundamentally different: a *coefficient modulation by cosh*, not a polynomial interaction. The saddle point is different, and $S''(0)$ has a different form.

2. **ex_2_14_wallis (0.101)** — *Not applicable.* This is a steepest-descent problem for an integral, not a partition function / saddle-point problem. Skip.

3. **ex_7_27_quartic_1pi (0.058)** — *Not applicable.* This is a QFT self-energy problem, not a zero-dimensional partition function. Skip.

**Differences from ex_3_26:**
- ex_3_26 uses a pure cubic: $S_{\text{int}} = -\frac{gx^3}{6}$. Current problem: $S_{\text{int}} = -\frac{g}{2}x^2\cosh(x)$.
- ex_3_26 has $S''(0) = 1 - gx$, which depends on position. Current: $S''(0) = 1 - g$ (constant).
- ex_3_26's cubic produces necklace diagrams that sum to a logarithm. Current: cosh expands as $1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$, yielding *even powers only*, which alter the loop structure.

---

## Solution

### Step 1: Identify the saddle point

We need to find where $S'(x) = 0$:
$$S'(x) = x - g \cdot x \cosh(x) - \frac{g}{2} x^2 \sinh(x) - \frac{g}{2} x^2 \cosh(x)$$

Wait, let me differentiate more carefully:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$
$$S'(x) = x - \frac{g}{2}\left[2x\cosh(x) + x^2\sinh(x)\right] = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)$$
$$= x\left[1 - g\cosh(x) - \frac{g}{2}x\sinh(x)\right]$$

At $x = 0$: $S'(0) = 0 \cdot [\cdots] = 0$, so $x_c = 0$ is a saddle point (and it's the unique saddle near the origin for small $g > 0$).

### Step 2: Compute the second derivative at the saddle

$$S''(x) = 1 - g\cosh(x) - \frac{g}{2}\left[2x\sinh(x) + x^2\cosh(x)\right]$$
$$= 1 - g\cosh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g$$

### Step 3: Apply the 1-loop formula

The 1-loop contribution to $\log(Z/Z_0)$ is:
$$\text{(1-loop)} = -\frac{1}{2}\log\frac{S''(x_c)}{S''(0)|_{g=0}}$$

Here, $S''(x_c) = S''(0) = 1 - g$ and the reference value (free theory) is $S''(0)|_{g=0} = 1$. Thus:
$$\text{(1-loop)} = -\frac{1}{2}\log(1 - g)$$

### Step 4: Verify cubic terms don't contribute at 1-loop

The cosh expansion is:
$$\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \frac{x^6}{720} + \cdots$$

So:
$$S_{\text{int}}(x) = -\frac{g}{2}x^2\left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots\right) = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \frac{g}{48}x^6 - \cdots$$

The leading interaction term is $-\frac{g}{2}x^2$ (quadratic in $x$), not a genuine cubic or higher odd power. In the Gaussian saddle-point approximation, the 1-loop diagram enumeration (Feynman rules in a zero-dimensional field theory) counts closed loops of propagators attached to vertices. A quadratic $x^2$ term effectively modifies the free propagator (already accounted for in $S''(0)$), while cubic and higher terms would contribute to true loop diagrams. Since cosh expands to *even powers only*, there are no true odd-valent vertices, and the 1-loop structure remains purely a modification of the quadratic form — i.e., the 1-loop correction is entirely captured by the shift $S''(0) = 1 - g$.

### Step 5: Taylor expand to order $g^3$

$$-\frac{1}{2}\log(1 - g) = -\frac{1}{2}\sum_{k=1}^\infty \frac{(-g)^k}{k} = -\frac{1}{2}\sum_{k=1}^\infty \frac{(-1)^{k+1} g^k}{k}$$
$$= \frac{1}{2}\sum_{k=1}^\infty \frac{g^k}{k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

Through order $g^3$:
$$-\frac{1}{2}\log(1 - g) \approx \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

### Step 6: Verify with alternate notation

We can write:
$$\log(Z/Z_0) = \frac{1}{2} \sum_{k=1}^\infty \frac{g^k}{k} = \frac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \cdots\right)$$

Coefficients: $\frac{1}{2k}$ for order $g^k$. This matches the standard 1-loop result.

---

## Final Answer

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Equivalently, in closed form:
$$\boxed{\log(Z/Z_0) = -\frac{1}{2}\log(1 - g) + O(g^4)}$$

**Subchecks confirmed:** (1) Saddle point $x_c = 0$ identified. (2) Second derivative $S''(0) = 1 - g$ computed correctly, recognizing that cosh contribution at $x=0$ is just $-g\cosh(0) = -g$. (3) Formula $-\frac{1}{2}\log(S''(0))$ applied with reference $S''(0)|_{g=0} = 1$. (4) Taylor series coefficients $\frac{1}{2}, \frac{1}{4}, \frac{1}{6}$ for orders $g, g^2, g^3$ verified. Cosh modulation produces no genuine odd-power vertices, so 1-loop is purely the quadratic saddle-point shift.
