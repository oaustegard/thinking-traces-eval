Let the integral be $V(n) = \int_0^{\pi/2} (\sin x)^n (\cos x)^{n/2} dx$. We want to find the leading asymptotic behavior of $V(n)$ as $n \to \infty$. We will use the steepest descent (or Laplace) method.

The steepest descent method is used to approximate integrals of the form $\int_a^b e^{n f(x)} g(x) dx$ as $n \to \infty$. Our integral is not directly in this form. We can rewrite it by taking the logarithm of the integrand.
Let $h(x) = (\sin x)^n (\cos x)^{n/2}$.
Then $\ln h(x) = n \ln(\sin x) + \frac{n}{2} \ln(\cos x)$.
So, $V(n) = \int_0^{\pi/2} e^{n (\ln(\sin x) + \frac{1}{2} \ln(\cos x))} dx$.
This integral is in the form $\int_a^b e^{n f(x)} dx$, where $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$. The function $g(x)$ here is implicitly 1.

The steepest descent method requires finding the maximum of the real-valued function $f(x)$ in the interval of integration. We need to find the critical points of $f(x)$ by setting its derivative to zero.
$f'(x) = \frac{d}{dx} (\ln(\sin x) + \frac{1}{2} \ln(\cos x))$
$f'(x) = \frac{\cos x}{\sin x} + \frac{1}{2} \frac{-\sin x}{\cos x}$
$f'(x) = \cot x - \frac{1}{2} \tan x$

To find the critical point $x^*$, we set $f'(x) = 0$:
$\cot x^* - \frac{1}{2} \tan x^* = 0$
$\frac{\cos x^*}{\sin x^*} = \frac{1}{2} \frac{\sin x^*}{\cos x^*}$
$2 \cos^2 x^* = \sin^2 x^*$

We can use the identity $\sin^2 x^* = 1 - \cos^2 x^*$:
$2 \cos^2 x^* = 1 - \cos^2 x^*$
$3 \cos^2 x^* = 1$
$\cos^2 x^* = \frac{1}{3}$

Since $x$ is in the interval $[0, \pi/2]$, $\cos x \ge 0$. Thus, $\cos x^* = \frac{1}{\sqrt{3}}$.
This means $\sin^2 x^* = 1 - \cos^2 x^* = 1 - \frac{1}{3} = \frac{2}{3}$.
Since $x$ is in $[0, \pi/2]$, $\sin x \ge 0$. Thus, $\sin x^* = \sqrt{\frac{2}{3}} = \frac{\sqrt{2}}{\sqrt{3}}$.
The location of the critical point is $x^* = \arccos\left(\frac{1}{\sqrt{3}}\right) = \arcsin\left(\frac{\sqrt{2}}{\sqrt{3}}\right)$.
This point $x^*$ is within the interval $[0, \pi/2]$.

Next, we need to evaluate the phase function $f(x)$ at the critical point $x^*$.
$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$f(x^*) = \ln\left(\frac{\sqrt{2}}{\sqrt{3}}\right) + \frac{1}{2} \ln\left(\frac{1}{\sqrt{3}}\right)$
$f(x^*) = \ln(\sqrt{2}) - \ln(\sqrt{3}) + \frac{1}{2} (\ln(1) - \ln(\sqrt{3}))$
$f(x^*) = \frac{1}{2} \ln(2) - \frac{1}{2} \ln(3) - \frac{1}{2} \ln(3)$
$f(x^*) = \frac{1}{2} \ln(2) - \ln(3)$
$f(x^*) = \ln\left(\frac{\sqrt{2}}{3}\right)$

The asymptotic behavior is given by $V(n) \sim \sqrt{\frac{2\pi}{n |f''(x^*)|}} e^{n f(x^*)} g(x^*)$.
In our case, $g(x) = 1$, so $g(x^*) = 1$. We need to compute the second derivative of $f(x)$ at $x^*$.
$f'(x) = \cot x - \frac{1}{2} \tan x$
$f''(x) = -\csc^2 x - \frac{1}{2} \sec^2 x$

Now evaluate $f''(x^*)$:
$\csc^2 x^* = \frac{1}{\sin^2 x^*} = \frac{1}{2/3} = \frac{3}{2}$
$\sec^2 x^* = \frac{1}{\cos^2 x^*} = \frac{1}{1/3} = 3$

$f''(x^*) = -\frac{3}{2} - \frac{1}{2} (3)$
$f''(x^*) = -\frac{3}{2} - \frac{3}{2}$
$f''(x^*) = -3$

The magnitude $|f''(x^*)| = 3$.

Now we assemble the Gaussian-fluctuation prefactor and the exponential term.
The integral is approximately:
$V(n) \sim \sqrt{\frac{2\pi}{n |-3|}} e^{n (\ln(\frac{\sqrt{2}}{3}))}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3}\right)^n$

