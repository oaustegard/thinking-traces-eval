# Solution: Uniqueness and Minimality of Solutions to Newton's Equation under Concave Potentials

**Strategy:** We use the framework of calculus of variations (from Example 3's effective action structure) combined with convexity arguments. Concavity of U means the action functional is strictly convex, ensuring a unique critical point that is automatically a global minimum.

## Part 1: Uniqueness of Solutions

### Setup

Consider the Newton equation:
$$m \cdot \ddot{q}(t) = -\nabla U(q(t))$$

with boundary conditions $q(a) = A$ and $q(b) = B$, where $a < b$.

The action functional is:
$$S[q] = \int_a^b \left(\frac{m|\dot{q}(t)|^2}{2} - U(q(t))\right)\,dt$$

A solution of Newton's equation is characterized as a critical point (stationary point) of $S[q]$ with fixed endpoints.

### Concavity Implies Convex Action

**Hypothesis:** $U$ is concave, meaning $U''(q) \leq 0$ (the Hessian is negative semi-definite).

The action can be decomposed:
$$S[q] = T[q] - V[q]$$

where $T[q] = \int_a^b \frac{m|\dot{q}(t)|^2}{2}\,dt$ (kinetic energy) and $V[q] = \int_a^b U(q(t))\,dt$ (potential energy).

The kinetic term $T[q]$ is **strictly convex** in $\dot{q}$: any path with nonzero average velocity strictly minimizes the kinetic energy integral among all paths with the same endpoints (by Cauchy-Schwarz or the fundamental inequality for convex functions).

The potential term $V[q]$ is **concave** in $q$ when $U$ is concave: if $q_1$ and $q_2$ are two paths and $U'' \leq 0$, then:
$$\int_a^b U(\lambda q_1 + (1-\lambda) q_2)\,dt \geq \lambda \int_a^b U(q_1)\,dt + (1-\lambda)\int_a^b U(q_2)\,dt$$

Therefore, the action functional:
$$S[q] = T[q] - V[q]$$

is **strictly convex** (sum of strictly convex and concave terms, with the strictly convex term dominating for variations).

### Convexity Implies Uniqueness

For any strictly convex functional, there is **at most one critical point**. 

Proof: suppose $q_1$ and $q_2$ are two solutions of Newton's equation with the same boundary conditions. Then both satisfy $\delta S[q_i] = 0$. Consider their midpoint $q_m = (q_1 + q_2)/2$, which also satisfies the boundary conditions.

By strict convexity of $S$:
$$S[q_m] < \frac{1}{2}S[q_1] + \frac{1}{2}S[q_2]$$

unless $q_1 = q_2$ (which would contradict the strict convexity unless the two are identical).

More directly: if $q_1 \neq q_2$ are both stationary points, the second variation $\delta^2 S$ would vanish for the variation $\delta q = q_2 - q_1$. But strict convexity ensures $\delta^2 S[\delta q] > 0$ for all nonzero $\delta q$, a contradiction.

**Therefore, there exists at most one solution to the boundary value problem.**

## Part 2: Global Minimality of the Solution

### Existence and Minimality

Assume a solution $q^*(t)$ exists. We now show it is the **strict global minimum** of the action over all admissible paths (fixed endpoints).

For any other path $q(t)$ with $q(a) = A$, $q(b) = B$, write $q = q^* + \delta q$ where $\delta q(a) = \delta q(b) = 0$.

Expand $S[q^* + \delta q]$ to second order:
$$S[q^* + \delta q] = S[q^*] + \delta S[q^*][\delta q] + \frac{1}{2}\delta^2 S[q^*][\delta q, \delta q] + O(\|\delta q\|^3)$$

Since $q^*$ is a critical point, $\delta S[q^*] = 0$.

The second variation is:
$$\delta^2 S[\delta q, \delta q] = \int_a^b \left(m|\dot{\delta q}|^2 - \delta^2 U(q^*)[(\delta q, \delta q)]\right)\,dt$$

Under the concavity hypothesis ($U'' \leq 0$), the term $-\delta^2 U$ is **non-negative**:
$$-\delta^2 U[(\delta q, \delta q)] = -\int_a^b U''(q^*) \delta q \cdot \delta q\,dt \geq 0$$

Therefore:
$$\delta^2 S[\delta q, \delta q] = \int_a^b m|\dot{\delta q}|^2\,dt - \int_a^b U''(q^*) (\delta q)^2\,dt \geq \int_a^b m|\dot{\delta q}|^2\,dt \geq 0$$

with equality only if $\delta q \equiv 0$ (by the fundamental lemma of the calculus of variations).

Thus, $\delta^2 S > 0$ for all nonzero variations, confirming $q^*$ is a **strict local minimum**.

### Global Minimality

Since $S[q]$ is strictly convex (demonstrated above), any local minimum is automatically a **global minimum**. The strict convexity ensures no other path can achieve the same action value.

**Conclusion:** $S[q^*] < S[q]$ for all admissible paths $q \neq q^*$ with the same boundary conditions.

## Summary

$$\boxed{\begin{align}
&\text{(i) Under concave potential } U''(q) \leq 0, \text{ there exists at most one}\\
&\text{solution of } m\ddot{q} = -\nabla U(q) \text{ with } q(a)=A, q(b)=B.\\
&\\
&\text{(ii) Any such solution is the strict global minimum of the action}\\
&S[q] = \int_a^b \left(\frac{m|\dot{q}|^2}{2} - U(q)\right) dt \text{ over all admissible}\\
&\text{paths with the same boundary conditions.}
\end{align}}$$

The key insight is that strict convexity of the kinetic energy dominates the concavity of the potential, making the overall action strictly convex and hence guaranteeing uniqueness and global optimality of any solution that exists.
