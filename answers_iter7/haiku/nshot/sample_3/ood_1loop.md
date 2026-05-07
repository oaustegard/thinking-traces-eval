# Solution: ood_1loop (1-loop effective action with cosh interaction)

## Worked Examples

**Example 1 (ex_3_26_effective_action): 1-loop formula and necklace diagrams.** For $S(x) = x^2/2 - gx^3/6$, the 1-loop contribution is $S_1(x_c) = \frac{1}{2}\log S''(x_c) = \frac{1}{2}\log(1 - gx_c)$. The second derivative at the saddle is $S''(x_c) = 1 - gx_c$. Necklace diagrams (a $k$-cycle of trivalent vertices) sum to this logarithm via geometric series. The critical observation is that $S''$ is evaluated at the classical saddle, not at arbitrary $x$.

**Example 2 (ex_2_14_wallis): Power-series expansion from asymptotics.** The Wallis integral asymptotic $\sim \sqrt{\pi/(2n)}$ is extracted via the Taylor expansion of $\log\cos y = -y^2/2 - y^4/12 - \ldots$. Similarly, expanding a logarithm $\log(1-g) = -\sum_{k \geq 1} g^k/k$ is fundamental. For our cosh action, the expansion of $\log(1-g)$ to order $g^3$ gives all coefficients needed.

**Example 3 (ex_7_27_quartic_1pi): Loop structure and higher orders.** The 1-loop self-energy includes a tadpole $\propto g$ and 2-loop contributions $\propto g^2$. The symmetry factors reflect the combinatorial structure: a single-vertex tadpole has $S=2$, while multi-vertex arrangements have dihedral symmetries. At higher orders, the loop number $L$ drives the $g$-power via $1PI$ graph structure.

## Solving ood_1loop

The action is $S(x) = \frac{x^2}{2} - \frac{g}{2}x^2\cosh(x)$.

**Step 1: Identify the saddle point.**

By inspection, $S'(x) = x - gx\cosh(x) - \frac{g}{2}x^2\sinh(x) = x(1 - g\cosh(x) - \frac{g}{2}x\sinh(x))$.

At $x=0$: $S'(0) = 0$ (always a saddle). So the classical field is $x_c = 0$.

**Step 2: Compute the second derivative.**

$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - \frac{g}{2}x\sinh(x) - \frac{g}{2}x\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

Simplifying:
$$S''(x) = 1 - g\cosh(x) - gx\sinh(x) - gx\sinh(x) - \frac{g}{2}x^2\cosh(x) = 1 - g\cosh(x) - 2gx\sinh(x) - \frac{g}{2}x^2\cosh(x).$$

At $x_c = 0$:
$$S''(0) = 1 - g\cosh(0) - 0 - 0 = 1 - g.$$

**Step 3: Apply the 1-loop formula.**

The 1-loop contribution to $\log(Z/Z_0)$ is:
$$\frac{1}{2}\log\frac{S''(0)}{S''(0)|_{g=0}} = \frac{1}{2}\log(1 - g).$$

Expanding:
$$\log(1-g) = -\sum_{k=1}^{\infty} \frac{g^k}{k} = -g - \frac{g^2}{2} - \frac{g^3}{3} - \frac{g^4}{4} - \ldots$$

Thus:
$$\log(Z/Z_0)|_{1\text{-loop}} = -\frac{1}{2}\log(1-g)^{-1} = \frac{1}{2}\log(1-g) = -\frac{g}{2} - \frac{g^2}{4} - \frac{g^3}{6} - \ldots$$

Wait, I need to be careful about signs. The standard formula (Etingof/Coleman-Weinberg) is:
$$S_{\text{eff}} = S + \frac{\hbar}{2}\log S'' + O(\hbar^2).$$

So the 1-loop effective action is $S_1 = \frac{1}{2}\log S''(0)$, and the log-partition-function contribution is its integral or functional-trace encoding. For a **zero-dimensional** path integral, $\log(Z/Z_0) = -S_{\text{eff}}(x_c) + \text{source terms}$. At $g=0$ (free theory), $S_0(x) = x^2/2$, so $S_0''(0) = 1$. The ratio $S''(0)/S''(0)|_{g=0} = 1-g$.

The 1-loop contribution is:
$$\Delta(\log Z) = -\Delta S_{\text{eff}} = -\frac{1}{2}\Delta\log S'' = -\frac{1}{2}\log(1-g) + \frac{1}{2}\log(1) = -\frac{1}{2}\log(1-g).$$

Expanding:
$$-\frac{1}{2}\log(1-g) = \frac{1}{2}\sum_{k=1}^{\infty} \frac{g^k}{k} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \ldots$$

**Step 4: Verify: cubic terms in $\cosh$ expansion.**

Expanding $\cosh(x) = 1 + \frac{x^2}{2} + \frac{x^4}{24} + \ldots$, the interaction becomes:
$$-\frac{g}{2}x^2\cosh(x) = -\frac{g}{2}x^2\left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \ldots\right) = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \frac{g}{48}x^6 - \ldots$$

These higher-order vertex terms ($x^4, x^6$, etc.) contribute **only at 2-loop and higher** to $\log(Z/Z_0)$; they do not enter the 1-loop contribution, which depends only on $S''(0) = 1 - g$.

## Final Answer

$$\log(Z/Z_0)|_{1\text{-loop}} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

More explicitly:
$$\boxed{\log(Z/Z_0) = \frac{1}{2}\sum_{k=1}^{\infty}\frac{g^k}{k} = \frac{1}{2}\log\frac{1}{1-g} = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + \frac{g^4}{8} + \ldots}$$

The saddle is at $x_c = 0$, and $S''(0) = 1-g$ is the only second-derivative contribution to the 1-loop formula. The cubic and higher terms in the cosh expansion do not affect the 1-loop result; they contribute starting at 2-loop order.
