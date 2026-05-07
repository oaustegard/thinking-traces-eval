# Solution to AIME Problem: $12x^2 - xy - 6y^2 = 0$

## Problem
Find the number of ordered pairs $(x,y)$, where both $x$ and $y$ are integers between $-100$ and $100$, inclusive, such that $12x^2 - xy - 6y^2 = 0$.

## Solution

I'll solve by treating this as a quadratic equation in $x$.

### Factoring via quadratic formula

The equation is:
$$12x^2 - xy - 6y^2 = 0$$

Using the quadratic formula with $a = 12$, $b = -y$, $c = -6y^2$:
$$x = \frac{y \pm \sqrt{y^2 + 4(12)(6y^2)}}{24}$$
$$x = \frac{y \pm \sqrt{y^2 + 288y^2}}{24}$$
$$x = \frac{y \pm \sqrt{289y^2}}{24}$$
$$x = \frac{y \pm 17|y|}{24}$$

### Cases based on sign of $y$

For any $y$ (whether positive or negative), the two solutions are:
- $x = \frac{y + 17|y|}{24}$
- $x = \frac{y - 17|y|}{24}$

**For $y > 0$:** $|y| = y$
- $x = \frac{y + 17y}{24} = \frac{18y}{24} = \frac{3y}{4}$
- $x = \frac{y - 17y}{24} = \frac{-16y}{24} = -\frac{2y}{3}$

**For $y = 0$:**
- $x = 0$ (both formulas give this)

**For $y < 0$:** $|y| = -y$
- $x = \frac{y - 17y}{24} = \frac{-16y}{24} = -\frac{2y}{3}$
- $x = \frac{y + 17y}{24} = \frac{18y}{24} = \frac{3y}{4}$

In summary, the solutions satisfy either $x = \frac{3y}{4}$ or $x = -\frac{2y}{3}$.

## Counting Integer Solutions

### Case 1: $x = \frac{3y}{4}$

For $x$ to be an integer, we need $4 \mid 3y$. Since $\gcd(3, 4) = 1$, we must have $4 \mid y$.

Let $y = 4k$ for integer $k$. Then $x = 3k$.

With the constraint $-100 \leq y \leq 100$:
$$-100 \leq 4k \leq 100$$
$$-25 \leq k \leq 25$$

This gives $k \in \{-25, -24, \ldots, 24, 25\}$, yielding **51 pairs**.

### Case 2: $x = -\frac{2y}{3}$

For $x$ to be an integer, we need $3 \mid 2y$. Since $\gcd(2, 3) = 1$, we must have $3 \mid y$.

Let $y = 3m$ for integer $m$. Then $x = -2m$.

With the constraint $-100 \leq y \leq 100$:
$$-100 \leq 3m \leq 100$$
$$-33.\overline{3} \leq m \leq 33.\overline{3}$$

This gives $m \in \{-33, -32, \ldots, 32, 33\}$, yielding **67 pairs**.

### Checking for overlap

Both conditions hold when:
- $y = 4k = 3m$ and
- $x = 3k = -2m$

From the first: $k = \frac{3m}{4}$

Substituting into the second:
$$3 \cdot \frac{3m}{4} = -2m$$
$$\frac{9m}{4} = -2m$$
$$9m = -8m$$
$$17m = 0$$
$$m = 0$$

When $m = 0$: $y = 0$ and $x = 0$.

The pair $(0, 0)$ is counted in both cases, so we subtract 1 to avoid double-counting.

## Final Count

$$51 + 67 - 1 = \boxed{117}$$
