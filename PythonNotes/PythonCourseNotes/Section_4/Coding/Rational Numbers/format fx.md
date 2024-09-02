#python #coding-lesson 

---
## `format` Function

**Purpose:**
- Formats strings according to a specified format.

**Syntax:**
```python
format(value, format_spec)
```

**Parameters:**
- `value`: The value to be formatted.
- `format_spec`: A format specification string that defines the format.

**Returns:**
- A formatted string.

**Common Usage:**

- **Decimal Formatting:**
  ```python
  pi = 3.14159265358979
  formatted_pi = format(pi, '.2f')  # Limits to 2 decimal places
  print(formatted_pi)  # Output: '3.14'
  ```

- **Padding and Alignment:**
  ```python
  number = 42
  formatted_number = format(number, '10')  # Right-aligns in a 10-character width
  print(formatted_number)  # Output: '        42'
  ```

**Notes:**
- The `format` function can be used for various types of formatting, including floating-point precision, alignment, and padding.
- Can also be used within f-strings for more complex formatting needs.
