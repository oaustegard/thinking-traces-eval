# 1-Loop Partition Function: Non-polynomial cosh Interaction

## Problem
Compute the 1-loop contribution to $\log(Z/Z_0)$ for the zero-dimensional action 
$$S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x),$$
where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free (g=0) partition function. Expand the answer as a power series in $g$ through order $g^3$.

## Retrieved Examples and Relevance

**Example 1 (ex_3_26_effective_action)**: 1-loop effective action for $S(x) = \frac{x^2}{2} - \frac{g x^3}{6}$. This is *highly relevant* because it uses the 1-loop determinant formula $S_1(x_c) = \frac{1}{2} \log S''(x_c)$ and Taylor-expands the logarithm to extract power-series coefficients. *Key difference*: The example has a cubic $x^3$ interaction (polynomial), while our problem uses $\cosh(x)$ (transcendental, requires series expansion).

**Example 2 (ex_2_14_wallis)**: Wallis integral steepest descent. This is minimally relevant; it demonstrates phase-function analysis but not partition-function perturbation theory. *Key difference*: Entirely different framework (real integration, not Euclidean path integrals).

**Example 3 (ex_7_27_quartic_1pi)**: 1PI 2-point function in QFT with quartic potential. This is somewhat relevant because it uses Feynman-diagram calculations and perturbative expansions, but it computes a 2-point function (external legs) rather than an effective action at the saddle. *Key difference*: External structure; our problem is a zero-dimensional "bubble" with no external legs.

The most useful is **Example 1** (ex_3_26), which directly teaches the 1-loop formula and logarithmic expansion strategy. We adapt this to handle the $\cosh$ nonlinearity.

## Solution

**Step 1: Identify the saddle point.**

The partition function in Euclidean form is 
$$Z = \int_{-\infty}^{\infty} e^{-S(x)/\hbar} \, dx.$$

The saddle point is where $S'(x_c) = 0$:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2} x^2 \sinh(x).$$

At $x_c = 0$: $S'(0) = 0 - 0 - 0 = 0$. ✓ So $x_c = 0$ is the saddle.

**Step 2: Compute the second derivative at the saddle.**

$$S''(x) = 1 - g\cosh(x) - g\cosh(x) - 2gx\sinh(x) - gx^2\cosh(x) - gx\sinh(x) - gx\sinh(x).$$

Wait, let me recompute carefully. We have 
$$S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x).$$

Taking the derivative:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2} \cdot 2x \sinh(x) - \frac{g}{2}x^2\cosh(x).$$

Simplify:
$$S''(x) = 1 - g\cosh(x) - 2gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

Hmm, let me restart more systematically:
$$\frac{d}{dx}\left[x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x)\right] = 1 - g[\cosh(x) + x\sinh(x)] - g[x\sinh(x) + \frac{x^2}{2}\cosh(x)].$$

At $x = 0$: $\cosh(0) = 1$, $\sinh(0) = 0$, so 
$$S''(0) = 1 - g \cdot 1 - 0 = 1 - g.$$

**Step 3: Apply the 1-loop formula.**

The 1-loop contribution to $\log(Z/Z_0)$ is 
$$\log(Z/Z_0)\big|_{1\text{-loop}} = \frac{1}{2} \log \frac{S''(x_c)}{S''(0)\big|_{g=0}} = \frac{1}{2} \log \frac{1-g}{1} = \frac{1}{2} \log(1-g).$$

(Here $S''(0)|_{g=0} = 1$ is the free kinetic term.)

**Step 4: Taylor expand.**

Use $\log(1-g) = -\sum_{k=1}^{\infty} \frac{g^k}{k}$, so 
$$\frac{1}{2}\log(1-g) = -\frac{1}{2} \sum_{k=1}^{\infty} \frac{g^k}{k} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \cdots$$

Therefore, through order $g^3$:
$$\log(Z/Z_0)\big|_{1\text{-loop}} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4).$$

Equivalently, writing coefficients as positive:
$$\log(Z/Z_0)\big|_{1\text{-loop}} = -\frac{1}{2} g - \frac{1}{4} g^2 - \frac{1}{6} g^3 + O(g^4).$$

**Step 5: Verify the cubic contribution is at 1-loop.**

The action has $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots$, so 
$$-\frac{g}{2}x^2\cosh(x) = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \frac{g}{48}x^6 - \cdots$$

There is no cubic term in the interaction. The cubic power-series coefficient $g^3$ in $\log(Z/Z_0)$ comes entirely from the Taylor expansion of $\frac{1}{2}\log(1-g)$ at the 1-loop level—not from Feynman diagrams with cubic vertices. Higher-loop diagrams contribute at $g^2$ and beyond, but the problem isolates the 1-loop answer, which is the $\log S''(x_c)$ determinant contribution.

## Final Answer

$$\boxed{\log(Z/Z_0) = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4)}$$

Or in the compact logarithmic form:
$$\boxed{\log(Z/Z_0) = \frac{1}{2}\log(1-g) + O(g^4)}$$

The critical checks are satisfied:
1. Saddle point identified: $x_c = 0$ ✓
2. Second derivative at saddle: $S''(0) = 1 - g$ ✓
3. 1-loop determinant applied: $\frac{1}{2}\log(1-g)$ ✓
4. Taylor series: coefficients $1/(2k)$ for order $g^k$ ✓
