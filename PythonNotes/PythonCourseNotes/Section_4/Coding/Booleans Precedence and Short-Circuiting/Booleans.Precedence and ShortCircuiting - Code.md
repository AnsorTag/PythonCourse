#python #coding-lesson 

---
## Lecture Notes: Boolean Operators and Short Circuiting

### 1. **Boolean Operator Precedence**

- **Operator Precedence**:
  - `NOT` has the highest precedence.
  - `AND` has a medium precedence.
  - `OR` has the lowest precedence.

- **Example**: `True or True and False`
  - Evaluates to `True`.
  - **Reason**: `AND` is evaluated before `OR`.
  - Breakdown:
    - First, `True and False` is evaluated, which results in `False`.
    - Then, `True or False` is evaluated, which results in `True`.

- **Parentheses for Clarity**:
  - `True or (True and False)` evaluates as `True` (same result).
  - **Recommendation**: Use parentheses to clarify precedence and enhance code readability.

### 2. **Short Circuiting**

- **Concept**:
  - Short circuiting means that Python will stop evaluating a boolean expression as soon as the result is determined.
  - For `OR`, if the left operand is `True`, the right operand is not evaluated.
  - For `AND`, if the left operand is `False`, the right operand is not evaluated.

- **Examples**:

  **Example 1: Prevent Division by Zero**
  ```python
  A = 10
  B = 2

  if B > 0 and A / B > 2:
      print("A is at least twice B")
  ```
  - **Explanation**: If `B` is `0`, the expression `B > 0` is `False`, so `A / B` is not evaluated.

  **Example 2: Using Truthiness**
  ```python
  if B and A / B > 2:
      print("A is at least twice B")
  ```
  - **Explanation**: `B` being `0` (Falsy) causes the entire expression to short circuit and not evaluate `A / B`.

  **Example 3: Handling None Values**
  ```python
  if name is not None and len(name) > 0 and name[0] in string.digits:
      print("Name cannot start with a digit")
  ```
  - **Explanation**: Short circuiting avoids calling `len(name)` or accessing `name[0]` if `name` is `None`.

### 3. **Using the String Module**

- **Module Import**:
  ```python
  import string
  ```

- **Useful Constants**:
  - `string.ascii_lowercase` - all lowercase ASCII characters.
  - `string.ascii_uppercase` - all uppercase ASCII characters.
  - `string.digits` - all digits `0-9`.

- **Example**: Check if the first character of a name is a digit.
  ```python
  name = "Bob"
  if name and name[0] in string.digits:
      print("Name cannot start with a digit")
  ```
  - **Explanation**: Handles empty strings and ensures that only non-empty names are checked.

### 4. **Truthiness and Short Circuiting**

- **Truthiness**:
  - Non-empty strings are truthy.
  - Empty strings are falsy.
  - `None` is falsy.

- **Example**:
  ```python
  if name:
      if name[0] in string.digits:
          print("Name cannot start with a digit")
  ```
  - **Explanation**: If `name` is `None` or an empty string, the check is skipped.

- **Shortened Code**:
  ```python
  if name and name[0] in string.digits:
      print("Name cannot start with a digit")
  ```
  - **Explanation**: Combines checks to handle `None`, empty strings, and digit checking more concisely.