# Solution: ex_1_2_i — Variational Uniqueness and Minimality in Classical Mechanics

## Relevance of Examples

**Retrieved Examples 1, 2, and 3 (ex_2_14_wallis, ex_5_18_euler_char, ex_2_20_morse):** None of these retrieved examples are directly relevant to variational mechanics or Lagrangian dynamics. They address (respectively) asymptotic analysis of integrals, Euler characteristics of groups, and Morse coordinate transformations—none of which involve the Euler-Lagrange equation or action minimization.

**Assessment:** All three retrieved examples are noise. However, the problem statement is self-contained and does not require specialized machinery beyond standard variational calculus. I will solve it from first principles, noting that this is an off-domain test where RAG does not help.

---

## Solution

### Setup

We consider a particle with mass $m$ moving in a Euclidean vector space $V$ under a potential $U: V \to \mathbb{R}$ satisfying the **concavity condition**: $U''(q) \leq 0$ as a quadratic form on $V$ (equivalently, the Hessian $\nabla^2 U$ is negative semi-definite everywhere).

The action functional is:
$$S[q] = \int_a^b \left(\frac{m|q'(t)|^2}{2} - U(q(t))\right) dt$$

over all paths $q: [a,b] \to V$ satisfying Dirichlet boundary conditions $q(a) = A$ and $q(b) = B$.

**Goal:** Show that:
1. At most one solution $q^*$ to the Newton equation $m q''(t) = -\nabla U(q(t))$ exists with these boundary conditions.
2. If such a $q^*$ exists, it is the unique global minimizer of $S[q]$ over the admissible path space.

### Part 1: Uniqueness of the Solution

Suppose $q^*$ and $\tilde{q}$ are two distinct solutions to Newton's equation with the same boundary conditions. Define $\eta = \tilde{q} - q^*$, so $\eta(a) = \eta(b) = 0$ and:
$$m\eta''(t) = -\nabla U(\tilde{q}(t)) + \nabla U(q^*(t))$$

Integrate the inner product $\langle \eta'(t), m\eta''(t) \rangle$ over $[a,b]$:
$$m\int_a^b \langle \eta'(t), \eta''(t) \rangle dt = -\int_a^b \langle \eta'(t), \nabla U(\tilde{q}(t)) - \nabla U(q^*(t)) \rangle dt$$

The left side is an integration by parts (with boundary terms vanishing):
$$m \int_a^b \frac{d}{dt}\left(\frac{|\eta'(t)|^2}{2}\right) dt = m\left[\frac{|\eta'(b)|^2}{2} - \frac{|\eta'(a)|^2}{2}\right] = 0$$

For the right side, apply the mean-value theorem for vector-valued functions. For each $t$, write:
$$\nabla U(\tilde{q}(t)) - \nabla U(q^*(t)) = \int_0^1 \nabla^2 U(q^* + \lambda\eta)\, \eta(t)\, d\lambda$$

By concavity, $\nabla^2 U \leq 0$, so:
$$\langle \eta'(t), \nabla U(\tilde{q}) - \nabla U(q^*) \rangle \leq 0$$

(with the quadratic form $\nabla^2 U$ applied to the vector $\eta$, scaled by the inner product with $\eta'$).

Thus:
$$0 = m \int_a^b 0\, dt \geq -\int_a^b \langle \eta'(t), \nabla U(\tilde{q}) - \nabla U(q^*) \rangle dt \geq 0$$

Equality must hold throughout. This implies $\eta' = 0$ (from the kinetic energy term), so $\eta = \text{const}$. Since $\eta(a) = 0$, we have $\eta \equiv 0$, i.e., $\tilde{q} = q^*$.

**Conclusion:** Uniqueness holds.

### Part 2: Global Minimality of the Action

Suppose $q^*$ satisfies Newton's equation and the boundary conditions. Consider any other admissible path $q = q^* + \eta$ with $\eta(a) = \eta(b) = 0$.

Expand the action:
$$S[q^* + \eta] = \int_a^b \left(\frac{m|q'^* + \eta'|^2}{2} - U(q^* + \eta)\right) dt$$

$$= \int_a^b \left(\frac{m|q'^*|^2}{2} - U(q^*)\right) dt + \int_a^b \left(m\langle q'^*, \eta'\rangle + \frac{m|\eta'|^2}{2} - [U(q^* + \eta) - U(q^*)]\right) dt$$

**First variation (Euler-Lagrange):**
$$\delta S = \int_a^b \left(m\langle q'^*, \eta' \rangle - \langle \nabla U(q^*), \eta \rangle\right) dt = 0$$

by integration by parts and using $mq''^* = -\nabla U(q^*)$.

**Second variation:**
$$\delta^2 S = \int_a^b \left(\frac{m|\eta'|^2}{2} - \frac{1}{2}\eta(t)^T \nabla^2 U(q^*(t)) \eta(t)\right) dt$$

where the quadratic form $\nabla^2 U(q^*)$ acts on the vector $\eta$.

By concavity, $\nabla^2 U \leq 0$, so $-\nabla^2 U \geq 0$. Thus:
$$\delta^2 S = \int_a^b \frac{m|\eta'|^2}{2} dt + \int_a^b \frac{1}{2}\eta(t)^T (-\nabla^2 U(q^*)) \eta(t) dt \geq 0$$

with equality if and only if $\eta' = 0$ and $(-\nabla^2 U)\eta = 0$. Since $-\nabla^2 U \geq 0$ is positive semi-definite and orthogonal to all $\eta$, and $\eta(a) = 0$, we must have $\eta \equiv 0$.

**Conclusion:** $q^*$ is the strict global minimum of $S[q]$ over the admissible path space.

---

## Final Answer

$$\boxed{\text{Under the concavity condition } U'' \leq 0, \text{ there exists at most one solution to Newton's equation}}$$
$$\boxed{\text{with prescribed boundary conditions, and this solution is the strict global minimizer of the action } S[q].}$$

The proof combines:
1. **Uniqueness:** A comparison of two solutions via energy balance, exploiting concavity to show the difference must vanish.
2. **Minimality:** The variational principle (first and second variations) and the negative semi-definiteness of $\nabla^2 U$ guarantees the action increases away from $q^*$.
