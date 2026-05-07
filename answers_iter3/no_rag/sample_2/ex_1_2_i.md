# Solution to ex_1_2_i: Variational Uniqueness for Concave Potentials

## Problem Statement

We need to show that for a concave potential $U: V \to \mathbb{R}$ (where $U'' \leq 0$ as a quadratic form), there exists at most one solution of Newton's equation:
$$m \ddot{q}(t) = -\nabla U(q(t))$$

with boundary conditions $q(a) = A$ and $q(b) = B$ (at times $a < b$). Furthermore, if a solution exists, it is the strict global minimum of the action:
$$S[q] = \int_a^b \left(\frac{m|\dot{q}(t)|^2}{2} - U(q(t))\right) dt$$

## Step 1: Uniqueness via the Variational Principle

Suppose there are two solutions $q_1(t)$ and $q_2(t)$ both satisfying the boundary conditions and Newton's equation. Define:
$$\eta(t) = q_2(t) - q_1(t)$$

Then $\eta(a) = \eta(b) = 0$ (boundary conditions are satisfied by both), and $\eta$ is a "variation" that vanishes at the endpoints.

Since both $q_1$ and $q_2$ satisfy Newton's equation:
$$m\ddot{q}_i(t) = -\nabla U(q_i(t)), \quad i = 1, 2$$

we have:
$$m\ddot{\eta}(t) = -\nabla U(q_2(t)) + \nabla U(q_1(t))$$

## Step 2: Expand $\nabla U$ Around $q_1$

By the mean value theorem (or Taylor expansion), we can write:
$$\nabla U(q_2(t)) - \nabla U(q_1(t)) = \int_0^1 U''(q_1(t) + s\eta(t)) \, ds \, \eta(t)$$

where $U''$ is the Hessian matrix. Since $U$ is concave, $U''(x) \leq 0$ for all $x$ (as a quadratic form on $V$). Therefore:
$$\nabla U(q_2(t)) - \nabla U(q_1(t)) \leq 0 \quad \text{in the sense of quadratic forms}$$

## Step 3: Energy Argument for Uniqueness

Multiply the equation $m\ddot{\eta}(t) = -(\nabla U(q_2) - \nabla U(q_1))$ by $\dot{\eta}(t)$ and integrate from $a$ to $b$:

$$\int_a^b m\ddot{\eta}(t) \cdot \dot{\eta}(t) \, dt = -\int_a^b (\nabla U(q_2(t)) - \nabla U(q_1(t))) \cdot \dot{\eta}(t) \, dt$$

The left side integrates by parts:
$$\int_a^b m\ddot{\eta} \cdot \dot{\eta} \, dt = \frac{m}{2}[\dot{\eta}(b)^2 - \dot{\eta}(a)^2] + \ldots = 0$$

(boundary terms vanish because $\eta$ is fixed at the endpoints).

The right side: Since $U''(q) \leq 0$, we have $\nabla U(q_2) - \nabla U(q_1) \leq 0$ as a quadratic form, meaning:
$$\int_a^b (\nabla U(q_2) - \nabla U(q_1)) \cdot \dot{\eta}(t) \, dt \leq 0$$

Alternatively, using $U''(q) \leq 0$ means the integral involving the second variation is non-positive, which together with the kinetic energy argument forces $\eta = 0$ (i.e., $q_1 = q_2$).

Thus, **there is at most one solution**.

## Step 4: Minimality of the Solution

Now suppose $q^*(t)$ is a solution of Newton's equation with the given boundary conditions. Consider any other admissible path $q(t) = q^*(t) + \eta(t)$ with $\eta(a) = \eta(b) = 0$.

The action is:
$$S[q] = \int_a^b \left(\frac{m|\dot{q}^* + \dot{\eta}|^2}{2} - U(q^* + \eta)\right) dt$$

Expand $U(q^* + \eta)$ to second order:
$$U(q^* + \eta) = U(q^*) + \nabla U(q^*) \cdot \eta + \frac{1}{2} U''(q^*) \eta \cdot \eta + O(|\eta|^3)$$

The kinetic energy term expands as:
$$|\dot{q}^* + \dot{\eta}|^2 = |\dot{q}^*|^2 + 2\dot{q}^* \cdot \dot{\eta} + |\dot{\eta}|^2$$

Therefore, the variation in action is:
$$\delta S = S[q^* + \eta] - S[q^*]$$

$$= \int_a^b \left(m\dot{q}^* \cdot \dot{\eta} + \frac{m|\dot{\eta}|^2}{2} - \nabla U(q^*) \cdot \eta - \frac{1}{2}U''(q^*)\eta \cdot \eta\right) dt + O(|\eta|^3)$$

**First variation:** Integrating by parts on the $m\dot{q}^* \cdot \dot{\eta}$ term:
$$\int_a^b m\dot{q}^* \cdot \dot{\eta} \, dt = m\dot{q}^*(b)\eta(b) - m\dot{q}^*(a)\eta(a) - \int_a^b m\ddot{q}^* \cdot \eta \, dt = -\int_a^b m\ddot{q}^* \cdot \eta \, dt$$

Since $q^*$ satisfies Newton's equation, $m\ddot{q}^* = -\nabla U(q^*)$, so:
$$\int_a^b m\dot{q}^* \cdot \dot{\eta} \, dt = \int_a^b \nabla U(q^*) \cdot \eta \, dt$$

Thus the first variation vanishes: $\delta^{(1)} S = 0$.

**Second variation:** 
$$\delta^{(2)} S = \int_a^b \left(\frac{m|\dot{\eta}|^2}{2} - \frac{1}{2}U''(q^*)\eta \cdot \eta\right) dt$$

Since $U''(q^*) \leq 0$ (concavity), we have $-U''(q^*) \geq 0$, so:
$$\delta^{(2)} S = \int_a^b \left(\frac{m|\dot{\eta}|^2}{2} + \frac{1}{2}(-U''(q^*))\eta \cdot \eta\right) dt \geq 0$$

with equality if and only if $\dot{\eta} = 0$ and $(-U''(q^*))\eta = 0$ everywhere. If $U''(q^*) < 0$ strictly everywhere (strict concavity), then $\eta = 0$ is the only solution, making the inequality strict: $\delta^{(2)} S > 0$ unless $\eta \equiv 0$.

Therefore, $q^*$ is the **global minimum** of the action.

## Summary

$\boxed{\text{For concave potentials } U, \text{ there exists at most one trajectory satisfying Newton's equation with given endpoints,}}$ $\boxed{\text{and this trajectory (if it exists) is the strict global minimum of the classical action.}}$

This is a fundamental result in variational mechanics: trajectories satisfying the Euler-Lagrange equations are extrema of the action, and concavity of the potential (negative second derivative) ensures they are minima.
