#python #general_knowledge #data-structures 

coding lesson notes: [[Integers_Constructors and Bases - Coding]]

---
# Changing Number Bases and Encoding in Python

## Part 1: Understanding Base Conversion

### Concept Overview
- **Base Conversion**: Changing a number from one base (radix) to another. For example, converting a decimal (base 10) number to binary (base 2) or hexadecimal (base 16).

### Key Points

1. **Representation of Numbers**:
   - In any base, a number is represented as a sum of digits multiplied by powers of the base.
   - For example, in base 10 (decimal), the number 4321 is represented as:

     $$4321 = 4 \times 10^3 + 3 \times 10^2 + 2 \times 10^1 + 1 \times 10^0$$

   - Similarly, in base $b$, a number $N$ is represented as:

     $$N = d_n \times b^n + d_{n-1} \times b^{n-1} + \dots + d_1 \times b^1 + d_0 \times b^0$$

     where $d_n, d_{n-1}, \dots, d_0$ are the digits of $N$ in base $b$.

2. **Conversion Algorithm**:
   - To convert a decimal number $N$ to a different base $b$:
     1. **Divide** $N$ by $b$ to get a quotient and remainder.
     2. **Record** the remainder as the least significant digit (rightmost).
     3. **Update** $N$ to the quotient.
     4. **Repeat** until the quotient is zero.
     5. **Digits** are collected in reverse order, as the first remainder is the least significant digit.

### Example
- **Converting 4321 from base 10 to base 5**:
  1. $4321 \div 5 = 864$ remainder $1$ → 1 (rightmost digit).
  2. $864 \div 5 = 172$ remainder $4$ → 4.
  3. $172 \div 5 = 34$ remainder $2$ → 2.
  4. $34 \div 5 = 6$ remainder $4$ → 4.
  5. $6 \div 5 = 1$ remainder $1$ → 1.
  6. $1 \div 5 = 0$ remainder $1$ → 1 (leftmost digit).
- Result: $4321_{10} = 144241_5$.

## Part 2: In-Depth Base Conversion Process

### Understanding Limits and Process Continuation

- When converting a number like 46 to base 5:
  - The highest digit in base 5 is 4. However, $46$ is greater than the maximum single-digit value in base 5.
  - The formula used is:

    $$46 = (46 \div 5) \times 5 + (46 \mod 5)$$

    $$46 = 9 \times 5 + 1$$

  - Here, $9 \times 5$ exceeds the digit limit for base 5, so we must continue the division.

### Continuation Example
- Further breaking down 9 into base 5:

  $$9 = (9 \div 5) \times 5 + (9 \mod 5)$$

  $$9 = 1 \times 5 + 4$$

- Expanding the original equation:

  $$46 = 1 \times 5^2 + 4 \times 5 + 1$$

  - Result: $46_{10} = 141_5$.

### Algorithm for Base Conversion

1. **Initialize** an empty list `digits` to store the results.
2. **Loop** while $N$ is greater than 0:
   - Compute the remainder $N \mod b$ and update $N$ to $N \div b$.
   - Insert the remainder at the beginning of the list.
3. **Return** the list of digits, which represents the number in the new base.

### Python Implementation Example

```python
def convert_base(N, base):
    if base < 2 or N < 0:
        raise ValueError("Base must be >= 2 and N must be non-negative.")
    if N == 0:
        return [0]
    
    digits = []
    while N > 0:
        digits.insert(0, N % base)
        N = N // base
    
    return digits
```

### Encoding Base Conversion Results

- After converting, the results are in digit form, e.g., `[1, 4, 1, 2]` for base 5.
- Encoding involves mapping these digits to specific characters (e.g., in base 16, 10 = 'A', 11 = 'B').

### Example Encoding Map

- For base 16: `0-9`, `A-F` where:

  $$10 \rightarrow A, \ 11 \rightarrow B, \dots, 15 \rightarrow F$$

### Python Example for Encoding

```python
def encode_digits(digits, base_map):
    return ''.join(base_map[d] for d in digits)
```

### Considerations for Efficiency

- Avoid string concatenation in loops; use list comprehensions and `''.join()` for better performance.