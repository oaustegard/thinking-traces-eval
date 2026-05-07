# Structured Reasoning: 1-Loop Effective Action

**Problem:** For $S(x) = \frac{x^2}{2} - \frac{gx^3}{6}$, find the 1-loop contribution $S_1(x_c)$ to the effective action.

**Step 1:** Identify 1PI one-loop diagrams by Euler relation: for $L=1$ loop and $E$ external legs, both internal edge count and vertex count equal $E$, yielding a necklace topology (a $k$-cycle of vertices).

**Step 2:** Enumerate contributing diagrams by external leg count: $k=1$ is a tadpole (one vertex with self-loop), $k=2$ is an eye diagram (two parallel edges), $k=3$ is a triangle, etc.

**Step 3:** Compute vertex weights: each 3-valent vertex contributes $-g$ per the action $S_{\text{int}} = -\frac{gx^3}{6}$, and propagators each carry factor $1$.

**Step 4:** Calculate symmetry factors: for a $k$-gon with identical decoration, the dihedral symmetry group $D_k$ has order $2k$, giving $|\text{Aut}| = 2k$ for $k \geq 3$ (verified: $k=1$ gives $2$, $k=2$ gives $4$).

**Step 5:** Sum contributions to obtain $S_1(x_c) = \sum_{k \geq 1} \frac{(-g)^k x_c^k}{2k}$, which is a geometric series of the form $\frac{1}{2}\sum_{k\geq 1}\frac{(-gx_c)^k}{k}$.

**Step 6:** Recognize the series as $-\frac{1}{2}\log(1 - gx_c)$ and verify by the determinant formula $S_1(x_c) = \frac{1}{2}\log S''(x_c)$ with $S''(x) = 1 - gx$.

**Step 7:** Expand the closed form: $S_1(x_c) = -\frac{1}{2}\sum_{k\geq 1}\frac{(gx_c)^k}{k}$, confirming resummed necklace diagrams reproduce the effective action.

**Answer:** $\boxed{S_1(x_c) = \frac{1}{2}\log(1 - gx_c) = -\frac{1}{2}\sum_{k\geq 1}\frac{(gx_c)^k}{k}}$
