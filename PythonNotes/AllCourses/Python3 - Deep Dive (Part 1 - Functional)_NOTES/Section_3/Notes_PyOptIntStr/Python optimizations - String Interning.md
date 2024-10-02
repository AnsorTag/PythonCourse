#python #general_knowledge 

---
## Overview
- This lecture covers **string interning** and how it can optimize Python code.
- **Interning**: Reusing strings to optimize performance and memory usage.

## Identifiers and Interning
- **Identifiers**: Variable names, function names, class names, etc.
- **Interning**: Applies to some string literals, especially those resembling identifiers.
- **Rules for Identifiers**: Must start with a letter or underscore and can include letters, numbers, and underscores.

## Why Intern Strings?
- **Speed Optimization**: Reduces time spent comparing strings character by character.
- **Memory Optimization**: Reuses strings to save memory.

### Example of Optimization
- **Without Interning**:
  ```python
  a = "some long string"
  b = "some long string"
  # Comparison: a == b involves checking each character
  ```
- **With Interning**:
  - Interned strings share the same memory address.
  - Comparison can be done using the identity operator `is`:
    ```python
    a = "some long string"
    b = "some long string"
    # Comparison: a is b (faster, checks memory addresses)
    ```

## Forcing Interning
- **Using `sys.intern`**:
  ```python
  import sys
  a = sys.intern("Hello world")
  b = sys.intern("Hello world")
  ```
  - Ensure all instances of the string are interned for consistency.
  
- **Example**:
  ```python
  import sys
  
  a = sys.intern("Hello world")
  b = sys.intern("Hello world")
  c = "Hello world"
  
  print(id(a))  # ID of interned string
  print(id(b))  # Same ID as a
  print(id(c))  # Different ID (not interned)
  
  print(a is b)  # True
  print(a is c)  # False
  ```

## When to Use String Interning
- **High Repetition**: Useful for large datasets with repeated strings (e.g., text tokenization).
- **String Comparisons**: Faster comparisons if many comparisons are needed.

### Benchmark Example
- **Equality Comparison**:
  ```python
  def compare_using_equals(n):
      a = "long string" * 200
      b = "long string" * 200
      for _ in range(n):
          if a == b:
              pass
  
  def compare_using_interning(n):
      import sys
      a = sys.intern("long string" * 200)
      b = sys.intern("long string" * 200)
      for _ in range(n):
          if a is b:
              pass
  ```
  
- **Timing**:
  ```python
  import time
  
  start = time.perf_counter()
  compare_using_equals(10_000_000)
  end = time.perf_counter()
  print(f"Equality comparison took {end - start} seconds")
  
  start = time.perf_counter()
  compare_using_interning(10_000_000)
  end = time.perf_counter()
  print(f"Interned comparison took {end - start} seconds")
  ```

## Conclusion
- **String Interning**: Useful for optimizing performance in scenarios with high repetition and frequent string comparisons.
- **Recommendation**: Use string interning only when performance gains are significant; otherwise, stick to normal string handling.