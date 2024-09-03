#python #coding-lesson 

---
### Complex Numbers in Python: A Comprehensive Guide

### 1. **Defining Complex Numbers in Python**

- **Constructor Method**:
  - Complex numbers can be defined using the `complex()` constructor, which takes two arguments: the real part and the imaginary part.
  - Example: `a = complex(1, 2)` creates a complex number with a real part of `1` and an imaginary part of `2`.

- **Literal Method**:
  - You can also define complex numbers using literals with the `j` notation.
  - Example: `b = 1 + 2j` or `b = 1 + 2J`.
  - Comparing `a == b` returns `True` as both methods create the same complex number.

---

### 2. **Accessing Real and Imaginary Parts**

- **Real Part**:
  - Use the `.real` attribute to access the real part of a complex number.
  - Example: `a.real` returns `1.0`.

- **Imaginary Part**:
  - Use the `.imag` attribute to access the imaginary part.
  - Example: `a.imag` returns `2.0`.

- **Note**: The real and imaginary parts are stored as floats in Python, even if you define them as integers. This can lead to the same approximation issues encountered with floats.

---

### 3. **Complex Conjugate**

- **Conjugate Method**:
  - The conjugate of a complex number (changing the sign of the imaginary part) can be accessed using the `.conjugate()` method.
  - Example: `a.conjugate()` returns `1 - 2j`.

---

### 4. **Arithmetic Operations with Complex Numbers**

- **Supported Operations**:
  - Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`) work as expected with complex numbers.
  - Example:
    ```python
    a = 1 + 2j
    b = 10 + 8j
    result_add = a + b  # 11 + 10j
    result_mul = a * b  # -6 + 28j
    ```

- **Unsupported Operations**:
  - The floor division (`//`) and modulo (`%`) operations are not defined for complex numbers and will raise an error if attempted.

---

### 5. **Equality and Approximation Issues**

- **Equality (`==`)**:
  - The equality operator works for complex numbers but beware of approximation errors, especially when dealing with floating-point components.
  - Example: 
    ```python
    c = 0.1j
    c_plus = c + c + c
    c_plus == 0.3j  # Returns False due to floating-point precision issues
    ```

- **Handling Approximation**:
  - Similar to floats, use the `math.isclose()` function to compare complex numbers with a tolerance for approximation errors.

---

### 6. **Using the `cmath` Library**

- **Purpose**:
  - The `cmath` library in Python is specialized for complex numbers, providing functions analogous to those in the `math` library but adapted for complex arithmetic.

- **Key Functions**:
  - **Square Root**: `cmath.sqrt(z)` where `z` is a complex number.
  - **Exponent**: `cmath.exp(z)` for computing the exponential of a complex number.
  - **Trigonometric and Hyperbolic Functions**: `cmath.sin(z)`, `cmath.cos(z)`, etc.
  - **Phase**: `cmath.phase(z)` returns the phase (or angle) of the complex number in polar coordinates.
  - **Absolute Value**: `abs(z)` returns the Euclidean norm (magnitude) of the complex number.

- **Example**:
  ```python
  import cmath
  z = 1 + 1j
  magnitude = abs(z)  # 1.4142135623730951
  angle = cmath.phase(z)  # 0.7853981633974483 (π/4)
  ```

---

### 7. **Converting Between Rectangular and Polar Coordinates**

- **Rectangular to Polar**:
  - Use `cmath.phase(z)` for the angle and `abs(z)` for the magnitude.

- **Polar to Rectangular**:
  - Use `cmath.rect(r, phi)`, where `r` is the magnitude and `phi` is the angle.
  - Example:
    ```python
    r = cmath.sqrt(2)
    phi = cmath.pi / 4
    z = cmath.rect(r, phi)  # Returns approximately 1 + 1j
    ```

---

### 8. **Euler's Identity**

- **Overview**:
  - Euler's identity is a fundamental equation in complex analysis: \( e^{i\pi} + 1 = 0 \).

- **Testing Euler's Identity in Python**:
  - Example:
    ```python
    import cmath
    result = cmath.exp(cmath.pi * 1j) + 1
    is_zero = cmath.isclose(result, 0, abs_tol=1e-15)  # Returns True
    ```
  - Due to floating-point precision, the result might not be exactly zero, but `cmath.isclose()` can be used to verify that it is close enough.