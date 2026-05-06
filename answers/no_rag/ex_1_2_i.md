# Solution to Problem ex_1_2_i: Uniqueness and Minimality for Concave Potentials

## Problem Statement

Given:
- Motion in Euclidean space $V$ under Newton's equation: $m\ddot{q}(t) = -\nabla U(q(t))$
- Concave potential: $U''(q) \leq 0$ (as a quadratic form)
- Boundary conditions: $q(a) = A$ and $q(b) = B$ with $a < b$
- Action functional: $S[q] = \int_a^b \left(\frac{m|\dot{q}(t)|^2}{2} - U(q(t))\right) dt$

We must show:
1. At most one solution exists with these boundary conditions
2. If it exists, it is the strict global minimum of the action

## Part 1: Uniqueness

### Proof by Contradiction

Suppose two distinct solutions exist: $q_1(t)$ and $q_2(t)$, both satisfying the Newton equation with $q_1(a) = q_2(a) = A$ and $q_1(b) = q_2(b) = B$.

Define the difference:
$$h(t) = q_1(t) - q_2(t)$$

Then $h(a) = h(b) = 0$ (boundary condition difference is zero).

### Differential Equation for the Difference

Since both $q_1$ and $q_2$ satisfy Newton's equation:
$$m\ddot{q}_1 = -\nabla U(q_1), \quad m\ddot{q}_2 = -\nabla U(q_2)$$

Subtracting:
$$m\ddot{h} = -\nabla U(q_1) + \nabla U(q_2) = -\int_0^1 U''(q_2 + sh) \cdot h \, ds$$

where we used the fundamental theorem applied to $\nabla U$ as a vector field.

### Energy-Like Quantity

Define the "energy" associated with the difference:
$$E(t) = \frac{m}{2}|\dot{h}(t)|^2 + \int_0^1 U''(q_2(t) + sh(t)) \cdot h(t) \otimes h(t) \, ds$$

Taking the time derivative:
$$\frac{dE}{dt} = m\dot{h} \cdot \ddot{h} + \frac{d}{dt}\left[\int_0^1 U''(q_2 + sh) \cdot h \otimes h \, ds\right]$$

The first term: $m\dot{h} \cdot \ddot{h} = \dot{h} \cdot (-\nabla U(q_1) + \nabla U(q_2))$

By the mean-value theorem and the concavity condition $U'' \leq 0$:
$$\int_0^1 U''(q_2 + sh) \cdot h \otimes h \, ds \leq 0$$

This is **non-positive** (concave potential implies the quadratic form is non-positive).

### The Multiplier Method

An alternative elegant approach: multiply the equation $m\ddot{h} = -\int_0^1 U''(q_2 + sh) \cdot h \, ds$ by $\dot{h}$ and integrate from $a$ to $b$:

$$m \int_a^b \dot{h} \cdot \ddot{h} \, dt = -\int_a^b \dot{h} \cdot \left(\int_0^1 U''(q_2 + sh) \cdot h \, ds\right) dt$$

The left side: $m \int_a^b d/dt\left[\frac{|\dot{h}|^2}{2}\right] dt = \frac{m}{2}(|\dot{h}(b)|^2 - |\dot{h}(a)|^2) = 0$

(since $h(a) = h(b) = 0$ implies $\dot{h}(a) = \dot{h}(b) = 0$ by continuity of $\dot{h}$ and the boundary conditions).

The right side: $\leq 0$ (by concavity of $U$).

Therefore: $0 \leq 0$, and equality holds **only if** $\dot{h}(t) = 0$ for all $t \in [a,b]$.

Thus $h(t) = \text{const} = 0$ (by $h(a) = 0$), so $q_1 = q_2$.

## Part 2: Global Minimality of the Action

### Action Difference Between Solution and Perturbation

Let $q(t)$ be the unique solution of Newton's equation, and $\tilde{q}(t)$ be any admissible path with $\tilde{q}(a) = A$, $\tilde{q}(b) = B$.

Define the perturbation: $\eta(t) = \tilde{q}(t) - q(t)$, with $\eta(a) = \eta(b) = 0$.

The action difference is:
$$\Delta S = S[\tilde{q}] - S[q] = \int_a^b \left[\frac{m}{2}(|\dot{q} + \dot{\eta}|^2 - |\dot{q}|^2) - (U(q + \eta) - U(q))\right] dt$$

### Taylor Expansion

Expanding to second order in $\eta$:
$$\Delta S = \int_a^b \left[m\dot{q} \cdot \dot{\eta} - \nabla U(q) \cdot \eta\right] dt + \int_a^b \left[\frac{m}{2}|\dot{\eta}|^2 - \int_0^1 U''(q + s\eta) \cdot \eta \otimes \eta \, ds\right] dt$$

### First Variation (Vanishes by Euler-Lagrange)

The first-order term, integrated by parts:
$$\int_a^b m\dot{q} \cdot \dot{\eta} \, dt - \int_a^b \nabla U(q) \cdot \eta \, dt = [m\dot{q} \cdot \eta]_a^b - \int_a^b (m\ddot{q} + \nabla U(q)) \cdot \eta \, dt = 0$$

since $q$ satisfies Newton's equation and $\eta(a) = \eta(b) = 0$.

### Second Variation (Non-negative by Concavity)

$$\delta^2 S = \int_a^b \left[\frac{m}{2}|\dot{\eta}|^2 - \int_0^1 U''(q + s\eta) \cdot \eta \otimes \eta \, ds\right] dt$$

By concavity, $U''(q + s\eta) \leq 0$ as a quadratic form, so:
$$-\int_0^1 U''(q + s\eta) \cdot \eta \otimes \eta \, ds \geq 0$$

Therefore:
$$\delta^2 S \geq \frac{m}{2}\int_a^b |\dot{\eta}|^2 \, dt \geq 0$$

with equality **only if** $\dot{\eta} = 0$, i.e., $\eta$ is constant. But $\eta(a) = 0$ forces $\eta \equiv 0$, so $\tilde{q} = q$.

Thus $\Delta S > 0$ for all $\tilde{q} \neq q$, proving **strict global minimality**.

## Conclusion

$$\boxed{\text{For concave potentials, the unique solution of Newton's equations with given boundary conditions is the}}$$
$$\boxed{\text{strict global minimum of the action functional among all admissible paths.}}$$

This result is a classical consequence of the variational principle and the concavity of the potential, which ensures both uniqueness (via the energy argument) and optimality (via positive-definiteness of the second variation).
