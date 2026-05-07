# Solution: OOD 1-loop Partition Function Problem

## Reasoning

For the action $S(x) = \tfrac{x^2}{2} - \tfrac{g}{2}x^2\cosh(x)$, I compute the 1-loop contribution to $\log(Z/Z_0)$ and expand as a power series in $g$ through order $g^3$.

**Step 1: Identify the saddle point.** The classical equation of motion is $S'(x) = 0$:
$$S'(x) = x - g x\cosh(x) - \tfrac{g}{2}x^2\sinh(x) = 0.$$
For small coupling $g$, the saddle point is close to $x = 0$. Direct inspection: $S'(0) = 0 - 0 - 0 = 0$. So $x_c = 0$ is the saddle.

**Step 2: Compute the second derivative at the saddle.** The potential curvature is:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \tfrac{g}{2}x^2\cosh(x).$$
Simplifying:
$$S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \tfrac{g}{2}x^2\cosh(x).$$
At $x=0$ (where $\cosh(0) = 1$, $\sinh(0) = 0$):
$$S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g.$$

**Step 3: Apply the 1-loop determinant formula.** The 1-loop contribution to the effective action is:
$$S_1(x_c) = \tfrac{1}{2}\log S''(x_c) = \tfrac{1}{2}\log(1-g).$$

**Step 4: Taylor expansion.** For $|g| < 1$, expand:
$$\log(1-g) = -\sum_{k=1}^{\infty}\frac{g^k}{k} = -g - \frac{g^2}{2} - \frac{g^3}{3} - \frac{g^4}{4} - \cdots$$
Thus,
$$S_1(0) = \tfrac{1}{2}\log(1-g) = -\frac{1}{2}\sum_{k=1}^{\infty}\frac{g^k}{k} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \frac{g^4}{8} - \cdots$$

**Step 5: Interpretation.** The fact that $S_1$ depends only on $S''(0)$ and not on higher derivatives indicates that the non-polynomial $\cosh$ terms in $S$ do not contribute to the 1-loop partition function at the saddle $x_c = 0$. This is because:
- The cosh expansion is $\cosh(x) = 1 + \tfrac{x^2}{2} + \tfrac{x^4}{24} + \cdots$
- At the saddle, only the curvature $S''(0)$ matters for the 1-loop Gaussian integral.
- Higher-order terms in the cosh contribute to 2-loop and beyond.

For the necklace 1PI diagram picture (as in the effective-action trace), the 1-loop diagrams are a geometric series that sums to the log determinant form, with no sensitivity to cubic or higher couplings at the saddle point.

## Final Answer

$$\boxed{\log(Z/Z_0)|_{\text{1-loop}} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \frac{g^4}{8} - \cdots = -\frac{1}{2}\log(1-g).}$$

Equivalently,
$$\log(Z/Z_0)|_{\text{1-loop}} = \sum_{k=1}^{\infty} \frac{g^k}{2k}.$$

**Critical subchecks:**
- Saddle point: $x_c = 0$ (verified by $S'(0) = 0$). ✓
- Second derivative at saddle: $S''(0) = 1 - g$ (the $\cosh(0) = 1$ term; other contributions vanish at $x=0$). ✓
- 1-loop formula applied: $-\tfrac{1}{2}\log(1-g)$. ✓
- Taylor coefficients: $g/2, g^2/4, g^3/6, \ldots$ matching $1/(2k)$ for order $g^k$. ✓
- Non-polynomial cosh does NOT contribute to 1-loop at the saddle. ✓
