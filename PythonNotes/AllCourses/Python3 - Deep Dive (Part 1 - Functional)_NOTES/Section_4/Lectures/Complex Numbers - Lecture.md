#python #data-structures #general_knowledge 

coding lesson notes: [[Complex Numbers - Code]]

---
## Complex Numbers in Python

### Introduction
- **Complex Numbers** in Python are implemented using the built-in `complex` class.
- The **constructor** takes two parameters:
  - `x`: Real part.
  - `y`: Imaginary part.
- **Complex literals** are written as `x + yj`, where `j` represents the imaginary part.
  - `j` can be lowercase or uppercase.

### Examples
```python
a = complex(1, 2)
b = 1 + 2j
a == b  # True
```
- **Note**: `x` and `y` in complex numbers are stored as **floats**, even if they are defined as integers.

### Instance Properties and Methods
- **Real Part**: `complex_number.real`
- **Imaginary Part**: `complex_number.imag`
- **Complex Conjugate**: `complex_number.conjugate()`

#### Example
```python
d = 2 - 3j
d.real       # 2.0 (float)
d.imag       # -3.0 (float)
d.conjugate()  # 2 + 3j
```

### Arithmetic with Complex Numbers
- **Operators**: `+`, `-`, `/`, `*`, and `**` work as expected with complex numbers.
- **Mixing Real and Complex Numbers**: Supported (e.g., `1 + 2j + 5`).

### Unsupported Operations
- **Div and Mod Operators**: Not supported; will raise exceptions.

### Equality and Comparison
- **Equality (`==`)** and **Inequality (`!=`)**: Supported but with caution due to float precision issues.
- **Comparison (`<`, `>`, etc.)**: Not supported, as ordering complex numbers is not straightforward.

### Math Functions with Complex Numbers
- **Standard Math Module**: Functions from the `math` module do not work with complex numbers.
- **Use `cmath` Module**: Equivalent to `math` but for complex numbers. Includes additional complex-specific functions.
  - Functions include **exponentials**, **logs**, **trigonometric** functions, **hyperbolic** functions, and conversions between **polar** and **rectangular** coordinates.
  - **isclose()** method in `cmath` also works similarly to its `math` counterpart.

---

## Polar and Rectangular Coordinates

### Converting Rectangular to Polar
- **Phase Angle (φ)**: Use `cmath.phase(complex_number)` to get the angle (φ).
  - Range: `-π to π`, measured clockwise from the real axis.
- **Magnitude (r)**: Use `abs(complex_number)` to get the magnitude (r).

#### Example
```python
import cmath

a = -1 + 0j
cmath.phase(a)  # π
abs(a)          # 1.0

b = 1 + 1j
cmath.phase(b)  # π/4
abs(b)          # 1.414 (sqrt(2))
```

### Converting Polar to Rectangular
- Use `cmath.rect(r, φ)` to convert polar coordinates (r, φ) to rectangular coordinates.

#### Example
```python
import cmath
import math

r = math.sqrt(2)
φ = math.pi / 4
cmath.rect(r, φ)  # Returns 1 + 1j
```
- **Note**: Ensure that the first argument to `rect` is a real number, not a complex number.

---

## Euler's Identity

### Euler’s Formula
- **Formula**: \( e^{i\pi} + 1 = 0 \)
- **Implementation**:
```python
import cmath

result = cmath.exp(cmath.pi * 1j) + 1
print(result)  # Close to 0, but not exactly due to float precision issues.
```
- **isclose() Method**:
```python
cmath.isclose(cmath.exp(cmath.pi * 1j) + 1, 0, abs_tol=1e-9)  # True
```
- **Important**: Use `abs_tol` for comparisons close to zero. Without specifying `abs_tol`, the result may be `False`.