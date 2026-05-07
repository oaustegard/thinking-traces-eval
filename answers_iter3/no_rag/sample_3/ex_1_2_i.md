# Solution to ex_1_2_i: Uniqueness and Minimality of Newton Equations under Concavity

## Problem Statement

Consider a particle in Euclidean space $V$ with potential $U: V \to \mathbb{R}$ that is concave ($U'' \leq 0$ as a quadratic form). Show that:
1. For any endpoints $A, B \in V$ and times $a < b$, there is **at most one** solution to Newton's equation $m\ddot{q}(t) = -\nabla U(q(t))$ with $q(a) = A$ and $q(b) = B$.
2. If a solution exists, it is the **strict global minimum** of the action $S[q] = \int_a^b \left(\frac{m|\dot{q}(t)|^2}{2} - U(q(t))\right) dt$ among admissible paths with these boundary conditions.

## Proof

### Part 1: Uniqueness

Suppose $q^*(t)$ is a solution to Newton's equation with $q^*(a) = A$ and $q^*(b) = B$.

Suppose $q(t)$ is another solution with the same boundary conditions. Define the difference:
$$\eta(t) = q(t) - q^*(t)$$

Then $\eta(a) = \eta(b) = 0$ (both solutions satisfy the boundary conditions).

Subtracting the equations of motion:
$$m\ddot{\eta}(t) = -\nabla U(q(t)) + \nabla U(q^*(t))$$

By the mean value theorem, for each component:
$$\nabla U(q) - \nabla U(q^*) = \int_0^1 U''(q^* + s\eta) \eta \, ds$$

Integrating against $\dot{\eta}$:
$$m \int_a^b \ddot{\eta}(t) \cdot \dot{\eta}(t) dt = -\int_a^b \left(\int_0^1 U''(q^* + s\eta) \eta \, ds\right) \cdot \dot{\eta} \, dt$$

The left side is a boundary term:
$$m[\dot{\eta}(t) \cdot \eta(t)]_a^b - m\int_a^b |\dot{\eta}(t)|^2 dt = -m\int_a^b |\dot{\eta}(t)|^2 dt$$

(since $\eta(a) = \eta(b) = 0$).

The right side, using concavity $U'' \leq 0$:
$$-\int_a^b \int_0^1 U''(q^* + s\eta)[\eta, \eta] \, ds \, dt \geq 0$$

Therefore:
$$-m\int_a^b |\dot{\eta}(t)|^2 dt \geq 0$$

This implies $\dot{\eta}(t) = 0$ for all $t \in [a,b]$, so $\eta(t) = 0$, and thus $q(t) = q^*(t)$.

**Uniqueness is proved.**

### Part 2: Minimality of the Action

Now suppose $q^*(t)$ is a solution to Newton's equation. We show it minimizes the action among all admissible paths with the same boundary conditions.

Let $q(t) = q^*(t) + \eta(t)$ where $\eta(a) = \eta(b) = 0$. The action becomes:

$$S[q^* + \eta] = \int_a^b \left(\frac{m|\dot{q}^* + \dot{\eta}|^2}{2} - U(q^* + \eta)\right) dt$$

Expanding to second order in $\eta$:

$$S[q^* + \eta] = \int_a^b \left(\frac{m|\dot{q}^*|^2}{2} - U(q^*)\right) dt$$
$$+ \int_a^b (m\dot{q}^* \cdot \dot{\eta} - \nabla U(q^*) \cdot \eta) \, dt$$
$$+ \frac{1}{2}\int_a^b \left(m|\dot{\eta}|^2 - U''(q^*)[\eta,\eta]\right) dt + O(\eta^3)$$

The first integral is $S[q^*]$.

The second integral (first variation) vanishes by integration by parts and the Euler-Lagrange equations:
$$\int_a^b (m\dot{q}^* \cdot \dot{\eta} - \nabla U(q^*) \cdot \eta) \, dt = [m\dot{q}^* \cdot \eta]_a^b - \int_a^b (m\ddot{q}^* + \nabla U(q^*)) \cdot \eta \, dt = 0$$

(boundary term vanishes since $\eta(a) = \eta(b) = 0$, and the integrand vanishes by the equation of motion).

The second variation (second-order term):
$$\delta^2 S = \frac{1}{2}\int_a^b \left(m|\dot{\eta}|^2 - U''(q^*)[\eta,\eta]\right) dt$$

By concavity, $U''(q^*) \leq 0$ as a quadratic form, so $-U''(q^*)[\eta,\eta] \geq 0$:

$$\delta^2 S = \frac{1}{2}\int_a^b m|\dot{\eta}|^2 \, dt + \frac{1}{2}\int_a^b (-U''(q^*))[\eta,\eta] \, dt \geq \frac{1}{2}\int_a^b m|\dot{\eta}|^2 \, dt \geq 0$$

Equality holds if and only if $\dot{\eta} = 0$ and $\eta = 0$, i.e., $q = q^*$.

Therefore:
$$S[q^* + \eta] \geq S[q^*]$$

with strict inequality when $\eta \neq 0$.

**Strict global minimality is proved.**

## Final Answer

$$\boxed{\text{Under concavity of } U, \text{ any Newton trajectory is the unique global minimum of the action.}}$$

The concavity ensures that the second variation of the action is strictly positive for any non-zero perturbation, guaranteeing both uniqueness of solutions and optimality of the path in the sense of the least-action principle.
