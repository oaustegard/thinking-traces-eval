# OOD Steepest Descent Solution

## Problem Setup

We need to find the leading asymptotic behavior of:
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$ using steepest descent (Laplace's method).

## Step 1: Identify the Phase Function

Rewrite the integrand in exponential form:
$$(\sin x)^n (\cos x)^{n/2} = \exp\left[n \log(\sin x) + \frac{n}{2} \log(\cos x)\right]$$

Define the phase function:
$$f(x) = \log(\sin x) + \frac{1}{2} \log(\cos x)$$

Then:
$$V(n) = \int_0^{\pi/2} e^{n f(x)} \, dx$$

## Step 2: Find the Critical Point

Taking the derivative:
$$f'(x) = \cot x - \frac{1}{2} \tan x$$

Setting $f'(x) = 0$:
$$\cot x = \frac{1}{2} \tan x$$

$$\frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x}$$

$$2 \cos^2 x = \sin^2 x$$

$$\tan^2 x = 2$$

$$x^* = \arctan(\sqrt{2})$$

## Step 3: Evaluate the Phase at the Critical Point

From $\tan x^* = \sqrt{2}$, we get a right triangle with opposite $\sqrt{2}$, adjacent $1$, and hypotenuse $\sqrt{3}$.

Therefore:
- $\sin x^* = \sqrt{\frac{2}{3}}$
- $\cos x^* = \sqrt{\frac{1}{3}} = \frac{1}{\sqrt{3}}$

Evaluating the phase:
$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2} \log\sqrt{\frac{1}{3}}$$

$$= \frac{1}{2} \log\frac{2}{3} + \frac{1}{4} \log\frac{1}{3}$$

$$= \frac{1}{2} \log 2 - \frac{1}{2} \log 3 - \frac{1}{4} \log 3$$

$$= \frac{1}{2} \log 2 - \frac{3}{4} \log 3$$

## Step 4: Compute the Second Derivative

$$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$$

At $x^*$:
- $\csc^2 x^* = \frac{3}{2}$ (since $\sin^2 x^* = 2/3$)
- $\sec^2 x^* = 3$ (since $\cos^2 x^* = 1/3$)

Therefore:
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

## Step 5: Apply Laplace's Method

The leading asymptotic for $\int e^{nf(x)} dx$ around a critical point is:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n |f''(x^*)|}}$$

Substituting:
$$V(n) \sim e^{n(\frac{1}{2}\log 2 - \frac{3}{4}\log 3)} \sqrt{\frac{2\pi}{3n}}$$

$$= 2^{n/2} \cdot 3^{-3n/4} \sqrt{\frac{2\pi}{3n}}$$

This can be rewritten as:
$$V(n) \sim \left(\frac{2}{3^{3/2}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

or equivalently:
$$V(n) \sim \left(\frac{2}{3\sqrt{3}}\right)^{n/2} \sqrt{\frac{2\pi}{3n}}$$

## Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

Key features:
- Critical point: $x^* = \arctan(\sqrt{2})$ with $\tan^2 x^* = 2$
- Phase value: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$
- Second derivative: $|f''(x^*)| = 3$
- Gaussian prefactor: $\sqrt{2\pi/(3n)}$
