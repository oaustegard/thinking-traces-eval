# AIME Problem: Permutations of 1-8 Divisible by 22

## Problem
There are $8! = 40320$ eight-digit positive integers that use each of the digits 1, 2, 3, 4, 5, 6, 7, 8 exactly once. Let N be the number of these integers that are divisible by 22. Find the difference between N and 2025.

## Solution

### Step 1: Divisibility Conditions
A number is divisible by 22 if and only if it is divisible by both 2 and 11 (since $22 = 2 \times 11$ and $\gcd(2,11) = 1$).

**Divisibility by 2:** The last digit must be even. Among {1,2,3,4,5,6,7,8}, the even digits are {2,4,6,8}.

**Divisibility by 11:** A number is divisible by 11 if the alternating sum of its digits is divisible by 11.

For an 8-digit number $d_1d_2d_3d_4d_5d_6d_7d_8$:
$$(d_1 + d_3 + d_5 + d_7) - (d_2 + d_4 + d_6 + d_8) \equiv 0 \pmod{11}$$

### Step 2: Finding the Alternating Sum Condition
Let $S_{\text{odd}}$ = sum of digits in odd positions and $S_{\text{even}}$ = sum of digits in even positions.

We have:
$$S_{\text{odd}} + S_{\text{even}} = 1+2+3+4+5+6+7+8 = 36$$

We need:
$$S_{\text{odd}} - S_{\text{even}} \equiv 0 \pmod{11}$$

From these two equations:
- $S_{\text{odd}} - S_{\text{even}} \equiv 0 \pmod{11}$
- $S_{\text{odd}} + S_{\text{even}} = 36$

Since both equations must hold and $S_{\text{odd}} - S_{\text{even}}$ must equal $36 - 2S_{\text{even}}$, and this must be divisible by 11:
$$2S_{\text{odd}} = S_{\text{odd}} + S_{\text{even}} + (S_{\text{odd}} - S_{\text{even}})$$

For the alternating sum to be 0 (mod 11) with sum 36, we get $S_{\text{odd}} = 18$ and $S_{\text{even}} = 18$.

### Step 3: Finding Valid Digit Partitions
We need to partition {1,2,3,4,5,6,7,8} into two sets of 4 digits each, both summing to 18.

The valid partitions are:
1. {1,2,7,8} and {3,4,5,6}
2. {1,3,6,8} and {2,4,5,7}
3. {1,4,5,8} and {2,3,6,7}
4. {1,4,6,7} and {2,3,5,8}
5. {2,3,5,8} and {1,4,6,7}
6. {2,3,6,7} and {1,4,5,8}
7. {2,4,5,7} and {1,3,6,8}
8. {3,4,5,6} and {1,2,7,8}

### Step 4: Counting Valid Arrangements
For each partition, one set goes to odd positions {1,3,5,7} and the other to even positions {2,4,6,8}.

The constraint is that position 8 (even position) must contain an even digit.

For each of the 8 partitions:
- Each partition has exactly one set assigned to even positions
- Each even-position set contains exactly 2 even digits from {2,4,6,8}
- Number of ways to arrange: (# of even digits in even set) × 3! × 4! = 2 × 6 × 24 = 288

### Step 5: Computing N
$$N = 8 \times 288 = 2304$$

### Step 6: Finding the Difference
$$N - 2025 = 2304 - 2025 = 279$$

$$\boxed{279}$$
