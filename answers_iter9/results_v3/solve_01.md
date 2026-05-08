# Solution: Area of Heptagon AFNBCEM

## Problem Setup
On triangle ABC:
- Side AB: AD = 4, DE = 16, EB = 8 → AE = 20, AB = 28
- Side AC: AF = 13, FG = 52, GC = 26 → AG = 65, AC = 91
- M is reflection of D through F
- N is reflection of G through E
- Area(DEGF) = 288

## Solution

### Step 1: Set up coordinates
Place A at origin and B on the x-axis:
- A = (0, 0)
- B = (28, 0)
- C = (c_x, c_y) to be determined

### Step 2: Locate points on sides
On AB:
- D = (4, 0)
- E = (20, 0)

On AC (normalized by distance 91):
- F = (13c_x/91, 13c_y/91)
- G = (65c_x/91, 65c_y/91)

### Step 3: Use area constraint for DEGF
Using the shoelace formula for quadrilateral DEGF = 288:

The area calculation yields:
$$\text{Area}(DEGF) = \frac{624c_y}{91} = 288$$

Therefore: $c_y = \frac{288 \cdot 91}{624} = 42$

### Step 4: Find the triangle area
$$\text{Area}(ABC) = \frac{1}{2} \cdot AB \cdot h = \frac{1}{2} \cdot 28 \cdot 42 = 588$$

### Step 5: Analyze the reflections
M is the reflection of D through F:
- M = 2F - D

N is the reflection of G through E:
- N = 2E - G

### Step 6: Calculate areas of triangles DFM and EGN
Using shoelace formula for triangles formed by reflections:

For triangle DFM (with D, F, M collinear through reflection):
- Area(DFM) = 0 (the points are collinear by definition of reflection)

For triangle EGN (with E, G, N collinear through reflection):
- Area(EGN) = 0 (the points are collinear by definition of reflection)

### Step 7: Calculate heptagon area
The heptagon AFNBCEM is the triangle ABC with quadrilateral DEGF removed:

$$\text{Area}(AFNBCEM) = \text{Area}(ABC) - \text{Area}(DEGF)$$
$$= 588 - 288$$
$$= 300$$

$\boxed{300}$
