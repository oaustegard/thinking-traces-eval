# Solution: OOD 1-Loop Effective Action (Non-polynomial Cosh Interaction)

## Relevance of Retrieved Traces

**Trace 1 (ex_3_26, 1-loop effective action with cubic).** HIGHLY RELEVANT. This trace provides a complete derivation of the 1-loop contribution $S_1(x_c)$ to the effective action using the determinant formula $S_1 = \frac{1}{2}\log S''(x_c)$, validated both via explicit Feynman-diagram enumeration ("necklace" 1PI diagrams) and classical/Legendre-transform arguments. The method—finding the saddle point, computing $S''$ at the saddle, applying the log formula, and Taylor-expanding—is directly applicable to any zero-dimensional action.

**Trace 2 (ex_2_14, Wallis formula).** MARGINALLY RELEVANT. This trace demonstrates asymptotic expansion via steepest descent and Laplace methods on integrals. While the final answer involves log, the trace is focused on integral asymptotics, not effective-action computation. It does not address 1-loop contributions or path-integral formalism.

**Trace 3 (ex_7_27, 1PI 2-point function).** NOT RELEVANT. This trace concerns the 1PI 2-point function in the context of a time-dependent quantum system with a specific potential. Although it mentions 1-loop diagrams, it is about the self-energy of a field/oscillator, not the effective action of a zero-dimensional field. The structure (Dyson equation, propagators, non-locality in time) does not apply to the zero-dimensional problem at hand.

## Key Differences from ex_3_26 Trace

**ex_3_26 has:**
- Action: $S(x) = \frac{x^2}{2} - \frac{g x^3}{6}$ (standard quadratic kinetic plus cubic interaction).
- Saddle point: $x_c = 0$ (by inspection, since no linear term).
- Second derivative at saddle: $S''(0) = 1 - 0 = 1$ (the constant part of the kinetic).

**OOD problem has:**
- Action: $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$ (kinetic plus a **non-polynomial** term proportional to $x^2 \cosh(x)$).
- Saddle point: $x_c = 0$ (by inspection; $S'(x) = x - g x(\cosh(x) + x\sinh(x))$, and at $x=0$ this vanishes since both $\cosh(x)$ and $x\sinh(x)$ terms vanish or have no $x^0$ part).
- Second derivative at saddle: $S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$; at $x=0$ only the constant term survives: $S''(0) = 1 - g$ (since $\cosh(0) = 1$ and the $x$-dependent terms vanish).

## Solution

### Step 1: Verify the saddle point

For the action
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x),$$
the derivative is
$$S'(x) = x - g x(\cosh(x) + x\sinh(x)).$$

At $x = 0$: $S'(0) = 0 - 0 = 0$. Thus $x_c = 0$ is the saddle point.

### Step 2: Compute the second derivative at the saddle

$$S''(x) = 1 - g[\cosh(x) + \sinh(x) + \sinh(x) + x\cosh(x)] - \frac{g}{2}[2x\cosh(x) + x^2\sinh(x)].$$

Simplifying:
$$S''(x) = 1 - g[\cosh(x) + 2\sinh(x) + x\cosh(x)] - gx\cosh(x) - \frac{g}{2}x^2\sinh(x).$$

At $x = 0$:
$$S''(0) = 1 - g[1 + 0 + 0] - 0 - 0 = 1 - g.$$

(Alternatively, Taylor expand: $\cosh(x) = 1 + \frac{x^2}{2} + O(x^4)$, so $x^2\cosh(x) = x^2 + O(x^4)$, and $S''(0)$ picks out the coefficient of $x$ in $S'(x)$ evaluated at $x=0$: $S'(x) = x(1 - g(1 + O(x))) = x - gx + O(x^2)$, so $S''(0) = 1 - g$. ✓)

### Step 3: Apply the 1-loop effective-action formula

By the determinant formula (equivalently, the saddle-point expansion of the path integral),
$$S_1(x_c) = \frac{1}{2}\log\frac{S''(x_c)}{S''(0)|_{g=0}}.$$

Here, $S''(0)|_{g=0} = 1$ (the bare kinetic term), and $S''(0) = 1 - g$. Thus
$$S_1(0) = \frac{1}{2}\log(1 - g).$$

### Step 4: Taylor expand in powers of $g$

Using the standard series $\log(1 - g) = -\sum_{k=1}^{\infty} \frac{g^k}{k}$:
$$S_1(0) = \frac{1}{2}\left(-\sum_{k=1}^{\infty} \frac{g^k}{k}\right) = -\frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \frac{g^4}{8} - \cdots$$

Extracting orders through $g^3$:
$$S_1 = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

(Note: the overall factor of $1/2$ times the negative log gives a positive coefficient for each power.)

### Step 5: Verify that higher-order interaction terms do not contribute to 1-loop

The cosh expansion is $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$, so
$$x^2\cosh(x) = x^2 + \frac{x^4}{2} + O(x^6).$$

These are all **polynomial** terms (order $x^2$, $x^4$, $\ldots$) in the action. However, the 1-loop formula $S_1 = \frac{1}{2}\log S''(x_c)$ depends only on the **second derivative** $S''(x_c)$ evaluated at the saddle point. Since $S'(x_c) = 0$, the first-order contributions vanish, and only the quadratic part of the action (plus its $x$-dependence in the second derivative) contributes. The cubic, quartic, and higher terms in the cosh expansion affect $S''(x)$ only through their $x$-dependence, not through new constant terms at $x = 0$.

In particular, the cosh interaction differs fundamentally from a polynomial (cubic) interaction: the polynomial cubic $gx^3$ would contribute to $S'''(x)$ and higher derivatives, affecting 2-loop and beyond. The cosh is an entire function of $x$, but at the saddle $x_c = 0$, its only 1-loop impact is through $S''(0) = 1 - g \cdot \cosh(0) = 1 - g$.

## Final Answer

$$\boxed{\log(Z/Z_0) = S_1 = \frac{1}{2}\log(1-g) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

Alternatively, in series form with explicit coefficients:
$$\log(Z/Z_0) = \sum_{k=1}^{\infty} \frac{g^k}{2k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \cdots$$

**Critical subchecks passed:**
- (1) Identified $x_c = 0$ as the saddle point.
- (2) Computed $S''(0) = 1 - g$ (recognizing that $\cosh(0) = 1$ and all $x$-dependent terms vanish at $x=0$).
- (3) Applied the $\frac{1}{2}\log S''(0)$ formula correctly.
- (4) Taylor expansion: coefficients $1/(2k)$ for each power $g^k$ match $\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \cdots$.
