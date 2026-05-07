# Solution: Steepest Descent for V(n)

We compute the leading asymptotic behavior of
$$V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$$
as $n \to \infty$ using the steepest descent (Laplace) method.

## Step 1: Identify the Phase Function

Rewrite the integrand:
$$(\sin x)^n (\cos x)^{n/2} = \exp[n \log(\sin x) + \frac{n}{2}\log(\cos x)] = \exp[n f(x)]$$

where the phase function is:
$$f(x) = \log(\sin x) + \frac{1}{2}\log(\cos x)$$

## Step 2: Find the Critical Point

For steepest descent, we need $f'(x^*) = 0$:
$$f'(x) = \frac{\cos x}{\sin x} - \frac{\sin x}{2\cos x} = \cot x - \frac{1}{2}\tan x$$

Setting this to zero:
$$\cot x = \frac{1}{2}\tan x$$
$$\frac{\cos x}{\sin x} = \frac{1}{2} \cdot \frac{\sin x}{\cos x}$$
$$2\cos^2 x = \sin^2 x$$
$$\tan^2 x = 2$$

Thus $\tan x^* = \sqrt{2}$ (taking the positive root in $(0, \pi/2)$), which gives:
$$x^* = \arctan(\sqrt{2})$$

## Step 3: Compute Trigonometric Values at the Critical Point

From $\tan x^* = \sqrt{2}$, we have a right triangle with opposite side $\sqrt{2}$ and adjacent side $1$, so hypotenuse is $\sqrt{3}$:
$$\sin x^* = \frac{\sqrt{2}}{\sqrt{3}} = \sqrt{\frac{2}{3}}$$
$$\cos x^* = \frac{1}{\sqrt{3}} = \sqrt{\frac{1}{3}}$$

## Step 4: Evaluate the Phase at the Critical Point

$$f(x^*) = \log\sqrt{\frac{2}{3}} + \frac{1}{2}\log\sqrt{\frac{1}{3}}$$
$$= \frac{1}{2}\log\frac{2}{3} + \frac{1}{4}\log\frac{1}{3}$$
$$= \frac{1}{2}\log 2 - \frac{1}{2}\log 3 - \frac{1}{4}\log 3$$
$$= \frac{1}{2}\log 2 - \frac{3}{4}\log 3$$

## Step 5: Compute the Second Derivative

$$f''(x) = -\csc^2 x - \frac{1}{2}\sec^2 x$$

At $x^*$:
$$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{3}{2}$$
$$\sec^2 x^* = \frac{1}{\cos^2 x^*} = 3$$

Therefore:
$$f''(x^*) = -\frac{3}{2} - \frac{3}{2} = -3$$

## Step 6: Apply the Laplace Formula

The leading asymptotic is:
$$V(n) \sim e^{n f(x^*)} \sqrt{\frac{2\pi}{n|f''(x^*)|}}$$

$$= \exp\left[n\left(\frac{1}{2}\log 2 - \frac{3}{4}\log 3\right)\right] \sqrt{\frac{2\pi}{3n}}$$

$$= 2^{n/2} \cdot 3^{-3n/4} \cdot \sqrt{\frac{2\pi}{3n}}$$

This can be written equivalently as:
$$V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3^{3/2}}\right)^{n/2} = \sqrt{\frac{2\pi}{3n}} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}$$

## Final Answer

$$\boxed{V(n) \sim \sqrt{\frac{2\pi}{3n}} \cdot 2^{n/2} \cdot 3^{-3n/4}}$$

or equivalently:

$$\boxed{V(n) \sim \left(\frac{2\pi}{3n}\right)^{1/2} \cdot \left(\frac{2}{3\sqrt{3}}\right)^{n/2}}$$

**Critical checks:** (1) Critical point equation yields $\tan^2 x^* = 2$. (2) Phase value: $f(x^*) = \frac{1}{2}\log 2 - \frac{3}{4}\log 3$. (3) Second derivative: $|f''(x^*)| = 3$. (4) Gaussian prefactor: $\sqrt{\frac{2\pi}{3n}}$.
