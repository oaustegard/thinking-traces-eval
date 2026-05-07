# Uniqueness and Minimality in Concave Potentials

## Problem Statement

Consider a particle moving in Euclidean space $V$ under a concave potential $U: V \to \mathbb{R}$ (i.e., $U'' \leq 0$ as a quadratic form). We must show:
1. For any endpoints $A, B \in V$ and times $a < b$, there exists **at most one** solution to $m q''(t) = -\nabla U(q(t))$ with $q(a) = A$ and $q(b) = B$.
2. If such a solution exists, it is the **strict global minimum** of the action:
$$S[q] = \int_a^b \left(\frac{m |q'(t)|^2}{2} - U(q(t))\right) dt$$
over all admissible paths (those satisfying the boundary conditions).

## Proof of Uniqueness and Minimality

### Step 1: Euler-Lagrange Equations

The action functional is:
$$S[q] = \int_a^b L(q, \dot{q}, t) \, dt, \quad L = \frac{m\dot{q}^2}{2} - U(q)$$

The Euler-Lagrange equation is:
$$\frac{d}{dt}\frac{\partial L}{\partial \dot{q}} - \frac{\partial L}{\partial q} = 0 \implies m\ddot{q} + \nabla U(q) = 0$$

This is exactly the Newton equation in the problem. So any critical point of $S$ satisfies the equation of motion.

### Step 2: Second Variation and Concavity

Suppose $q^*$ is a solution of the equation of motion with $q^*(a) = A$ and $q^*(b) = B$. Consider any other admissible path:
$$q(t) = q^*(t) + \eta(t)$$
where $\eta(a) = \eta(b) = 0$ (boundary conditions).

Expand the action to second order:
$$S[q^* + \eta] = S[q^*] + \delta S[\eta] + \frac{1}{2}\delta^2 S[\eta] + O(\|\eta\|^3)$$

**First variation:** By Euler-Lagrange, $\delta S[\eta] = 0$ when $q^*$ satisfies the equations of motion and $\eta$ vanishes at the boundary.

**Second variation:**
$$\delta^2 S[\eta] = \int_a^b \left[m |\eta'(t)|^2 - \eta(t) \cdot U''(q^*(t)) \cdot \eta(t)\right] dt$$

The first term is manifestly non-negative (kinetic energy). For the second term, use the concavity condition $U'' \leq 0$ (as a quadratic form):
$$\eta(t) \cdot U''(q^*(t)) \cdot \eta(t) \leq 0$$

Therefore:
$$-\eta(t) \cdot U''(q^*(t)) \cdot \eta(t) \geq 0$$

### Step 3: Positivity of Second Variation

Combining:
$$\delta^2 S[\eta] = \int_a^b m |\eta'(t)|^2 \, dt - \int_a^b \eta(t) \cdot U''(q^*(t)) \cdot \eta(t) \, dt \geq \int_a^b m |\eta'(t)|^2 \, dt \geq 0$$

with equality **if and only if** $\eta'(t) = 0$ for all $t$ and the quadratic form term also contributes zero. The first condition means $\eta = c$ (constant), and since $\eta(a) = 0$, we have $\eta = 0$.

### Step 4: Uniqueness from Uniqueness of Solutions to ODE

The Newton equation $m\ddot{q} = -\nabla U$ is a second-order ODE. Given initial conditions $q(a) = A$ and $\dot{q}(a) = v_0$, there is a unique solution (by the Picard-Lindelöf theorem, assuming $\nabla U$ is Lipschitz—true for smooth $U$).

The boundary value problem (BVP) prescribing $q(a) = A$ and $q(b) = B$ either has a unique solution (if the solution map from $v_0$ to $q(b)$ is bijective), or no solution, or infinitely many solutions.

The **action minimization principle** implies uniqueness in the following sense: if $q^*$ minimizes the action among all paths with the prescribed endpoints, then $q^*$ satisfies the Euler-Lagrange equations and is the unique critical point (given the strict convexity of the second variation in $\eta$).

Conversely, any two distinct solutions to the BVP would correspond to two distinct paths with the same endpoints. But the second variation argument shows there is at most one minimizer. By the uniqueness of critical points and the strict positivity of $\delta^2 S[\eta]$ for $\eta \neq 0$, there is **at most one solution**.

## Conclusion

For a concave potential $U$:

$$\boxed{\text{Any boundary value problem } q(a) = A, q(b) = B \text{ has at most one solution; if a solution exists, it is the strict global minimum of the action } S[q].}$$

The proof rests on three pillars: (i) the Euler-Lagrange equation characterizing critical points, (ii) the second-variation calculation showing strict positivity of deviations, and (iii) concavity of $U$ ensuring the quadratic form term is non-positive.
