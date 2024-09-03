#python #coding-lesson 

---
## Mathematical Operations with Decimals

### Importing the Decimal Module
To work with decimal operations, first import the `decimal` module and the `Decimal` class:
```python
from decimal import Decimal
```

### Division and Modulus Operators

#### Integer vs Decimal
- **Integer Division (`//`)**: For integers, division yields the quotient.
- **Decimal Division (`divmod`)**: For decimals, division is handled differently. The results may vary based on the sign of the numbers.

#### Example with Integers
```python
x = 10
y = 3
print(x // y)  # Outputs: 3
print(x % y)   # Outputs: 1
print(divmod(x, y))  # Outputs: (3, 1)
```

Verify the equation:
\[ x = y \times (x \, \text{div} \, y) + (x \, \text{mod} \, y) \]
This equation holds true for integers.

#### Example with Decimals
```python
from decimal import Decimal

x = Decimal('10')
y = Decimal('3')
print(x // y)  # Outputs: 3
print(x % y)   # Outputs: 1
print(divmod(x, y))  # Outputs: (3, 1)
```

#### Changing Signs
```python
x = Decimal('-10')
y = Decimal('3')
print(x // y)  # Outputs: -4
print(x % y)   # Outputs: 2

x = Decimal('10')
y = Decimal('-3')
print(x // y)  # Outputs: -4
print(x % y)   # Outputs: -2
```

### Mathematical Functions in Decimal Class

#### Available Functions
- **Exponentiation**: `Decimal('e') ** x`
- **Natural Logarithm**: `.ln()`
- **Logarithm Base 10**: `.log10()`
- **Logarithm Base B**: `.logb(B)`
- **Square Root**: `.sqrt()`
- **Max/Min Functions**

#### Calling Methods
```python
a = Decimal('1.5')
print(a.ln())        # Natural logarithm of a
print(Decimal('e') ** a)  # e raised to the power of a
print(a.sqrt())     # Square root of a
```

### Comparing with Float Functions

#### Using Math Module
```python
import math

a = Decimal('1.5')
print(math.sqrt(float(a)))  # Converts Decimal to float
```

#### Differences in Precision
- **Floats**: May not maintain the precision of decimals.
- **Decimals**: Maintain exact precision.

#### Example
```python
# Integer examples
x = Decimal('2')
root_float = math.sqrt(float(x))  # Float conversion
root_decimal = x.sqrt()           # Decimal operation

print(root_float, root_decimal)

# Difference in Precision
print(root_float * root_float)  # Slightly off from 2
print(root_decimal * root_decimal)  # Exactly 2

# Example with small decimal
x = Decimal('0.01')
root_decimal = x.sqrt()
print(root_decimal)  # Outputs: 0.1
```

### Key Points
- **Math Module**: Useful for functions not available in the `Decimal` class, but be aware of precision loss due to float conversion.
- **Decimal Class**: Provides a robust set of mathematical functions with exact precision, suitable for financial and high-precision calculations.