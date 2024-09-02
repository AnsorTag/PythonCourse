#python #general_knowledge #data-structures 

---
# Lecture: Operations with Integers

## Overview
In this lecture, we explore the various arithmetic operations we can perform with integers in Python, including addition, subtraction, multiplication, division, exponents, and specific operators like floor division and modulo. Understanding the resulting types and behavior of these operations is crucial, especially when dealing with division and negative numbers.

---

## 1. **Basic Arithmetic Operations with Integers**

### Supported Operations:
- **Addition** (`+`): Returns an integer.
  - Example: `3 + 4 = 7`
- **Subtraction** (`-`): Returns an integer.
  - Example: `10 - 6 = 4`
- **Multiplication** (`*`): Returns an integer.
  - Example: `2 * 3 = 6`
- **Exponentiation** (`**`): Returns an integer.
  - Example: `2 ** 3 = 8`
- **Division** (`/`): Always returns a float.
  - Example: `10 / 2 = 5.0`

### Important Note:
- Even when dividing two integers with no remainder, the result will be a float.
  - Example: `10 / 2` returns `5.0`, not `5`.

---

## 2. **Special Integer Operations**

### 2.1 **Floor Division** (`//`)
- **Definition**: The floor division operator returns the largest integer less than or equal to the result of division.
  - Example: `155 // 4 = 38`
- **Behavior with Negative Numbers**: 
  - Example: `-155 // 4 = -39` (because `-39` is the largest integer less than `-38.75`).

### 2.2 **Modulo** (`%`)
- **Definition**: The modulo operator returns the remainder after division.
  - Example: `155 % 4 = 3`
- **Behavior with Negative Numbers**:
  - Example: `-155 % 4 = 1`

### 2.3 **The Div-Mod Relationship**
- **Equation**: `n = d * (n // d) + (n % d)`
  - This equation is always true, ensuring consistency between division and modulo operations.
  - Example with positive numbers: `155 = 4 * 38 + 3`
  - Example with negative numbers: `-155 = 4 * (-39) + 1`

---

## 3. **Understanding Floor Division (`//`)**

### 3.1 **What is the Floor of a Number?**
- **Definition**: The floor of a number is the largest integer less than or equal to the number.
  - Example: `floor(3.14) = 3`
- **Important with Negative Numbers**:
  - Example: `floor(-3.14) = -4`

### 3.2 **Floor Division Examples**
- **Positive Numbers**:
  - Example: `135 // 4 = 33` and `135 % 4 = 3`
- **Negative Numbers**:
  - Example: `-135 // 4 = -34` and `-135 % 4 = 1`

---

## 4. **Comparison: Floor vs Truncation**

### 4.1 **Truncation**
- **Definition**: Truncation removes the fractional part of a number, leaving the integer portion.
  - Example: `truncate(-3.14) = -3`

### 4.2 **Floor vs Truncation**
- **Positive Numbers**: Floor and truncation give the same result.
- **Negative Numbers**: They differ, as floor always returns the largest integer less than or equal to the number.
  - Example: `floor(-3.14) = -4` vs. `truncate(-3.14) = -3`

---

## 5. **Modulo Operation and Its Behavior**

### 5.1 **Modulo with Positive Numbers**
- **Example**: `13 % 4 = 1`
- **Verification**: `4 * 3 + 1 = 13`

### 5.2 **Modulo with Negative Numbers**
- **Negative Numerator**:
  - Example: `-13 % 4 = 3`
- **Negative Denominator**:
  - Example: `13 % -4 = -3`
- **Both Negative**:
  - Example: `-13 % -4 = -1`

### 5.3 **Consistent Equation Verification**
- **Equation**: Always ensure `n = d * (n // d) + (n % d)` holds true.
  - Example: `-13 = -4 * 4 + 3`

---

## 6. **Python Code Examples**

### 6.1 **Arithmetic Operation Types**
```python
type(1 + 1)  # int
type(2 * 3)  # int
type(4 - 10) # int
type(3 ** 6) # int
type(2 / 3)  # float
```

### 6.2 **Using `math.floor`**
```python
import math
math.floor(3.15)  # 3
math.floor(-3.14) # -4
```

### 6.3 **Floor Division in Action**
```python
a, b = 33, 16
print(a // b) # 2
print(math.floor(a / b)) # 2

a, b = -33, 16
print(a // b) # -3
print(math.floor(a / b)) # -3
```

### 6.4 **Using Modulo Operator**
```python
a, b = 13, 4
print(a % b) # 1

a, b = -13, 4
print(a % b) # 3

a, b = 13, -4
print(a % b) # -3

a, b = -13, -4
print(a % b) # -1
```