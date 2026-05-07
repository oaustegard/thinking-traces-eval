# Steepest Descent: Leading Asymptotic of V(n)

## Problem Setup
We compute the leading asymptotic behavior of 
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} \, dx$$
as $n \to \infty$ using the method of steepest descent (Laplace's method).

## Step 1: Identify the Phase Function
Rewrite the integrand as
$$(\sin x)^n (\cos x)^{n/2} = \exp\left[n \log(\sin x) + \frac{n}{2} \log(\cos x)\right] = \exp[n f(x)]$$
where the phase function is
$$f(x) = \log(\sin x) + \frac{1}{2} \log(\cos x).$$

## Step 2: Find the Critical Point
For steepest descent, we need the saddle point where $f'(x) = 0$:
$$f'(x) = \cot x - \frac{1}{2} \tan x = \frac{\cos x}{\sin x} - \frac{1}{2} \frac{\sin x}{\cos x} = 0.$$

Multiply by $\sin x \cos x$:
$$\cos^2 x - \frac{1}{2} \sin^2 x = 0 \quad \Rightarrow \quad 2\cos^2 x = \sin^2 x.$$

This gives $\tan^2 x = 2$, so $\tan x = \sqrt{2}$ (taking the positive root in $(0, \pi/2)$).

At this critical point $x^* = \arctan(\sqrt{2})$:
- $\sin x^* = \frac{\sqrt{2}}{\sqrt{3}} = \sqrt{\frac{2}{3}}$
- $\cos x^* = \frac{1}{\sqrt{3}} = \sqrt{\frac{1}{3}}$

## Step 3: Evaluate the Phase at the Critical Point
$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2} \log\sqrt{\frac{1}{3}} = \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3}$$
$$= \frac{1}{2}(\log 2 - \log 3) + \frac{1}{4}(- \log 3) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3.$$

Alternatively: $\exp(f(x^*)) = (2/3)^{1/2} \cdot (1/3)^{1/4} = 2^{1/2} \cdot 3^{-3/4}$.

## Step 4: Compute the Second Derivative
$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x.$$

At $x^*$, with $\sin x^* = \sqrt{2/3}$ and $\cos x^* = \sqrt{1/3}$:
- $\csc^2 x^* = \frac{3}{2}$
- $\sec^2 x^* = 3$

$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3.$$

## Step 5: Apply the Laplace/Steepest Descent Formula
The leading asymptotic is given by the Gaussian approximation:
$$V(n) \sim \exp[n f(x^*)] \sqrt{\frac{2\pi}{n |f''(x^*)|}} = \exp[n f(x^*)] \sqrt{\frac{2\pi}{3n}}.$$

Substituting $\exp(f(x^*)) = 2^{1/2} \cdot 3^{-3/4}$:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}.$$

This can also be written as:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}.$$

## Summary of Key Results
- **Critical point:** $x^* = \arctan(\sqrt{2})$; equivalently $\tan^2 x^* = 2$
- **Phase value:** $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$
- **Second derivative:** $f''(x^*) = -3$
- **Gaussian prefactor:** $\sqrt{\frac{2\pi}{3n}}$

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

Equivalently:
$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$
