#python #coding-lesson 

---
## `limit_denominator` Method

**Purpose:**
- Finds the closest rational approximation to a given fraction with a denominator no greater than a specified maximum.

**Syntax:**
```python
Fraction.limit_denominator(max_denominator)
```

**Parameters:**
- `max_denominator`: The maximum value for the denominator of the approximated fraction.

**Returns:**
- A `Fraction` object that is the closest approximation to the original fraction, with the denominator less than or equal to `max_denominator`.

**Example:**
```python
from fractions import Fraction
import math

# Approximate π with a denominator ≤ 1000
approx_pi = Fraction(math.pi).limit_denominator(1000)
print(approx_pi)  # Output: 355/113
```

**Notes:**
- Useful for finding a simple fraction representation of irrational numbers or floats with limited precision.
- Provides a balance between precision and simplicity.