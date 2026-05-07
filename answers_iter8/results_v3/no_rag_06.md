# AIME Problem Solution: Last Word Contains G

## Problem
The twelve letters A, B, C, D, E, F, G, H, I, J, K, and L are randomly grouped into six pairs. The two letters in each pair are placed in alphabetical order to form six two-letter words, and these words are listed alphabetically. Find the probability that the last word listed contains G.

## Solution

**Key Insight:** When the six two-letter words are sorted alphabetically, the last word is determined by which pair contains the maximum "smaller letter."

For each of the 6 pairs, we write it in alphabetical order. If a pair is {x, y} with x < y, the word is xy. Among all six words, the one that comes last alphabetically is the word whose first letter is the maximum among all minimum elements of the pairs.

**When is G in the last word?**

G is in the last word if and only if G is the maximum of the six "minimum elements" (the smaller letter in each pair).

This occurs when:
- G is paired with a letter larger than G (so G is the smaller in its pair)
- All other five pairs, formed from {A, B, C, D, E, F, I, J, K, L}, automatically have their minimum elements all less than G

Therefore, G must be paired with one of the five letters greater than G: **{H, I, J, K, L}**.

**Counting:**

Total number of ways to partition 12 letters into 6 unordered pairs:
$$\frac{12!}{2^6 \cdot 6!}$$

Number of ways where G is paired with one of {H, I, J, K, L}:
- Choose which of the 5 larger letters pairs with G: 5 choices
- Partition the remaining 10 letters into 5 pairs: $\frac{10!}{2^5 \cdot 5!}$ ways
- Total: $5 \cdot \frac{10!}{2^5 \cdot 5!}$

**Probability Calculation:**
$$P = \frac{5 \cdot \frac{10!}{2^5 \cdot 5!}}{\frac{12!}{2^6 \cdot 6!}} = \frac{5 \cdot 10! \cdot 2^6 \cdot 6!}{2^5 \cdot 5! \cdot 12!}$$

$$= \frac{5 \cdot 10! \cdot 2 \cdot 6!}{5! \cdot 12!} = \frac{5 \cdot 10! \cdot 2 \cdot 720}{120 \cdot 12 \cdot 11 \cdot 10!}$$

$$= \frac{5 \cdot 2 \cdot 720}{120 \cdot 132} = \frac{7200}{15840} = \frac{5}{11}$$

Since $\gcd(5, 11) = 1$, we have $m = 5$ and $n = 11$.

Therefore, $m + n = 5 + 11 = \boxed{16}$
