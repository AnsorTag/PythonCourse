#python #data-structures

Almost same as Maps in Javascript, key:value pairs

## Python Dictionaries

### Overview
- **Dictionary (dict)**: A collection of key-value pairs where each key is unique.
- **Syntax**: Defined using curly braces `{}` with key-value pairs inside.

### Features
- **Key-Value Pairs**: Keys map to specific values.
- **Unique Keys**: Each key in a dictionary must be unique.
- **Mutable**: You can add, modify, or delete key-value pairs.
- **Unordered**: Insertion order is maintained (from Python 3.7+).

### Common Operations
```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
name = my_dict["name"]  # Outputs: "Alice"

# Modifying values
my_dict["age"] = 31

# Adding key-value pairs
my_dict["country"] = "USA"

# Removing key-value pairs
del my_dict["city"]

# Safe access
age = my_dict.get("age", "Not found")  # Outputs: 31
```

### Built-in Methods
- `.keys()`: Returns a view object of all keys.
- `.values()`: Returns a view object of all values.
- `.items()`: Returns a view object of all key-value pairs.
- `.get(key, default)`: Returns the value for `key` if `key` is in the dictionary, else returns `default`.
- `.pop(key)`: Removes and returns the value for `key`.

### Example
```python
person = {
    "name": "Bob",
    "age": 25,
    "job": "Developer"
}
person["age"] = 26  # Updates age to 26
person["city"] = "San Francisco"  # Adds a new key-value pair
```