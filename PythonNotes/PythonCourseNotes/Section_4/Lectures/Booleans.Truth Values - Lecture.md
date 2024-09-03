#python #data-structures #general_knowledge 

coding lesson notes: [[Booleans.Truth Values - Code]]

---
## Booleans and Object Truth Values in Python

### Introduction to Object Truth Values
- **All objects in Python have an associated truth value.**
- **Truthiness of Integers:**
  - `bool(0)` returns `False`
  - `bool(1)` returns `True`
  - **Any integer other than 0 is considered truthy.**

### General Rules for Object Truthiness
- **Default behavior:** 
  - **All objects evaluate to `True` by default, except in specific cases.**
- **Falsy Objects:**
  - `None` object
  - `False` singleton object
  - `0` in any numeric type (int, float, complex, decimal)
  - **Empty sequences** (e.g., lists, tuples, strings)
  - **Empty mapping types** (e.g., dictionaries, sets, frozensets)
  - **Custom classes** can be made falsy by defining specific methods.

### Custom Class Truthiness
- **Defining truth values in custom classes:**
  - Implement the `__bool__` or `__len__` methods.
  - **If `__bool__` or `__len__` returns `False` or `0`, the object is considered falsy.**
  - **If these methods return `True` or any non-zero value, the object is truthy.**

### How Python Evaluates Truthiness
- **Python uses the `__bool__` method first**:
  - **If `__bool__` is defined, it returns the value from this method.**
  - **If `__bool__` is not found, Python tries the `__len__` method.**
  - **If neither method is defined, the object defaults to `True`.**

### Example: Integer Class Implementation
- **`int` class defines `__bool__` as follows:**
  ```python
  def __bool__(self):
      return self != 0
  ```
  - **Explanation:**
    - **For `bool(100)`, Python checks if `100 != 0`, which is `True`.**
    - **For `bool(0)`, Python checks if `0 != 0`, which is `False`.**

### Truthiness Examples
- **Lists:**
  - `bool([1, 2, 3])` → `True` (non-empty list)
  - `bool([])` → `False` (empty list)
- **None:**
  - `bool(None)` → `False`
- **Strings:**
  - `bool("ABC")` → `True` (non-empty string)
  - `bool("")` → `False` (empty string)
- **Numbers:**
  - `bool(0)` → `False`
  - `bool(-1)` → `True` (non-zero integer)
  - `bool(0.0)` → `False` (zero float)
  - `bool(0 + 0j)` → `False` (zero complex number)
  - `bool(1.1)` → `True` (non-zero float)
  - `bool(1 + 1j)` → `True` (non-zero complex number)

### Evaluating Conditions with Truthiness
- **Example Code:**
  ```python
  if my_list:
      # Code block executes if my_list is not None and not empty
  ```
  - **Equivalent to:**
    ```python
    if my_list is not None and len(my_list) > 0:
        # Code block executes
    ```
  - **Explanation:**
    - **`my_list` must be a valid list (not `None`).**
    - **`my_list` must have elements (length > 0).**

### Summary
- **Default truthiness is `True`, unless specific methods (`__bool__`, `__len__`) return `False` or `0`.**
- **Understanding object truth values is crucial for writing effective conditional statements in Python.**