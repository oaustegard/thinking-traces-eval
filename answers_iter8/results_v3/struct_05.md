# Solution: Isosceles Trapezoid with Inscribed Circle

## Problem
An isosceles trapezoid has an inscribed circle tangent to each of its four sides. The radius of the circle is $3$, and the area of the trapezoid is $72$. Let the parallel sides of the trapezoid have lengths $r$ and $s$, with $r \neq s$. Find $r^2+s^2$.

## Solution

**Step 1 — Set up variables:**
Let the parallel sides be $a$ and $b$ (with $a < b$), and let the legs be $c$ (equal, since it's isosceles).
- Inscribed circle radius: $\rho = 3$
- Height of trapezoid: $h = 2\rho = 6$

**Step 2 — Use the tangential trapezoid property:**
For any tangential polygon (one with an inscribed circle), the sum of opposite sides are equal:
$$a + b = 2c$$

**Step 3 — Apply the area formula:**
$$A = \frac{1}{2}(a+b) \cdot h = 72$$
$$\frac{1}{2}(a+b) \cdot 6 = 72$$
$$a + b = 24$$

**Step 4 — Determine the leg length:**
From the tangential property:
$$2c = a + b = 24$$
$$c = 12$$

**Step 5 — Use the Pythagorean theorem:**
When we drop perpendiculars from the ends of the shorter base to the longer base, each horizontal projection is $\frac{b-a}{2}$.

$$\left(\frac{b-a}{2}\right)^2 + 6^2 = 12^2$$
$$\left(\frac{b-a}{2}\right)^2 = 144 - 36 = 108$$
$$\frac{b-a}{2} = 6\sqrt{3}$$
$$b - a = 12\sqrt{3}$$

**Step 6 — Solve for $a$ and $b$:**
From $a + b = 24$ and $b - a = 12\sqrt{3}$:
$$b = \frac{24 + 12\sqrt{3}}{2} = 12 + 6\sqrt{3}$$
$$a = \frac{24 - 12\sqrt{3}}{2} = 12 - 6\sqrt{3}$$

**Step 7 — Calculate $r^2 + s^2$:**
$$a^2 = (12 - 6\sqrt{3})^2 = 144 - 144\sqrt{3} + 108 = 252 - 144\sqrt{3}$$
$$b^2 = (12 + 6\sqrt{3})^2 = 144 + 144\sqrt{3} + 108 = 252 + 144\sqrt{3}$$

$$r^2 + s^2 = a^2 + b^2 = 252 - 144\sqrt{3} + 252 + 144\sqrt{3} = 504$$

## Answer
$\boxed{504}$
