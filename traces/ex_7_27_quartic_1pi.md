# Trace: Etingof Exercise 7.27 (1PI 2-point function for quartic oscillator)

**Problem.** Calculate the 1-particle irreducible 2-point function $\Sigma(t_1,t_2)$ for a quantum particle with potential $U(q) = \tfrac{m^2 q^2}{2} + \tfrac{g q^4}{24}$.

## Reasoning trace

**Setup.** Euclidean action $S[q] = \int dt \bigl(\tfrac12 \dot q^2 + \tfrac{m^2}{2} q^2 + \tfrac{g}{24} q^4\bigr)$. Free propagator (mass $m$, coincident-time and unequal-time):
$$G_0(t_1, t_2) = \langle q(t_1) q(t_2)\rangle_0 = \frac{1}{2m} e^{-m|t_1 - t_2|}.$$

Feynman rules: each $q^4$ vertex carries weight $-g$ (from $-S_{\text{int}}/\hbar$ expansion, with $1/4!$ from the action canceling the $4!$ leg-permutation count up to symmetry factors). External legs amputated (the 1PI part has them stripped).

**Definition recap.** The full 2-point function $G_2(t_1, t_2) = \langle q(t_1) q(t_2)\rangle$ relates to the 1PI 2-point function (self-energy) $\Sigma$ by Dyson's equation:
$$G_2 = G_0 + G_0 \star \Sigma \star G_0 + G_0 \star \Sigma \star G_0 \star \Sigma \star G_0 + \cdots = (G_0^{-1} - \Sigma)^{-1}.$$
$\Sigma$ is the sum of all *connected* Feynman diagrams with two external legs that **cannot be disconnected by cutting a single internal line**. The two external legs are amputated (no external-leg propagators).

**Order $g^0$ (free theory).** $\Sigma^{(0)} = 0$. (No vertices, nothing to be 1PI about.)

**Order $g^1$ (1-loop).** Diagrams with one $q^4$ vertex and 2 external legs.

The vertex has 4 half-edges. Two are external (legs to $t_1, t_2$); the remaining two contract with each other to form a single closed loop ("tadpole" / "figure-eight" diagram on the 2-point function).

