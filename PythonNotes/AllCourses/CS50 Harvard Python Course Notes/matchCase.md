---
tags:
  - python
  - flow-control
---
## Python `match-case` Statement

### Overview
- **`match-case`**: A control flow structure introduced in Python 3.10 for pattern matching.
- **Syntax**: Similar to switch-case statements in other languages but with more powerful pattern-matching capabilities.

### Basic Structure
```python
match variable:
    case "The sought value":
        action
    case _:
        last action
```

- **`match variable`**: The variable whose value is being matched against the cases.
- **`case "The sought value":`**: Checks if the variable matches the specified value.
- **`case _:`**: The wildcard case that matches anything (similar to `default` in other languages).

### Example Usage

#### Matching Strings
```python
fruit = "apple"

match fruit:
    case "apple":
        print("You chose an apple.")
    case "banana":
        print("You chose a banana.")
    case _:
        print("Unknown fruit.")
```
- **Output**: `You chose an apple.`

#### Matching Numbers
```python
number = 42

match number:
    case 1:
        print("The number is 1.")
    case 42:
        print("The number is 42.")
    case _:
        print("Number not recognized.")
```
- **Output**: `The number is 42.`

#### Matching Data Structures
```python
point = (0, 0)

match point:
    case (0, 0):
        print("The point is at the origin.")
    case (x, 0):
        print(f"The point is on the x-axis at {x}.")
    case (0, y):
        print(f"The point is on the y-axis at {y}.")
    case (x, y):
        print(f"The point is at ({x}, {y}).")
    case _:
        print("It's a different point.")
```
- **Output**: `The point is at the origin.`

### Features
- **Pattern Matching**: Matches not just values but also structures like tuples, lists, and even classes.
- **Wildcard `_`**: Acts as a catch-all case, similar to the `default` case in switch statements in other languages.
- **No Need for `break`**: Python automatically exits the `match` block after executing a matching case.

### More Complex Patterns

#### Matching with Conditions (Guards)
```python
x = 10

match x:
    case _ if x > 0:
        print("Positive number.")
    case _ if x < 0:
        print("Negative number.")
    case _:
        print("Zero.")
```
- **Output**: `Positive number.`

#### Destructuring in `match-case`
```python
person = {"name": "Alice", "age": 30}

match person:
    case {"name": "Alice", "age": age}:
        print(f"Alice is {age} years old.")
    case {"name": name, "age": 30}:
        print(f"{name} is 30 years old.")
    case _:
        print("Unknown person.")
```
- **Output**: `Alice is 30 years old.`