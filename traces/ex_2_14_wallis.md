# Trace: Etingof Exercise 2.14 (Wallis formula)

**Problem.** Calculate $W_n := \int_0^{\pi/2} \sin^n x\, dx$ for nonneg integers $n$ using integration by parts. Then apply steepest descent to this integral and discover a formula for $\pi$ (Wallis).

## Reasoning trace

I'll do the two parts: exact recursion, then asymptotic.

**Part A — recursion via integration by parts.**

For $n\ge 2$, write $\sin^n x = \sin^{n-1}x \cdot \sin x$ and integrate by parts with $u = \sin^{n-1}x$, $dv = \sin x\, dx$:
$$W_n = [-\sin^{n-1}x \cos x]_0^{\pi/2} + (n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2 x\,dx.$$
The boundary term vanishes (both endpoints kill it). Substitute $\cos^2 x = 1-\sin^2 x$:
$$W_n = (n-1)(W_{n-2} - W_n) \implies W_n = \frac{n-1}{n}W_{n-2}.$$

Initial values $W_0 = \pi/2$, $W_1 = 1$. Iterating:
- Even index: $W_{2m} = \dfrac{2m-1}{2m}\cdot\dfrac{2m-3}{2m-2}\cdots\dfrac{1}{2}\cdot\dfrac{\pi}{2} = \dfrac{(2m-1)!!}{(2m)!!}\cdot\dfrac{\pi}{2}.$
- Odd index: $W_{2m+1} = \dfrac{2m}{2m+1}\cdot\dfrac{2m-2}{2m-1}\cdots\dfrac{2}{3}\cdot 1 = \dfrac{(2m)!!}{(2m+1)!!}.$

Useful identity by direct multiplication:
$$W_{2m}\cdot W_{2m+1} = \frac{\pi}{2}\cdot\frac{(2m-1)!!\,(2m)!!}{(2m)!!\,(2m+1)!!} = \frac{\pi}{2(2m+1)}.\tag{*}$$

**Part B — steepest descent on $W_n$.**

Write $W_n = \int_0^{\pi/2} e^{n\log\sin x}\,dx$. The phase $f(x) = \log\sin x$ is increasing on $(0,\pi/2)$ with maximum at the **boundary** $x = \pi/2$, where $f(\pi/2) = 0$. So this is a Laplace-type integral with an interior boundary maximum, not an interior critical point.

Substitute $x = \pi/2 - y$, $y\in[0,\pi/2]$, $\sin x = \cos y$. Near $y=0$: $\cos y = 1 - y^2/2 + y^4/24 - \dots$, so
$$\log\cos y = -\tfrac{y^2}{2} - \tfrac{y^4}{12} - \dots = -\tfrac{y^2}{2}\bigl(1 + \tfrac{y^2}{6} + O(y^4)\bigr).$$
Therefore
$$W_n = \int_0^{\pi/2} e^{n\log\cos y}\,dy = \int_0^{\pi/2} e^{-ny^2/2}\bigl(1 - \tfrac{n y^4}{12} + O(\text{higher})\bigr)dy.$$

The Gaussian damping makes the upper limit irrelevant up to exponentially small error. Leading order:
$$W_n \sim \int_0^\infty e^{-ny^2/2}\,dy = \sqrt{\frac{\pi}{2n}}.$$

(One can extract the next correction from the $y^4$ term: $\int_0^\infty y^4 e^{-ny^2/2}dy = 3\sqrt{\pi/2}/n^{5/2}$, giving $W_n \sim \sqrt{\pi/(2n)}\bigl(1 - \tfrac{1}{4n} + O(n^{-2})\bigr)$. Not needed for the leading Wallis formula.)

**Part C — extracting $\pi$.**

From (*): $\pi = 2(2m+1) W_{2m} W_{2m+1}$. As $m\to\infty$, both $W_{2m}, W_{2m+1}$ are $\sim\sqrt{\pi/(2n)}$ at $n=2m$ and $n=2m+1$ — so $W_{2m}W_{2m+1} \sim \pi/(2\cdot 2m) = \pi/(4m)$. Plugging back gives the tautology $\pi = \pi$, so the leading asymptotic alone cannot produce $\pi$ — we need to combine the **exact** closed form with the asymptotic.

Equating the exact and asymptotic forms of $W_{2m}$:
$$\frac{(2m-1)!!}{(2m)!!}\cdot\frac{\pi}{2} \sim \sqrt{\frac{\pi}{4m}}.$$
Square both sides and solve for $\pi$:
$$\frac{\pi^2}{4}\left[\frac{(2m-1)!!}{(2m)!!}\right]^2 \sim \frac{\pi}{4m} \implies \pi \sim \frac{1}{m}\left[\frac{(2m)!!}{(2m-1)!!}\right]^2.$$

Equivalently, using $(2m)!! = 2^m m!$ and $(2m-1)!! = (2m)!/(2^m m!)$:
$$\boxed{\pi = \lim_{m\to\infty}\frac{1}{m}\left(\frac{2^{2m}(m!)^2}{(2m)!}\right)^2 = \lim_{m\to\infty}\frac{2^{4m}(m!)^4}{m\,((2m)!)^2}.}$$

This is the Wallis formula in its Stirling-equivalent form. The classical product version $\pi/2 = \prod_{m\ge 1}\tfrac{(2m)^2}{(2m-1)(2m+1)}$ follows by combining (*) with $W_{2m+1}/W_{2m}\to 1$ (which comes from the recursion plus monotonicity, not from steepest descent).

## Final answer

$$\pi = \lim_{m\to\infty}\frac{2^{4m}(m!)^4}{m\,((2m)!)^2}.$$
