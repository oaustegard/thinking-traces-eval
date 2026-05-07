# Solution: Sum of Integer Bases

## Problem
Find the sum of all integer bases $b > 9$ for which $17_b$ is a divisor of $97_b$.

## Solution

**Step 1 — Convert to Base 10**
- $17_b = 1 \cdot b + 7 = b + 7$
- $97_b = 9 \cdot b + 7 = 9b + 7$

Note: We require $b > 9$ because the digit 9 appears in $97_b$.

**Step 2 — Set Up the Divisibility Condition**
We need $(b + 7) \mid (9b + 7)$.

**Step 3 — Find Linear Combination**
If $(b + 7) \mid (9b + 7)$, then $(b + 7)$ divides any linear combination of these expressions.

Compute: $9(b + 7) - (9b + 7) = 9b + 63 - 9b - 7 = 56$

Therefore $(b + 7) \mid 56$.

**Step 4 — List Divisors of 56**
The divisors of 56 are: $1, 2, 4, 7, 8, 14, 28, 56$.

**Step 5 — Determine Valid Values of $b$**
From $b + 7 = d$ where $d$ divides 56:
- $b + 7 = 1 \Rightarrow b = -6$ (invalid)
- $b + 7 = 2 \Rightarrow b = -5$ (invalid)
- $b + 7 = 4 \Rightarrow b = -3$ (invalid)
- $b + 7 = 7 \Rightarrow b = 0$ (invalid)
- $b + 7 = 8 \Rightarrow b = 1$ (invalid, need $b > 9$)
- $b + 7 = 14 \Rightarrow b = 7$ (invalid, need $b > 9$)
- $b + 7 = 28 \Rightarrow b = 21$ (valid, $21 > 9$)
- $b + 7 = 56 \Rightarrow b = 49$ (valid, $49 > 9$)

**Step 6 — Verify Solutions**

For $b = 21$:
- $17_{21} = 21 + 7 = 28$
- $97_{21} = 9(21) + 7 = 189 + 7 = 196$
- $196 \div 28 = 7$ ✓

For $b = 49$:
- $17_{49} = 49 + 7 = 56$
- $97_{49} = 9(49) + 7 = 441 + 7 = 448$
- $448 \div 56 = 8$ ✓

**Step 7 — Calculate Sum**
The sum of all valid bases is $21 + 49 = 70$.

## Answer
$\boxed{70}$
