#python #general_knowledge 

---
## Variable Reassignment

### Concept of Variable Reassignment

- **Initial Assignment**:
  - **Code**: `myvar = 10`
  - **Explanation**: 
    - Creates an integer object with value `10` at a memory address.
    - `myvar` is a reference (pointer) to this integer object.

- **Reassignment**:
  - **Code**: `myvar = 15`
  - **Explanation**: 
    - A new integer object with value `15` is created at a different memory address.
    - `myvar` now points to this new object.
    - The original object with value `10` remains unchanged.

### Reassignment Example

- **Code**:
  ```python
  myvar = 10
  myvar = myvar + 5
  ```
- **Explanation**:
  - Python evaluates `myvar + 5` first.
  - Creates a new integer object with value `15`.
  - `myvar` now points to the new object with value `15`.
  - The original object (value `10`) is unchanged.

### Immutability

- **Key Point**: 
  - The contents of integer objects (and other immutable objects) cannot be changed once created.
  - Reassignment creates a new object rather than modifying the existing one.

### Code Demonstration

- **Initial Assignment**:
  ```python
  a = 10
  ```
  - Memory address of `a` is noted.

- **Reassignment**:
  ```python
  a = 15
  ```
  - Memory address of `a` changes.
  - `a` now points to a new object with value `15`.

- **Further Reassignment**:
  ```python
  a = a + 1
  ```
  - Memory address of `a` changes again.
  - `a` now points to a new object with value `16`.

### Object Sharing

- **Code**:
  ```python
  a = 10
  b = 10
  ```
  - **Observation**:
    - Memory addresses of `a` and `b` are the same.
    - Both variables point to the same integer object with value `10`.

### Next Steps

- **Upcoming Topics**:
  - **Mutability vs. Immutability**: Understanding how Python handles different types of objects.
  - **Memory Optimization**: Why Python might reuse memory addresses for certain objects.