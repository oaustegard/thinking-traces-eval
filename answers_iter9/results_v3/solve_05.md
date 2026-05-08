# Solution to AIME Problem: Isosceles Trapezoid with Inscribed Circle

## Problem
An isosceles trapezoid has an inscribed circle tangent to each of its four sides. The radius of the circle is $3$, and the area of the trapezoid is $72$. Let the parallel sides of the trapezoid have lengths $r$ and $s$, with $r \neq s$. Find $r^2+s^2$.

## Solution

### Step 1: Determine the height from the inscribed circle
For a trapezoid with an inscribed circle, the height equals the diameter of the circle:
$$h = 2R = 2(3) = 6$$

### Step 2: Find the sum of parallel sides using the area formula
The area of a trapezoid is:
$$A = \frac{1}{2}(b_1 + b_2) \cdot h$$

Substituting the known values:
$$72 = \frac{1}{2}(r + s) \cdot 6$$
$$72 = 3(r + s)$$
$$r + s = 24$$

### Step 3: Apply the tangential quadrilateral property
For a tangential quadrilateral (a quadrilateral with an inscribed circle), the sum of opposite sides are equal. For our isosceles trapezoid with parallel sides $r$ and $s$, and equal legs of length $\ell$:
$$r + s = 2\ell$$

Therefore:
$$\ell = \frac{r + s}{2} = \frac{24}{2} = 12$$

### Step 4: Use the Pythagorean theorem on the right triangle formed
When we drop perpendiculars from the shorter parallel side to the longer parallel side, we create a right triangle with:
- Height: $h = 6$
- Base: $\frac{|s - r|}{2}$ (half the difference of the parallel sides)
- Hypotenuse: $\ell = 12$ (the leg of the trapezoid)

By the Pythagorean theorem:
$$\ell^2 = h^2 + \left(\frac{|s-r|}{2}\right)^2$$
$$12^2 = 6^2 + \left(\frac{|s-r|}{2}\right)^2$$
$$144 = 36 + \left(\frac{|s-r|}{2}\right)^2$$
$$\left(\frac{|s-r|}{2}\right)^2 = 108$$
$$\frac{|s-r|}{2} = 6\sqrt{3}$$
$$|s - r| = 12\sqrt{3}$$

### Step 5: Solve for the individual parallel sides
We have two equations:
- $r + s = 24$
- $s - r = 12\sqrt{3}$ (assuming $s > r$)

Adding these equations:
$$2s = 24 + 12\sqrt{3}$$
$$s = 12 + 6\sqrt{3}$$

Subtracting from the first:
$$2r = 24 - 12\sqrt{3}$$
$$r = 12 - 6\sqrt{3}$$

### Step 6: Calculate $r^2 + s^2$
$$r^2 = (12 - 6\sqrt{3})^2 = 144 - 2(12)(6\sqrt{3}) + 36(3)$$
$$r^2 = 144 - 144\sqrt{3} + 108 = 252 - 144\sqrt{3}$$

$$s^2 = (12 + 6\sqrt{3})^2 = 144 + 2(12)(6\sqrt{3}) + 36(3)$$
$$s^2 = 144 + 144\sqrt{3} + 108 = 252 + 144\sqrt{3}$$

Therefore:
$$r^2 + s^2 = (252 - 144\sqrt{3}) + (252 + 144\sqrt{3}) = 504$$

## Answer
$\boxed{504}$
