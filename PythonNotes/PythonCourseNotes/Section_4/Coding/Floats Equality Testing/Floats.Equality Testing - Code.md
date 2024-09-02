#python #coding-lesson 

---
## Equality Testing with Floats in Python

### **Overview**
- **Floating-point numbers**: Cannot always be stored exactly due to their binary representation in computers.
  - Example: `0.1` cannot be stored exactly, while `0.125` (which is 1/8) can be stored precisely.
  
### **Floating-Point Representation**
- **Approximation**: Numbers like `0.1` are approximated in memory.
  - Printing `0.1` shows `0.1`, but its true value has more digits.
  - Exact storage is possible for numbers like `0.125` because they are powers of two.
  
### **Basic Comparison**
- **Exact comparison**:
  - For exact numbers (e.g., `0.125 + 0.125 + 0.125 == 0.375`), `==` works as expected.
  - For inexact numbers (e.g., `0.1 + 0.2 != 0.3`), `==` fails due to approximation errors.
  
### **Rounding Method**
- **Rounding floats**:
  - One approach to compare floats is to round them to a certain number of decimal places before comparing.
  - Example:
    ```python
    round(x, 3) == round(y, 3)
    ```
  - **Limitation**: Rounding checks only within an absolute tolerance and can lead to inaccurate results, especially with numbers of varying magnitudes.
  
### **Problems with Absolute Tolerance**
- **Magnitude Issues**:
  - For large numbers, a small difference may be negligible.
  - For small numbers, the same difference might be significant.
  - Example:
    - `10000.01` vs. `10000.02` (delta = 0.01) — might be considered close.
    - `0.01` vs. `0.02` (same delta = 0.01) — relatively very different.

### **Using `math.isclose()`**
- **`isclose()` method**:
  - A more sophisticated approach that checks if numbers are close within both relative and absolute tolerances.
  - **Parameters**:
    - `rel_tol` (relative tolerance): Defaults to `1e-9`.
    - `abs_tol` (absolute tolerance): Defaults to `0`, meaning no absolute tolerance is considered unless specified.
  - **Combination**: Using both relative and absolute tolerance gives a more accurate comparison for a wider range of numbers.

### **Examples and Comparison**
- **Example 1**: Comparison of large numbers using `isclose()`:
  ```python
  x = 123456789.01
  y = 123456789.02
  math.isclose(x, y, rel_tol=1e-9)  # Returns True
  ```
- **Example 2**: Comparison of small numbers:
  ```python
  x = 0.01
  y = 0.02
  math.isclose(x, y, rel_tol=1e-9)  # Returns False
  ```
- **Small Number Issues**:
  - Small numbers close to zero may fail relative tolerance checks.
  - Example:
    ```python
    x = 0.000001
    y = 0.000002
    math.isclose(x, y, rel_tol=1e-9)  # Returns False
    ```
  - **Solution**: Add an absolute tolerance to handle small numbers better:
    ```python
    math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-5)  # Returns True
    ```

### **Best Practices**
- **Set Tolerances Appropriately**:
  - Determine appropriate `rel_tol` and `abs_tol` for your specific use case.
  - Keep these tolerances consistent throughout your program.
- **Avoid Changing Tolerances Frequently**:
  - Set once based on expected ranges of numbers to ensure consistent results.

### **Conclusion**
- **Comparison Strategy**:
  - Use `math.isclose()` with both relative and absolute tolerances to handle most float comparison cases accurately.
  - Avoid simple equality checks (`==`) for floats due to the potential pitfalls of floating-point representation.