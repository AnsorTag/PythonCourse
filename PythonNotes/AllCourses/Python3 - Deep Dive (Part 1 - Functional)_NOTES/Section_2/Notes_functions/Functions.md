#python #flow-control 

---
### Functions in Python

- **Built-in Functions**: Python provides many functions by default, like `len()`. Additional functions can be imported from modules, e.g., `from math import sqrt`.

- **Defining Functions**: Use the `def` keyword.
  ```python
  def func1():
      print("Running func1")
  ```

  - Call a function using its name followed by parentheses: `func1()`.
  - Functions can take parameters:
    ```python
    def multiply(a, b):
        return a * b
    ```

- **Polymorphism**: Python functions are polymorphic. They can operate on different data types depending on the input:
  ```python
  multiply(2, 3)       # Returns 6
  multiply("a", 3)     # Returns 'aaa'
  ```

- **Function Objects**: Functions are objects and can be assigned to variables:
  ```python
  my_func = multiply
  result = my_func(2, 3)
  ```

- **Lambda Functions**: An anonymous function that is defined using the `lambda` keyword.
  ```python
  square = lambda x: x ** 2
  square(4)  # Returns 16
  ```

  - Lambdas are often used for short, throwaway functions.

- **Order of Definition**: Functions must be defined before they are invoked, but Python doesn't execute the function body until it’s called, so you can reference functions that are defined later in the code.