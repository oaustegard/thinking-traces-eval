# Solution: Eight-digit Permutations Divisible by 22

## Problem
Find N, the count of eight-digit positive integers using digits 1-8 exactly once that are divisible by 22. Then find N - 2025.

## Solution

### Step 1: Divisibility Requirement
A number is divisible by 22 = 2 × 11 if and only if:
- **Divisible by 2:** Last digit is even (from {2,4,6,8})
- **Divisible by 11:** Alternating sum of digits ≡ 0 (mod 11)

### Step 2: Apply Divisibility by 11
For an 8-digit number with positions 1-8, the divisibility by 11 condition is:
$$(d_1 + d_3 + d_5 + d_7) - (d_2 + d_4 + d_6 + d_8) \equiv 0 \pmod{11}$$

Let $S_{odd}$ = sum of digits in odd positions
Let $S_{even}$ = sum of digits in even positions

Constraints:
- $S_{odd} + S_{even} = 1+2+3+4+5+6+7+8 = 36$
- $S_{odd} - S_{even} \equiv 0 \pmod{11}$

### Step 3: Solve for Position Sums
From $S_{odd} - S_{even} = 11k$ and $S_{odd} + S_{even} = 36$:
- $S_{odd} = 18 + 5.5k$

For integer solutions, k must be even. With the constraint $10 \leq S_{odd}, S_{even} \leq 26$:
- k = 0: $S_{odd} = S_{even} = 18$ ✓

Therefore: **Both odd and even position digits must sum to 18.**

### Step 4: Find Valid Partitions
Find all 4-element subsets of {1,2,3,4,5,6,7,8} summing to 18:

1. {1,2,7,8}
2. {1,3,6,8}
3. {1,4,5,8}
4. {1,4,6,7}
5. {2,3,5,8}
6. {2,3,6,7}
7. {2,4,5,7}
8. {3,4,5,6}

**Count: 8 partitions**

### Step 5: Verify Even Number Distribution
Each partition separates {1,2,3,4,5,6,7,8} (4 odd, 4 even) into two 4-element sets.
By pigeonhole, each set has exactly 2 even numbers and 2 odd numbers.

### Step 6: Count Valid Arrangements
For each partition with sets A and B:

**Option 1:** A in odd positions {1,3,5,7}, B in even positions {2,4,6,8}
- Arrange A in odd positions: 4! = 24 ways
- Arrange B in even positions with an even digit in position 8: 2 × 3! = 12 ways
- Subtotal: 24 × 12 = 288

**Option 2:** B in odd positions, A in even positions
- Similarly: 4! × (2 × 3!) = 288

**Per partition total:** 288 + 288 = 576

### Step 7: Calculate N
$$N = 8 \text{ partitions} \times 576 \text{ arrangements per partition} = 4608$$

### Step 8: Find the Difference
$$N - 2025 = 4608 - 2025 = 2583$$

\boxed{2583}
