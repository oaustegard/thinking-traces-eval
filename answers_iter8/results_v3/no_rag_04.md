# Solution: Permutations of 1-8 Divisible by 22

## Problem
Find the number N of 8-digit permutations of {1,2,3,4,5,6,7,8} divisible by 22, then find N - 2025.

## Solution

**Divisibility Conditions:**
- Divisible by 22 = divisible by 2 and 11
- Divisible by 2: last digit must be even (2, 4, 6, or 8)
- Divisible by 11: alternating digit sum must be ≡ 0 (mod 11)

**Divisibility by 11:**
For number $d_1d_2d_3d_4d_5d_6d_7d_8$:
$$(d_2 + d_4 + d_6 + d_8) - (d_1 + d_3 + d_5 + d_7) \equiv 0 \pmod{11}$$

Let E = sum of even-positioned digits, O = sum of odd-positioned digits.
- E + O = 36 (sum of 1-8)
- E - O ≡ 0 (mod 11)

From these conditions:
- 2E ≡ 36 ≡ 3 (mod 11)
- E ≡ 7 (mod 11)

Since 10 ≤ E ≤ 26, we have **E = 18** and **O = 18**.

**Finding Valid Subsets:**
4-element subsets of {1,2,3,4,5,6,7,8} summing to 18:
1. {1,2,7,8}
2. {1,3,6,8}
3. {1,4,5,8}
4. {1,4,6,7}
5. {2,3,5,8}
6. {2,3,6,7}
7. {2,4,5,7}
8. {3,4,5,6}

**Counting Arrangements:**
Each subset has exactly 2 even numbers. Since position 8 must be even:
- 2 choices for which even digit in position 8
- 3! = 6 ways to arrange other 3 digits in positions 2, 4, 6
- 4! = 24 ways to arrange complementary digits in positions 1, 3, 5, 7

Per subset: 2 × 6 × 24 = 288 arrangements
Total: 8 × 288 = **N = 2304**

**Final Answer:**
N - 2025 = 2304 - 2025 = **279**

$\boxed{279}$
