# Structured Reasoning: Wallis Formula

**Problem:** Calculate $W_n := \int_0^{\pi/2} \sin^n x\, dx$ and apply steepest descent to derive a formula for $\pi$ (Wallis).

**Step 1:** Set up integration by parts recursion by writing $\sin^n x = \sin^{n-1}x \cdot \sin x$ with $u = \sin^{n-1}x$, $dv = \sin x\, dx$ to obtain boundary-free relation $W_n = \frac{n-1}{n}W_{n-2}$.

**Step 2:** Iterate the recursion from initial values $W_0 = \pi/2$, $W_1 = 1$ to express even and odd cases in terms of double factorials: $W_{2m} \cdot W_{2m+1} = \frac{\pi}{2(2m+1)}$.

**Step 3:** Rewrite $W_n$ as exponential integral $\int_0^{\pi/2} e^{n\log\sin x}\,dx$ and identify the phase function $f(x) = \log\sin x$ achieves its maximum at the boundary $x = \pi/2$.

**Step 4:** Substitute $x = \pi/2 - y$ to move the maximum to $y=0$ and expand $\log\cos y \approx -\frac{y^2}{2}(1 + \frac{y^2}{6} + \cdots)$ near the boundary.

**Step 5:** Extract the leading asymptotic behavior $W_n \sim \sqrt{\frac{\pi}{2n}}$ by evaluating the Gaussian integral $\int_0^\infty e^{-ny^2/2}dy$ (upper limit becomes irrelevant due to exponential damping).

**Step 6:** Equate exact and asymptotic forms of $W_{2m}$ to cancel $\pi$ from both sides and obtain the ratio $\pi = \frac{1}{m}\left[\frac{(2m)!!}{(2m-1)!!}\right]^2$ in the limit.

**Step 7:** Rewrite using $\pi = \lim_{m\to\infty}\frac{2^{4m}(m!)^4}{m\,((2m)!)^2}$.

**Answer:** $\boxed{\pi = \lim_{m\to\infty}\frac{2^{4m}(m!)^4}{m\,((2m)!)^2}}$
