# Trace: Etingof Exercise 5.18 (Euler char of a 2-generator group)

**Problem.** Let $\Gamma$ be the group with generators $a, b, c$ and the single defining relation $ab = ba$. Find the Euler characteristic $\chi(\Gamma)$.

## Reasoning trace

**Recognize the group.** The relation $ab = ba$ involves only $a$ and $b$; $c$ is unconstrained. So $\Gamma$ is the free product
$$\Gamma = \langle a, b \mid ab = ba\rangle * \langle c\rangle = \mathbb{Z}^2 * \mathbb{Z}.$$

**Strategy.** For torsion-free discrete groups, $\chi(\Gamma)$ equals the topological Euler characteristic of any $K(\Gamma, 1)$ (Eilenberg–MacLane space). Build a $K(\Gamma, 1)$ by free-product topology, then count cells.

**Build $K(\Gamma, 1)$.** Both factors are torsion-free with explicit classifying spaces:
- $K(\mathbb{Z}^2, 1) = T^2 = S^1 \times S^1$, the 2-torus. Cell decomposition: one 0-cell, two 1-cells, one 2-cell. $\chi(T^2) = 1 - 2 + 1 = 0$.
- $K(\mathbb{Z}, 1) = S^1$. Cells: one 0-cell, one 1-cell. $\chi(S^1) = 1 - 1 = 0$.

For free products, $K(A * B, 1) = K(A,1) \vee K(B,1)$ (wedge sum at a chosen basepoint), which is itself a $K(\pi, 1)$ when both factors are aspherical. So
$$K(\Gamma, 1) = T^2 \vee S^1.$$

**Compute $\chi$ via the wedge formula.** For pointed CW complexes, $\chi(X \vee Y) = \chi(X) + \chi(Y) - 1$ (the basepoint is identified, so one 0-cell is double-counted in $\chi(X) + \chi(Y)$ and must be subtracted). Thus
$$\chi(\Gamma) = \chi(T^2 \vee S^1) = \chi(T^2) + \chi(S^1) - 1 = 0 + 0 - 1 = -1.$$

**Cross-check via cell counting.** $T^2 \vee S^1$ has cells: one 0-cell (basepoint), three 1-cells (two from $T^2$, one from $S^1$), one 2-cell (from $T^2$). Then
$$\chi = 1 - 3 + 1 = -1. \quad\checkmark$$

**Cross-check via free-product formula for $\chi$.** For groups of finite cohomological type, $\chi(A * B) = \chi(A) + \chi(B) - 1$ (this is the group-theoretic specialization of the wedge formula above, valid because free products of torsion-free groups have classifying spaces given by wedges). $\chi(\mathbb{Z}^2) = 0$, $\chi(\mathbb{Z}) = 0$, so $\chi(\Gamma) = 0 + 0 - 1 = -1$. ✓

## Final answer

$$\boxed{\chi(\Gamma) = -1.}$$
