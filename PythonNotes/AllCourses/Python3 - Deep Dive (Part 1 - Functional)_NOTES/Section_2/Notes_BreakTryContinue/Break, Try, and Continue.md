#python #flow-control 

---
### Break, Continue, and the Try Statement

#### Key Concepts:

- **Try Statement**:
  - **Structure**: `try`, `except`, `finally` blocks.
  - **Finally Block**: Always executes regardless of whether an exception occurred.
  - **ZeroDivisionError Example**:
    - Dividing by zero triggers a `ZeroDivisionError`.
    - The `finally` block runs even if an exception is caught.

- **While Loop with Try, Break, and Continue**:
  - **Scenario**: Increment and decrement variables in a loop until a division by zero occurs.
  - **Continue Statement**:
    - Placed inside `except` block after catching an exception.
    - Causes the loop to skip the remaining code and start the next iteration.
    - Despite `continue`, the `finally` block still runs.
  - **Break Statement**:
    - Can replace `continue` to exit the loop immediately after an exception.
    - The `finally` block will still execute before the loop breaks.

- **Else Clause in While Loop**:
  - **When it Executes**: Only if the loop terminates normally (i.e., without encountering a `break`).
  - **Example**: No `ZeroDivisionError` leads to the `else` clause executing.

#### Code Examples:

```python
# Example with Continue
a = 0
b = 2
while a < 4:
    print("---")
    a += 1
    b -= 1
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Division by zero: {a}, {b}")
        continue
    finally:
        print(f"This always executes: {a}, {b}")

    print(f"In the main loop: {a}, {b}")

# Example with Break
a = 0
b = 2
while a < 4:
    print("---")
    a += 1
    b -= 1
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Division by zero: {a}, {b}")
        break
    finally:
        print(f"This always executes: {a}, {b}")

    print(f"In the main loop: {a}, {b}")

# Adding an Else Clause
a = 0
b = 10
while a < 4:
    print("---")
    a += 1
    b -= 1
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Division by zero: {a}, {b}")
        break
    finally:
        print(f"This always executes: {a}, {b}")
else:
    print("Code executed without a ZeroDivisionError")
```

#### Summary:
- The `finally` block in a `try` statement always runs, even if a `break` or `continue` is encountered.
- The `else` clause in a loop runs only if the loop exits normally (without a `break`).