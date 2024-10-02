#python #general_knowledge  #data-structures 

coding lesson notes: [[Floats.Equality Testing - Code]]

---
## Dealing with Floating-Point Equality in Python

### Overview

Floating-point numbers in Python, and generally in computer science, can lead to unexpected results when it comes to equality testing. This is due to their binary representation which can cause precision issues. This note explores common pitfalls and best practices for handling floating-point comparisons.

### Understanding Floating-Point Representation

1. **Binary Representation:**
   - Floats are stored using binary representation.
   - Operations and comparisons may not behave as expected due to precision limitations inherent to binary formats.

2. **Example of Issue:**
   - Consider:
     ```python
     X = 0.1 + 0.1 + 0.1
     Y = 0.3
     ```
   - Comparing `X == Y` can yield `False` because `0.1` and `0.3` are approximations in binary representation.

3. **Display Precision:**
   - Python formats floating-point numbers to a default precision when printed.
   - This formatting can obscure the underlying precision issues.

### Handling Precision Issues

1. **Rounding Method:**
   - Rounding might not always solve the problem as it may not address the underlying precision issue:
     ```python
     round(0.1, 1)  # Still yields 0.1
     ```

2. **Absolute Tolerance:**
   - Compare the difference against a small tolerance value, `epsilon`:
     ```python
     epsilon = 0.0001
     abs(X - Y) < epsilon
     ```
   - **Limitation:** Absolute tolerance is not effective when numbers vary greatly in magnitude (e.g., `10,000.1` vs `30,000.3`).

3. **Relative Tolerance:**
   - Uses a percentage of the magnitude of the numbers:
     ```python
     relative_tolerance = 0.001  # 0.001%
     tolerance = relative_tolerance * max(abs(X), abs(Y))
     abs(X - Y) < tolerance
     ```
   - **Limitation:** Can be problematic with numbers close to zero as the tolerance becomes too large.

### Combining Tolerances

1. **Best Approach:**
   - Combine absolute and relative tolerances:
     ```python
     def are_close(x, y, abs_tol=1e-9, rel_tol=1e-9):
         return abs(x - y) <= max(abs_tol, rel_tol * max(abs(x), abs(y)))
     ```
   - **Reasoning:**
     - This approach ensures that both absolute and relative differences are considered, accommodating numbers close to zero and large numbers.

2. **Practical Example:**
   - For `X = 0.00000001` and `Y = 0.00000002`, relative tolerance may yield a larger comparison range, while absolute tolerance might fail.

### `math.isclose` Method

1. **Usage:**
   - The `math.isclose` method provides built-in comparison with tolerance:
     ```python
     import math
     math.isclose(X, Y, rel_tol=1e-9, abs_tol=1e-9)
     ```
   - **Parameters:**
     - `rel_tol` (default `1e-9`): Relative tolerance.
     - `abs_tol` (default `0.0`): Absolute tolerance, which should be specified if dealing with numbers close to zero.

2. **Default Behavior:**
   - Without `abs_tol`, `math.isclose` relies solely on relative tolerance, which may not be adequate for numbers close to zero.

3. **Practical Example:**
   - Comparing large numbers:
     ```python
     math.isclose(1000.01, 1000.02, rel_tol=1e-5, abs_tol=1e-5)  # True
     ```
   - Comparing small numbers:
     ```python
     math.isclose(0.000001, 0.000002, rel_tol=1e-5, abs_tol=1e-5)  # False
     ```

### Alternatives

1. **Exact Representations:**
   - Use `fractions.Fraction` for exact rational number representation:
     ```python
     from fractions import Fraction
     Fraction(1, 3)  # Exact representation of 1/3
     ```

2. **Decimal Module:**
   - For precise decimal arithmetic, use the `decimal` module (to be discussed in a future video).

### Recommendations

- **Use `math.isclose` for float comparisons** to avoid precision issues.
- **Experiment with different tolerances** to find what works best for your specific case.
- **Understand the limitations of floating-point arithmetic** and apply appropriate methods based on the context.