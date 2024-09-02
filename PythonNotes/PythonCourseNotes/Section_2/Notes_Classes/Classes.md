#python #flow-control 

---

## Python Classes and Properties

### Special Methods in Python Classes

- **Comparison Methods**: 
  - If `__gt__` (greater than) is not implemented, Python will try `__lt__` (less than) to compare objects.
  - However, `<=` (less than or equal to) and `>=` (greater than or equal to) will not work unless explicitly implemented.

### Properties in Python

- **Direct Access**:
  - Directly accessing and modifying properties like `width` and `height` can lead to issues. For example, setting `R1.width = -100` is allowed, but it doesn’t make sense to have a negative width or height for a rectangle.

- **Encapsulation**:
  - To prevent this, use getter and setter methods.
  - In Python, private variables are not truly private. Instead, we use a naming convention: prefixing with an underscore (e.g., `_width`) to indicate they should not be accessed directly.

### Getters and Setters

#### Example without Getter/Setter
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

R1 = Rectangle(10, 20)
R1.width = -100  # This is allowed but doesn't make sense.
```

#### Implementing Getters and Setters
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        self._width = width

R1 = Rectangle(10, 20)
R1.set_width(-10)  # Raises ValueError
```

### Pythonic Way: Using `@property`

- **Using `@property` Decorator**:
  - Allows you to keep using `R1.width` without breaking compatibility while still applying logic when getting or setting values.

#### Example
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        self._width = width

R1 = Rectangle(10, 20)
print(R1.width)  # Uses the getter
R1.width = -10  # Raises ValueError
```

### Key Points

- **Backward Compatibility**:
  - You can add getters and setters later using `@property` without breaking existing code that uses direct access.
  
- **No Need for Immediate Getters/Setters**:
  - In Python, it’s common to start with public attributes and only add getters/setters if necessary.

- **Usage of `@property`**:
  - `@property` makes it possible to transition from public attributes to getters/setters smoothly.

### Internal vs External Access

- **Internal Access**:
  - Inside the class, you can still use `self._width` directly if you need to bypass the getter/setter logic, though this is not usually recommended.

- **Initialization**:
  - You can use the setters in the `__init__` method to enforce validation rules from the start.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width  # Calls the setter, enforcing positive values
        self.height = height

    # Properties and methods as above
```