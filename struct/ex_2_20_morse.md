# Struct: Etingof Exercise 2.20 (explicit Morse coordinates for a cubic)

Problem: Given $f(x,y) = a(y) + b(y)x + c(y)x^2 + d(y)x^3$ with $a(0) = a'(0) = b(0) = b'(0) = 0$, $a''(0) = c(0) = 2$, find explicit local coordinates $u(x,y), v(x,y)$ such that $f = u^2 + v^2$ near the origin.

Step 1: Verify the origin is a critical point and apply Morse lemma via Hessian. Compute $\nabla f|_0 = (0,0)$ and check that $H_f|_0 = \text{diag}(4, 2)$ is positive definite, confirming Morse lemma applies.

Step 2: Factor the cubic-and-quadratic $x$-terms. Write $c(y)x^2 + d(y)x^3 = x^2(c(y) + d(y)x)$. Since $c(0) = 2 > 0$, the expression $c(y) + d(y)x$ is positive near the origin, so $\sqrt{c(y) + d(y)x}$ is smooth.

Step 3: Define the $x$-coordinate as $u(x,y) := x\sqrt{c(y) + d(y)x}$. Then $u^2 = x^2(c(y) + d(y)x) = c(y)x^2 + d(y)x^3$, capturing the entire $x$-piece of $f$.

Step 4: Apply Taylor's theorem with integral remainder to the residual. The remaining terms $a(y) + b(y)x$ satisfy: $a(y) = y^2 h(y)$ with $h(0) = 1$, and $b(y) = y^2 k(y)$ with $k(0) = b''(0)/2$. Thus $a(y) + b(y)x = y^2(h(y) + k(y)x)$ with $h(y) + k(y)x \to 1 > 0$ near the origin.

Step 5: Define the $y$-coordinate as $v(x,y) := y\sqrt{h(y) + k(y)x}$. Then $v^2 = y^2(h(y) + k(y)x) = a(y) + b(y)x$.

Step 6: Verify that $(u,v)$ form a local diffeomorphism. Compute the Jacobian at the origin: $u_x(0,0) = \sqrt{2}$, $u_y(0,0) = 0$, $v_x(0,0) = 0$, $v_y(0,0) = 1$. Determinant $= \sqrt{2} \ne 0$, so the map is a local diffeomorphism by the inverse function theorem.

Step 7: Combine. Verify that $u^2 + v^2 = c(y)x^2 + d(y)x^3 + a(y) + b(y)x = f(x,y)$.

Answer: $\boxed{u(x,y) = x\sqrt{c(y) + d(y)\,x}, \quad v(x,y) = y\sqrt{\frac{a(y)}{y^2} + \frac{b(y)}{y^2}\,x}}$
