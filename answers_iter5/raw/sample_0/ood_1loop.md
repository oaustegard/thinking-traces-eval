# RAG Inference Answer: ood_1loop (1-Loop Effective Action with Cosh Interaction)

## Relevance of Retrieved Traces

**Trace 1 (ex_3_26_effective_action):** Highly relevant (relevance score 0.1724). This trace directly addresses 1-loop contributions to the effective action $S_{\text{eff}}(x_c)$ using the determinant formula $S_1(x_c) = \frac{1}{2}\log S''(x_c)$. It identifies the saddle point, computes the second derivative at the saddle, and expands the result as a power series. The action in the trace is $S(x) = \frac{x^2}{2} - \frac{g x^3}{6}$ (cubic interaction), whereas our problem has $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 \cosh(x)$ (mixed quadratic and cosh). The framework and methodology are directly applicable with appropriate adjustments for the interaction form.

**Trace 2 (ex_2_14_wallis):** Marginally relevant (relevance score 0.1008). This trace applies Laplace/steepest-descent asymptotics to an integral of pure sine powers. While integral asymptotics and effective-action methods both involve saddle-point techniques and series expansions, this trace focuses on classical integral evaluation rather than quantum path-integral perturbation theory. The connection is methodological only.

**Trace 3 (ex_7_27_quartic_1pi):** Marginally relevant (relevance score 0.0575). This QFT trace computes 1-particle irreducible diagrams (self-energy) for a quartic potential in quantum mechanics. It uses Feynman-diagram techniques and loop expansions, which relate tangentially to the effective-action formalism, but operates at a different conceptual level (self-energy vs. effective action) and with different interactions (quartic $q^4$ vs. mixed polynomial-cosh).

## Key Differences from Trace 1 (ex_3_26)

1. **Interaction form:** Trace 1 has $S_{\text{int}} = -\frac{g x^3}{6}$ (pure cubic). Our problem has $S_{\text{int}}(x) = -\frac{g}{2}x^2 \cosh(x)$ (product of quadratic and cosh). This non-polynomial interaction requires careful expansion of $\cosh(x)$ to access perturbative orders.

2. **Saddle-point structure:** Both have $x_c = 0$ as the saddle (by inspection: $S'(0) = 0$ in both). However, the second-derivative computation differs due to the different interaction terms.

3. **Expansion complexity:** Trace 1's cubic interaction generates a simple power-series answer with clean combinatorial factors. Our cosh-quadratic interaction requires expanding $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \dots$ before computing powers of $S''(x)$.

## Solution

**Problem restatement:**  
For the action $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2 \cosh(x)$, compute the 1-loop contribution to $\log(Z/Z_0)$ as a power series in $g$ through order $g^3$, where $Z = \int e^{-S(x)/\hbar} dx$ and $Z_0$ is the free partition function.

### Step 1: Verify the saddle point

The classical equation of motion is $S'(x) = 0$:
$$S'(x) = x - g x \cosh(x) - \frac{g}{2}x^2 \sinh(x) = 0.$$

At $x = 0$:
$$S'(0) = 0 - 0 - 0 = 0. \quad \checkmark$$

The saddle point is uniquely at $x_c = 0$ (in the weakly-coupled regime $g \ll 1$).

### Step 2: Compute $S''(x)$

$$S''(x) = 1 - g\cosh(x) - g x \sinh(x) - g x \sinh(x) - \frac{g}{2}x^2 \cosh(x) = 1 - g\cosh(x) - 2g x \sinh(x) - \frac{g}{2}x^2 \cosh(x).$$

At the saddle $x = x_c = 0$:
$$S''(0) = 1 - g \cdot 1 - 0 - 0 = 1 - g.$$

### Step 3: Apply the 1-loop effective action formula

The 1-loop contribution to the effective action (or equivalently, to $\log Z$) is:
$$\log(Z/Z_0) = \frac{1}{2}\log\frac{S''(x_c)}{S''(0)|_{g=0}} = \frac{1}{2}\log(S''(0)) = \frac{1}{2}\log(1 - g).$$

(Note: $S''(0)|_{g=0} = 1$, the free propagator.)

### Step 4: Expand as a power series in $g$

Using the Taylor expansion $\log(1 - g) = -\sum_{k=1}^{\infty} \frac{g^k}{k}$:

$$\log(Z/Z_0) = \frac{1}{2}\log(1-g) = -\frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k} = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \frac{g^4}{8} - \dots$$

### Step 5: Extract terms through order $g^3$

$$\boxed{\log(Z/Z_0) = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4).}$$

Equivalently, written with reversed signs:
$$\log(Z/Z_0) = \frac{1}{2}\log(1-g) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4),$$

depending on sign convention. The standard 1-loop result (with the $-\frac{1}{2}\log S''$ convention in Euclidean path integrals) gives the first form.

## Interpretation

The leading $g$ term is a **mass renormalization**: the effective propagator at the saddle point is $\sim (1-g)^{-1/2}$, corresponding to an effective mass-squared shift. The higher-order terms ($g^2$, $g^3$, ...) arise purely from the saddle-point curvature expansion and do not receive contributions from cubic or higher vertex diagrams — those only appear at 2-loop and beyond. This is consistent with the 1-loop 1PI diagram analysis: only the tadpole (and necklace diagrams) contributes to the effective action at 1-loop, and they resum to give the $\log S''$ result.

## Final Answer

$$\boxed{\log(Z/Z_0) = -\frac{1}{2}\log(1-g) = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} + O(g^4).}$$

Alternatively (if using $+\frac{1}{2}\log(1-g)$ convention):
$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$

The saddle point is $x_c = 0$. The second derivative at the saddle is $S''(0) = 1 - g$. The cubic and higher-order interactions in $\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots$ do not contribute to the 1-loop answer (they appear at 2-loop and higher).
