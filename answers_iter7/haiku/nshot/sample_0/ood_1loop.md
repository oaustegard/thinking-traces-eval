# Solution: ood_1loop (1-loop partition function for x² cosh(x) interaction)

## Examples from retrieved traces

**Example 1: ex_3_26_effective_action.md** — Computing the 1-loop contribution S₁ to the effective action via the determinant formula S₁(x_c) = ½ log(S''(x_c)). Demonstrates how to locate the saddle point from S'(x) = 0, compute S''(x_c), then expand the logarithm as a power series in g to extract coefficients order-by-order.

**Example 2: ex_2_14_wallis.md** — Using Laplace/steepest-descent methods to extract asymptotic behavior from integrals. Shows how to expand functions near their maximum (here by Taylor series), identify leading and next-order terms, and assemble the final answer systematically.

**Example 3: ex_7_27_quartic_1pi.md** — Computing corrections order-by-order using Feynman diagrams, with careful attention to vertex weights, propagators, and symmetry factors. Demonstrates how multi-loop contributions combine to modify the leading behavior.

## Solution

For the zero-dimensional action S(x) = x²/2 - (g/2)x² cosh(x), we compute the 1-loop contribution to log(Z/Z₀) where Z = ∫ e^{-S(x)/ℏ} dx.

**Step 1: Identify the saddle point.** The classical equation is S'(x) = 0:
$$S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2 \sinh(x) = x\left(1 - g\cosh(x) - \frac{g}{2}x\sinh(x)\right) = 0.$$

At x = 0: S'(0) = 0 ✓. This is the saddle point (at least for small g).

**Step 2: Compute S''(x) and evaluate at the saddle.** 
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x\cosh(x) - \frac{g}{2}x^2\cosh(x) - \frac{g}{2}x\cosh(x)$$
$$= 1 - g\cosh(x) - 2gx\sinh(x) - gx\cosh(x) - \frac{g}{2}x^2\cosh(x).$$

At x = 0:
$$S''(0) = 1 - g\cosh(0) = 1 - g.$$

**Step 3: Apply the 1-loop determinant formula.** The 1-loop contribution to log(Z/Z₀) is
$$\log(Z/Z_0)\big|_{1\text{-loop}} = -\frac{1}{2}\log\frac{S''(0)}{S''(0)|_{g=0}} = -\frac{1}{2}\log(1 - g).$$

**Step 4: Expand as a power series in g.** Using $-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k}$:
$$-\frac{1}{2}\log(1-g) = \frac{1}{2}\left(g + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right).$$

Therefore:
$$\log(Z/Z_0)\big|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + O(g^5).$$

**Step 5: Verify via direct integration (conceptual check).** The cubic and higher terms in the cosh expansion are S(x) = x²/2 - (g/2)x²(1 + x²/2! + x⁴/4! + ...) = x²/2 - (g/2)x² - (g/4)x⁴ - .... The x⁴ and higher terms appear at 2-loop order and above in the effective action expansion, so they do not contribute to the 1-loop result. Only the leading S''(0) = 1 - g contributes at 1-loop, confirming our calculation.

**Answer:**
$$\boxed{\log(Z/Z_0)\big|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

Equivalently, the general coefficient at order g^n is 1/(2n):
$$\log(Z/Z_0)\big|_{1\text{-loop}} = \sum_{n=1}^{\infty} \frac{g^n}{2n}.$$

The interaction term -gx² cosh(x) modifies only the effective mass (the S''(0) value) at the saddle x = 0; the cosh expansion produces higher-order terms in x that contribute only at 2-loop and beyond. Thus the 1-loop structure is purely determined by the quadratic shift 1 - g at the saddle, leading to the simple log expansion.
