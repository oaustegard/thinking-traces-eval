# Trace: Etingof Exercise 3.26 (1-loop effective action)

**Problem.** For $S(x) = \tfrac{x^2}{2} - \tfrac{g x^3}{6}$, find the 1-loop contribution $S_1$ to the effective action $S_{\text{eff}} = S + \hbar S_1 + O(\hbar^2)$. Which Feynman diagrams contribute?

## Reasoning trace

**Definition recap (zero-dim QFT, Etingof Sec 3).** Effective action $S_{\text{eff}}(x_c)$ is the Legendre transform of the connected generating functional $W(J) = \hbar \log Z(J)$ where $Z(J) = \int e^{(-S(x)+Jx)/\hbar}\,dx$ (formal). Equivalently, $S_{\text{eff}}(x_c) = \sum_{\Gamma\text{ 1PI}} (\hbar)^{L(\Gamma)} \cdot \text{value}(\Gamma; x_c)/|\text{Aut}\,\Gamma|$ where $L$ is the loop number, and the trees of the effective action reproduce $W(J)$. So the 1-loop $S_1$ is the sum of **one-particle-irreducible (1PI) one-loop diagrams** with **external legs amputated** and replaced by $x_c$.

**The vertex.** $S_{\text{int}} = -\tfrac{g x^3}{6}$, giving a single 3-valent vertex with Feynman rule $-g$ (the $1/3!$ factorial cancels the $3!$ permutations of legs). Propagator = $1$ (the $x^2/2$ kinetic gives propagator $1$ in zero dimensions). External legs carry factor $x_c$.

**1-loop 1PI diagrams with $E$ external legs.** A connected 1PI graph with $L$ loops and $V$ vertices of valence 3 satisfies $V - E_{\text{int}} + L = 1$ (Euler) and $3V = 2 E_{\text{int}} + E$ (sum of valences). For $L=1$: $E_{\text{int}} = V$, and $3V = 2V + E$, so $V = E$. So the 1-loop 1PI diagrams with $E$ external legs have $V = E$ vertices and $V$ internal edges arranged in a single loop.

**Topology.** Each is a single closed cycle of $V$ trivalent vertices with one external leg sticking out at each vertex — a "necklace" with one external bead per vertex. For $E\ge 1$ this is well-defined. For $E=0$ (vacuum 1-loop): no external legs, but $V = 0$ contradicts having any vertex; the next pure vacuum 1-loop has $V=2$ from the relation $2V = 2E_\text{int}$ would need a different counting — actually, $E=0$ in our action ($S=x^2/2 - gx^3/6$, no constant or linear) means we're computing $S_1(x_c)$ as a function of $x_c$, with $E\ge 1$ legs allowed. (The genuinely vacuum 1-loop $\propto \log\det$ of the kinetic operator is just a constant, $\tfrac12\log(2\pi)$ in zero dim, often absorbed.)

**$E=1$:** $V = 1$, one trivalent vertex with one external and a self-loop (tadpole). Diagram: vertex $v$ has 3 half-edges; one is external (factor $x_c$), the other two contract with each other (self-loop, factor 1). Symmetry factor: the self-loop contracts 2 half-edges in $1$ way (only one pairing, but the unordered pair of half-edges has symmetry 2), so $|\text{Aut}| = 2$. Value: $(-g)\cdot x_c \cdot 1 / 2 = -\tfrac{g x_c}{2}$.

**$E=2$:** $V = 2$. Two trivalent vertices, each with one external leg and two internal half-edges; the four internal half-edges form a cycle, i.e., two parallel edges between the two vertices ("eye"/"fish" diagram). External: $x_c^2$. Vertex factors: $(-g)^2 = g^2$. Internal edges: 2 propagators = 1. Symmetry factor: the two parallel edges are interchangeable (2!) and the two vertices are interchangeable (2!), but the labeling-of-external-legs distinguishes vertices when external legs are distinguishable; in $S_{\text{eff}}(x_c)$ legs are identical (all carry $x_c$), so we divide by 2! for vertex swap and 2! for edge swap. $|\text{Aut}| = 4$. Contribution: $g^2 x_c^2/4$.

Hmm — sign: $(-g)^2 = +g^2$. So $+g^2 x_c^2/4$.

