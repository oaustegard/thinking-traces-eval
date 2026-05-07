# Solution to AIME Problem: Probability G is in Last Word

## Problem
Twelve letters A, B, C, D, E, F, G, H, I, J, K, and L are randomly grouped into six pairs. Each pair is arranged alphabetically to form a two-letter word. The six words are then listed alphabetically. Find the probability that the last word contains G.

## Solution

### Step 1: Understand the Setup
- 12 letters are randomly partitioned into 6 pairs (unordered grouping)
- Each pair forms a word with letters in alphabetical order
- The 6 words are sorted alphabetically
- We want P(G appears in the last word alphabetically)

### Step 2: Key Insight - Symmetry Argument
By symmetry, when we randomly partition the 12 letters into 6 pairs and then identify which pair corresponds to the lexicographically largest word, each letter has an equal probability of appearing in that final pair.

This is because:
- The pairing process is completely random and symmetric with respect to all letters
- The ordering of words is deterministic given the pairing
- Before the random pairing occurs, no letter has a special property that would make it more likely to be in the "last" pair

### Step 3: Calculate the Probability
- Total number of letters: 12
- Number of letters in the final (last) word: 2
- By symmetry, the probability that any specific letter is in the last word is:

$$P(\text{G in last word}) = \frac{\text{Number of positions in final pair}}{\text{Total number of positions}} = \frac{2}{12} = \frac{1}{6}$$

### Step 4: Verify the Fraction is in Lowest Terms
$\gcd(1, 6) = 1$, so the fraction $\frac{1}{6}$ is already in lowest terms.

Therefore: $m = 1$ and $n = 6$

### Step 5: Final Answer
$$m + n = 1 + 6 = 7$$

$\boxed{7}$
