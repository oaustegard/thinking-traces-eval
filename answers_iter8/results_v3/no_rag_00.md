# Solution: Integer Bases Where $17_b$ divides $97_b$

## Problem
Find the sum of all integer bases $b > 9$ for which $17_b$ is a divisor of $97_b$.

## Solution

First, convert the base-$b$ representations to base 10:
- $17_b = 1 \cdot b + 7 = b + 7$
- $97_b = 9 \cdot b + 7 = 9b + 7$

We need $(b + 7) \mid (9b + 7)$.

**Finding the divisibility condition:**

If $(b + 7)$ divides $9b + 7$, then it must also divide any linear combination. Let's express $9b + 7$ in terms of $(b + 7)$:

$$9b + 7 = 9(b + 7) - 63 + 7 = 9(b + 7) - 56$$

Therefore, $(b + 7) \mid (9b + 7)$ if and only if $(b + 7) \mid 56$.

**Finding all divisors of 56:**

$56 = 2^3 \cdot 7$

The divisors of 56 are: $1, 2, 4, 7, 8, 14, 28, 56$

**Solving for $b$:**

For each divisor $d$ of 56, we have $b + 7 = d$, so $b = d - 7$:

| $d$ | $b$ | Valid? |
|-----|-----|--------|
| 1 | -6 | No ($b \leq 0$) |
| 2 | -5 | No ($b \leq 0$) |
| 4 | -3 | No ($b \leq 0$) |
| 7 | 0 | No ($b \leq 0$) |
| 8 | 1 | No ($b \not> 9$) |
| 14 | 7 | No ($b \not> 9$) |
| 28 | 21 | Yes ($b > 9$) |
| 56 | 49 | Yes ($b > 9$) |

**Valid bases:** $b \in \{21, 49\}$

**Verification:**

For $b = 21$:
- $17_{21} = 1(21) + 7 = 28$
- $97_{21} = 9(21) + 7 = 189 + 7 = 196$
- $196 \div 28 = 7$ ✓

For $b = 49$:
- $17_{49} = 1(49) + 7 = 56$
- $97_{49} = 9(49) + 7 = 441 + 7 = 448$
- $448 \div 56 = 8$ ✓

**Final Answer:**

The sum of all valid bases is:
$$21 + 49 = 70$$

$\boxed{70}$
