#python #coding-lesson 

---

### Python: `divmod()` Function

**Description:**
The `divmod()` function in Python takes two numbers and returns a tuple containing the quotient and remainder when dividing the first number by the second.

**Syntax:**
```python
divmod(a, b)
```

- **`a`**: The dividend (numerator).
- **`b`**: The divisor (denominator).

**Returns:**
A tuple `(quotient, remainder)`.

**Examples:**

1. **Basic Usage:**
    ```python
    result = divmod(10, 3)
    # result is (3, 1)
    ```
   Here, `10` divided by `3` gives a quotient of `3` and a remainder of `1`.

2. **Negative Numbers:**
    ```python
    result = divmod(-10, 3)
    # result is (-4, 2)
    ```
   Dividing `-10` by `3` results in a quotient of `-4` and a remainder of `2`.

3. **Floating Point Numbers:**
    ```python
    result = divmod(10.5, 3)
    # result is (3.0, 1.5)
    ```
   When using floating-point numbers, the quotient will be a float.

**Use Case:**
`divmod()` is useful when both the quotient and remainder of a division are needed, especially in scenarios like converting time units (e.g., seconds to minutes and seconds).

**Additional Notes:**
- This function is more efficient than calculating the quotient and remainder separately since it only performs the division once.
- Works with both integers and floating-point numbers.