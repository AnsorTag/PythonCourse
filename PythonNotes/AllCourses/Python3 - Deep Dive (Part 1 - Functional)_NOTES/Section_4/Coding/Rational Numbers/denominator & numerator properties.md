#python #coding-lesson 

---
## `.denominator` Property

**Purpose:**
- Retrieves the denominator of a `Fraction` object.

**Syntax:**
```python
Fraction.denominator
```

**Returns:**
- An integer representing the denominator of the fraction.

**Example:**
```python
from fractions import Fraction

f = Fraction(22, 7)
print(f.denominator)  # Output: 7
```

**Notes:**
- The `.denominator` property is read-only.
- Represents the bottom part of the fraction (the divisor).

---

## `.numerator` Property

**Purpose:**
- Retrieves the numerator of a `Fraction` object.

**Syntax:**
```python
Fraction.numerator
```

**Returns:**
- An integer representing the numerator of the fraction.

**Example:**
```python
from fractions import Fraction

f = Fraction(22, 7)
print(f.numerator)  # Output: 22
```

**Notes:**
- The `.numerator` property is read-only.
- Represents the top part of the fraction (the dividend).
