# T³-Struct: Etingof Exercise 9.13 (Amitsur–Levitzki identity)

Problem: Prove that the standard polynomial $s_{2n}(X_1, \ldots, X_{2n}) := \sum_{\sigma \in S_{2n}} (-1)^\sigma X_{\sigma(1)} \cdots X_{\sigma(2n)} = 0$ for all $n \times n$ matrices over a commutative ring.

Step 1: **Use trace argument by nondegeneracy.** By multilinearity and the nondegeneracy of the trace pairing on $M_n$, it suffices to show $\mathrm{tr}(s_{2n}(X_1, \ldots, X_{2n}) Y) = 0$ for all $Y$.

Step 2: **Expand the trace.** $\mathrm{tr}(s_{2n}(X_1, \ldots, X_{2n}) Y) = \sum_{\sigma \in S_{2n}} (-1)^\sigma \mathrm{tr}(X_{\sigma(1)} \cdots X_{\sigma(2n)} Y)$, a sum of traces of cyclic words.

Step 3: **Interpret as closed walks on a directed graph.** Expand each $\mathrm{tr}(X_{\sigma(1)} \cdots X_{\sigma(2n)} Y)$ by matrix indices. A term corresponds to a closed walk of length $2n+1$ in the complete directed graph $\overline{K_n}$ on $n$ vertices, where edges are labeled by the matrix indices.

Step 4: **Identify the determinant structure.** The sum over $\sigma \in S_{2n}$ with signs $(-1)^\sigma$ is a Leibniz determinant: $\det M$, where $M$ is a $2n \times 2n$ matrix with rows indexed by walk steps and columns by matrix labels, entry $(k, j)$ being $(X_j)_{i_{k-1} i_k}$.

Step 5: **Apply Swan's repeated-edge lemma.** A closed walk of length $2n+1$ on $n$ vertices must revisit some directed edge. When two walk steps use the same directed edge $(p, q)$, the corresponding rows of $M$ are identical (both contain entries from the same matrix position $(p, q)$).

Step 6: **Conclude determinant vanishes.** A determinant with two equal rows is zero, so every term in the index expansion contributes zero.

Step 7: **Deduce the identity.** $\mathrm{tr}(s_{2n}(X_1, \ldots, X_{2n}) Y) = 0$ for all $Y$; by nondegeneracy of trace, $s_{2n}(X_1, \ldots, X_{2n}) = 0$.

Answer: $\boxed{\sum_{\sigma \in S_{2n}} (-1)^\sigma X_{\sigma(1)} \cdots X_{\sigma(2n)} = 0}$
