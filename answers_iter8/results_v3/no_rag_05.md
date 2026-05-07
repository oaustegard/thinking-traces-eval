# AIME Problem Solution

## Problem
An isosceles trapezoid has an inscribed circle tangent to each of its four sides. The radius of the circle is $3$, and the area of the trapezoid is $72$. Let the parallel sides of the trapezoid have lengths $r$ and $s$, with $r \neq s$. Find $r^2+s^2$.

## Solution

### Step 1: Properties of Tangential Trapezoid
For a tangential polygon (one with an inscribed circle), the sum of opposite sides are equal. For an isosceles trapezoid with parallel sides $r$ and $s$ and equal legs of length $\ell$:
$$r + s = 2\ell$$

### Step 2: Determine Height
Since the inscribed circle has radius $R = 3$ and is tangent to both parallel sides, the height of the trapezoid equals the diameter:
$$h = 2R = 6$$

### Step 3: Use Area Formula
The area of a trapezoid is:
$$A = \frac{1}{2}(r + s) \cdot h$$

Substituting $A = 72$ and $h = 6$:
$$72 = \frac{1}{2}(r + s) \cdot 6$$
$$72 = 3(r + s)$$
$$r + s = 24$$

### Step 4: Find Leg Length
From the tangential property:
$$r + s = 2\ell$$
$$24 = 2\ell$$
$$\ell = 12$$

### Step 5: Relate Leg to Bases
For an isosceles trapezoid, the leg length relates to the height and the difference in parallel sides by the Pythagorean theorem:
$$\ell^2 = h^2 + \left(\frac{s-r}{2}\right)^2$$

Substituting $\ell = 12$ and $h = 6$:
$$144 = 36 + \left(\frac{s-r}{2}\right)^2$$
$$108 = \left(\frac{s-r}{2}\right)^2$$
$$\frac{s-r}{2} = 6\sqrt{3}$$
$$s - r = 12\sqrt{3}$$

### Step 6: Solve for r and s
We have the system:
- $r + s = 24$
- $s - r = 12\sqrt{3}$

Adding: $2s = 24 + 12\sqrt{3}$, so $s = 12 + 6\sqrt{3}$

Subtracting: $2r = 24 - 12\sqrt{3}$, so $r = 12 - 6\sqrt{3}$

### Step 7: Calculate $r^2 + s^2$
$$r^2 = (12 - 6\sqrt{3})^2 = 144 - 144\sqrt{3} + 108 = 252 - 144\sqrt{3}$$

$$s^2 = (12 + 6\sqrt{3})^2 = 144 + 144\sqrt{3} + 108 = 252 + 144\sqrt{3}$$

$$r^2 + s^2 = 252 - 144\sqrt{3} + 252 + 144\sqrt{3} = 504$$

## Answer
$\boxed{504}$
