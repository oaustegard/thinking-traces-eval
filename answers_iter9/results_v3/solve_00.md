# Solution: Sum of Integer Bases for Divisibility

## Problem
Find the sum of all integer bases $b > 9$ for which $17_b$ is a divisor of $97_b$.

## Solution

### Step 1: Convert Base-b Representations to Decimal
In base $b$:
- $17_b = 1 \cdot b + 7 = b + 7$
- $97_b = 9 \cdot b + 7 = 9b + 7$

### Step 2: Set Up the Divisibility Condition
We need $(b + 7) \mid (9b + 7)$.

### Step 3: Find What $(b + 7)$ Must Divide
If $(b + 7) \mid (9b + 7)$, then $(b + 7)$ must also divide any linear combination:
$$9(b + 7) = 9b + 63$$

Therefore:
$$(b + 7) \mid [(9b + 63) - (9b + 7)] = 56$$

This gives us the key constraint: **$(b + 7)$ must be a divisor of $56$**.

### Step 4: Factor and Find All Divisors
$$56 = 2^3 \cdot 7$$

Divisors of $56$: $\{1, 2, 4, 7, 8, 14, 28, 56\}$

### Step 5: Determine Valid Bases
For each divisor $d$ of $56$, we have $b + 7 = d$, so $b = d - 7$:

| Divisor | $b = d - 7$ | Valid? ($b > 9$) |
|---------|-----------|------------------|
| 1       | -6        | No               |
| 2       | -5        | No               |
| 4       | -3        | No               |
| 7       | 0         | No               |
| 8       | 1         | No               |
| 14      | 7         | No               |
| 28      | 21        | **Yes**          |
| 56      | 49        | **Yes**          |

Valid bases: $b \in \{21, 49\}$

### Step 6: Verify Validity of Base Representations
The base must be larger than the largest digit used. Since we use the digit $9$ in $97_b$:
- For $b = 21$: $21 > 9$ ✓
- For $b = 49$: $49 > 9$ ✓

Both representations are valid.

### Step 7: Verify Divisibility
For $b = 21$:
- $17_{21} = 21 + 7 = 28$
- $97_{21} = 9(21) + 7 = 189 + 7 = 196$
- $196 \div 28 = 7$ ✓

For $b = 49$:
- $17_{49} = 49 + 7 = 56$
- $97_{49} = 9(49) + 7 = 441 + 7 = 448$
- $448 \div 56 = 8$ ✓

### Step 8: Calculate the Sum
$$\text{Sum} = 21 + 49 = 70$$

$\boxed{70}$