Let's check the exponent more carefully.
$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*)$
$(\sin x^*)^n (\cos x^*)^{n/2} = \left(\sqrt{\frac{2}{3}}\right)^n \left(\frac{1}{\sqrt{3}}\right)^{n/2} = \left(\frac{\sqrt{2}}{\sqrt{3}}\right)^n \left(\frac{1}{3^{1/4}}\right)^n = \left(\frac{\sqrt{2}}{3^{1/2} 3^{1/4}}\right)^n = \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n$.
This is $e^{n f(x^*)}$.
$e^{n f(x^*)} = e^{n (\ln(\sqrt{2}) - \frac{3}{2} \ln(\sqrt{3}))} = e^{n (\frac{1}{2} \ln 2 - \frac{3}{2} \ln 3)} = e^{n \ln(2^{1/2}/3^{3/2})} = (2^{1/2}/3^{3/2})^n = (\sqrt{2}/(3\sqrt{3}))^n$.

Let's re-evaluate $f(x^*)$:
$f(x^*) = \ln(\sin x^*) + \frac{1}{2} \ln(\cos x^*) = \ln\left(\left(\frac{\sqrt{2}}{\sqrt{3}}\right) \left(\frac{1}{\sqrt{3}}\right)^{1/2}\right) = \ln\left(\frac{\sqrt{2}}{3^{1/2}} \frac{1}{3^{1/4}}\right) = \ln\left(\frac{\sqrt{2}}{3^{3/4}}\right)$.
So $e^{n f(x^*)} = \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n$.

The prefactor is $\sqrt{\frac{2\pi}{n |f''(x^*)|}} = \sqrt{\frac{2\pi}{3n}}$.

So the asymptotic behavior is $\sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n$.

Let's rewrite the integrand in the standard form:
$V(n) = \int_0^{\pi/2} e^{n f(x)} dx$, where $f(x) = \ln(\sin x) + \frac{1}{2} \ln(\cos x)$.
The maximum of $f(x)$ occurs at $x^*$, where $\cos^2 x^* = 1/3$ and $\sin^2 x^* = 2/3$.
$f(x^*) = \ln(\sqrt{2/3}) + \frac{1}{2} \ln(\sqrt{1/3}) = \frac{1}{2} \ln(2/3) + \frac{1}{4} \ln(1/3) = \frac{1}{2} \ln 2 - \frac{1}{2} \ln 3 + \frac{1}{4} (-\ln 3) = \frac{1}{2} \ln 2 - \frac{3}{4} \ln 3 = \ln(2^{1/2}/3^{3/4})$.
So $e^{n f(x^*)} = (2^{1/2}/3^{3/4})^n = (\sqrt{2}/3^{3/4})^n$.

$f''(x^*) = -3$.

The asymptotic formula is $\sqrt{\frac{2\pi}{n|f''(x^*)|}} e^{n f(x^*)}$.
$V(n) \sim \sqrt{\frac{2\pi}{n \cdot 3}} e^{n \ln(\sqrt{2}/3^{3/4})}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n$

Let's check the original integrand at $x^*$:
$(\sin x^*)^n (\cos x^*)^{n/2} = (\sqrt{2/3})^n (1/\sqrt{3})^{n/2} = (2/3)^{n/2} (1/3)^{n/4} = \frac{2^{n/2}}{3^{n/2}} \frac{1}{3^{n/4}} = \frac{2^{n/2}}{3^{3n/4}}$.
This matches $e^{n f(x^*)}$.

The location $x^*$ of the critical point is given by $\cos x^* = 1/\sqrt{3}$.
The value of the phase at $x^*$ is $f(x^*) = \ln(\sqrt{2}/3^{3/4})$.
The Gaussian-fluctuation prefactor is $\sqrt{2\pi / (3n)}$.

Therefore, the leading asymptotic behavior is:
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \left(\frac{\sqrt{2}}{3^{3/4}}\right)^n$.

Let's express the term $(\frac{\sqrt{2}}{3^{3/4}})^n$ in a cleaner way.
$(\frac{\sqrt{2}}{3^{3/4}})^n = \frac{(\sqrt{2})^n}{(3^{3/4})^n} = \frac{2^{n/2}}{3^{3n/4}}$.

Final Answer:
The location of the critical point is $x^*$ where $\cos x^* = 1/\sqrt{3}$.
The value of the phase function at $x^*$ is $f(x^*) = \ln(\sqrt{2}) - \frac{3}{4}\ln(3)$.
The second derivative of the phase function at $x^*$ is $f''(x^*) = -3$.
The leading asymptotic behavior is given by $\sqrt{\frac{2\pi}{n|f''(x^*)|}} e^{n f(x^*)}$.
$V(n) \sim \sqrt{\frac{2\pi}{n \cdot 3}} e^{n (\ln(\sqrt{2}) - \frac{3}{4}\ln(3))}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} e^{\ln((\sqrt{2})^n) - \ln((3^{3/4})^n)}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \frac{(\sqrt{2})^n}{(3^{3/4})^n}$
$V(n) \sim \sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}$

The final answer is $\boxed{\sqrt{\frac{2\pi}{3n}} \frac{2^{n/2}}{3^{3n/4}}}$.