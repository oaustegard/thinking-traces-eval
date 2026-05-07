# Steepest Descent: Mixed sin/cos Power Integral

## Problem
Compute the leading asymptotic behavior of the integral 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$, using steepest descent / Laplace method. Identify the critical point $x^*$ of the phase function, evaluate the phase at $x^*$, and assemble the Gaussian-fluctuation prefactor.

## Retrieved Examples and Relevance

**Example 1 (ex_2_14_wallis): Wallis Formula**
Wallis applies steepest descent to $\int_0^{\pi/2} (\sin x)^n dx$, identifying a boundary maximum at $x = \pi/2$ and using change of variables $x = \pi/2 - y$ to shift it to the origin, then extracting the asymptotic via Gaussian approximation. 

*Relevance*: High. The methodology is directly transferable: exponential reformulation, phase-function identification, critical-point localization, second-derivative evaluation, Gaussian prefactor assembly. The technique is the same.

*Key Difference*: Wallis has a boundary maximum (the exponent $\log \sin x$ is largest at the boundary), whereas the mixed $\log(\sin x) + \frac{1}{2}\log(\cos x)$ creates an interior critical point. The phase function, critical-point equation, and second-derivative formula are all distinct. Wallis's solution cannot be copied; instead, adapt the framework to the current nonstandard exponent structure.

**Example 2 (ex_2_20_morse): Morse Lemma**
Morse lemma applies to smooth functions on $\mathbb{R}^2$ (or higher dimensions) to establish local coordinate systems near nondegenerate critical points. It is a Morse-theoretical result, not an asymptotic integral evaluation.

*Relevance*: Minimal. While Morse lemma confirms that a nondegenerate critical point admits a canonical form, it does not provide the integral asymptotics directly. The domain is multidimensional Euclidean space, not a bounded interval with transcendental functions.

*Key Difference*: Entirely different domain (manifold vs. interval), entirely different application (local coordinates vs. integral evaluation). Not applicable here.

**Example 3 (ex_7_27_quartic_1pi): QFT 2-Point Function**
This is a quantum-field-theory path-integral problem using Feynman diagrams and summing perturbative contributions.

*Relevance*: Negligible. It addresses a different mathematical domain (path integrals and Feynman diagrams) and does not teach steepest descent on real integrals with transcendental phase functions.

*Key Difference*: Fundamentally different framework (QFT vs. classical analysis), different techniques (diagram enumeration vs. Laplace analysis).

---

## Solution

### Step 1: Reformulate as Exponential Integral

Write the integral in the form suitable for steepest descent:
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx = \int_0^{\pi/2} \exp\left[n \log(\sin x) + \frac{n}{2} \log(\cos x)\right] dx = \int_0^{\pi/2} e^{n f(x)} \, dx$$

where the phase function (exponent per unit $n$) is:
$$f(x) = \log(\sin x) + \frac{1}{2} \log(\cos x)$$

For large $n$, the integral is exponentially dominated by the maximum of $f(x)$ on $[0, \pi/2]$.

### Step 2: Localize the Interior Critical Point

Compute the first derivative:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2} \tan x$$

Set $f'(x) = 0$ to find critical points:
$$\cot x = \frac{1}{2} \tan x$$

Multiply through by $\sin x \cos x$:
$$\cos^2 x = \frac{1}{2} \sin^2 x \quad \Rightarrow \quad 2\cos^2 x = \sin^2 x$$

Using $\sin^2 x + \cos^2 x = 1$, substitute $\sin^2 x = 2\cos^2 x$:
$$2\cos^2 x + \cos^2 x = 1 \quad \Rightarrow \quad \cos^2 x = \frac{1}{3}, \quad \sin^2 x = \frac{2}{3}$$

Thus $\tan^2 x^* = 2$, and since $x^* \in (0, \pi/2)$:
$$x^* = \arctan(\sqrt{2}), \quad \sin x^* = \sqrt{\frac{2}{3}}, \quad \cos x^* = \sqrt{\frac{1}{3}}$$

This is an interior critical point, distinct from the boundary maxima seen in Wallis.

### Step 3: Evaluate the Phase at the Critical Point

$$f(x^*) = \log\left(\sqrt{\frac{2}{3}}\right) + \frac{1}{2} \log\left(\sqrt{\frac{1}{3}}\right) = \frac{1}{2} \log\left(\frac{2}{3}\right) + \frac{1}{4} \log\left(\frac{1}{3}\right)$$

Expand:
$$f(x^*) = \frac{1}{2}(\log 2 - \log 3) + \frac{1}{4}(0 - \log 3) = \frac{1}{2} \log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3 = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

Equivalently, the exponential factor is:
$$e^{f(x^*)} = 2^{1/2} \cdot 3^{-3/4} = \frac{\sqrt{2}}{3^{3/4}} = \sqrt{\frac{2}{3\sqrt{3}}}$$

### Step 4: Compute the Second Derivative to Verify the Maximum

$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$$

At $x^*$, where $\sin^2 x^* = 2/3$ and $\cos^2 x^* = 1/3$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}, \quad \sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$$

Therefore:
$$f''(x^*) = -\frac{3}{2} - \frac{1}{2}(3) = -\frac{3}{2} - \frac{3}{2} = -3$$

Since $f''(x^*) < 0$, the critical point is indeed a maximum, confirming the validity of steepest descent.

### Step 5: Apply Laplace's Method (Gaussian Approximation)

For an integral $\int_a^b e^{n f(x)} dx$ with an interior maximum at $x^* \in (a,b)$ where $f''(x^*) < 0$, Laplace's method gives:
$$\int_a^b e^{n f(x)} dx \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}} \quad \text{as } n \to \infty$$

Substitute $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$ and $|f''(x^*)| = 3$:
$$V(n) \sim e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} \sqrt{\frac{2\pi}{3n}} = 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}$$

### Step 6: Simplify the Exponential Prefactor

The exponential part can be consolidated as a single base:
$$2^{n/2} \cdot 3^{-3n/4} = (2)^{n/2} \cdot (3^{-3/4})^{n} = \left(2 \cdot 3^{-3/2}\right)^{n/2} = \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

---

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

Equivalently:
$$\boxed{V(n) \sim 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}}$$

**Critical subchecks confirmed:**
1. Interior critical point: $\tan^2 x^* = 2$ ✓
2. Phase value: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$ ✓
3. Second derivative: $|f''(x^*)| = 3$ ✓
4. Gaussian prefactor: $\sqrt{\frac{2\pi}{3n}}$ ✓
