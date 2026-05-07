# Solution: OOD 1-Loop Effective Action with Cosh Interaction

## Relevance Assessment

**Retrieved traces:**
1. **ex_3_26_effective_action** (relevance 0.17): *Highly relevant.* This trace computes the 1-loop effective action $S_{\text{eff}}(x_c) = S(x_c) + \hbar S_1(x_c)$ for the cubic action $S(x) = x^2/2 - gx^3/6$. It establishes the determinant formula $S_1(x_c) = \tfrac{1}{2}\log S''(x_c)$ and shows how to expand it as a power series via necklace diagrams.

2. **ex_2_14_wallis** (relevance 0.10): *Marginally relevant.* While this is a steepest descent problem for integrals with specific boundary structure, it is tangential to the effective action calculation. The methods are orthogonal.

3. **ex_7_27_quartic_1pi** (relevance 0.06): *Marginally relevant.* This computes the 1PI 2-point self-energy $\Sigma(t_1, t_2)$ for a quartic potential, demonstrating loop diagrams and symmetry factors in QFT. However, it addresses the full 2-point function (not effective action) and operates at finite coupling order, not the resummed $\log$ form.

## Key Differences from ex_3_26 Trace

The retrieved trace analyzes $S(x) = x^2/2 - gx^3/6$ (cubic interaction). The main problem features:
$$S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 \cosh(x).$$

**Interaction structure:** Instead of a pure cubic $-gx^3/6$, the interaction is $-\tfrac{g}{2}x^2\cosh(x)$, which mixes a mass-like quadratic term with a non-polynomial cosh factor. This requires careful handling of the second derivative at the saddle point, which differs from the cubic case.

**Method persistence:** The determinant formula $S_1(x_c) = \tfrac{1}{2}\log[S''(x_c)/S''_0(x_c)]$ still applies, but the computation of $S''(0)$ requires expanding $\cosh(x)$ around the saddle and tracking only the contribution at the saddle, not at general $x_c$.

## Solution

**Step 1: Identify the saddle point.**

By inspection, $S'(x) = x - \frac{g}{2}[2x\cosh(x) + x^2\sinh(x)] = x[1 - g\cosh(x) - \frac{g}{2}x\sinh(x)]$.

At $x = 0$: $S'(0) = 0 \cdot [\ldots] = 0$ ✓.

So the saddle is at $x_c = 0$.

**Step 2: Compute the second derivative at the saddle.**

$$S''(x) = 1 - \frac{g}{2}[2\cosh(x) + 2x\sinh(x) + 2x\sinh(x) + x^2\cosh(x)].$$

Simplifying:
$$S''(x) = 1 - g[\cosh(x) + 2x\sinh(x) + \tfrac{1}{2}x^2\cosh(x)].$$

At $x = 0$:
$$S''(0) = 1 - g[\cosh(0) + 0 + 0] = 1 - g.$$

The free-theory (g=0) second derivative is:
$$S''_0(0) = 1.$$

**Step 3: Apply the 1-loop effective action formula.**

The standard result (Etingof, Coleman–Weinberg) is:
$$\log\frac{Z}{Z_0} = -\frac{1}{2\hbar}\log\frac{S''(x_c)}{S''_0(x_c)} + O(\hbar^{-1} \cdot \text{higher loops}).$$

At 1-loop order ($\hbar \to 1$):
$$\log\frac{Z}{Z_0}\bigg|_{1\text{-loop}} = -\frac{1}{2}\log(1-g).$$

**Step 4: Expand as a power series in $g$.**

Using $\log(1-g) = -\sum_{k=1}^\infty \frac{g^k}{k}$:

$$-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^\infty \frac{g^k}{k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \cdots$$

Through order $g^3$:

$$\boxed{\log\frac{Z}{Z_0} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

## Verification of Critical Subchecks

1. **Saddle identification:** $x_c = 0$ is correct; $S'(0) = 0$ and $S'(x) \approx x[1 - g - \cdots]$ is strictly first-order in $x$ near the origin. ✓

2. **Second derivative at saddle:** $S''(0) = 1 - g$ correctly accounts for the $\cosh(x)$ expansion: $\cosh(0) = 1$, and the derivative terms $2x\sinh(x)$ and $x^2\cosh(x)$ vanish at $x=0$. ✓

3. **1-loop formula:** $-\tfrac{1}{2}\log S''(0) = -\tfrac{1}{2}\log(1-g)$ applied correctly. ✓

4. **Taylor expansion:** The series $\frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \cdots = \frac{1}{2}\sum_{k \geq 1} \frac{g^k}{k}$ has the correct coefficients $\frac{1}{2k}$ for each order. ✓

## Note on Higher-Loop Contributions

The $\cosh(x)$ interaction does not contribute additional cubic or quartic vertex terms at the saddle $x_c = 0$ (all $x$-derivatives vanish). Thus, there are no 2-loop or higher-loop terms involving genuine cubic or quartic vertex insertions at this order — only from the resummation of the determinant. The series terminates at the answer given.
