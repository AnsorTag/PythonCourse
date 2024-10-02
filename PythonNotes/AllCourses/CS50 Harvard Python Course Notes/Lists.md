#python #data-structures 

## Python Lists

### Overview
- **List**: An ordered, mutable collection of elements.
- **Syntax**: Defined using square brackets `[]`.

### Features
- **Dynamic Sizing**: Lists can grow or shrink as needed.
- **Heterogeneous Elements**: Can contain elements of different data types (e.g., integers, strings, other lists).
- **Indexing**: Access elements by their position (0-based index).
- **Slicing**: Extract sublists using `start:stop:step` syntax.

### Common Operations
```python
my_list = [1, 2, "apple", [3, 4]]

# Accessing elements
first_element = my_list[0]  # Outputs: 1
nested_element = my_list[3][1]  # Outputs: 4

# Modifying elements
my_list[1] = "banana"

# Adding elements
my_list.append(5)
my_list.insert(1, "orange")

# Removing elements
my_list.remove("apple")
last_item = my_list.pop()  # Removes and returns the last item
```

### Built-in Methods
- `.append(x)`: Add `x` to the end of the list.
- `.insert(i, x)`: Insert `x` at position `i`.
- `.remove(x)`: Remove the first occurrence of `x`.
- `.pop(i)`: Remove and return the item at position `i` (last item if `i` is omitted).
- `.reverse()`: Reverse the order of the list.
- `.sort()`: Sort the list in ascending order.

### Example
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # ["apple", "banana", "cherry", "orange"]
fruits[1] = "kiwi"  # ["apple", "kiwi", "cherry", "orange"]
```

---

