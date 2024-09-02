#python #general_knowledge 

---
# Python Optimizations: Integer Interning

## Overview
- This lecture focuses on **integer interning** and its role in Python optimizations.
- **Interning** is the reuse of objects to save memory and optimize performance.

## Python Implementations
- **CPython**: The reference implementation, written in C.
- Other implementations include:
  - **Jython**: Python on the Java platform, compiles to Java bytecode.
  - **IronPython**: Written in C#, targets .NET CLR.
  - **PyPy**: Written in Python, uses a subset called RPython.
- **Version Specifics**: Optimization details can vary by Python version (this course uses CPython 3.6).

## Integer Interning
- **Interning**: Python reuses integer objects for values in a specific range.
- **Cached Range**: `-5` to `256` inclusive.
  - **Why**: Small integers are common, caching avoids frequent object creation.

### How Interning Works
- **Within Range**: Values from `-5` to `256` are reused.
  - Example:
    ```python
    a = 10
    b = 10
    # a and b refer to the same object in memory
    ```
- **Outside Range**: Values below `-5` and above `256` create new objects.
  - Example:
    ```python
    a = 500
    b = 500
    # a and b refer to different objects in memory
    ```

### Singleton Objects
- **Singleton**: Only one instance of a class exists.
  - Interned integers are singleton objects in the specified range.
  - Single instance for each value in the cached range.

### Practical Code Examples
- **Checking Interned Integers**:
  ```python
  a = 10
  b = 10
  print(id(a) == id(b))  # True

  a = -5
  b = -5
  print(id(a) == id(b))  # True

  a = 256
  b = 256
  print(id(a) == id(b))  # True

  a = 257
  b = 257
  print(id(a) == id(b))  # False
  ```

### Creating Integers
- **Direct Assignment**:
  ```python
  a = 10
  b = 10
  ```

- **Using Constructor**:
  ```python
  b = int(10)
  c = int("10")
  d = int("1010", 2)  # Binary representation of 10
  ```

- **Memory Address Verification**:
  ```python
  print(id(a))  # Same address for all instances
  print(id(b))
  print(id(c))
  print(id(d))
  ```

## Conclusion
- Integer interning optimizes performance by reusing integer objects in a specific range.
- This reduces memory usage and object creation overhead.

## Additional Notes
- Interning is specific to the Python implementation and version.
- For more details on Python implementations and internals, refer to [Python Implementations](http://python.org).