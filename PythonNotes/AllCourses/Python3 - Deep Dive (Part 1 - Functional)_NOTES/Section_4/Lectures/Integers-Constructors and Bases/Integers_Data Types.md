#python #data-structures 

---
# Integers in Python

## Overview

- **Data Type**: `int`
  - Represents integral numbers (e.g., 0, 10, -10, 100 million).

## Binary Representation

- **Computers use binary** (base 2) to store integers.
- **Example**: Binary `10011`
  - Decimal equivalent: 
    - `1*16 + 0*8 + 0*4 + 1*2 + 1*1 = 19`
  - `10011` (base 2) = `19` (base 10)

## Bit Limitations

### 8 Bits

- **Unsigned**: Max value = `2^8 - 1 = 255`
- **Signed**: 
  - 1 bit for sign
  - Max value = `2^7 - 1 = 127`
  - **Range**: `-128` to `127`

### General Formula for Signed Integers

- **Range**: `-2^(N-1)` to `2^(N-1) - 1`
  - `N` = number of bits

### Examples

- **16 Bits**:
  - **Range**: `-32,768` to `32,767`
  
- **32 Bits**:
  - **Range**: `-2,147,483,648` to `2,147,483,647`

## Unsigned Integers

- **32-bit Unsigned**:
  - **Range**: `0` to `2^32 - 1 = 4,294,967,295`

## Practical Considerations

### 32-bit Operating Systems

- **Memory Limitation**: 
  - Maximum addressable memory = `2^32 bytes = 4 GB`
  - Higher memory (e.g., 64 GB) can't be fully utilized on a 32-bit system.

## Python’s Integer Handling

### Dynamic Bit Usage

- **Python `int` Type**:
  - Grows in bit size as needed.
  - Limited by available memory.

### Memory Usage

- **Object Overhead**:
  - Example:
    - `int(0)`: 24 bytes
    - `int(1)`: 28 bytes (4 bytes for storing the value)
    - Larger integers (e.g., `int(1000)`) use more memory.

## Performance Considerations

### Arithmetic Operations

- **Large Integers**:
  - Operations become slower as integers get larger.
  - **Benchmarking**:
    - Small integer (e.g., `10`): ~0.5 seconds for 10 million multiplications.
    - Large integer (e.g., `2^100`): ~0.9 seconds.
    - Very large integer (e.g., `2^10,000`): ~6.69 seconds.

## Summary

- **Python Integers**:
  - Can be arbitrarily large.
  - Memory and performance impact as integers grow.