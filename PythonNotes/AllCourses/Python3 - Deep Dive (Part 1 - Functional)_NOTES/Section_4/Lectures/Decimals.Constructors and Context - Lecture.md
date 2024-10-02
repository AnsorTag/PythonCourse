#python #data-structures #general_knowledge 

coding lesson notes: [[Decimals.Constructors and Context - Code]]

---

# Decimal Constructors and Contexts

## Introduction
- This lecture covers:
  - How to construct a `Decimal` object using the `decimal` module.
  - The role of contexts in `Decimal` operations.

## Importing the Decimal Class
- To construct a `Decimal` object:
  ```python
  from decimal import Decimal
  ```
  - `Decimal` with a capital "D" is the class.
  - `decimal` with a lowercase "d" is the module.
  - Importing `Decimal` separately is often convenient, especially when working with contexts.

## Constructing Decimal Objects
- The `Decimal` constructor takes a single parameter `x`.
- `x` can be of various data types:
  - **Integer**:
    ```python
    a = Decimal(10)
    ```
  - **String**:
    ```python
    a = Decimal("0.1")
    ```
    - This stores the exact value `0.1`, unlike floats.
  - **Tuple**:
    - Example to store `-3.1415`:
      ```python
      a = Decimal((1, (3, 1, 4, 1, 5), -4))
      ```
    - The tuple consists of three elements:
      - **Sign**: `0` for non-negative, `1` for negative.
      - **Digits**: Tuple of individual digits.
      - **Exponent**: Integer representing the power of ten.

### Float Consideration
- **Floats** can be passed but are generally avoided:
  - Example:
    ```python
    a = Decimal(0.1)
    ```
  - This stores the float approximation (`0.10000000000000000555`) and **not** `0.1`.

## Understanding Tuple Constructor
- The tuple format for `Decimal` can be broken down:
  - **1.23** is equivalent to `+123 * 10^(-2)`.
  - **-1.23** is equivalent to `-123 * 10^(-2)`.
  
### Example Breakdown
- Example of representing `-3.1415`:
  - **Sign**: `1` (negative).
  - **Digits**: `(3, 1, 4, 1, 5)`.
  - **Exponent**: `-4`.
  - Tuple:
    ```python
    a = Decimal((1, (3, 1, 4, 1, 5), -4))
    ```
  - Result:
    - `Decimal` stores `-3.1415`.

## Context, Precision, and Constructor
- **Context Precision** affects mathematical operations, **not** the constructor.
- Example:
  - Set global context precision:
    ```python
    from decimal import getcontext
    getcontext().prec = 2
    ```
  - Constructing a `Decimal`:
    ```python
    a = Decimal("0.12345")
    ```
    - Stores exactly `0.12345`, ignoring context precision.

### Mathematical Operations
- **Precision** matters during operations:
  - Example:
    ```python
    b = Decimal("0.12345")
    c = a + b  # Result will be rounded to context precision
    ```
  - If the precision is `2`, the result is `0.25`.

## Global vs Local Contexts
- **Global Context**:
  - Precision applies throughout unless overridden.
  - Example:
    ```python
    getcontext().prec = 6
    ```
- **Local Context**:
  - Use a `with` statement for temporary precision:
    ```python
    from decimal import localcontext
    
    with localcontext() as ctx:
        ctx.prec = 2
        c = a + b
    ```
  - After exiting the block, `c` retains the precision applied within the local context:
    - `c = 0.25` even when global context has higher precision.

### Key Takeaway
- Precision of context does **not** retroactively change stored decimal values.
- Once a `Decimal` is created, its precision is fixed.

## Conclusion
- **Constructor**: Creates `Decimal` objects precisely based on input types.
- **Context Precision**: Only affects operations, not the initial creation of `Decimal` objects.