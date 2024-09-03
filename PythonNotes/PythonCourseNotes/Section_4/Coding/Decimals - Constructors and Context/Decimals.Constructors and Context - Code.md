#python #coding-lesson 

---
## 1. Imports and Constructor Overview

**Imports:**
```python
from decimal import Decimal
```

**Constructor Details:**
- **Syntax:** `Decimal(value)`
- **Parameters:**
  - `value` can be an integer, string, tuple, or another `Decimal` object.
  - If no value is provided, it returns `Decimal('0')`.

## 2. Using Different Data Types with `Decimal`

### 2.1. Integers

**Example:**
```python
a = Decimal(10)
```
- **Result:** `Decimal('10')`

### 2.2. Strings

**Examples:**
```python
a = Decimal("10.1")
```
- **Result:** `Decimal('10.1')`

**Negative Numbers:**
```python
b = Decimal("-3.1415")
```
- **Result:** `Decimal('-3.1415')`

### 2.3. Tuples

**Tuple Format:** `(sign, (digits), exponent)`

**Example for `3.1415`:**
```python
t = (0, (3, 1, 4, 1, 5), -4)
a = Decimal(t)
```
- **Result:** `Decimal('3.1415')`

**Important:** Ensure tuple is correctly formatted:
- **Correct:** `Decimal((0, (3, 1, 4, 1, 5), -4))`
- **Incorrect:** `Decimal(0, (3, 1, 4, 1, 5), -4)` (treated as multiple parameters).

### 2.4. Floats

**Avoid Using Floats:**
```python
a = Decimal(0.1)
```
- **Issue:** Floats can introduce precision issues. Use strings or tuples for exact values.

## 3. Context Precision and Its Effect

### 3.1. Global Context Precision

**Setting Precision:**
```python
from decimal import getcontext
getcontext().prec = 6
```

**Precision and Constructor:**
- Precision affects arithmetic operations, not the value stored.
  
**Example:**
```python
a = Decimal("0.123456789")
```
- **Stored As:** `Decimal('0.123456789')` regardless of the precision setting.

### 3.2. Arithmetic Operations

**Example:**
```python
a = Decimal("0.12345")
b = Decimal("0.12345")
```

**Addition:**
```python
c = a + b
print(c)  # Result depends on current context precision
```

**Result with Precision 2:**
```python
getcontext().prec = 2
print(a + b)  # Result: Decimal('0.25')
```

### 3.3. Local Context Precision

**Using Local Context:**
```python
from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print("C within local context:", c)
```

**Global Context After Local Context:**
```python
getcontext().prec = 6
print("C after local context:", c)  # Result: Decimal('0.25')
```

**Key Point:** Local context affects calculations but does not change the stored value of `Decimal` objects.

## 4. Key Takeaways

**Precision:**
- Affects arithmetic operations.
- Does not alter the precision of values stored in `Decimal` objects.

**Constructors:**
- Use strings or tuples for exact representation.
- Avoid using floats due to precision loss.

## 5. Conclusion

**Decimal Construction:**
- Can be done with integers, strings, tuples, or another `Decimal`.
- Avoid floats due to precision issues.

**Context Precision:**
- Impacts arithmetic operations, not the precision of stored values.