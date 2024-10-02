#python #data-structures #general_knowledge 

coding lesson notes: [[Decimals - Code]]

---
## Decimals in Python

### Overview
- **Floats**: Previously discussed; a way to represent real numbers using binary floats.
- **Decimals**: An alternative to floats, provided by Python's `decimal` module, designed to represent floating-point numbers more accurately, particularly for financial and precise calculations.

### Key Points
- **Binary Float Issues**:
  - Decimal numbers like 0.1 have finite decimal representations but infinite binary expansions.
  - This leads to inexact representations when stored in binary format.
  - In critical fields (e.g., finance), these inaccuracies can accumulate and cause significant errors.

- **Rational Numbers**:
  - Any real number with a finite number of digits is a rational number and can be expressed as a fraction.
  - Although fractions offer exact representations, they require more computational resources and memory compared to floats.

### Why Decimals?
- **Exact Representations**: Essential in industries like finance, where exact values are crucial (e.g., bank account balances).
- **Precision Issues**: In scenarios like summing large numbers of transactions, small errors in float representation can accumulate, leading to significant discrepancies.

### Decimal Module

#### Basic Usage
- **Creating Decimals**: Use the `Decimal` class from the `decimal` module to create decimal numbers.
- **Precision and Rounding**: The module allows specifying the precision and rounding mechanisms, which are crucial for controlling how decimal arithmetic is handled.

#### Contexts
- **Global Context**: Default settings for decimal operations.
- **Local Context**: Temporary settings that override the global context for specific operations.

#### Managing Precision and Rounding
- **Precision**: Specifies how many digits should be preserved in arithmetic operations.
- **Rounding**: Specifies how rounding should be handled (e.g., towards even, away from zero).

#### Working with Contexts

- **Global Context**:
  ```python
  import decimal
  context = decimal.getcontext()  # Fetch global context
  context.prec = 28  # Set precision
  context.rounding = decimal.ROUND_HALF_EVEN  # Set rounding
  ```

- **Local Context**:
  ```python
  with decimal.localcontext() as ctx:
      ctx.prec = 10  # Temporary precision for this block
      ctx.rounding = decimal.ROUND_HALF_UP  # Temporary rounding
  ```
  - **Context Manager**: `decimal.localcontext()` returns a context manager, useful for temporarily changing settings without affecting the global context.

#### Rounding Algorithms
- **ROUND_HALF_EVEN**: Default, ties round to the nearest even number (same as float).
- **ROUND_HALF_UP**: Rounds away from zero, common in everyday rounding.
- **Other Algorithms**: Various other rounding mechanisms available for specific use cases.