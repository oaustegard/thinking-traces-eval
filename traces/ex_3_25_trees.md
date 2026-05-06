# Trace: Etingof Exercise 3.25 (EGF for 1/4-valent labeled trees)

**Problem.** Find the exponential generating function $\sum_n a_n z^n/n!$ for the numbers $a_n$ of labeled $n$-vertex trees with only 1-valent and 4-valent vertices. Express the answer via inverse functions to polynomials.

## Reasoning trace

Etingof's framework: trees in QFT are tree-level Feynman diagrams of an action with monomial vertices. For only 1- and 4-valent vertices, take the formal action with a tadpole (1-valent source) and a 4-valent vertex.

**Connected tree EGF from a perturbative action.** The standard result (Etingof Sec 3): if the action is $S(x) = \tfrac{x^2}{2} + \sum_{v\ge 1} \tfrac{g_v}{v!}\, x^v$ where $g_v$ couples the $v$-valent vertex, then the **connected tree-level effective action** (semiclassical limit, $\hbar\to 0$) is the Legendre transform of $-S$ evaluated at the source $J$:
$$W_{\text{tree}}(J) = -\inf_x\bigl(S(x) - Jx\bigr).$$
The classical equation of motion $S'(x) = J$ defines $x = x(J)$ as the inverse of the polynomial $S'$. Differentiating $W_{\text{tree}}$ yields $W'_{\text{tree}}(J) = x(J)$.

**For our problem,** vertices are 1-valent and 4-valent only. Take $g_1 = z$ (tagged-vertex weight) and $g_4 = z$ (4-valent weight, also tagged with $z$ so each vertex contributes a factor $z$). All vertices are weighted equally so the EGF is in a single variable $z$.