Combinatorial weight:
- $\binom{4}{2} = 6$ ways to choose which 2 of the 4 vertex legs are external (ordered as leg-to-$t_1$, leg-to-$t_2$ — but legs are identical, so divide by $2!$ for the unordered external pair: $6 / 2 = 3$ distinct pairings... wait: actually the 4 legs are *interchangeable* in the action's $q^4/4!$, so the $\binom{4}{2} \cdot 2!$ assignments to external positions and the $2!$ for the closed self-loop are absorbed by the $4!$ in the denominator).

Cleanest: the symmetry factor for this graph is $S = 2$ (the closed loop has a $\mathbb{Z}_2$ symmetry from interchanging the two ends of the loop edge). So
$$\Sigma^{(1)}(t_1, t_2) = (-g) \cdot \frac{1}{S} \cdot \delta(t_1 - t_v)\,\delta(t_2 - t_v)\, G_0(t_v, t_v),$$
integrated over the vertex time $t_v$. Performing the $\delta$-integration:
$$\Sigma^{(1)}(t_1, t_2) = -\frac{g}{2} \, G_0(t_1, t_1) \, \delta(t_1 - t_2) = -\frac{g}{2} \cdot \frac{1}{2m} \cdot \delta(t_1 - t_2) = -\frac{g}{4m} \, \delta(t_1 - t_2).$$

(Recall $G_0(t,t) = 1/(2m)$.) The result is local in time, as expected for a one-vertex contribution at quartic interaction.

**Interpretation.** $\Sigma^{(1)} \propto \delta(t_1 - t_2)$ acts as a **mass renormalization**: in the Dyson equation, this shifts the effective mass-squared by $\Delta(m^2) = g/(4m) \cdot 2 = g/(2m)$ (the factor of 2 from the conventional $m^2/2$ kinetic vs $m^2$ in the inverse propagator). To leading order, the dressed propagator is
$$G(t_1, t_2) \approx \frac{1}{2 m_{\text{eff}}} e^{-m_{\text{eff}} |t_1 - t_2|}, \quad m_{\text{eff}}^2 = m^2 + \frac{g}{2m} + O(g^2).$$

**Order $g^2$ (2-loop).** Two-vertex 1PI diagrams contributing to $\Sigma$:
- **Sunset ("setting sun"):** two vertices connected by *three* internal propagators, two external legs (one on each vertex). Internal structure: two vertices each have 2 internal half-edges going to the other, plus a third edge — wait, vertices are 4-valent. So at each vertex: 1 external leg + 3 internal half-edges. Three internal propagators connect the two vertices. This is 1PI (cutting any single internal line leaves it connected via the other two).
- **Double tadpole on a single propagator line:** two separate tadpoles each on a single external leg — but this is *not* 1PI (cutting the propagator between them disconnects). Actually this graph is reducible. It does NOT contribute to $\Sigma$; it's a $\Sigma^{(1)} \star G_0 \star \Sigma^{(1)}$ piece of $G_2$, already captured by Dyson.
- **Double tadpole within one external leg:** one vertex has two self-loops? No — that doesn't preserve valence ($4 - 4 = 0$ external legs).

Counting more carefully: the only 1PI 2-loop 2-point diagram with quartic vertices is the sunset.

Sunset symmetry factor: the 3 parallel internal edges between the two vertices have $S_3$-symmetry → factor $3!$. So $S_{\text{sunset}} = 3! = 6$.

$$\Sigma^{(2)}_{\text{sunset}}(t_1, t_2) = (-g)^2 \cdot \frac{1}{6} \int dt_v \, G_0(t_1, t_v)\, [G_0(t_v, t_v')]^3 \, G_0(t_v', t_2)$$

— wait, the sunset has 2 vertex times $t_v, t_v'$ and the 3 internal propagators connect them, so it's:
$$\Sigma^{(2)}_{\text{sunset}}(t_1, t_2) = \frac{g^2}{6} \int dt_v \, dt_{v'} \, \delta(t_1 - t_v) \, [G_0(t_v, t_{v'})]^3 \, \delta(t_{v'} - t_2) = \frac{g^2}{6} \, [G_0(t_1, t_2)]^3.$$

Substituting $G_0(t_1, t_2) = e^{-m|t_1-t_2|}/(2m)$:
$$\Sigma^{(2)}_{\text{sunset}}(t_1, t_2) = \frac{g^2}{6 \cdot 8 m^3} \, e^{-3m|t_1-t_2|} = \frac{g^2}{48 m^3} \, e^{-3 m |t_1-t_2|}.$$

This is **non-local** in time (in contrast to the $g^1$ tadpole's $\delta$-function locality), reflecting that 2-loop self-energy carries genuine momentum dependence in higher-dim QFT (here in QM, "momentum" = energy and the $e^{-3m|\cdot|}$ structure comes from 3 propagators in series).

**Total 1PI 2-point through order $g^2$.**
$$\boxed{\;\Sigma(t_1, t_2) = -\frac{g}{4m}\,\delta(t_1 - t_2) + \frac{g^2}{48 m^3}\, e^{-3m|t_1-t_2|} + O(g^3).\;}$$

The $O(g^1)$ term is a local mass renormalization. The $O(g^2)$ sunset is the leading non-trivial momentum-dependent self-energy. Higher-order ($g^3$, $g^4$, ...) include nested sunsets, "bird tracks," and other multi-loop 1PI topologies; the symmetry factors grow combinatorially.

## Final answer

$$\Sigma(t_1, t_2) = -\frac{g}{4m}\,\delta(t_1 - t_2) \;+\; \frac{g^2}{48 m^3}\, e^{-3m|t_1-t_2|} \;+\; O(g^3).$$

The leading $g^1$ piece renormalizes the mass: $m_{\text{eff}}^2 = m^2 + g/(2m) + O(g^2)$. The $g^2$ "sunset" diagram contributes the first non-local (momentum-dependent) correction.
