## Reasoning trace

**Definition of 1-loop contribution in zero-dimensional QFT.**
For a zero-dimensional quantum field theory with action $S(x)$, the partition function is $Z = \int e^{-S(x)/\hbar}\,dx$. The free partition function is $Z_0 = \int e^{-S_0(x)/\hbar}\,dx$ where $S_0(x)$ is the quadratic part of $S(x)$.
The 1-loop contribution to $\log(Z/Z_0)$ is obtained by considering the Gaussian approximation of the path integral around the classical minimum $x_c$. If $S(x_c)=0$ (which is true for our action at $x_c=0$), then
$$\log Z = \frac{1}{2}\log(2\pi\hbar) - \frac{1}{2}\log S''(x_c).$$
For the free theory, $S_0(x) = x^2/2$, so $S_0''(0) = 1$. Thus, $\log Z_0 = \frac{1}{2}\log(2\pi\hbar) - \frac{1}{2}\log(1) = \frac{1}{2}\log(2\pi\hbar)$.
Therefore, the 1-loop contribution to $\log(Z/Z_0)$ is given by
$$\log(Z/Z_0) = -\frac{1}{2}\log S''(x_c),$$
where $x_c$ is the classical minimum of $S(x)$.

**Finding the classical minimum $x_c$.**
The classical minimum $x_c$ satisfies $S'(x_c) = 0$.
Our action is $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$.
Let's compute the first derivative $S'(x)$:
$$S'(x) = \frac{d}{dx}\left(\frac{x^2}{2}\right) - \frac{g}{2}\frac{d}{dx}(x^2 \cosh(x))$$
$$S'(x) = x - \frac{g}{2}(2x\cosh(x) + x^2\sinh(x)).$$
Setting $S'(x_c) = 0$:
$$x_c - \frac{g}{2}(2x_c\cosh(x_c) + x_c^2\sinh(x_c)) = 0.$$
One obvious solution is $x_c=0$. Substituting $x_c=0$ into $S'(x)$ yields $0 - 0 = 0$. So $x_c=0$ is a classical critical point. We assume $g$ is small enough for it to be a minimum.

**Calculating $S''(x_c)$.**
Now we compute the second derivative $S''(x)$ and evaluate it at $x_c=0$:
$$S''(x) = \frac{d}{dx}\left(x - \frac{g}{2}(2x\cosh(x) + x^2\sinh(x))\right)$$
$$S''(x) = 1 - \frac{g}{2}\frac{d}{dx}(2x\cosh(x) + x^2\sinh(x)).$$
Let's differentiate the term in the parenthesis:
$$\frac{d}{dx}(2x\cosh(x) + x^2\sinh(x)) = (2\cosh(x) + 2x\sinh(x)) + (2x\sinh(x) + x^2\cosh(x))$$
$$= (2+x^2)\cosh(x) + 4x\sinh(x).$$
So,
$$S''(x) = 1 - \frac{g}{2}((2+x^2)\cosh(x) + 4x\sinh(x)).$$
Now, evaluate at $x_c=0$:
$$S''(0) = 1 - \frac{g}{2}((2+0)\cosh(0) + 4(0)\sinh(0))$$
$$S''(0) = 1 - \frac{g}{2}(2 \cdot 1 + 0) = 1 - \frac{g}{2}(2) = 1-g.$$

**The 1-loop contribution to $\log(Z/Z_0)$.**
Plugging $S''(0) = 1-g$ into the formula for $\log(Z/Z_0)$:
$$\log(Z/Z_0) = -\frac{1}{2}\log(1-g).$$

**Expansion in $g$ through order $g^3$.**
Using the Taylor series expansion for $\log(1-u) = -u - \frac{u^2}{2} - \frac{u^3}{3} - O(u^4)$:
$$\log(Z/Z_0) = -\frac{1}{2}\left(-g - \frac{g^2}{2} - \frac{g^3}{3} - O(g^4)\right)$$
$$\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).$$

**Feynman diagram interpretation (optional check, not required by problem but good for consistency).**
The interaction part of the action is $S_{\text{int}}(x) = -\frac{g}{2}x^2\cosh(x)$. Expanding $\cosh(x) = \sum_{k=0}^\infty \frac{x^{2k}}{(2k)!}$:
$S_{\text{int}}(x) = -\frac{g}{2}\sum_{k=0}^\infty \frac{x^{2k+2}}{(2k)!} = -\frac{g}{2}x^2 - \frac{g}{4}x^4 - \frac{g}{48}x^6 - \dots$.
The 1-loop contribution to $\log(Z/Z_0)$ (the vacuum energy) is the sum of all connected 1-loop vacuum diagrams. A 1-loop vacuum diagram, by definition, must be a single closed cycle of propagators and vertices. For a vertex of valence $N$, it can form a single loop only if $N=2$. If $N>2$, a single vertex would form $N/2$ loops (e.g., a 4-valent vertex forms a "figure eight" diagram which is a 2-loop diagram).
Thus, only the 2-valent interaction term $-(g/2)x^2$ contributes to the 1-loop vacuum energy. This term effectively modifies the quadratic part of the action from $x^2/2$ to $(1-g)x^2/2$, precisely leading to the $1-g$ factor in $S''(0)$. The diagrams are necklaces of 2-valent vertices: a single 2-valent vertex forming a loop ($g/2$), two 2-valent vertices forming a loop ($g^2/4$), three 2-valent vertices forming a loop ($g^3/6$), etc., which sum up to $-\frac{1}{2}\log(1-g)$.

## Final answer

The 1-loop contribution to $\log(Z/Z_0)$ is given by $-\frac{1}{2}\log S''(x_c)$, where $S'(x_c)=0$.
For the given action $S(x) = \frac{x^2}{2} - \frac{g}{2} x^2 \cosh(x)$, the classical minimum is $x_c=0$.
The second derivative at $x_c=0$ is $S''(0) = 1-g$.
Thus, the 1-loop contribution to $\log(Z/Z_0)$ is:
$$-\frac{1}{2}\log(1-g).$$
Expanding this as a power series in $g$ through order $g^3$:
$$\boxed{\log(Z/Z_0) = \frac{g}{2} + \frac{g^2}{4} + \frac{g^3}{6} + O(g^4).}$$