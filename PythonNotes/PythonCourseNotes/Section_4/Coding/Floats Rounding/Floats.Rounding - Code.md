#python #coding-lesson 

---
# Python Rounding: Code Implementation

## Introduction

In this lecture, we delve into the code implementation of rounding in Python, expanding on the `round()` function discussed earlier. Python's `round()` is a built-in function and doesn't require importing from any module. Let's explore how it works with various examples.

---

## Basic Rounding with One Parameter

When the `round()` function is used with a single parameter, the second parameter (`n`) defaults to `0`, which rounds the number to the nearest integer.

### Example
```python
A = round(1.9)
print(A)             # Output: 2
print(type(A))       # Output: <class 'int'>
```
- **Explanation**: The number `1.9` is rounded to the nearest integer (`2`). The type of `A` is an integer.

### Rounding with Explicit `n=0`
```python
A = round(1.9, 0)
print(A)             # Output: 2.0
print(type(A))       # Output: <class 'float'>
```
- **Explanation**: When `n=0` is explicitly specified, the return type matches the input type. Here, `1.9` (a float) results in `2.0`, a float.

---

## Rounding with Positive `n` (n > 0)

When `n` is positive, `round()` rounds the number to the specified number of decimal places.

### Example: Rounding to 3 Decimal Places
```python
print(round(1.8888, 3))  # Output: 1.889
print(round(1.8888, 2))  # Output: 1.89
print(round(1.8888, 1))  # Output: 1.9
print(round(1.8888, 0))  # Output: 2.0
```
- **Explanation**:
    - `1.8888` rounded to 3 decimal places results in `1.889`.
    - Rounded to 2 decimal places: `1.89`.
    - Rounded to 1 decimal place: `1.9`.
    - Rounded to 0 decimal places: `2.0`.

---

## Rounding with Negative `n` (n < 0)

When `n` is negative, `round()` rounds the number to the left of the decimal point, to the nearest power of ten.

### Example: Rounding to Negative Powers of Ten
```python
print(round(8880.88, -1))  # Output: 8890.0
print(round(8880.88, -2))  # Output: 8900.0
print(round(8880.88, -3))  # Output: 9000.0
print(round(8880.88, -4))  # Output: 0.0
```
- **Explanation**:
    - Rounding `8880.88` to `-1` rounds to the nearest ten: `8890.0`.
    - Rounding to `-2` rounds to the nearest hundred: `8900.0`.
    - Rounding to `-3` rounds to the nearest thousand: `9000.0`.
    - Rounding to `-4` rounds to the nearest ten thousand, but `8880.88` is closer to `0` than `10,000`, so the result is `0.0`.

---

## Handling Ties

### Banker’s Rounding (Default)
Python uses **Banker’s Rounding** where ties are resolved by rounding to the nearest even digit.

### Example: Ties in Rounding
```python
print(round(1.25, 1))  # Output: 1.2
print(round(1.35, 1))  # Output: 1.4
print(round(-1.25, 1)) # Output: -1.2
print(round(-1.35, 1)) # Output: -1.4
```
- **Explanation**:
    - `1.25` rounds to `1.2` because `1.2` has an even digit.
    - `1.35` rounds to `1.4` because `1.4` has an even digit.
    - Same rules apply for negative numbers.

---

## Custom Rounding: Rounding Away from Zero

If you want to implement rounding away from zero, Python’s built-in functions won’t suffice. You need to create a custom function.

### Custom Function Implementation
```python
from math import copysign

def round_away_from_zero(x):
    return int(x + 0.5 * copysign(1, x))

# Example Usage
print(round_away_from_zero(1.5))  # Output: 2
print(round_away_from_zero(2.5))  # Output: 3
print(round_away_from_zero(-1.5)) # Output: -2
print(round_away_from_zero(-2.5)) # Output: -3
```
- **Explanation**:
    - The function `round_away_from_zero` rounds numbers away from zero, regardless of ties.

### Note on Function Naming
- Avoid overwriting the built-in `round()` function. Name your custom function something unique like `_round_away_from_zero`.

---

## Conclusion

- The `round()` function in Python provides a powerful way to round numbers, especially with its default Banker’s Rounding.
- Custom rounding logic like "rounding away from zero" can be implemented as needed.
- Python's flexibility with types and rounding behaviors makes it versatile for various numerical applications.