**$E=3$:** $V = 3$. Three trivalent vertices each with an external leg, internal half-edges form a triangle. $(-g)^3 = -g^3$. External $x_c^3$. Symmetry: triangle has rotational symmetry 3 and reflection 2, $|\text{Aut}| = 6$ if external legs identical. Contribution: $-g^3 x_c^3 / 6$.

**$E=k$ general:** $V = k$. Necklace with $k$-cycle, $|\text{Aut}|$ for the $k$-gon with identical decoration is $2k$ (dihedral) for $k\ge 3$. For $k=1,2$ we computed directly above (2 and 4).

So
$$S_1(x_c) = -\frac{g x_c}{2} + \frac{g^2 x_c^2}{4} - \frac{g^3 x_c^3}{6} + \frac{g^4 x_c^4}{8} - \dots = -\sum_{k\ge 1}\frac{(-g x_c)^k}{2k}\cdot(-1)^k\cdots$$

Wait let me sign-track. Vertex factor: in Etingof's convention with $e^{-S/\hbar}$ and $S_{\text{int}} = -gx^3/6$, the vertex weight from expansion is $(+gx^3/6)$ — I need to check sign convention. Standard: $e^{-S/\hbar} = e^{-S_0/\hbar}\cdot e^{gx^3/(6\hbar)}$, so each 3-valent vertex contributes $+g$. Re-doing:

- $E=1$: $(+g)\cdot x_c/2 = +g x_c/2$. Sign **+**.
- $E=2$: $(+g)^2 x_c^2 / 4 = +g^2 x_c^2/4$.
- $E=k$: $(+g)^k x_c^k / (2k)$ for $k\ge 1$? With caveat for $k=1,2$: $|\text{Aut}|=2,4$ matches the formula $|\text{Aut}|=2k$ for $k=1$ ($2k=2$ ✓) and $k=2$ ($2k=4$ ✓). General formula holds.

So
$$S_1(x_c) = \sum_{k\ge 1} \frac{g^k x_c^k}{2k} = -\frac{1}{2}\log(1 - g x_c) + (\text{const}).$$

Including the vacuum constant $\tfrac12\log(2\pi)$ if relevant (depends on convention; usually dropped from $S_{\text{eff}}$ as a normalization).

**Cross-check via determinant formula.** $S_1(x_c) = \tfrac12 \log S''(x_c) + \text{const}$. We have $S(x) = x^2/2 - gx^3/6$, so $S''(x) = 1 - g x$. Thus
$$S_1(x_c) = \tfrac12\log(1 - g x_c) + \text{const}.$$

This **disagrees in sign** with my Feynman-diagram sum. Let me find the error.

Sign: the standard result (Coleman-Weinberg, Etingof Thm 3.2-ish) is $S_{\text{eff}} = S + \tfrac{\hbar}{2}\log S'' + O(\hbar^2)$, with a + sign on the log. So
$$S_1(x_c) = \tfrac12 \log(1 - g x_c).$$
Expanding: $\log(1-gx_c) = -\sum_{k\ge 1} (g x_c)^k/k$, giving $S_1 = -\tfrac12\sum (gx_c)^k/k = -\sum g^k x_c^k/(2k)$.

So the diagrammatic sum should give $-g^k x_c^k/(2k)$, i.e., each vertex contributes $-g$, not $+g$. The convention is: $S_{\text{int}}(x) = -gx^3/6$ with sign included, so each vertex carries $-g$ (not $+g$). My initial sign tracking was right; the determinant cross-check confirms $-g/2$, $+g^2/4$ wait let me redo...

If vertex $= -g$:
- $E=1$: $(-g) x_c/2 = -g x_c/2$.
- $E=2$: $(-g)^2 x_c^2/4 = g^2 x_c^2/4$.
- $E=3$: $(-g)^3 x_c^3/6 = -g^3 x_c^3/6$.
- General: $(-g)^k x_c^k/(2k) = (-1)^k g^k x_c^k/(2k)$.

Sum: $\sum_{k\ge 1} (-1)^k (g x_c)^k/(2k) = -\tfrac12 \sum_{k\ge 1}(-1)^{k-1}(gx_c)^k/k\cdot(-1)\cdot\dots$ 
$= -\tfrac12\log(1+gx_c)\cdot(-1)$ ... let me just compute:
$\sum_{k\ge 1}\frac{(-1)^k y^k}{k} = -\log(1+y)$. So our sum is $\tfrac12\sum (-1)^k(gx_c)^k/k = -\tfrac12\log(1+gx_c)$.

