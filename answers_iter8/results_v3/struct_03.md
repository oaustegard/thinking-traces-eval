# Solution to AIME Problem: Integer Solutions to $12x^2 - xy - 6y^2 = 0$

## Problem Statement
Find the number of ordered pairs $(x,y)$, where both $x$ and $y$ are integers between $-100$ and $100$, inclusive, such that $12x^2-xy-6y^2=0$.

## Solution

### Step 1: Factor the Quadratic Form
Treat $12x^2 - xy - 6y^2 = 0$ as a quadratic equation in $x$:
$$12x^2 - xy - 6y^2 = 0$$

### Step 2: Apply the Quadratic Formula
Using the quadratic formula with $a=12$, $b=-y$, $c=-6y^2$:
$$x = \frac{y \pm \sqrt{y^2 + 4(12)(6y^2)}}{2(12)} = \frac{y \pm \sqrt{y^2 + 288y^2}}{24} = \frac{y \pm \sqrt{289y^2}}{24} = \frac{y \pm 17|y|}{24}$$

### Step 3: Determine the Factor Form
This gives us two linear relationships:
$$x = \frac{3y}{4} \quad \text{or} \quad x = \frac{-2y}{3}$$

We can verify by factoring: $12x^2 - xy - 6y^2 = (4x - 3y)(3x + 2y) = 0$

### Step 4: Find Integer Solutions for $x = \frac{3y}{4}$
For $x$ to be an integer, $y$ must be divisible by 4. Let $y = 4k$ where $k$ is an integer.
Then $x = 3k$.

**Range constraints:**
- $-100 \leq 3k \leq 100 \Rightarrow -33.33... \leq k \leq 33.33...$
- $-100 \leq 4k \leq 100 \Rightarrow -25 \leq k \leq 25$

Both constraints are satisfied when $k \in \{-25, -24, ..., 24, 25\}$.

**Count:** 51 values

### Step 5: Find Integer Solutions for $x = \frac{-2y}{3}$
For $x$ to be an integer, $y$ must be divisible by 3. Let $y = 3m$ where $m$ is an integer.
Then $x = -2m$.

**Range constraints:**
- $-100 \leq -2m \leq 100 \Rightarrow -50 \leq m \leq 50$
- $-100 \leq 3m \leq 100 \Rightarrow -33.33... \leq m \leq 33.33...$

Both constraints are satisfied when $m \in \{-33, -32, ..., 32, 33\}$.

**Count:** 67 values

### Step 6: Account for Overlap
We must subtract any pairs that appear in both families.

For a pair to satisfy both conditions:
- $3k = -2m$ and $4k = 3m$

From the first equation: $m = -\frac{3k}{2}$

Substituting into the second: $4k = 3 \cdot (-\frac{3k}{2}) = -\frac{9k}{2}$

This gives: $8k = -9k \Rightarrow 17k = 0 \Rightarrow k = 0$

When $k = 0$, we have $(x,y) = (0,0)$, which also corresponds to $m = 0$.

**Overlap count:** 1 pair

### Step 7: Calculate Total
$$\text{Total} = 51 + 67 - 1 = 117$$

\boxed{117}
