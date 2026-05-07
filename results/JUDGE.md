# Judging (Opus 4.7, inline)

Scoring criteria per problem:
- **C (correct):** final answer correct in form and content; reasoning sound (minor algebra slips OK if they don't propagate).
- **P (partial):** part of the problem correct, part wrong, or right form with a wrong coefficient/sign.
- **W (wrong):** answer is wrong in a substantive way (wrong technique, wrong setup, missed required regime).

For ex_2_15 there are two regimes (a→+∞, a→i∞), each judged separately; "leading" and "second-order" judged separately within +∞.

## ex_2_15 — Bessel I_0(a) asymptotic

**Reference answer.** a → +∞: $I_0(a) \sim \frac{e^a}{\sqrt{2\pi a}}\bigl(1 + \frac{1}{8a} + O(a^{-2})\bigr)$. a → i∞ (write $a=ib$): $I_0(ib) \sim \sqrt{\frac{2}{\pi b}}\cos\!\bigl(b - \frac{\pi}{4}\bigr) + O(b^{-3/2})$, two stationary points combining into a cosine.

| Sub-judgment | No-RAG | RAG |
|---|---|---|
| +∞ leading $e^a/\sqrt{2\pi a}$ | **C** | **W** — boxed as $\sqrt{e^a/(4\pi a)}$ which equals $e^{a/2}/(2\sqrt{\pi a})$, missing a factor of $e^{a/2}$. (The pre-boxed line had it right; the simplification step is wrong.) |
| +∞ second-order $+1/(8a)$ | **W** — got $-1/(8a)$ | **C** — got $+1/(8a)$ |
| i∞ leading $\sqrt{2/(\pi b)}\cos(b-\pi/4)$ | **C** — identifies two stationary points, combines into cosine, $-\pi/4$ phase correct | **W** — uses one stationary point only; result $\propto e^{ib}/\sqrt{b}$ instead of $\cos b/\sqrt{b}$, missing the $\theta=\pi$ contribution entirely |

**Net:** No-RAG wins 2 sub-judgments, RAG wins 1. RAG mangled the +∞ leading form and missed the two-stationary-point combination at i∞.

**Diagnosis (RAG failure mode 1 — single-template anchoring).** The retrieved Wallis Struct describes a *single boundary maximum*, single-point Laplace expansion. RAG-Haiku anchored on this template and applied "expand around one stationary point and Gaussianize" to the i∞ case, which has two stationary points. No-RAG-Haiku, with no template to anchor on, correctly identified both.

## ex_3_24 — 1-loop log Z/Z₀ for S(x) = x²/2 − g(x² + x³/6)

**Reference answer.** The action contains both an $x^2$ mass-shift term and the cubic. Around $x=0$, the modified propagator from the $-gx^2$ term gives $1/(1-2g)$; the cubic contributes via diagrams as in ex_3_26 but with this modified propagator. The clean answer (saddle expansion at $x_c=0$) is $\log(Z/Z_0) = -\tfrac12\log(1-2g)$ + cubic-diagram contributions starting at $O(g^2)$. The graph count problem requires enumerating 1-loop graphs with $v_3=v_1$ (equal numbers of trivalent and univalent vertices since $L=1 \Leftrightarrow v_3=v_1$).

| Sub-judgment | No-RAG | RAG |
|---|---|---|
| Action correctly read | **C** — kept $x^2$ and $x^3/6$ both | **W** — dropped the $-gx^2$ term silently; analyzed $S = x^2/2 - gx^3/6$ (i.e. ex_3_26's action) |
| 1-loop log Z/Z₀ formula | **W** — produced $-g^2\hbar/72$ as the entire answer; missing the mass-shift contribution and most cubic contributions | **W** — derived $-\tfrac12\log(1-gx_c)$, which is the answer to ex_3_26, not ex_3_24 |
| Graph count $v_3=v_1$ identified | **C** — correctly derived $v_3 = v_1$ from Euler relation | **W** — never noticed the $v_1$ vertices because the action it analyzed has no 1-valent term |
| Graph count formula | **P** — gave correct counts for n=2,4,6 from intuition (1, 3, 15) but no closed form derivation | **W** — gave $\sum \binom{n}{k}(k-1)!/2$ which is the count of pure cycles, not graphs with both 1- and 3-valent vertices |

**Net:** Both wrong. RAG wrong worse — it transposed the problem to its retrieved example.

**Diagnosis (RAG failure mode 2 — problem transposition).** The RAG-Haiku agent did not just adopt the retrieved technique; it adopted the retrieved problem's *setup*. Because ex_3_26's Struct opens with "for $S(x) = x^2/2 - gx^3/6$, find...", RAG-Haiku silently substituted that action for the actual ex_3_24 action. This is a serious failure mode for niche RAG: when retrievals are highly framework-similar to the target, the model may copy too literally.

## ex_1_2_i — concave potential, action minimum (off-domain test)

**Reference answer.** Standard variational uniqueness/minimality argument: write any other admissible path as $q^* + \eta$ with $\eta(a)=\eta(b)=0$, expand action, first variation vanishes via Euler-Lagrange + boundary conditions, second variation $\delta^2 S \ge \int m|\dot\eta|^2/2 \ge 0$ with equality iff $\eta\equiv 0$, where the inequality uses concavity ($-U'' \ge 0$).

| Sub-judgment | No-RAG | RAG |
|---|---|---|
| Variational framing | **C** | **C** |
| Uniqueness argument | **P** — energy method has a slip (claims $\dot h(a)=\dot h(b)=0$ which doesn't follow from $h(a)=h(b)=0$); but recovers via second-variation argument | **C** — uses strict-convexity-of-action argument, clean and correct |
| Strict global minimality | **C** | **C** |

**Net:** RAG slightly cleaner. No poisoning observed despite no relevant trace in corpus.

**Diagnosis (no poisoning).** The retrieved examples are not relevant (none cover variational mechanics), but RAG-Haiku ignored them appropriately and gave a clean convexity-based proof. The "strategy" line at the top mentions ex_3_26 as inspiration but the actual proof doesn't use it. Consistent with H2 (off-domain no-harm) at this sample size.

## Aggregate

| Eval problem | No-RAG | RAG | Δ (RAG − No-RAG) |
|---|---|---|---|
| ex_2_15 (matched, intra-chapter) | ~0.7 | ~0.3 | **−0.4** |
| ex_3_24 (matched, same-technique) | ~0.4 | ~0.2 | **−0.2** |
| ex_1_2_i (off-domain) | ~0.8 | ~0.95 | **+0.15** |
| **Mean** | ~0.63 | ~0.48 | **−0.15** |

(Continuous scores are subjective Opus-judge approximations of "fraction of solution correct.")

Direction at this n=1 × 3 sample: **RAG slightly hurts in-domain, slightly helps off-domain.** Both directions are within sample noise — no statistical claim possible at n=3.