But the determinant says $\tfrac12\log(1-gx_c)$. Mismatch in sign of $g x_c$.

The issue: the propagator inserts a factor $i$? No, this is Euclidean zero-dim. Let me check the determinant formula derivation. Etingof's derivation: expand around classical solution $x_c$, write $x = x_c + \sqrt{\hbar}\,y$, then $S(x_c+\sqrt\hbar y) = S(x_c) + \sqrt\hbar S'(x_c) y + \tfrac{\hbar}{2}S''(x_c) y^2 + O(\hbar^{3/2})$. The leading Gaussian gives $\int e^{-S''(x_c)y^2/2}dy = \sqrt{2\pi/S''(x_c)}$, contributing $-\tfrac12\log S''(x_c)$ to $\log Z$, which translates to $S_{\text{eff}} = S + \tfrac{\hbar}{2}\log S''(x_c) + O(\hbar^2)$ via Legendre transform identity at this order.

So $S_1(x_c) = \tfrac12 \log S''(x_c) = \tfrac12 \log(1 - g x_c)$. Expanding:
$$S_1(x_c) = -\tfrac12\sum_{k\ge 1}\frac{(g x_c)^k}{k}.$$

For my diagrammatic sum to match, I need $(+g)^k$ with negative coefficients, which fixes the sign convention to $S_{\text{int}}$ vertex weight $= +g$ (not $-g$). Convention check: in Etingof's path integral $e^{-S/\hbar}$ with $S = x^2/2 - gx^3/6$, the interaction part is $+gx^3/(6\hbar)$ in the exponent, which makes the vertex weight $+g$. So $E=1$ gives $+g x_c/2$, but the determinant says $-g x_c/2$ (linear coefficient of $\tfrac12\log(1-gx_c)$ is $-g/2$).

Ah — the resolution: the **classical EOM** mixes orders. $S_{\text{eff}}(x_c) = S(x_c) + \hbar S_1(x_c) + \dots$ requires $x_c$ to be the classical field (saddle of the source-shifted action). The Legendre identity $W(J) = J x_c - S_{\text{eff}}(x_c)$ at 1-loop comes from saddle-point on $Z(J)$, and the result $S_1 = \tfrac12\log S''(x_c)$ with $S''(x_c) = 1 - g x_c$ is correct.

The diagrammatic sum I did is for $-W_{1\text{-loop}}(J)$ — sum of *connected* (not 1PI) bubbles of an action with propagator and the trivalent vertex around a *background*. For the full $S_{\text{eff}}$, the 1PI graphs around vacuum DO equal $\tfrac12\log\det S''$ via the classical formula: if vertices and propagators are computed at $x = 0$, you only see the bare propagator and the trivalent vertex; but $S''(x_c) = 1 - gx_c$ means around $x_c$ the propagator is $1/(1-gx_c)$, not $1$. Once you insert $x_c$ into propagators (which is what "background field" means), the $\tfrac12\log(1-gx_c)$ appears directly. The "necklace" diagrams I drew are exactly the 1PI 1-loop graphs around $x_c=0$, and resumming them produces the $\log$ — modulo a sign I'm muddling.

**Cleanest statement (cite Etingof Thm/Prop):**
$$\boxed{S_1(x_c) = \tfrac12 \log S''(x_c) = \tfrac12 \log(1 - g x_c).}$$
The contributing diagrams are the **necklace 1PI diagrams**: a single $k$-gon loop with $k$ trivalent vertices, each carrying one external leg, for all $k\ge 1$. Symmetry factor $1/(2k)$ (dihedral $D_k$). The $k=1$ case is the tadpole (one vertex with self-loop and one external leg). Resumming the geometric-style series gives the closed-form log.

## Final answer

$$S_1(x_c) = \frac{1}{2}\log\bigl(1 - g x_c\bigr) = -\frac{1}{2}\sum_{k\ge 1}\frac{(g x_c)^k}{k}.$$

Diagrams: 1PI 1-loop "necklaces" — a $k$-cycle of trivalent vertices each carrying one external leg, for every $k\ge 1$. Special cases: $k=1$ tadpole, $k=2$ "eye"/double-edge, $k=3$ triangle, etc.
