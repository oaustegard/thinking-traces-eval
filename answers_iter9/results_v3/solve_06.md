# Solution to AIME Pairing Problem

## Problem Setup
- 12 letters A through L are randomly grouped into 6 pairs
- Each pair forms a 2-letter word with letters in alphabetical order
- The 6 words are then sorted alphabetically
- Find the probability that the last (maximum) word contains G

## Solution

### Step 1: Understanding the Structure
When 12 letters are partitioned into 6 pairs, each pair forms a 2-letter word in alphabetical order. We then sort these 6 words lexicographically and seek the probability that G appears in the last word.

### Step 2: Key Insight
Given that G must be paired with exactly one other letter, there are 11 possible partners for G.

### Step 3: Determining When G's Word is Maximum
If G is paired with letter X, the resulting word is:
- `XG` if X < G (i.e., X ∈ {A, B, C, D, E, F})
- `GX` if X > G (i.e., X ∈ {H, I, J, K, L})

### Step 4: Analysis by Cases

**Case 1: G paired with A, B, C, D, E, or F**
If G is paired with one of these letters, the word is of the form `XG` (X < G).

For this word to be the maximum, we would need all other 5 words to be ≤ `XG`. But the other 5 words use letters from {H, I, J, K, L} and the remaining letters from {A-F}. Any word starting with H, I, J, K, or L would exceed `XG` (e.g., `GH` > `FG`). So G cannot be in the last word when paired with A-F.

**Case 2: G paired with H, I, J, K, or L**
If G is paired with one of these letters, the word is of the form `GX` (X ∈ {H, I, J, K, L}).

The maximum possible word starting with G is `GL`. The minimum is `GH`.

For `GX` to be the maximum word overall:
- All other words must be ≤ `GX` lexicographically
- Any word starting with A through F satisfies this (< `GX`)
- Any word starting with G must be ≤ `GX`, which is impossible since we can only form one word starting with G
- Any word starting with H-L that's not `GX`: but these letters are already used or are the partner of G

After pairing G with one of {H, I, J, K, L}, the remaining 10 letters form 5 pairs. These remaining letters are:
- All of {A, B, C, D, E, F} (6 letters)
- Four of {H, I, J, K, L} (the four not paired with G)

All possible 2-letter words from these 10 letters start with either A-F or H-L (excluding the letter paired with G). Every such word is < `GX` for any X ∈ {H, I, J, K, L}.

Therefore, whenever G is paired with one of {H, I, J, K, L}, the resulting word is automatically the maximum word in the sorted list.

### Step 5: Calculate Probability
The probability that G is paired with one of {H, I, J, K, L} equals the number of favorable partners divided by the total number of possible partners:

$$P(\text{G in last word}) = \frac{5}{11}$$

Since 5 and 11 are coprime, $m = 5$ and $n = 11$.

### Final Answer
$$m + n = 5 + 11 = 16$$

$\boxed{16}$
