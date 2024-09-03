#python #data-structures #general_knowledge 

coding lesson notes: [[Booleans.Precedence and ShortCircuiting - Code]]

---
# Boolean Operators and Short Circuit Evaluation

## Overview
In this lecture, we will:
- Explore Boolean operators (`not`, `and`, `or`).
- Understand operator precedence.
- Learn about short circuit evaluation.

## Boolean Operators

### Truth Tables
A truth table lists all possible combinations of input variables and the results of Boolean expressions.

#### Example:
For two Boolean variables \( X \) and \( Y \) (where `false = 0` and `true = 1`):

**NOT Operator:**
| \( X \) | NOT \( X \) |
|--------|-------------|
| false  | true        |
| true   | false       |

**OR Operator:**
| \( X \) | \( Y \) | \( X \) OR \( Y \) |
|--------|--------|---------------------|
| false  | false  | false               |
| false  | true   | true                |
| true   | false  | true                |
| true   | true   | true                |

**AND Operator:**
| \( X \) | \( Y \) | \( X \) AND \( Y \) |
|--------|--------|---------------------|
| false  | false  | false               |
| false  | true   | false               |
| true   | false  | false               |
| true   | true   | true                |

### Electrical Circuit Analogy
- **OR**: Represented as switches in parallel. Current flows if at least one switch is closed.
- **AND**: Represented as switches in series. Current flows only if all switches are closed.

## Properties of Boolean Operators

### Commutativity
- **OR**: \( A \) OR \( B \) = \( B \) OR \( A \)
- **AND**: \( A \) AND \( B \) = \( B \) AND \( A \)

### Distributivity
- \( A \) AND (\( B \) OR \( C \)) = (\( A \) AND \( B \)) OR (\( A \) AND \( C \))
- \( A \) OR (\( B \) AND \( C \)) = (\( A \) OR \( B \)) AND (\( A \) OR \( C \))

### Associativity
- **OR**: \( A \) OR (\( B \) OR \( C \)) = (\( A \) OR \( B \)) OR \( C \)
- **AND**: \( A \) AND (\( B \) AND \( C \)) = (\( A \) AND \( B \)) AND \( C \)

### De Morgan's Laws
- **NOT (\( A \) OR \( B \))** = (NOT \( A \)) AND (NOT \( B \))
- **NOT (\( A \) AND \( B \))** = (NOT \( A \)) OR (NOT \( B \))

### Miscellaneous
- **NOT \( X < Y \)**: \( X \) is greater than or equal to \( Y \)
- **NOT \( X \leq Y \)**: \( X \) is greater than \( Y \)
- **Double NOT**: NOT (NOT \( A \)) = \( A \)

## Operator Precedence

### Precedence Order
1. **Parentheses** (highest precedence)
2. **Comparison Operators** (e.g., `<`, `>`, `==`, `!=`)
3. **NOT**
4. **AND**
5. **OR** (lowest precedence)

### Example
Consider the expression: `true or true and false`

- **Step 1:** Evaluate `true and false` (AND has higher precedence)
- **Step 2:** Result of `true and false` is `false`
- **Step 3:** Evaluate `true or false` (OR operation)

### Parentheses for Clarity
Always use parentheses to clarify precedence and improve readability:
- Without parentheses: `true or true and false`
- With parentheses: `(true or true) and false` results in `false`

## Short Circuit Evaluation

### Concept
- **OR**: If the first operand is `true`, the result is `true` regardless of the second operand.
- **AND**: If the first operand is `false`, the result is `false` regardless of the second operand.

### Examples
- **OR Example**:
  ```python
  if x or y:  # If x is True, y is not evaluated
      do_something()
  ```

- **AND Example**:
  ```python
  if x and y:  # If x is False, y is not evaluated
      do_something()
  ```

### Practical Use Case

#### Stock Symbol Check
Suppose you have a data feed of stock symbols and want to:
1. Check if the symbol is in a watch list.
2. Retrieve the stock price and compare it to a threshold.

With short circuiting:
```python
if symbol in watch_list and price_of_symbol > threshold:
    do_something()
```
- If `symbol not in watch_list`, the second condition is not evaluated.

#### Nullable String Check
Suppose you need to check if the first character of a string is a digit:
```python
if name and name[0] in string.digits:
    do_something()
```
- If `name` is `None` or an empty string, the second condition is not evaluated, preventing errors.

## Summary
- Boolean operators are foundational for logical operations in programming.
- Understanding operator precedence and short circuit evaluation helps in writing efficient and readable code.
- Use parentheses to make expressions clear and maintainable.