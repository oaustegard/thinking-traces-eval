# One-Loop Effective Action: Hyperbolic-Coupling Partition Function

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action:
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$$

where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free ($g=0$) partition function. Expand the answer as a power series in $g$ through order $g^3$.

## Retrieved Examples and Relevance

**Example 1 (ex_3_26_effective_action): 1-Loop Effective Action**
Example 3_26 addresses the 1-loop effective action for $S(x) = \frac{x^2}{2} - \frac{gx^3}{6}$ via Feynman diagrams and necklace enumeration. It identifies the saddle point (x_c = 0), computes the second derivative at the saddle, applies the 1-loop determinant formula $S_1(x_c) = \frac{1}{2}\log S''(x_c)$, and sums an infinite series of necklace diagrams to obtain $S_1(x_c) = -\frac{1}{2}\log(1 - gx_c)$.

*Relevance*: High. The fundamental 1-loop formula and saddle-point structure are directly applicable. The action contains a perturbative coupling and a free quadratic term; the partition function is evaluated near a saddle point; the 1-loop contribution comes from the second-derivative determinant.

*Key Differences*: (1) Example 3_26 has a cubic coupling ($-\frac{gx^3}{6}$) with a nonzero saddle $x_c = gx_c$ (determined self-consistently); the current problem has a nonpolynomial coupling $-\frac{g}{2} x^2 \cosh(x)$ with saddle $x_c = 0$. (2) Example 3_26 computes an effective action $S_1(x_c)$ depending on the saddle location; here we evaluate $\log(Z/Z_0)$, a ratio of partition functions. (3) The expansion structure differs: cubic interactions generate vertex weights $-g$; the hyperbolic coupling generates weights from the cosh Taylor series, with the quadratic part of $x^2\cosh(x) = x^2(1 + x^2/2 + \ldots)$ dominating the 1-loop contribution. (4) The final answer is a power series in $g$ (not a closed form in $x_c$) because the saddle is fixed at the origin.

**Example 2 (ex_2_14_wallis): Wallis Formula**
This is a classical analysis problem using steepest descent on a trigonometric integral, unrelated to partition functions or quantum field theory.

*Relevance*: Negligible. The domain, method, and physical interpretation are entirely different.

**Example 3 (ex_7_27_quartic_1pi): QFT 2-Point Function**
A quantum-field-theory problem using perturbative Feynman diagrams with a quartic interaction.

*Relevance*: Minimal. While it demonstrates 1-loop diagram summing, the action is different (quartic, not hyperbolic coupling), and the external structure (2-point function vs. partition function) is different.

---

## Solution

### Step 1: Identify the Saddle Point

The saddle point is determined by the condition $S'(x_c) = 0$:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x)$$

At $x = 0$:
- First term: $0$
- Second term: $-g \cdot 0 \cdot \cosh(0) = 0$
- Third term: $-\frac{g}{2} \cdot 0^2 \cdot \sinh(0) = 0$

Thus $S'(0) = 0$, and **$x_c = 0$ is the saddle point**. This is the unique critical point for small $g$ (perturbative continuity from the $g=0$ saddle).

### Step 2: Compute the Second Derivative at the Saddle

Take the second derivative of $S(x)$:
$$S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2} x^2 \cosh(x)$$

Evaluate at $x = 0$:
- The constant term is $1$.
- $g\cosh(0) = g \cdot 1 = g$.
- $2gx\sinh(x)|_{x=0} = 0$ (vanishes due to the $x$ factor).
- $\frac{g}{2} x^2 \cosh(x)|_{x=0} = 0$ (vanishes due to the $x^2$ factor).

Therefore:
$$S''(0) = 1 - g$$

This is the key result: the second derivative at the saddle depends linearly on $g$, with coefficient $-1$.

### Step 3: Apply the 1-Loop Saddle-Point Formula

In the saddle-point approximation, the partition function is:
$$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} dx \approx \sqrt{\frac{2\pi\hbar}{S''(x_c)}} e^{-S(x_c)/\hbar}$$

For the free theory ($g = 0$):
$$Z_0 = \sqrt{\frac{2\pi\hbar}{S''(0)|_{g=0}}} = \sqrt{2\pi\hbar} \quad \text{(since } S''(0)|_{g=0} = 1\text{)}$$

The ratio is:
$$\frac{Z}{Z_0} = \sqrt{\frac{S''(0)|_{g=0}}{S''(0)}} \, e^{-[S(0) - S(0)|_{g=0}]/\hbar}$$

At $x_c = 0$, both $S(0) = 0$ and $S(0)|_{g=0} = 0$ (the action vanishes at the origin), so:
$$\log\frac{Z}{Z_0} = \frac{1}{2} \log\frac{1}{1-g} = -\frac{1}{2}\log(1-g)$$

### Step 4: Taylor Expand in the Coupling

Use the series expansion $\log(1-g) = -\sum_{k=1}^{\infty} \frac{g^k}{k}$:
$$-\frac{1}{2}\log(1-g) = \frac{1}{2} \sum_{k=1}^{\infty} \frac{g^k}{k} = \frac{1}{2}\left(\frac{g}{1} + \frac{g^2}{2} + \frac{g^3}{3} + \frac{g^4}{4} + \cdots\right)$$

Through order $g^3$:
$$\log\frac{Z}{Z_0} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)$$

### Step 5: Verify That Higher-Order Terms in the Action Do Not Contribute to 1-Loop

The hyperbolic coupling expands as:
$$\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots$$

So:
$$x^2 \cosh(x) = x^2 + \frac{x^4}{2} + \frac{x^6}{24} + \cdots$$

In perturbation theory, the 1-loop contribution arises solely from quadratic fluctuations around the saddle and the saddle-point determinant ($S''(x_c)$ formula). The higher-order terms in the action ($x^4, x^6$, etc., from cosh expansion) generate vertices that contribute to 2-loop diagrams and beyond. At 1-loop with saddle $x_c = 0$, only the quadratic part $S''(0) = 1 - g$ (which already accounts for the leading $g$-dependence) enters the determinant. Thus the power-series result is exact at 1-loop order.

---

## Final Answer

$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4)}$$

Equivalently, in closed form:
$$\boxed{\log(Z/Z_0) = -\frac{1}{2}\log(1-g) \quad \text{(through all orders in } g\text{)}}$$

**Critical subchecks confirmed:**
1. Saddle point: $x_c = 0$ (all three terms in $S'(x)$ vanish at $x=0$) ✓
2. Second derivative: $S''(0) = 1 - g$ (accounting for cosh expansion) ✓
3. 1-loop formula: $-\frac{1}{2}\log(1-g)$ from determinant ratio ✓
4. Taylor coefficients: $\frac{1}{2k}$ for the $g^k$ term, giving $1/2, 1/4, 1/6$ for $k=1,2,3$ ✓
5. Higher-order structure: cosh expansion generates higher-loop vertices, not 1-loop contributions ✓
