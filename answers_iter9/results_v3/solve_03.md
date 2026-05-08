# Solution to AIME Problem: Finding Integer Pairs

## Problem
Find the number of ordered pairs $(x,y)$, where both $x$ and $y$ are integers between $-100$ and $100$, inclusive, such that $12x^2-xy-6y^2=0$.

## Solution

### Step 1 — Factor the quadratic

We treat the equation as a quadratic in $x$:
$$12x^2 - xy - 6y^2 = 0$$

Using the quadratic formula:
$$x = \frac{y \pm \sqrt{y^2 + 4(12)(6y^2)}}{2(12)}$$

$$x = \frac{y \pm \sqrt{y^2 + 288y^2}}{24}$$

$$x = \frac{y \pm \sqrt{289y^2}}{24}$$

$$x = \frac{y \pm 17|y|}{24}$$

### Step 2 — Find the two cases

**Case 1:** $x = \frac{y + 17y}{24} = \frac{18y}{24} = \frac{3y}{4}$

**Case 2:** $x = \frac{y - 17y}{24} = \frac{-16y}{24} = \frac{-2y}{3}$

### Step 3 — Count solutions for Case 1: $x = \frac{3y}{4}$

For $x$ to be an integer, $y$ must be divisible by 4.
Let $y = 4k$ where $k$ is an integer.
Then $x = 3k$.

Constraints from $-100 \le x \le 100$ and $-100 \le y \le 100$:
- $-100 \le 3k \le 100 \Rightarrow -33.33... \le k \le 33.33...$
- $-100 \le 4k \le 100 \Rightarrow -25 \le k \le 25$

The effective constraint is $-25 \le k \le 25$, giving **51 values** of $k$ (integers from $-25$ to $25$ inclusive).

### Step 4 — Count solutions for Case 2: $x = \frac{-2y}{3}$

For $x$ to be an integer, $y$ must be divisible by 3.
Let $y = 3m$ where $m$ is an integer.
Then $x = -2m$.

Constraints from $-100 \le x \le 100$ and $-100 \le y \le 100$:
- $-100 \le -2m \le 100 \Rightarrow -50 \le m \le 50$
- $-100 \le 3m \le 100 \Rightarrow -33.33... \le m \le 33.33...$

The effective constraint is $-33 \le m \le 33$, giving **67 values** of $m$ (integers from $-33$ to $33$ inclusive).

### Step 5 — Check for overlap

For a pair to satisfy both cases simultaneously:
- Case 1: $x = 3k, y = 4k$
- Case 2: $x = -2m, y = 3m$

This requires:
$$3k = -2m \quad \text{and} \quad 4k = 3m$$

From the second equation: $m = \frac{4k}{3}$

Substituting into the first equation:
$$3k = -2 \cdot \frac{4k}{3} = \frac{-8k}{3}$$

Multiplying by 3:
$$9k = -8k$$
$$17k = 0$$
$$k = 0$$

When $k = 0$, we have $m = 0$, giving the point $(0, 0)$.

Thus there is exactly **1 overlapping point**.

### Step 6 — Apply inclusion-exclusion

Total number of ordered pairs:
$$51 + 67 - 1 = \boxed{117}$$