Wait — careful. We want to count labeled trees by total vertex count $n = (\#1\text{-valent}) + (\#4\text{-valent})$, with each vertex contributing a factor $z$. Use $S(x) = \tfrac{x^2}{2} + g_1 x + g_4 \tfrac{x^4}{4!}$ and set both $g_1 = g_4 = 1$ at the end, while attaching $z$ to each vertex of the diagram. The clean way: count by $z^{\#\text{vertices}}/\text{automorphism}$. For trees on $n$ labeled vertices the automorphism factor is 1 (labeled), so the EGF is $\sum a_n z^n/n!$.

The tree-level connected diagrams with 1 external source: take $J\partial/\partial J$ to count trees with one marked leaf, etc. But here we want **all vertices** (including 1-valent leaves) to count, with no external source — so the EGF we want is the **sum of vacuum tree diagrams** with the action where leaves are physical 1-valent vertices.

**Combinatorial setup directly.** Let $T(z)$ = EGF of *rooted* trees (rooted at a vertex of any valence) with valences in $\{1,4\}$. Standard symbolic-method translation:
- A rooted tree is either a leaf (1-valent root, no children) — contributes $z$.
- Or a 4-valent root with **3** ordered children subtrees (since one of the 4 incidences is consumed by the parent edge — but the root has no parent, so a 4-valent root has 4 children). Hmm.

Cleaner: let $R(z)$ be the EGF of trees rooted at an **edge endpoint** (so the root has degree 1 in its rooted view, i.e., one half-edge points up to the parent). Each non-root vertex has remaining valence $v-1$. Here valences are 1 and 4, so non-root vertex has 0 or 3 remaining children-edges.
$$R(z) = z + z\cdot\frac{R(z)^3}{3!} = z\left(1 + \frac{R(z)^3}{6}\right).$$
Each $z$ counts the root vertex; the $R^3/3!$ term counts the 3 unordered subtrees beneath a 4-valent root.

This is an algebraic equation: $R = z + zR^3/6$, i.e., $z = R/(1 + R^3/6) = 6R/(6 + R^3)$. So $z(R)$ is a rational function and $R(z)$ is its inverse.

**Reconstructing the unrooted EGF.** For a tree with $n$ vertices the rooting overcount: rooting at any vertex multiplies the count by $n$, so the EGF of edge-rooted trees over the edge-rooted formula and the EGF of labeled trees are related by the dissymmetry theorem for trees:
$$T(z) = T_v(z) - T_e(z) + T_{\text{ve}}(z),$$
where $T_v$ = vertex-rooted, $T_e$ = edge-rooted (unoriented edge), $T_{\text{ve}}$ = vertex-and-edge-rooted (i.e., a tree with a marked oriented edge). Standard for tree EGFs.

For our restricted-valence trees:
- $T_v(z)$: root is a vertex. If 1-valent: $z\cdot 1$ if it's the only vertex, else $z\cdot R(z)$ (one child subtree, edge-rooted). Wait, a 1-valent root has 1 incident edge, so 1 subtree below: contribution $z\cdot R(z)$ (but the special case $n=1$ is a single leaf with no edge, contributing just $z$). If 4-valent: 4 unordered subtrees, contribution $z\cdot R(z)^4/4!$.
$$T_v(z) = z + z R(z) + \frac{z R(z)^4}{24}.$$
Wait, the $z$ alone is the $n=1$ tree (single leaf). But we should be careful — in the $z R$ term, $R$ corresponds to a subtree which could be a single leaf, in which case the whole tree has 2 vertices. So $T_v$ counts: single leaf ($n=1$), edge with two endpoints, etc. Actually the formula $zR$ already includes "subtree = leaf only," so $z R$ represents trees where the root is 1-valent and connected to one subtree. The $n=1$ case (isolated vertex) is degenerate and shouldn't be counted as a 1-valent vertex (it has no edge), but Etingof's framework typically excludes the $n=1$ tree or includes it only formally. Let's assume $n\ge 2$ and drop the bare $z$.

$$T_v(z) = z R(z) + \frac{z R(z)^4}{24}.$$

- $T_e(z)$: root is an unoriented edge. An edge has two endpoints; remove the edge, get two rooted-edge trees, but they're unordered:
$$T_e(z) = \frac{R(z)^2}{2}.$$

- $T_{\text{ve}}(z)$: oriented edge = ordered pair of edge-rooted subtrees: $T_{\text{ve}}(z) = R(z)^2$.

Dissymmetry: $T(z) = T_v - T_e + T_{\text{ve}}$ does NOT directly give the unrooted EGF — the standard dissymmetry theorem for trees says
$$T = T_v + T_e - T_{ve}$$
(unrooted = vertex-rooted + edge-rooted - oriented-edge-rooted). Let me re-derive: an unrooted tree corresponds to an averaging over rootings. The clean statement (Bergeron-Labelle-Leroux): for tree species, $T + T^{\bullet-\bullet} = T^\bullet + T^{-}$, where $T^\bullet$ is vertex-rooted, $T^-$ is edge-rooted (unoriented), $T^{\bullet-\bullet}$ is oriented-edge-rooted. Solving:
$$T = T^\bullet + T^- - T^{\bullet-\bullet}.$$

So
$$T(z) = z R + \frac{z R^4}{24} + \frac{R^2}{2} - R^2 = zR + \frac{zR^4}{24} - \frac{R^2}{2}.$$

We can simplify using $z = 6R/(6+R^3)$, equivalently $z(6+R^3) = 6R$, so $zR^3 = 6R - 6z = 6(R-z)$, hence $zR^4 = 6R(R-z)$ and $zR = R^2 - zR^3/6 \cdot R/(\ldots)$ — actually cleaner: $zR^3 = 6(R-z)$ gives $zR^4/24 = R(R-z)/4$.

Also $zR = R\cdot 6R/(6+R^3) = 6R^2/(6+R^3)$.

So
$$T(z) = \frac{6R^2}{6+R^3} + \frac{R(R-z)}{4} - \frac{R^2}{2}.$$

This is the EGF expressed via $R = R(z)$, which is the **inverse of the rational function $z = 6R/(6+R^3)$**. Equivalently, $R$ is the inverse of the polynomial-fraction relation; one can clear denominators: $R$ satisfies $R^4 z + 6R z - 6R = 0$, but we wanted "inverse of polynomial," so write the relation as $z = 6R/(6+R^3)$ — i.e., $R$ is determined by inverting $w \mapsto 6w/(6+w^3)$.

**Final answer.**

Define $R(z)$ implicitly by
$$z = \frac{6R}{6 + R^3} \qquad (\text{equivalently } R = z + \tfrac{1}{6}zR^3).$$

Then
$$\sum_{n\ge 2} a_n \frac{z^n}{n!} = T(z) = z R(z) + \frac{z\, R(z)^4}{24} - \frac{R(z)^2}{2}.$$

The expression "inverse functions to polynomials" refers to $R$ being the compositional inverse of the relation above (a rational function whose numerator and denominator are polynomials of degree $\le 4$).

## Final answer

$$T(z) = z R + \frac{z R^4}{24} - \frac{R^2}{2}, \quad\text{where } R = R(z) \text{ solves } R = z\bigl(1 + \tfrac{R^3}{6}\bigr).$$
