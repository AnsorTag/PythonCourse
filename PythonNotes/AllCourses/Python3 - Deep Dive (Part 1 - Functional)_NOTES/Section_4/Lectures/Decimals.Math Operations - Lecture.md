#python #data-structures #general_knowledge 

coding lesson notes: [[Decimals.Math Operations - Code]]

---
# Mathematical Operations on Decimals

## 1. Introduction

In this lecture, we’ll explore how mathematical operations work with the `Decimal` class in Python. We’ll discuss how arithmetic operators behave differently with decimals compared to floats and integers, focusing on operations like division (`div`) and modulus (`mod`), as well as other mathematical functions.

## 2. Division and Modulus Operations

### 2.1. Division (`div` Operator)

**Behavior with Integers vs. Decimals:**

- **Integers:**
  - `a div b` performs floor division. For example:
    ```python
    10 // 3  # Results in 3
    ```

- **Decimals:**
  - `a div b` performs truncated division. For example:
    ```python
    from decimal import Decimal
    Decimal(10) // Decimal(3)  # Results in Decimal('3')
    ```
  - For negative numbers, results differ:
    ```python
    -10 // 3  # Results in -4 (floor division)
    Decimal(-10) // Decimal(3)  # Results in Decimal('-3') (truncated division)
    ```

**Explanation of Truncated Division:**

- **Process:**
  - Compute the result’s sign.
  - Use absolute values of the dividend and divisor.
  - Subtract the divisor from the dividend until the dividend is less than the divisor.
  - Count the number of subtractions and apply the sign.

**Examples:**

- **Positive Example:**
  ```python
  10 // 3  # Results in 3
  ```

- **Negative Example:**
  ```python
  -10 // 3  # Results in -4
  Decimal(-10) // Decimal(3)  # Results in Decimal('-3')
  ```

### 2.2. Modulus (`mod` Operator)

**Behavior with Integers vs. Decimals:**

- **Integers:**
  - `a mod b` gives the remainder of the division. For example:
    ```python
    10 % 3  # Results in 1
    ```

- **Decimals:**
  - `a mod b` gives the remainder based on truncated division. For example:
    ```python
    Decimal(-135) % Decimal(4)  # Results in Decimal('-3')
    ```

**Examples:**

- **Positive Example:**
  ```python
  -135 % 4  # Results in 1
  ```

- **Negative Example:**
  ```python
  Decimal(-135) % Decimal(4)  # Results in Decimal('-3')
  ```

### 2.3. Relationship Between `div` and `mod`

**Equation:** `a = (a div b) * b + (a mod b)`

**Validation:**
- For integers:
  ```python
  -135 = (-34 * 4) + 1
  ```

- For decimals:
  ```python
  -135 = (-33 * 4) + (-3)
  ```

## 3. Mathematical Operations in the `Decimal` Class

### 3.1. Available Operations

The `Decimal` class provides various mathematical operations, but not all functions from the `math` module are available.

**Functions in the `Decimal` Class:**
- Square root
- Logarithms (base 10, base e, and arbitrary bases)

**Functions Not in the `Decimal` Class:**
- Trigonometric functions

### 3.2. Using the `math` Module

**Limitations:**
- Functions from the `math` module convert `Decimal` to `float`, potentially losing precision.

**Examples:**

**Precision Loss with `math` Module:**
```python
import math
from decimal import Decimal

x = Decimal("0.01")
sqrt_float = math.sqrt(float(x))  # Converts Decimal to float
sqrt_mixed = math.sqrt(float(Decimal("0.01")))  # Converts Decimal to float
sqrt_decimal = x.sqrt()  # Uses Decimal's sqrt method

print(sqrt_float)  # Not exact
print(sqrt_mixed)  # Same result as sqrt_float
print(sqrt_decimal)  # Exact 0.1
```

**Verification:**
- Multiplying results by themselves should yield the original number.
  ```python
  (sqrt_float * sqrt_float)  # Approximate
  (sqrt_decimal * sqrt_decimal)  # Exact 0.01
  ```

## 4. Key Takeaways

- **Division (`div`) and Modulus (`mod`):**
  - `div` operator performs truncated division with `Decimal`, while it performs floor division with integers.
  - Modulus results differ based on whether integers or decimals are used.

- **Mathematical Operations:**
  - Use `Decimal` methods for precision.
  - Be cautious with functions from the `math` module due to potential precision loss.