#python #general_knowledge 

---
# Function Arguments and Mutability

## Introduction
- Welcome to this video on function arguments and mutability.
- We'll explore how variables might be affected when passed to functions and discuss the concept of mutability and immutability.

## Review of Immutability
- **Immutable Objects**: In Python, strings are immutable.
  - Once created, a string cannot be changed.
  - Example:
    ```python
    myvar = "Hello"
    ```
    - If `myvar` points to memory address 1000 containing `"Hello"`, the only way to change `myvar` is to point it to a different memory address.
    - The object at memory address 1000 cannot be altered because strings are immutable.

## Immutable Objects and Function Safety
- **Safety of Immutable Objects**: Immutable objects are generally safe from unintended side effects when passed to functions.
- Example with a string:
  - Function `process(s)` concatenates `"World"` to `s`.
  - If `myvar = "Hello"` and `process(myvar)` is called:
    - `myvar` points to memory address 1000 containing `"Hello"`.
    - The function receives this reference but creates a new string `"HelloWorld"` at a different memory address, leaving `myvar` unchanged.
  - Printing `myvar` after calling the function will still output `"Hello"`.
- **Conclusion**: This demonstrates the safety of immutable objects—they cannot be altered by functions that receive them as arguments.

## Mutable Objects and Function Side Effects
- **Mutable Objects**: Mutable objects, unlike immutable ones, are not safe from unintended side effects.
- Example with a list:
  - Function `process(lst)` appends `100` to `lst`.
  - If `mylist = [1, 2, 3]` and `process(mylist)` is called:
    - `mylist` points to memory address 1000 containing `[1, 2, 3]`.
    - The function appends `100` directly to this list, modifying the object at memory address 1000.
  - Printing `mylist` after calling the function will output `[1, 2, 3, 100]`.
- **Conclusion**: This demonstrates that mutable objects can be altered by functions that receive them as arguments.

## Special Case: Mutable Elements in Immutable Containers
- **Immutable Containers**: Immutable containers like tuples can hold mutable elements, leading to potential changes even if the container itself cannot be altered.
- Example with a tuple:
  - Function `process(t)` appends `3` to the first element, assuming it’s a list.
  - If `mytuple = ([1, 2], "A")` and `process(mytuple)` is called:
    - `mytuple` points to a memory address containing `([1, 2], "A")`.
    - The function appends `3` to the list `[1, 2]`, modifying it to `[1, 2, 3]`.
  - Printing `mytuple` after calling the function will output `([1, 2, 3], "A")`.
- **Conclusion**: Even though the tuple is immutable, its mutable element (the list) can be changed.

## Conclusion
- **Summary**: Immutable objects are generally safe from modification when passed to functions, but mutable objects are not.
- Even immutable containers like tuples can have their mutable elements modified.
- Understanding mutability and how it interacts with function arguments is crucial for writing safe and predictable code.