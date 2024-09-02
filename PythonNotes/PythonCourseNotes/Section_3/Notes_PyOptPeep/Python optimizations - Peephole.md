#python #general_knowledge 

---
## Peephole Optimizations in Python

### Introduction
In this lesson, we'll explore peephole optimizations in Python. Peephole optimizations are a type of optimization that occurs at compile time. While Python code is not compiled into an executable like C, it is compiled into bytecode that is executed by the Python interpreter. This compilation happens at runtime, and certain optimizations are applied to improve performance.

### Constant Expressions
Constant expressions are evaluated and optimized at compile time. For example:

```python
minutes = 24 * 60
```

Here, `24 * 60` is a constant expression, and Python will calculate it once and store the result (`1440`). This avoids recalculating `24 * 60` every time the line of code is executed.

### Short Sequences
Python also pre-calculates and stores short sequences (length less than 20) such as lists, tuples, and strings. For example:

- `tuple(1, 2) * 5` evaluates to `(1, 2, 1, 2, 1, 2, 1, 2, 1, 2)`
- `ABC * 3` evaluates to `ABCABCABC`
- `Hello + World` evaluates to `HelloWorld`

Sequences longer than 20 characters are not pre-calculated to balance between storage and computation efficiency.

### Membership Tests
Membership tests check if an element exists in a container. Python optimizes these tests by converting mutable containers into immutable ones for efficiency. For example:

- A list `[1, 2, 3]` is converted to a tuple `(1, 2, 3)`
- A set `{1, 2, 3}` is converted to a frozenset `frozenset({1, 2, 3})`

Sets are implemented similarly to dictionaries and provide faster membership tests compared to lists or tuples.

### Example Code

#### Defining Variables
```python
def myfunc():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'ABC' * 3
    d = 'AB' * 11  # Longer than 20 characters
    e = 'The quick brown fox' * 5  # Longer than 20 characters
    f = ['A', 'B'] * 3  # Mutable list
```

#### Inspecting Compiled Constants
```python
import dis
dis.dis(myfunc)
```
This will show you which constants are pre-calculated and stored.

#### Membership Testing Example
```python
def membership_test(n, container):
    for _ in range(n):
        if 'z' in container:
            pass
```

#### Timing Membership Tests
```python
import string
import time

ascii_letters = string.ascii_letters
list_container = list(ascii_letters)
tuple_container = tuple(ascii_letters)
set_container = set(ascii_letters)

def benchmark_membership(test_container, name):
    start = time.perf_counter()
    membership_test(10_000_000, test_container)
    end = time.perf_counter()
    print(f"{name} took {end - start:.2f} seconds")

benchmark_membership(list_container, "List")
benchmark_membership(tuple_container, "Tuple")
benchmark_membership(set_container, "Set")
```

#### Results
You should observe that set membership tests are significantly faster than list or tuple membership tests.

### Summary
- **Constant Expressions**: Pre-calculated and optimized at compile time.
- **Short Sequences**: Length less than 20 are pre-calculated.
- **Membership Tests**: Mutable containers (lists) are converted to immutable ones (tuples) for efficiency. Sets are the fastest for membership testing.