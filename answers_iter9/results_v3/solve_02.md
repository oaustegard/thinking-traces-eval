# Solution to AIME Ice Cream Problem

## Problem Setup

We have 9 baseball players, each choosing chocolate (c), vanilla (v), or strawberry (s) ice cream with constraints:
- c + v + s = 9
- c > v > s ≥ 1 (each flavor chosen by at least one player, strict inequalities)

We need to find N = number of valid flavor assignments, then find N mod 1000.

## Step 1: Enumerate Valid (c, v, s) Triples

Since s ≥ 1 and v > s, we have v ≥ 2. Since c > v, we have c ≥ 3.

**Case s = 1:**
- c + v = 8 with c > v > 1
  - v = 2: c = 6 ✓ (6 > 2)
  - v = 3: c = 5 ✓ (5 > 3)
  - v = 4: c = 4 ✗ (4 ≯ 4)
- Valid triples: (6, 2, 1), (5, 3, 1)

**Case s = 2:**
- c + v = 7 with c > v > 2
  - v = 3: c = 4 ✓ (4 > 3)
  - v = 4: c = 3 ✗ (3 ≯ 4)
- Valid triples: (4, 3, 2)

**Case s = 3:**
- c + v = 6 with c > v > 3
  - v = 4: c = 2 ✗ (2 ≯ 4)
- No valid triples

**Case s ≥ 4:** Not possible since 3(4) = 12 > 9.

Valid triples: **(6, 2, 1), (5, 3, 1), (4, 3, 2)**

## Step 2: Count Assignments for Each Triple

For each triple (c, v, s), the number of ways to assign flavors is the multinomial coefficient:
$$\binom{9}{c, v, s} = \frac{9!}{c! \cdot v! \cdot s!}$$

**For (6, 2, 1):**
$$\binom{9}{6, 2, 1} = \frac{9!}{6! \cdot 2! \cdot 1!} = \frac{362880}{720 \cdot 2 \cdot 1} = \frac{362880}{1440} = 252$$

**For (5, 3, 1):**
$$\binom{9}{5, 3, 1} = \frac{9!}{5! \cdot 3! \cdot 1!} = \frac{362880}{120 \cdot 6 \cdot 1} = \frac{362880}{720} = 504$$

**For (4, 3, 2):**
$$\binom{9}{4, 3, 2} = \frac{9!}{4! \cdot 3! \cdot 2!} = \frac{362880}{24 \cdot 6 \cdot 2} = \frac{362880}{288} = 1260$$

## Step 3: Calculate Total

$$N = 252 + 504 + 1260 = 2016$$

## Step 4: Find Remainder Modulo 1000

$$N \mod 1000 = 2016 \mod 1000 = 16$$

$\boxed{16}$
