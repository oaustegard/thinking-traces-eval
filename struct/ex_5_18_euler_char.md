# T³-Struct: Etingof Exercise 5.18 (Euler characteristic of a 2-generator group)

Problem: Find the Euler characteristic $\chi(\Gamma)$ where $\Gamma = \langle a, b, c \mid ab = ba \rangle$.

Step 1: **Identify the group structure.** The relation $ab = ba$ involves only $a$ and $b$; $c$ is free. Recognize as a free product: $\Gamma = \mathbb{Z}^2 * \mathbb{Z}$.

Step 2: **Recall classifying space for free products.** For torsion-free groups, $\chi(\Gamma)$ equals the topological Euler characteristic of a $K(\Gamma, 1)$. For free products, $K(A * B, 1) = K(A, 1) \vee K(B, 1)$ (wedge sum).

Step 3: **Compute classifying spaces of factors.** $K(\mathbb{Z}^2, 1) = T^2 = S^1 \times S^1$ with cell decomposition: one 0-cell, two 1-cells, one 2-cell; $\chi(T^2) = 0$. $K(\mathbb{Z}, 1) = S^1$ with: one 0-cell, one 1-cell; $\chi(S^1) = 0$.

Step 4: **Form the wedge.** $K(\Gamma, 1) = T^2 \vee S^1$, obtained by identifying a basepoint.

Step 5: **Apply wedge formula.** For pointed CW complexes, $\chi(X \vee Y) = \chi(X) + \chi(Y) - 1$ (basepoint double-counted, subtract once).

Step 6: **Calculate.** $\chi(\Gamma) = 0 + 0 - 1 = -1$.

Step 7: **Verify by cell count.** $T^2 \vee S^1$ has one 0-cell, three 1-cells (two from $T^2$, one from $S^1$), one 2-cell (from $T^2$). Check: $1 - 3 + 1 = -1$. ✓

Answer: $\boxed{\chi(\Gamma) = -1}$
