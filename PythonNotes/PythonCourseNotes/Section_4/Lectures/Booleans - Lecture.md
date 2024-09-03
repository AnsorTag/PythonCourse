#python #data-structures #general_knowledge 

---
## Booleans in Python

### Overview
- **Booleans** are a subclass of integers (`int`) in Python.
- **PEP 285** describes the rationale and implementation of the `bool` class.
- Python provides a concrete `bool` class to represent Boolean values.

### Boolean Class
- The `bool` class is a subclass of `int`.
- As a subclass, it inherits all properties and methods of `int`, such as:
  - Arithmetic operators: `+`, `-`, `/`, `%`, etc.
- The `bool` class also adds its own methods, such as:
  - Logical operators: `and`, `or`, `xor`.

### Singleton Objects
- **True** and **False** are singleton objects in Python.
  - `True` is internally equivalent to the integer `1`.
  - `False` is internally equivalent to the integer `0`.
- Singleton objects retain the same memory address throughout the program's execution.

### Memory and Identity
- The **identity operator (`is`)** compares memory addresses, while **equality (`==`)** compares values.
- Since `True` and `False` are singleton objects:
  - `True is True` will always return `True`.
  - `True == 1` will return `True` (due to value comparison), but `True is 1` will return `False` (due to different memory addresses).
  - Similarly, `False == 0` returns `True`, but `False is 0` returns `False`.

### Boolean Expressions
- **Boolean expressions** return Boolean values (`True` or `False`).
  - Example: `3 < 4` returns `True`.

### Boolean Arithmetic
- Boolean values can be used in arithmetic operations due to their integer nature:
  - `True + True + True` results in `3`.
  - `True + 1` results in `2`.
  - `100 * False` results in `0`.
  - `-True` results in `-1`.
  
### Boolean Comparisons
- Python allows for comparisons using Boolean values:
  - `True > False` returns `True` (since `1 > 0`).
  
### Boolean Constructor (`bool()`)
- The `bool()` constructor converts values into their Boolean equivalents based on their truthiness:
  - `bool(0)` returns `False`.
  - `bool(1)` returns `True`.
  - `bool(100)` returns `True`.
  - `bool(-1)` returns `True`.
- **Truthiness Rule**:
  - **Zero** evaluates to `False`.
  - **All other numbers** evaluate to `True`.

### Practical Implications
- Understanding that Booleans are integers allows for unconventional, but syntactically correct, expressions like:
  - `True + True + True % 2` resulting in `1`.
  - Using `True` and `False` in arithmetic and logical operations directly.

### Python Code Examples
- **Checking Type and ID**:
    ```python
    type(True)  # Output: <class 'bool'>
    id(True)    # Memory address of True
    int(True)   # Output: 1
    ```

- **Boolean Operations**:
    ```python
    1 + True  # Output: 2
    100 * False  # Output: 0
    True > False  # Output: True
    ```

- **Boolean Expressions**:
    ```python
    bool(0)  # Output: False
    bool(1)  # Output: True
    bool(-1)  # Output: True
    ```

### Key Points to Remember
- **True** and **False** are not the same as `1` and `0`, respectively, even though they are related.
- The `is` operator compares memory addresses, while `==` compares values.
- Boolean values behave as both integers and logical values, depending on the context.

### Additional Notes
- **Chained Operations**: Be cautious with chained comparisons like `1 == 2 == False`. The behavior might not be as expected due to how Python evaluates chained comparisons.

- **Truth Value of Objects**: Every object in Python has a truth value, determining how it evaluates in Boolean contexts. We'll explore this in more depth in later videos on Object-Oriented Programming.