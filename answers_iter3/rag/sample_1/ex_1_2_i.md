# Solution: ex_1_2_i - Variational Uniqueness and Minimality

## Relevance and Differences from Retrieved Examples

**Retrieved examples:**
1. **ex_2_14_wallis** (steepest descent/quadratic expansions) - MINIMALLY RELEVANT: uses Taylor expansion but in integral context, not variational
2. **ex_5_18_euler_char** (topological/algebraic methods) - NOT RELEVANT
3. **ex_2_20_morse** (Morse lemma, second-derivative test, positive-definiteness) - MARGINALLY RELEVANT for structure, but applies to static functions, not functionals

**Key Difference:** This problem is about **variational uniqueness** — a functional-analysis result, not a computational steepest-descent or topological problem. The retrieved examples offer limited technical overlap; I solve primarily from variational mechanics principles.

---

## Solution

### Part 1: Uniqueness of Solutions to the Newton Equation

**Problem Setup:**
- Potential: $U: V \to \mathbb{R}$ with $U'' \leq 0$ (concave)
- Boundary conditions: $q(a) = A$, $q(b) = B$ at times $a < b$
- Newton equation: $m\ddot{q}(t) = -\nabla U(q(t))$

**Claim:** At most one solution exists.

**Proof by Contradiction:**
Suppose two distinct solutions $q_1(t)$ and $q_2(t)$ both satisfy the boundary conditions and Newton equation.

Define the difference:
$$\eta(t) := q_1(t) - q_2(t)$$

Then $\eta(a) = \eta(b) = 0$ (boundary conditions match).

Subtract the two Newton equations:
$$m\ddot{q}_1 = -\nabla U(q_1), \quad m\ddot{q}_2 = -\nabla U(q_2)$$

$$m\ddot{\eta} = -\nabla U(q_1) + \nabla U(q_2)$$

**Apply mean-value theorem (matrix form):**
$$\nabla U(q_1) - \nabla U(q_2) = \int_0^1 U''(q_2 + s\eta)\,\eta\,ds$$

where $U''$ is the Hessian (matrix of second partial derivatives).

Thus:
$$m\ddot{\eta} = -\int_0^1 U''(q_2 + s\eta)\,\eta\,ds$$

**Multiply both sides by $\eta$ and integrate over $[a, b]$:**
$$m\int_a^b \eta \cdot \ddot{\eta}\,dt = -\int_a^b \eta \cdot \left(\int_0^1 U''(q_2 + s\eta)\,\eta\,ds\right)dt$$

**Left side (integration by parts):**
$$\int_a^b \eta \cdot \ddot{\eta}\,dt = [\eta \cdot \dot{\eta}]_a^b - \int_a^b \dot{\eta}^2\,dt = 0 - \int_a^b |\dot{\eta}|^2\,dt$$

(The boundary term vanishes since $\eta(a) = \eta(b) = 0$.)

**Right side:**
Since $U'' \leq 0$ (concave), for any vector $v$:
$$v \cdot U''(q)\,v \leq 0$$

Thus:
$$\int_0^1 U''(q_2 + s\eta)\,\eta \cdot \eta\,ds \leq 0$$

$$\Rightarrow -\int_a^b \eta \cdot \left(\int_0^1 U''(q_2 + s\eta)\,\eta\,ds\right)dt \geq 0$$

**Combine:**
$$-m\int_a^b |\dot{\eta}|^2\,dt \geq 0$$

Since $m > 0$ and $\int_a^b |\dot{\eta}|^2\,dt \geq 0$, we must have:
$$\int_a^b |\dot{\eta}|^2\,dt = 0$$

This implies $\dot{\eta} = 0$ almost everywhere, hence $\eta$ is constant. But $\eta(a) = 0$, so $\eta \equiv 0$.

**Conclusion:** $q_1 = q_2$, so the solution is unique.

---

### Part 2: Solution is a Global Minimum of the Action

**Definition:** The action functional is:
$$S[q] = \int_a^b \left(\frac{m|\dot{q}|^2}{2} - U(q)\right)dt$$

**Claim:** If $q^*$ is a solution to Newton's equation with the given boundary conditions, it is the strict global minimum of $S$ over all admissible paths $q$ with $q(a) = A, q(b) = B$.

**Proof:**
Let $q$ be any admissible path. Write:
$$q(t) = q^*(t) + \eta(t)$$

where $\eta(a) = \eta(b) = 0$ (variation vanishes at boundaries).

**Expand the action:**
$$S[q^* + \eta] = \int_a^b \left(\frac{m|\dot{q}^* + \dot{\eta}|^2}{2} - U(q^* + \eta)\right)dt$$

$$= \int_a^b \left(\frac{m|\dot{q}^*|^2}{2} + m\dot{q}^* \cdot \dot{\eta} + \frac{m|\dot{\eta}|^2}{2} - U(q^*) - \nabla U(q^*) \cdot \eta - \int_0^1 (1-s) U''(q^* + s\eta)[\eta, \eta]\,ds\right)dt$$

(Taylor expansion with integral remainder.)

**First variation (Euler-Lagrange):**
Integrating the second term by parts:
$$m\int_a^b \dot{q}^* \cdot \dot{\eta}\,dt = m[\dot{q}^* \cdot \eta]_a^b - m\int_a^b \ddot{q}^* \cdot \eta\,dt = -m\int_a^b \ddot{q}^* \cdot \eta\,dt$$

(Boundary term vanishes.)

The Euler-Lagrange equation for $q^*$ is $m\ddot{q}^* = -\nabla U(q^*)$, so:
$$-m\int_a^b \ddot{q}^* \cdot \eta\,dt = \int_a^b \nabla U(q^*) \cdot \eta\,dt$$

Thus, the $\eta$ term cancels:
$$\delta S = m\int_a^b \dot{q}^* \cdot \dot{\eta}\,dt - \int_a^b \nabla U(q^*) \cdot \eta\,dt = 0$$

**Second variation (Hessian):**
$$\delta^2 S = \frac{m}{2}\int_a^b |\dot{\eta}|^2\,dt - \int_a^b \left(\int_0^1 (1-s) U''(q^* + s\eta)[\eta, \eta]\,ds\right)dt$$

Since $U'' \leq 0$ (concavity), the second term is non-negative:
$$\int_0^1 (1-s) U''(q^* + s\eta)[\eta, \eta]\,ds \leq 0$$

Thus:
$$\delta^2 S \geq \frac{m}{2}\int_a^b |\dot{\eta}|^2\,dt \geq 0$$

with equality if and only if $\dot{\eta} = 0$, i.e., $\eta \equiv 0$ (given $\eta(a) = 0$).

**Conclusion:**
$$S[q^* + \eta] = S[q^*] + \delta S + \delta^2 S = S[q^*] + 0 + \delta^2 S \geq S[q^*]$$

with strict inequality for $\eta \not\equiv 0$. Thus, $q^*$ is the **strict global minimum** of the action.

---

## Final Answer

$$\boxed{\begin{align}
&\text{(Uniqueness) If } U'' \leq 0 \text{ (concave) on } V, \text{ then the initial-value/boundary-value}\\
&\text{problem } m\ddot{q} = -\nabla U(q), \quad q(a)=A, \quad q(b)=B\\
&\text{has at most one solution.}\\
&\\
&\text{(Minimality) This solution } q^* \text{ is the unique global minimizer of}\\
&S[q] = \int_a^b \left(\frac{m|\dot{q}|^2}{2} - U(q)\right)dt\\
&\text{over all admissible paths with the same boundary conditions.}
\end{align}}$$
