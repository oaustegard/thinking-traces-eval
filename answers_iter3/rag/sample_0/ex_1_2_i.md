# Solution to ex_1_2_i: Uniqueness and Minimality via Concavity

## Retrieved Examples and Relevance

**Example 1: ex_2_14_wallis (steepest descent on Wallis integral)** — Not relevant. This is asymptotic analysis of integrals; the current problem is variational mechanics.

**Example 2: ex_5_18_euler_char (Euler characteristic of free products)** — Not relevant. This is algebraic topology.

**Example 3: ex_2_20_morse (Morse coordinates and local diffeomorphisms)** — Marginally relevant in that it uses second-derivative analysis to establish smoothness and non-degeneracy, but does not address variational mechanics or concavity arguments.

**Assessment:** The retrieved examples are largely off-domain. The problem concerns the classical variational principle with concave potentials, which is not covered in the retrieval set. I will solve from first principles, noting that the argument is a standard calculus-of-variations + concavity combination.

---

## Solution

### Part 1: Uniqueness of Solutions

**Setup:** We seek solutions to the Newton equation
$$m \ddot{q}(t) = -\nabla U(q(t))$$
with Dirichlet boundary conditions $q(a) = A$ and $q(b) = B$.

**Proof of uniqueness:** Suppose $q_1(t)$ and $q_2(t)$ are two solutions satisfying the same boundary conditions. Define the difference $w(t) := q_1(t) - q_2(t)$. Then:
- $w(a) = w(b) = 0$ (both solutions agree at the boundaries)
- $m\ddot{w}(t) = -\nabla U(q_1(t)) + \nabla U(q_2(t))$ for all $t \in [a,b]$.

By the mean value theorem (or more precisely, the integral form), for each component $w_i$ and points $q_1, q_2$,
$$U(q_1) - U(q_2) = \int_0^1 U(q_2 + s(q_1 - q_2)) \cdot (q_1 - q_2) ds.$$

For a vector field interpretation, define the Hessian as a quadratic form:
$$\nabla U(q_1) - \nabla U(q_2) = \int_0^1 U''(q_2 + s(q_1 - q_2)) (q_1 - q_2) ds.$$

Since $U$ is concave, $U'' \leq 0$ as a quadratic form, meaning
$$(\nabla U(q_1) - \nabla U(q_2)) \cdot (q_1 - q_2) = \int_0^1 (q_1 - q_2)^T U''(\cdots) (q_1 - q_2) ds \leq 0.$$

Thus
$$m \ddot{w} \cdot w = -[\nabla U(q_1) - \nabla U(q_2)] \cdot w \geq 0.$$

Integrate from $a$ to $b$:
$$m \int_a^b \ddot{w} \cdot w \, dt = m\int_a^b \ddot{w} \cdot w \, dt.$$

Integrate by parts: $\int \ddot{w} \cdot w \, dt = [w \cdot \dot{w}]_a^b - \int |\dot{w}|^2 dt = -\int |\dot{w}|^2 dt$ (since $w(a) = w(b) = 0$).

Thus
$$-m\int_a^b |\dot{w}|^2 dt \geq 0,$$
which implies $\int_a^b |\dot{w}|^2 dt \leq 0$. Since $|\dot{w}|^2 \geq 0$, we have $\dot{w} \equiv 0$, so $w$ is constant. But $w(a) = 0$, so $w \equiv 0$ on $[a,b]$.

**Conclusion:** $q_1 = q_2$. The solution is unique.

### Part 2: Minimality of the Action

**Definition:** The action (Hamilton functional) is
$$S[q] = \int_a^b \left(\frac{m}{2}|\dot{q}(t)|^2 - U(q(t))\right) dt.$$

**Proof:** Let $q^*$ be the unique solution (the one satisfying Newton's equations). Let $q = q^* + \eta$ be any other path with $q(a) = A$ and $q(b) = B$, where $\eta(a) = \eta(b) = 0$.

Expand $S[q^* + \eta]$:
$$S[q^* + \eta] = \int_a^b \left[\frac{m}{2}|\dot{q}^* + \dot{\eta}|^2 - U(q^* + \eta)\right] dt.$$

$$= \int_a^b \left[\frac{m}{2}|\dot{q}^*|^2 - U(q^*)\right] dt + \int_a^b \left[m\dot{q}^* \cdot \dot{\eta} - (U(q^* + \eta) - U(q^*))\right] dt$$
$$+ \int_a^b \frac{m}{2}|\dot{\eta}|^2 dt.$$

The second integral is the **first variation**. Expand $U(q^* + \eta) - U(q^*) = \nabla U(q^*) \cdot \eta + O(\eta^2)$:
$$\delta S = \int_a^b [m\dot{q}^* \cdot \dot{\eta} - \nabla U(q^*) \cdot \eta] dt.$$

Integrate the first term by parts:
$$m\int_a^b \dot{q}^* \cdot \dot{\eta} \, dt = m[q^* \cdot \eta]_a^b - m\int_a^b \ddot{q}^* \cdot \eta \, dt = -m\int_a^b \ddot{q}^* \cdot \eta \, dt$$
(since $\eta(a) = \eta(b) = 0$).

Thus
$$\delta S = -\int_a^b (m\ddot{q}^* + \nabla U(q^*)) \cdot \eta \, dt = 0$$

by the Euler-Lagrange equation (Newton's law). So the first variation vanishes, confirming $q^*$ is a critical point.

**Second variation:** Expand $U(q^* + \eta) - U(q^*) - \nabla U(q^*) \cdot \eta = \frac{1}{2}\eta^T U''(q^* + \theta\eta) \eta$ for some $\theta \in [0,1]$. Near $q^*$, this is approximately $\frac{1}{2}\eta^T U''(q^*) \eta$.

Since $U$ is concave, $U''(q^*) \leq 0$. Thus
$$\delta^2 S = \int_a^b \left[\frac{m}{2}|\dot{\eta}|^2 - \frac{1}{2}\eta^T U''(q^*) \eta\right] dt.$$

With $-U''(q^*) \geq 0$ (negative of $U''$), we have
$$\delta^2 S = \int_a^b \left[\frac{m}{2}|\dot{\eta}|^2 + \frac{1}{2}\eta^T (-U''(q^*)) \eta\right] dt \geq 0.$$

Equality holds only if $\eta \equiv 0$.

**Conclusion:** $\delta^2 S > 0$ for all nonzero $\eta$, so $q^*$ is a **strict global minimum** of the action.

---

## Summary

The concavity of $U$ (i.e., $U'' \leq 0$) ensures:
1. **Uniqueness:** The integrand of $m\ddot{w} \cdot w$ is nonnegative, and integrating with boundary conditions $w(a) = w(b) = 0$ forces $w \equiv 0$.
2. **Minimality:** The second variation $\delta^2 S$ is strictly positive for all perturbations, making $q^*$ a global minimizer of the action functional.

These are consequences of convexity (of the kinetic term) combined with concavity (of the potential term) in the action.
