#python #general_knowledge 

---

## Dynamic Typing vs. Static Typing

### Static Typing

- **Definition**: In statically typed languages, the data type of a variable is known and enforced at compile time.
- **Languages**: Java, C++, C#, Swift, etc.

#### Example: Java

- **Code**:
  ```java
  String myvar = "Hello";
  ```
- **Explanation**:
  - `myvar` is a variable of type `String`.
  - `Hello` is a string literal assigned to `myvar`.
  - The type of `myvar` (i.e., `String`) is associated with the variable.
  - Changing the type of `myvar` later will result in a type error:
    ```java
    myvar = 10; // Error: incompatible types
    ```

### Dynamic Typing

- **Definition**: In dynamically typed languages, the type of a variable is determined at runtime and can change over time.
- **Languages**: Python, JavaScript, Ruby, etc.

#### Example: Python

- **Code**:
  ```python
  myvar = "Hello"
  print(type(myvar))  # Output: <class 'str'>
  
  myvar = 10
  print(type(myvar))  # Output: <class 'int'>
  
  myvar = lambda x: x**2
  print(type(myvar))  # Output: <class 'function'>
  
  myvar = 3 + 4j
  print(type(myvar))  # Output: <class 'complex'>
  ```
- **Explanation**:
  - `myvar` initially references a string object with value `"Hello"`.
  - The type of the object `myvar` references can change:
    - From `str` to `int`, `function`, `complex`, etc.
  - `type(myvar)` returns the type of the current object `myvar` is referencing.

### Key Differences

- **Static Typing**:
  - Type is associated with the variable and enforced at compile time.
  - Example languages: Java, C++, Swift.

- **Dynamic Typing**:
  - Type is associated with the object and determined at runtime.
  - Example languages: Python, JavaScript.