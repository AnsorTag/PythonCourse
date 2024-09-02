#python #data-structures #general_knowledge 

coding lesson notes: [[Floats.Coercing to Integers - Code]]

---
## Coercing Floats to Integers

### Overview
When converting a float (a number with a decimal point) to an integer in Python, data loss is inevitable. This is because the conversion involves removing the fractional part of the number. The main question is: **how do we handle the conversion?** Different methods will yield different results, depending on how you choose to deal with the digits after the decimal point.

### Methods for Coercing Floats to Integers
1. **Truncation**
2. **Floor**
3. **Ceiling**
4. **Rounding** *(covered in a separate video)*

### 1. Truncation
- **Description**: Truncation simply returns the integer portion of the number, ignoring everything after the decimal point.
- **Implementation**: 
    - Using `math.trunc()`:
      ```python
      import math
      math.trunc(10.4)  # Returns 10
      math.trunc(-10.4)  # Returns -10
      ```
    - Using the `int` constructor (which performs truncation):
      ```python
      int(10.4)  # Returns 10
      int(-10.4)  # Returns -10
      ```
- **Key Point**: Truncation discards the fractional part and keeps only the integer part, whether positive or negative.

### 2. Floor
- **Description**: The floor of a number is the largest integer that is less than or equal to the number.
- **Mathematical Notation**: `floor(x) = max(i)` for all integers `i` such that `i <= x`.
- **Implementation**:
    - Using `math.floor()`:
      ```python
      import math
      math.floor(10.4)  # Returns 10
      math.floor(-10.4)  # Returns -11
      ```
- **Example**:
    - **Positive Numbers**:
        - `floor(10.4) = 10` (Largest integer ≤ 10.4 is 10)
    - **Negative Numbers**:
        - `floor(-10.4) = -11` (Largest integer ≤ -10.4 is -11)
- **Special Case**: For positive numbers, `floor(x)` and `trunc(x)` give the same result, but they differ for negative numbers.

#### Relation to Floor Division
- **Floor Division (`//`)**: 
    - `A // B` is equivalent to `math.floor(A / B)`.
    - This is why the operation is known as "floor division."

### 3. Ceiling
- **Description**: The ceiling of a number is the smallest integer that is greater than or equal to the number.
- **Mathematical Notation**: `ceil(x) = min(i)` for all integers `i` such that `i >= x`.
- **Implementation**:
    - Using `math.ceil()`:
      ```python
      import math
      math.ceil(10.4)  # Returns 11
      math.ceil(-10.4)  # Returns -10
      ```
- **Example**:
    - **Positive Numbers**:
        - `ceil(10.4) = 11` (Smallest integer ≥ 10.4 is 11)
    - **Negative Numbers**:
        - `ceil(-10.4) = -10` (Smallest integer ≥ -10.4 is -10)
- **Key Point**: Ceiling and floor are opposites; while the floor rounds down, the ceiling rounds up.