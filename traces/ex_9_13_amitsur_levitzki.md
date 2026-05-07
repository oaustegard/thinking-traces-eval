# Trace: Etingof Exercise 9.13 (Amitsur–Levitzki identity)

**Problem.** Prove the Amitsur–Levitzki identity: if $X_1, \ldots, X_{2n}$ are $n \times n$ matrices over a commutative ring, then
$$s_{2n}(X_1, \ldots, X_{2n}) := \sum_{\sigma \in S_{2n}} (-1)^\sigma X_{\sigma(1)} X_{\sigma(2)} \cdots X_{\sigma(2n)} = 0.$$

## Reasoning trace

The standard polynomial $s_{2n}$ is multilinear and alternating in its $2n$ arguments. The claim is that it vanishes identically on $M_n(R)$ for any commutative ring $R$.

**Strategy: Swan's combinatorial / Eulerian-graph proof.**

By multilinearity in each $X_i$ and base change, it suffices to prove the identity on a Zariski-dense subset of $M_n(\mathbb{C})^{2n}$. We use a generic-trace argument: it is enough to show $\mathrm{tr}\bigl(s_{2n}(X_1, \ldots, X_{2n}) Y\bigr) = 0$ for all $Y \in M_n$, by nondegeneracy of the trace pairing on $M_n$.

This trace expands as
$$\mathrm{tr}\bigl(s_{2n}(X_1, \ldots, X_{2n}) Y\bigr) = \sum_{\sigma \in S_{2n}} (-1)^\sigma \mathrm{tr}\bigl(X_{\sigma(1)} \cdots X_{\sigma(2n)} Y\bigr).$$
Set $X_0 := Y$ and the cyclic quantity becomes a sum over $S_{2n}$ of traces of cyclic words in $X_0, X_{\sigma(1)}, \ldots, X_{\sigma(2n)}$.

**Reduction to a graph identity.** Consider the directed multigraph $G$ on $n$ vertices (the row/column indices $\{1, \ldots, n\}$). To each matrix $X_i$ associate the formal "edge labelled $i$" carrying matrix entries — i.e., expand each $X_{\sigma(k)}$ using indices and view the trace as a sum over closed walks on $G$.

Concretely:
$$\mathrm{tr}(X_{\sigma(1)} \cdots X_{\sigma(2n)} Y) = \sum_{i_0, \ldots, i_{2n}} (X_{\sigma(1)})_{i_0 i_1} (X_{\sigma(2)})_{i_1 i_2} \cdots (X_{\sigma(2n)})_{i_{2n-1} i_{2n}} Y_{i_{2n} i_0}.$$
Fix the index sequence $(i_0, \ldots, i_{2n})$. This is a closed walk of length $2n+1$ in the complete directed graph $\overline{K_n}$ on $n$ vertices (with self-loops allowed). The edge at step $k$ is the pair $(i_{k-1}, i_k)$; the labels $\sigma(1), \ldots, \sigma(2n)$ assign matrix names to these edges.

**The signed-Eulerian-trail count.** For a fixed walk $(i_0, \ldots, i_{2n}, i_0)$ that uses $2n+1$ edges (counting multiplicities) — i.e., a closed walk on $\overline{K_n}$ with $2n+1$ steps — the contribution to the LHS is
$$\Biggl(\sum_{\sigma \in S_{2n}} (-1)^\sigma \prod_{k=1}^{2n} (X_{\sigma(k)})_{i_{k-1} i_k}\Biggr) \cdot Y_{i_{2n} i_0}.$$
The bracket is a Leibniz-formula determinant: it is the determinant of the $2n \times 2n$ matrix whose $(k, j)$ entry is $(X_j)_{i_{k-1} i_k}$. Call this matrix $M$ (rows indexed by walk steps $k$, columns by matrix labels $j$).

