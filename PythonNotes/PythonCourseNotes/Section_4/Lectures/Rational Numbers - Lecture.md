#python #general_knowledge #data-structures 

coding lesson notes: [[Rational Numbers - Coding]]

---
## Rational Numbers and Python’s `fractions` Module

### Rational Numbers

**Definition:**
- Rational numbers are numbers that can be expressed as a fraction where both the numerator and the denominator are integers. Examples include \( \frac{1}{2} \), \( \frac{-22}{7} \), and \( \frac{8.3}{4} \).

**Irrational Numbers:**
- Numbers that cannot be expressed as a simple fraction. Examples include \( \sqrt{2} \) and \( \pi \). These numbers have infinite non-repeating decimal expansions.

**Finite Decimal Representation:**
- Any real number with a finite number of digits before and after the decimal point can be expressed as a rational number. For example:
  - \( 0.45 = \frac{45}{100} \)
  - \( 0.123456789 = \frac{123456789}{10^9} \)

### Using `fractions.Fraction` in Python

**Importing:**
- Import the `Fraction` class from the `fractions` module:
  ```python
  from fractions import Fraction
  ```

**Creating Fractions:**
- From integers:
  ```python
  f1 = Fraction(3, 4)   # Represents 3/4
  ```
- From floats:
  ```python
  f2 = Fraction(0.75)   # Represents 3/4
  ```
- From strings:
  ```python
  f3 = Fraction('22/7') # Represents 22/7
  ```

**Automatic Simplification:**
- The `Fraction` class automatically reduces fractions to their simplest form. For example:
  ```python
  f4 = Fraction(6, 10)  # Automatically reduced to 3/5
  ```

**Handling Negatives:**
- Negative signs are always placed in the numerator by Python. For example:
  ```python
  f5 = Fraction(-1, 4)  # Represents -1/4
  ```

**Arithmetic Operations:**
- Python supports standard arithmetic operations with fractions, and the result is always a fraction. For example:
  ```python
  f6 = Fraction(2, 3) * Fraction(1, 2)  # Results in 1/3
  ```

**Accessing Numerator and Denominator:**
- You can access the numerator and denominator of a `Fraction` object using:
  ```python
  f7 = Fraction(22, 7)
  numerator = f7.numerator   # 22
  denominator = f7.denominator # 7
  ```

### Floats and Rational Numbers

**Finite Precision:**
- Floats have finite precision and can be approximated by rational numbers, but not exactly. For example:
  - `Fraction(0.125)` results in \( \frac{1}{8} \)
  - `Fraction(0.3)` may result in a less simple fraction due to precision issues.

**Limiting Denominator:**
- Use the `limit_denominator(max_denominator)` method to constrain the denominator of a fraction. This finds the closest rational approximation:
  ```python
  from fractions import Fraction
  import math
  
  # Example with Pi
  f_pi = Fraction(math.pi).limit_denominator(1000)
  # Closest approximation to Pi with denominator ≤ 1000
  ```

**Examples:**
- `Fraction(math.pi).limit_denominator(10)` yields \( \frac{22}{7} \)
- `Fraction(math.pi).limit_denominator(100)` yields \( \frac{311}{99} \)
- `Fraction(math.pi).limit_denominator(500)` yields \( \frac{355}{113} \)