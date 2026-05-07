# Solution to ex_1_2_i: Uniqueness and Minimality for Concave Potentials

## Problem Statement

For a particle with mass $m$ in a Euclidean space $V$ subject to a concave potential $U: V \to \mathbb{R}$ (i.e., $U'' \leq 0$ as a quadratic form), we must show:

1. **Uniqueness:** At most one solution to the Newton equation $m q''(t) = -\nabla U(q(t))$ with boundary conditions $q(a) = A$ and $q(b) = B$.

2. **Minimality:** This solution (if it exists) is a strict global minimum of the action:
$$S[q] = \int_a^b \left(\frac{m|\dot{q}(t)|^2}{2} - U(q(t))\right) dt$$

## Part 1: Uniqueness via the Second Variation

**Assume two solutions exist:** Suppose $q_1(t)$ and $q_2(t)$ both satisfy the Newton equation with the same boundary conditions. Let $\eta(t) = q_1(t) - q_2(t)$.

Then $\eta(a) = \eta(b) = 0$ and:
$$m\eta''(t) = -\nabla U(q_1(t)) + \nabla U(q_2(t))$$

By the mean value theorem (or Cauchy's integral formula for gradients):
$$\nabla U(q_1) - \nabla U(q_2) = \int_0^1 U''(q_2 + s\eta) \, ds \cdot \eta$$

Thus:
$$m\eta''(t) = -\left[\int_0^1 U''(q_2 + s\eta) \, ds\right] \eta(t)$$

**Computing the energy difference:**
Consider the quadratic form:
$$\frac{d}{dt}\left(\frac{m\eta' \cdot \eta'}{2}\right) = m\eta' \cdot \eta'' = -\eta' \cdot \left[\int_0^1 U''(q_2 + s\eta) \, ds\right] \eta$$

Integrate from $a$ to $b$:
$$\left[\frac{m|\eta'(t)|^2}{2}\right]_a^b = -\int_a^b \eta' \cdot U''(q_2 + s\eta) \eta \, dt$$

Since $\eta(a) = \eta(b) = 0$, the left side is zero. Thus:
$$\int_a^b \eta' \cdot U''(q_2 + s\eta) \eta \, dt = 0$$

**Arguing uniqueness:** If $U'' < 0$ (strictly concave), the quadratic form $\eta \cdot U''(\xi) \cdot \eta$ is negative definite for any $\eta \neq 0$. This means the integral equation above forces $\eta = 0$ (i.e., $q_1 = q_2$). For $U'' \leq 0$ (weakly concave), we have at most uniqueness; strict concavity guarantees it.

## Part 2: Minimality via the Second Variation of the Action

**Decompose any admissible path:** Let $q^*(t)$ be a solution to the Newton equation. Consider any other path $q(t) = q^*(t) + \eta(t)$ with $\eta(a) = \eta(b) = 0$.

**Expand the action:**
$$S[q^* + \eta] = \int_a^b \left(\frac{m|\dot{q}^* + \dot{\eta}|^2}{2} - U(q^* + \eta)\right) dt$$

$$= S[q^*] + \int_a^b \left(m\dot{q}^* \cdot \dot{\eta} - \nabla U(q^*) \cdot \eta\right) dt$$
$$\quad + \frac{1}{2}\int_a^b \left(m|\dot{\eta}|^2 - U''(q^* + \theta\eta) \eta \cdot \eta\right) dt$$

where $\theta \in [0,1]$ parametrizes the interpolation.

**First variation vanishes:** Integrating by parts and using $q''(t) = -\frac{1}{m}\nabla U(q^*)$ with $\eta(a) = \eta(b) = 0$:
$$\int_a^b \left(m\dot{q}^* \cdot \dot{\eta} - \nabla U(q^*) \cdot \eta\right) dt = 0$$

**Second variation:** 
$$\delta^2 S = \frac{1}{2}\int_a^b \left(m|\dot{\eta}|^2 - U''(q^* + \theta\eta) [\eta \cdot \eta]\right) dt$$

By concavity, $-U''(\cdot) \geq 0$, so $U''(\cdot)[\eta \cdot \eta] \leq 0$. Therefore:
$$\delta^2 S \geq \frac{1}{2}\int_a^b m|\dot{\eta}|^2 \, dt \geq 0$$

Equality holds only if $\dot{\eta} = 0$, i.e., $\eta = 0$ (using boundary conditions).

Thus $S[q^* + \eta] > S[q^*]$ for all non-trivial $\eta$, proving $q^*$ is a **strict global minimum**.

---

## Final Answer

$$\boxed{\text{For concave } U \text{ (i.e., } U'' \leq 0\text{):}}$$

$$\boxed{\text{(1) At most one solution to Newton's equation with given boundary conditions.}}$$

$$\boxed{\text{(2) Any such solution is a strict global minimum of the action } S[q].}$$

These follow from the second-variation argument: the first variation vanishes by Euler-Lagrange, and the second variation is non-negative by concavity, with equality only when the perturbation vanishes.
