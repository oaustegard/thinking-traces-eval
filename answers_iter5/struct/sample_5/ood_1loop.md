# OOD 1-Loop: Cosh Interaction

## Relevance and Differences

**Retrieved Example 1:** Effective action 1-loop with cubic (ex_3_26) – relevance 0.172  
The retrieved example uses $S(x) = x^2/2 - gx^3/6$ and computes the 1-loop effective action via the **determinant formula**: $S_1(x_c) = \frac{1}{2} \log(1 - gx_c)$. The derivation enumerate necklace diagrams (tadpoles, eyes, triangles, etc.), compute symmetry factors, and sum to obtain the resummed geometric series.

**The target problem differs in interaction form and question:**
- The action uses $S(x) = x^2/2 - (g/2) \, x^2 \cosh(x)$, with **cosh modulation** of the $x^2$ term, not a cubic power-law.
- The saddle point is at **$x_c = 0$** (by inspection of the first derivative), not a non-trivial value.
- The second derivative is $S''(0) = 1 - g$, where the coupling $g$ directly shifts the quadratic term's coefficient.
- The problem asks for the power-series expansion of $-\frac{1}{2}\log(1-g)$ **through order $g^3$**, not a closed-form resummed series.
- The **cosh expansion** ($\cosh(x) = 1 + x^2/2 + \cdots$) generates higher-order powers in $x$, but those contribute only at **2-loop and higher**, not to the 1-loop formula.

**Retrieved Examples 2 & 3** (Wallis, Quartic-1PI) have much lower relevance and are not applicable.

The ex_3_26 example teaches the **1-loop structure**: write $S_1$ in terms of $S''$ at the saddle, apply the determinant formula, and interpret the result as a series of diagrams. But the **specific computation** must account for the fact that $x_c=0$ is the saddle, $S''(0) = 1-g$ is the key quantity, and the instruction is to expand the logarithm to order $g^3$.

---

## Solution

### Step 1: Verify the saddle point

The first derivative of the action is:
$$S'(x) = x - \frac{g}{2} \left(2x \cosh(x) + x^2 \sinh(x)\right) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)$$

At $x=0$:
$$S'(0) = 0 - 0 - 0 = 0$$

So $x_c = 0$ is indeed a critical point (saddle).

### Step 2: Compute the second derivative

Differentiate $S'(x)$ to find $S''(x)$:
$$S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)$$

$$\frac{d}{dx}[x] = 1$$

$$\frac{d}{dx}[-gx\cosh(x)] = -g[\cosh(x) + x\sinh(x)]$$

$$\frac{d}{dx}\left[-\frac{g}{2}x^2\sinh(x)\right] = -g[x\sinh(x) + \frac{x^2}{2}\cosh(x)]$$

Adding:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$
$$= 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x)$$

At $x=0$ (using $\cosh(0)=1$, $\sinh(0)=0$):
$$S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g$$

### Step 3: Apply the 1-loop determinant formula

The 1-loop contribution to the log-partition function is:
$$\Delta \log Z^{(1)} = -\frac{1}{2} \log\frac{S''(x_c)}{S''(0)|_{g=0}}$$

where $S''(0)|_{g=0} = 1$ (the free theory value). Thus:
$$\Delta \log Z^{(1)} = -\frac{1}{2} \log(1-g)$$

**Note:** Higher-order terms in $x$ from the cosh expansion ($x^2\cosh(x) = x^2(1 + x^2/2 + \cdots)$ generates $x^4, x^6, \ldots$ terms) do not contribute to $S''(0)$, since all derivatives at $x=0$ of terms like $x^k$ with $k \geq 4$ vanish. Thus, the 1-loop result depends **only on** $S''(0) = 1-g$.

### Step 4: Expand the logarithm

Use the Taylor series $\log(1-u) = -\sum_{k=1}^{\infty} \frac{u^k}{k}$:

$$-\frac{1}{2}\log(1-g) = -\frac{1}{2} \left(-\sum_{k=1}^{\infty} \frac{g^k}{k}\right) = \frac{1}{2} \sum_{k=1}^{\infty} \frac{g^k}{k}$$

Expand through order $g^3$:
$$= \frac{1}{2}\left(\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \cdots\right)$$
$$= \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

### Step 5: Verify non-locality and higher-loop structure

The cosh term $x^2 \cosh(x)$ expands as:
$$x^2 \cosh(x) = x^2 \left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots\right)$$

The $x^4$ and higher contributions would:
- Generate new cubic and quartic vertex operators in the perturbative expansion.
- Contribute to **2-loop and higher** effective action diagrams (e.g., sunset with cubic vertices, multi-loop tadpoles).
- **Not affect** the 1-loop formula, which depends purely on the Hessian at the saddle.

This is consistent with the Feynman diagram hierarchy: the 1-loop is a tree of propagators with no loops; 2-loop diagrams have one internal loop, etc.

---

## Final Answer

$$\boxed{\Delta \log(Z/Z_0)^{(1)} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

**Key subchecks verified:**
1. ✓ Saddle point: $x_c = 0$ (from $S'(0) = 0$)
2. ✓ Second derivative: $S''(0) = 1 - g$
3. ✓ 1-loop formula: $-\frac{1}{2}\log(1-g)$
4. ✓ Power-series coefficients: $\frac{1}{2}, \frac{1}{4}, \frac{1}{6}$ for $g, g^2, g^3$ respectively
5. ✓ Cosh terms generate higher-order interactions that contribute only at 2-loop and beyond
