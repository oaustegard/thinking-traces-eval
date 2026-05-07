Problem: Calculate the 1-particle irreducible 2-point function $\Sigma(t_1,t_2)$ for a quantum particle with potential $U(q) = \tfrac{m^2 q^2}{2} + \tfrac{g q^4}{24}$.

Step 1: Establish Euclidean action $S[q] = \int dt \bigl(\tfrac12 \dot q^2 + \tfrac{m^2}{2} q^2 + \tfrac{g}{24} q^4\bigr)$ and free propagator $G_0(t_1, t_2) = \frac{1}{2m} e^{-m|t_1 - t_2|}$ with Feynman rule: each $q^4$ vertex carries weight $-g$.

Step 2: Apply Dyson's equation: $G_2 = (G_0^{-1} - \Sigma)^{-1}$, where $\Sigma$ is the sum of all 1PI (two-external-leg, amputated) diagrams.

Step 3: Compute $\Sigma^{(0)} = 0$ (free theory has no vertices).

Step 4: At $O(g^1)$, draw the one-vertex 1PI diagram: a single $q^4$ vertex with two external legs (at $t_1, t_2$) and two internal legs forming a closed loop. Symmetry factor $S = 2$ (loop $\mathbb{Z}_2$ symmetry). Integrate over vertex time to get $\Sigma^{(1)}(t_1, t_2) = -\frac{g}{4m} \, \delta(t_1 - t_2)$.

Step 5: Recognize $\Sigma^{(1)} \propto \delta(t_1 - t_2)$ acts as mass renormalization, shifting $m_{\text{eff}}^2 = m^2 + \frac{g}{2m} + O(g^2)$.

Step 6: At $O(g^2)$, identify the unique 1PI 2-loop 2-point diagram: the sunset (two vertices connected by three parallel internal propagators, one external leg on each vertex). Symmetry factor $S_{\text{sunset}} = 6$ (permutations of 3 edges). Compute $\Sigma^{(2)}_{\text{sunset}}(t_1, t_2) = \frac{g^2}{6} \, [G_0(t_1, t_2)]^3 = \frac{g^2}{48 m^3} \, e^{-3m|t_1-t_2|}$.

Step 7: The $O(g^2)$ sunset is non-local in time (exponential $e^{-3m|\cdot|}$ rather than $\delta$-function), reflecting genuine momentum dependence from the three propagators in series.

Answer: $\boxed{\Sigma(t_1, t_2) = -\frac{g}{4m}\,\delta(t_1 - t_2) + \frac{g^2}{48 m^3}\, e^{-3m|t_1-t_2|} + O(g^3)}$
