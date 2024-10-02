#python #general_knowledge #data-structures 

coding lesson notes: [[Floats - Code]]

---
## Internal Representation of Floats in Python

### Overview

When dealing with real numbers in Python, the default representation is the `float` class. Python’s `float` is implemented using the C `double` type, which follows the IEEE 754 standard for double-precision floating-point arithmetic. This representation affects how real numbers are stored and computed in Python.

### Float Representation

**Default Class:**
- **`float`**: Represents real numbers.
- Example: `a = 10.5` uses a `float`.

**Standard Implementation:**
- **C `double`**: Follows IEEE 754 standard for double-precision floating-point.
- Commonly known as **binary 64**.
- **Fixed Width**: Uses 8 bytes (64 bits) to store floating-point numbers.

**Memory Usage:**
- **Python Object Overhead**: In CPython, each float uses approximately 24 bytes due to overhead.

**Precision:**
- **64 bits** are divided as follows:
  - **Sign Bit**: 1 bit
  - **Exponent**: 11 bits
  - **Significant Digits (Mantissa)**: 52 bits
- **Significant Digits**: Approximately 15 to 17 decimal digits of precision.

### Components of a Float

1. **Sign Bit:**
   - Indicates if the number is positive or negative.
   - `0` for positive, `1` for negative.

2. **Exponent:**
   - Represents the power of 2 by which the significant digits are multiplied.
   - 11 bits allow for an exponent range from -1022 to 1023.

3. **Significant Digits (Mantissa):**
   - Represents the precision of the number.
   - Stored as 52 bits.
   - Example: For `1.2345`, the significant digits are `12345`.

### Decimal Representation

**Base-10 Representation:**
- Numbers are represented as a sum of digits multiplied by powers of 10.
- Example: `0.75 = 7/10 + 5/100`.
- Significant digits are determined by the number of non-zero digits excluding leading and trailing zeros.

**Example Expansions:**
- `0.75` = `7 × 10^-1 + 5 × 10^-2` (2 significant digits)
- `0.256` = `2 × 10^-1 + 5 × 10^-2 + 6 × 10^-3` (3 significant digits)

### Binary Representation

**Base-2 (Binary) Representation:**
- Computers use binary (0s and 1s) instead of decimal.
- **Binary Point**: Similar to the decimal point but for base-2.

**Example:**
- `0.11` base-2 = `1/2 + 1/4 = 0.75` base-10.
- `0.1101` base-2 = `1/2 + 1/4 + 0/8 + 1/16 = 0.8125` base-10.

**Expansion Formula:**
- Binary representation: `Σ (digit × 2^power)`
- Digits are 0 or 1, and powers are negative for digits after the binary point.

### Issues with Binary Representation

**Finite vs. Infinite Representation:**
- Some decimal numbers cannot be represented exactly in binary.
- Example: `0.1` in decimal does not have a finite binary representation.

**Binary Expansion of `0.1`:**
- In binary, `0.1` is approximated as `0.0001100110011...` (repeating).
- An infinite series cannot be fully represented, leading to approximation errors.

### Precision and Approximation

**Exact vs. Approximate Representation:**
- **Finite Representations**: Some decimal numbers have exact binary equivalents (e.g., `0.75`).
- **Approximate Representations**: Numbers like `0.1` are approximated due to infinite binary series.

**Impact on Python Floats:**
- **Exact Representation**: Numbers like `0.75` are stored precisely.
- **Approximate Representation**: Numbers like `0.1` are stored approximately, with potential precision loss.

**General Insight:**
- This is a limitation inherent to all computing systems that use binary representation.
- Not a flaw in Python, but a characteristic of binary floating-point arithmetic.