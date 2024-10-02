#python #application

---
# Lecture: Timing Functions in Python

## Introduction
- **Objective**: Learn how to time a function's execution in Python, regardless of the function type or its arguments.
- **Goal**: Create a generic function `time_it()` to time any function with any parameters.

---

## Steps to Build the `time_it()` Function

### 1. **Importing Necessary Module**
```python
import time
```
- We'll use the `time` module to handle timing.

### 2. **Defining the `time_it()` Function**
```python
def time_it(fn, *args, **kwargs):
    start = time.perf_counter()  # Start timing
    result = fn(*args, **kwargs)  # Execute the function
    end = time.perf_counter()  # End timing
    return end - start
```
- **`fn`**: The function we want to time.
- **`*args`**: Positional arguments for the function.
- **`**kwargs`**: Keyword arguments for the function.

### 3. **Example: Timing the `print` Function**
```python
time_it(print, 1, 2, 3, sep=' - ', end=' *** ')
```
- **Explanation**: 
  - `*args`: (1, 2, 3)
  - `**kwargs`: {'sep': ' - ', 'end': ' *** '}

---

## Improving `time_it()` with Repetition
### 1. **Adding Repetition**
```python
def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for _ in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep  # Average time
```
- **`rep`**: Number of repetitions (default = 1).
- Executes the function multiple times to get an average execution time.

### 2. **Example with Repetition**
```python
time_it(print, 1, 2, 3, sep=' - ', end=' *** ', rep=5)
```
---

## Practical Example: Computing Powers
### 1. **Function: Compute Powers (v1)**
```python
def compute_powers_v1(n, *, start=1, end):
    result = []
    for i in range(start, end):
        result.append(n ** i)
    return result
```
- **Purpose**: Calculate `n` to the power of a range of values.

### 2. **Optimizing with List Comprehension (v2)**
```python
def compute_powers_v2(n, *, start=1, end):
    return [n ** i for i in range(start, end)]
```

### 3. **Using Generators (v3)**
```python
def compute_powers_v3(n, *, start=1, end):
    return (n ** i for i in range(start, end))  # Generator
```

---

## Timing the `compute_powers` Functions
```python
time_it(compute_powers_v1, 2, start=1, end=20000, rep=5)
time_it(compute_powers_v2, 2, start=1, end=20000, rep=5)
time_it(compute_powers_v3, 2, start=1, end=20000, rep=5)
```
- **Result**: Generators are faster at first but only because they lazily evaluate (compute values on demand).

---

## Key Concepts Recap
- **Positional Arguments (`*args`)**: Passed as a tuple.
- **Keyword Arguments (`**kwargs`)**: Passed as a dictionary.
- **Repetition**: Helps time functions by running them multiple times for better average measurements.
- **Generators**: Compute values only when needed, making them appear faster, but they don’t generate the full result up front.