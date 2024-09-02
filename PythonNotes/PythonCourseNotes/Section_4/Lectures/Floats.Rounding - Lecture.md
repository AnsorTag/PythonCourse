#python #data-structures #general_knowledge 

coding lesson notes: [[Floats.Rounding - Code]]

---
# Python `round()` Function

## Overview

The `round()` function is a built-in Python function used to round numbers. It accepts one mandatory parameter (the number to round) and an optional second parameter (`n`) that defaults to `0`, which specifies the precision (the number of decimal places or the power of ten to round to).

### Syntax
```python
round(number, n=0)
```

- **number**: The number you want to round.
- **n**: Specifies the number of decimal places to round to. Can be positive (decimal places) or negative (powers of ten).

### Examples
```python
round(1.23)      # Output: 1
round(1.23, 1)   # Output: 1.2
round(18.2, -1)  # Output: 20
```

---

## Rounding Mechanisms

### Rounding to Integers
- When `n` is not specified (defaults to `0`), `round()` returns an integer.
- Example:
    ```python
    round(1.23)  # Output: 1 (integer)
    ```

### Rounding to Decimal Places (`n > 0`)
- Rounds to the nearest multiple of `10^-n`.
- Example:
    ```python
    round(1.23, 1)  # Output: 1.2 (float)
    ```

### Rounding to Powers of Ten (`n < 0`)
- Rounds to the nearest multiple of `10^(-n)`.
- Example:
    ```python
    round(18.2, -1)  # Output: 20
    ```

---

## Handling Ties

### Rounding Away from Zero
- The standard rounding method most people are familiar with.
- **Example**:
    - `round(1.25, 1)` → Expected: `1.3`
    - `round(-1.25, 1)` → Expected: `-1.3`

### Python’s Default: Banker's Rounding
- Python uses **Banker’s Rounding** (also known as rounding to the nearest even digit).
- **Rules**:
    - Round to the nearest value.
    - If there’s a tie, round to the nearest even digit.
- **Example**:
    ```python
    round(1.25, 1)  # Output: 1.2 (even)
    round(1.35, 1)  # Output: 1.4 (even)
    round(15, -1)   # Output: 20
    round(25, -1)   # Output: 20
    ```

### Why Use Banker’s Rounding?
- **Reduces bias**: Always rounding away from zero can accumulate rounding errors over many calculations.
- **Example**:
    - Average of `0.5`, `1.5`, `2.5`:
        - Standard Rounding → Average: `2`
        - Banker’s Rounding → Average: `1.33...`

---

## Implementing Rounding Away from Zero

### Simple Method (Not Recommended)
- **Formula**: `int(x + 0.5)`
- **Problem**: Only works for positive numbers.
- **Fails** for negative numbers:
    ```python
    round(-10.3)  # Incorrect Output
    ```

### Correct Implementation
- **Steps**:
    1. Take the absolute value of `x`.
    2. Add `0.5`.
    3. Truncate the result.
    4. Apply the original sign of `x`.

- **Code**:
    ```python
    def round_away_from_zero(x):
        return int(abs(x) + 0.5) * (1 if x >= 0 else -1)
    ```

---

## Conclusion
- The `round()` function is versatile and powerful, providing different ways to handle rounding based on the needs of the computation.
- **Banker’s Rounding** helps reduce bias in large-scale computations.
- Custom rounding functions can be created for specific rounding behavior, like rounding away from zero.
