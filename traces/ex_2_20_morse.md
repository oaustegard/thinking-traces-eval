# Trace: Etingof Exercise 2.20 (explicit Morse coordinates for a cubic)

**Problem.** Let $f(x,y) = a(y) + b(y)x + c(y)x^2 + d(y)x^3$ with $a(0) = a'(0) = b(0) = b'(0) = 0$ and $a''(0) = c(0) = 2$. Find explicit local coordinates $u(x,y), v(x,y)$ near the origin such that $f = u^2 + v^2$.

## Reasoning trace

**Hessian check.** Compute partials at origin: $f_x(0) = b(0) = 0$, $f_y(0) = a'(0) = 0$ — so origin is critical. Then $f_{xx}(0) = 2c(0) = 4$, $f_{yy}(0) = a''(0) = 2$, $f_{xy}(0) = b'(0) = 0$. Hessian is diag$(4, 2)$, positive definite — Morse lemma applies; goal is to construct the coordinate change explicitly.

**Strategy: split $f$ into an "$x$-piece" and a "$y$-piece," build each as a square.**

Observe that the *cubic-in-$x$* terms $c(y)x^2 + d(y)x^3 = x^2(c(y) + d(y)x)$ factor cleanly. Since $c(0) = 2 > 0$ and we work near the origin, $c(y) + d(y)x > 0$ in a neighborhood of $0$, so its square root is smooth there. Define
$$u(x,y) := x\sqrt{c(y) + d(y)x}.$$
Then $u^2 = x^2(c(y) + d(y)x) = c(y)x^2 + d(y)x^3$ — capturing the entire $x$-cubic-and-quadratic content of $f$.

**Residual.** What remains is $f - u^2 = a(y) + b(y)x$. The conditions on $a$ and $b$ make both vanish to second order at $y=0$:
- $a(0) = a'(0) = 0$ and $a''(0) = 2$ ⇒ by Taylor's theorem with integral remainder, $a(y) = y^2 h(y)$ where $h$ is smooth and $h(0) = a''(0)/2 = 1$.
- $b(0) = b'(0) = 0$ ⇒ $b(y) = y^2 k(y)$ where $k$ is smooth, $k(0) = b''(0)/2$.

Therefore
$$a(y) + b(y)x = y^2 h(y) + y^2 k(y) x = y^2 \bigl(h(y) + k(y) x\bigr).$$
Near the origin, $h(y) + k(y)x \to h(0) = 1 > 0$, so its square root is smooth. Define
$$v(x,y) := y \sqrt{h(y) + k(y) x} = y \sqrt{\frac{a(y)}{y^2} + \frac{b(y)}{y^2} x}.$$
Then $v^2 = y^2(h(y) + k(y)x) = a(y) + b(y)x$.

**Combine.**
$$u^2 + v^2 = c(y) x^2 + d(y) x^3 + a(y) + b(y) x = f(x, y). \quad\checkmark$$

**Local-coordinate check.** Compute the Jacobian of $(u,v)$ at the origin.
- $u_x(0,0) = \sqrt{c(0) + 0} = \sqrt{2}$ (the $x$-derivative of the prefactor $\sqrt{c+dx}$ evaluated at $x=0$ vanishes after multiplication by $x$);
- $u_y(0,0) = 0$ (since $u$ has an $x$-prefactor, all $y$-derivatives at $x=0$ kill it);
- $v_y(0,0) = \sqrt{h(0)} = 1$ (similar argument);
- $v_x(0,0) = 0$.

Jacobian determinant $= \sqrt{2} \cdot 1 - 0 = \sqrt 2 \ne 0$, so $(u, v)$ are valid smooth local coordinates near the origin. The map $(x,y) \mapsto (u,v)$ is a local diffeomorphism by the inverse function theorem.

## Final answer

$$\boxed{\;u(x,y) = x\sqrt{c(y) + d(y)\,x},\qquad v(x,y) = y\sqrt{\frac{a(y)}{y^2} + \frac{b(y)}{y^2}\,x}.\;}$$

In these coordinates $f(x,y) = u^2 + v^2$ on a neighborhood of the origin. The two ratios $a(y)/y^2$ and $b(y)/y^2$ are smooth functions of $y$ (by Taylor's theorem with integral remainder, using the second-order vanishing of $a$ and $b$ at $y=0$), with values $1$ and $b''(0)/2$ at $y=0$ respectively.
