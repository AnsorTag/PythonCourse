#python #data-structures #general_knowledge 

coding lesson notes: [[Booleans.Boolean Operators - Code]]

---
## Overview

In this lecture, we delve deeper into Boolean operators within the context of truth values. We'll explore how these operators work and their results when applied to different types of objects.

---

## Truth Tables for Boolean Operators

### Basic Operators

- **AND (x and y):** Returns `True` only if both `x` and `y` are truthy.
- **OR (x or y):** Returns `True` if at least one of `x` or `y` is truthy.

**Truth Table for AND:**

| x     | y     | x and y |
|-------|-------|---------|
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

**Truth Table for OR:**

| x     | y     | x or y |
|-------|-------|--------|
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

### Boolean Algebra

- **AND and OR operators:** Defined to operate on Boolean values and return Boolean values. 
- **Boolean algebra:** Operators (`and`, `or`) are just elements of Boolean algebra and are only defined for Boolean values.

---

## Truthiness in Python

### Truthiness Concept

In Python, every object has a truth value (truthiness), which determines how it evaluates in Boolean contexts. 

- **Truthy:** Objects that evaluate to `True` (e.g., non-zero numbers, non-empty strings).
- **Falsy:** Objects that evaluate to `False` (e.g., `None`, `0`, `""`).

### Using Boolean Operators with Non-Boolean Objects

- **Example:**
  ```python
  a = 2
  b = 3
  result = (a > 0) and (b < 5)  # True and True evaluates to True
  ```

- **Short-circuiting Behavior:**
  - **OR:** `x or y` returns `x` if `x` is truthy, otherwise returns `y`.
  - **AND:** `x and y` returns `x` if `x` is falsy, otherwise returns `y`.

---

## Detailed Behavior of OR

**Definition:**
- If `x` is truthy, return `x`.
- Otherwise, return `y`.

**Examples:**

1. **Example 1:**
   ```python
   x = None
   y = "A"
   result = x or y  # Returns "A"
   ```

2. **Example 2:**
   ```python
   x = ""
   y = "A"
   result = x or y  # Returns "A"
   ```

3. **Example 3:**
   ```python
   x = "Hello"
   y = "World"
   result = x or y  # Returns "Hello"
   ```

**Use Case: Default Values**

- **Example:**
  ```python
  s = None
  a = s or "N/A"  # a = "N/A" if s is None or empty
  ```

- **Multiple Defaults:**
  ```python
  a = s1 or s2 or s3 or "N/A"  # Returns the first truthy value
  ```

---

## Detailed Behavior of AND

**Definition:**
- If `x` is falsy, return `x`.
- Otherwise, return `y`.

**Examples:**

1. **Example 1:**
   ```python
   x = 10
   y = 20 / x
   result = x and y  # Returns 2.0
   ```

2. **Example 2:**
   ```python
   x = 0
   y = 20 / x  # This will not be evaluated
   result = x and y  # Returns 0
   ```

**Use Case: Avoiding Errors**

- **Example:**
  ```python
  a = 10
  average = a and total / a  # Avoids division by zero if a is 0
  ```

---

## Handling Default Values and Falsy Values

1. **First Character of String:**
   ```python
   def first_char(s):
       return s and s[0] or ""
   ```

   - Returns the first character if `s` is truthy.
   - Returns an empty string if `s` is falsy.

---

## The NOT Operator

- **Definition:** `not x` returns `True` if `x` is falsy, and `False` if `x` is truthy.

**Examples:**

1. **Example 1:**
   ```python
   result = not None  # True
   ```

2. **Example 2:**
   ```python
   result = not ""  # True
   ```

3. **Example 3:**
   ```python
   result = not "Hello"  # False
   ```

**Note:** Unlike `and` and `or`, `not` always returns a Boolean value.

---

## Summary

- **AND** and **OR** operators return objects based on their truthiness and short-circuit evaluation.
- **NOT** always returns a Boolean value based on the truthiness of the object.