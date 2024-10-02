#python #coding-lesson 

---
## 1. The `or` Operator

### Definition and Behavior

- **Syntax**: `X or Y`
- **Behavior**:
  - If `X` is truthy (i.e., evaluates to `True`), the result is `X`. It does not evaluate `Y`.
  - If `X` is falsy, the result is `Y`.

### Examples

1. **Truthy `X`**:
    ```python
    string = "Hello"
    result = string or [1, 2]
    # Result: "Hello" (string is truthy, so it returns itself)
    ```

2. **Falsy `X`**:
    ```python
    empty_string = ""
    result = empty_string or [1, 2]
    # Result: [1, 2] (empty_string is falsy, so it returns [1, 2])
    ```

3. **Short-Circuiting**:
    ```python
    result = 1 or 1 / 0
    # Result: 1 (the right operand is not evaluated because 1 is truthy)
    
    result = 0 or 1 / 0
    # Division by zero error (0 is falsy, so it evaluates the right operand)
    ```

### Use Case: Default Values

- **Example**:
    ```python
    s1 = None
    s2 = ""
    s3 = "ABC"

    s1 = s1 or "not available"
    s2 = s2 or "not available"
    s3 = s3 or "not available"

    # Results:
    # s1: "not available" (None is falsy)
    # s2: "not available" (empty string is falsy)
    # s3: "ABC" (truthy string remains unchanged)
    ```

## 2. The `and` Operator

### Definition and Behavior

- **Syntax**: `X and Y`
- **Behavior**:
  - If `X` is falsy, the result is `X`. It does not evaluate `Y`.
  - If `X` is truthy, the result is `Y`.

### Examples

1. **Falsy `X`**:
    ```python
    result = None and 0
    # Result: None (None is falsy, so it returns None)
    ```

2. **Truthy `X`**:
    ```python
    result = True and [1, 2]
    # Result: [1, 2] (True is truthy, so it returns the second operand)
    ```

3. **Use Case**:
    - To avoid errors in calculations:
        ```python
        a = 2
        b = 0

        # Using if statement
        if b == 0:
            result = 0
        else:
            result = a / b

        # Using `or` operator
        result = (b and a / b) or 0
        ```

## 3. The `not` Operator

### Definition and Behavior

- **Syntax**: `not X`
- **Behavior**:
  - Negates the truth value of `X`. 
  - If `X` is truthy, `not X` returns `False`.
  - If `X` is falsy, `not X` returns `True`.

### Examples

1. **Truthy Values**:
    ```python
    result = not "ABC"
    # Result: False (since "ABC" is truthy)
    ```

2. **Falsy Values**:
    ```python
    result = not ""
    # Result: True (since the empty string is falsy)
    
    result = not None
    # Result: True (since None is falsy)
    ```

### Notes

- The `not` operator works with the truth value of the object and always returns a Boolean value (`True` or `False`).