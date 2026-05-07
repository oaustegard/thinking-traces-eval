# AIME Problem Solution

## Problem Statement
The 9 members of a baseball team went to an ice-cream parlor after their game. Each player had a single-scoop cone of chocolate, vanilla, or strawberry ice cream. At least one player chose each flavor, and the number of players who chose chocolate was greater than the number of players who chose vanilla, which was greater than the number of players who chose strawberry. Let $N$ be the number of different assignments of flavors to players that meet these conditions. Find the remainder when $N$ is divided by $1000$.

## Solution

Let $c$, $v$, and $s$ denote the number of players choosing chocolate, vanilla, and strawberry, respectively.

**Constraints:**
- $c + v + s = 9$
- $c \geq 1$, $v \geq 1$, $s \geq 1$ (at least one of each)
- $c > v > s$ (strict inequalities)

**Finding valid distributions:**

From $c > v > s \geq 1$, we must have:
- $s \geq 1$
- $v \geq s + 1 \geq 2$
- $c \geq v + 1 \geq 3$

Systematically checking all possibilities:

**Case 1: $s = 1$**
- Need $c + v = 8$ with $c > v > 1$
- $v = 2, c = 6$: ✓ $(6, 2, 1)$
- $v = 3, c = 5$: ✓ $(5, 3, 1)$
- $v = 4, c = 4$: ✗ (need $c > v$)

**Case 2: $s = 2$**
- Need $c + v = 7$ with $c > v > 2$
- $v = 3, c = 4$: ✓ $(4, 3, 2)$
- $v = 4, c = 3$: ✗ (need $c > v$)

**Case 3: $s = 3$**
- Need $c + v = 6$ with $c > v > 3$
- $v = 4, c = 2$: ✗ (need $c > v$)

Valid triples: $(6, 2, 1)$, $(5, 3, 1)$, $(4, 3, 2)$

**Counting assignments for each distribution:**

For a distribution $(c, v, s)$, the number of ways to assign these flavors to 9 players is the multinomial coefficient:
$$\binom{9}{c, v, s} = \frac{9!}{c! \cdot v! \cdot s!}$$

For $(6, 2, 1)$:
$$\binom{9}{6, 2, 1} = \frac{9!}{6! \cdot 2! \cdot 1!} = \frac{362880}{720 \cdot 2 \cdot 1} = \frac{362880}{1440} = 252$$

For $(5, 3, 1)$:
$$\binom{9}{5, 3, 1} = \frac{9!}{5! \cdot 3! \cdot 1!} = \frac{362880}{120 \cdot 6 \cdot 1} = \frac{362880}{720} = 504$$

For $(4, 3, 2)$:
$$\binom{9}{4, 3, 2} = \frac{9!}{4! \cdot 3! \cdot 2!} = \frac{362880}{24 \cdot 6 \cdot 2} = \frac{362880}{288} = 1260$$

**Total count:**
$$N = 252 + 504 + 1260 = 2016$$

**Final answer:**
$$N \bmod 1000 = 2016 \bmod 1000 = \boxed{16}$$