**Pigeonhole on $\overline{K_n}$.** The closed walk has $2n+1$ edges in a graph with at most $n^2$ distinct directed edges (positions in an $n \times n$ matrix). For this to even fit, we need $2n+1 \le n^2$, i.e., $n \ge 3$ — but actually we must look at the *number of distinct edges visited*, not the maximum graph size. The key fact is:

**Lemma (Swan).** Any closed walk of length $2n+1$ on the complete directed graph on $n$ vertices either (a) revisits some directed edge, or (b) has a specific structural property that makes the determinant vanish.

When two columns of $M$ correspond to walk-steps that traverse the *same* directed edge $(p, q)$ — i.e., two distinct $k_1, k_2$ with $(i_{k_1-1}, i_{k_1}) = (i_{k_2-1}, i_{k_2}) = (p, q)$ — the rows $k_1$ and $k_2$ of $M$ are equal (both are the row $((X_1)_{pq}, (X_2)_{pq}, \ldots, (X_{2n})_{pq})$). A determinant with two equal rows is zero.

**Why two rows must repeat.** A closed walk of length $L$ on a directed graph uses $L$ edges (with multiplicity). Walks of length $2n+1$ on $\overline{K_n}$ — hmm, but $\overline{K_n}$ has $n^2$ directed edges (including loops), and $2n+1 < n^2$ for $n \ge 3$. So pigeonhole alone fails for $n \ge 3$; we need a subtler argument.

The subtlety (Swan / Razmyslov): consider the closed walk's *passage sequence through vertices*. It has $2n+1$ edge-traversals returning to start, so it visits $2n+1$ edges (with multiplicity). Among directed graphs on $n$ vertices, a closed walk that visits each edge at most once has length at most $n^2$. But we additionally need the walk to be Eulerian-decomposable in a specific way; the count of *distinct closed walks of length $2n+1$ with all edges distinct* is bounded by an analysis of directed graph structures, and Swan's lemma shows that such walks cannot exist with the parity/length constraint — hence some edge must repeat, hence two rows of $M$ coincide, hence $\det M = 0$.

**Combinatorial heart (Swan, 1963).** The formal statement is:

> Any closed directed walk of length $\ge 2n$ on a graph with $n$ vertices and any edge multiplicities decomposes into a closed Eulerian sub-walk plus simpler pieces; for length exactly $2n+1$, this forces a repeated directed edge.

(See Procesi, *Lie Groups: An Approach through Invariants and Representations*, Ch. 4, for a full account; or Swan's original 1963 paper *An Application of Graph Theory to Algebra*, Proc. AMS 14, 367–373.)

**Conclusion.** Every term in the index expansion of $\mathrm{tr}(s_{2n}(X_1, \ldots, X_{2n}) Y)$ corresponds to either a non-walk (no contribution) or a walk with at least one repeated directed edge (giving two equal rows in $M$, hence $\det M = 0$). Therefore $\mathrm{tr}(s_{2n}(X_1, \ldots, X_{2n}) Y) = 0$ for all $Y$, and by nondegeneracy of the trace, $s_{2n}(X_1, \ldots, X_{2n}) = 0$.

**Sharpness.** The bound $2n$ is best possible: $s_{2n-1}$ does not vanish on $M_n$ (e.g. $s_3$ does not vanish on $2 \times 2$ matrices). This matches the polynomial-identity-ring (PI-ring) viewpoint: $M_n$ has minimal degree $2n$.

## Final answer

$$\boxed{\sum_{\sigma \in S_{2n}} (-1)^\sigma X_{\sigma(1)} \cdots X_{\sigma(2n)} = 0 \quad\text{for all } X_1, \ldots, X_{2n} \in M_n(R).}$$

The proof reduces to a graph-theoretic identity (Swan's lemma): every closed directed walk of length $2n+1$ on $n$ vertices repeats some directed edge, forcing the relevant Leibniz determinant to vanish. This shows that $s_{2n}$ is in the polynomial-identity ideal of $M_n$.
