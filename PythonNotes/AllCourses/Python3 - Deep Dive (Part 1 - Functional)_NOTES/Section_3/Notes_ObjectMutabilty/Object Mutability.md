#python #general_knowledge 

---
## Object Mutability and Immutability

### Introduction

- **Object in Memory**:
  - An object in Python has a **type**, **internal data (state)**, and is located at a specific **memory address**.
  - **Modifying the internal state** of an object is known as **mutation**.

### Example: Bank Account Object

- **Initial State**:
  - **Variable**: `my_account`
  - **Object Type**: `BankAccount`
  - **Memory Address**: `1000`
  - **Attributes**: 
    - `account_number = 12345`
    - `balance = 150`

- **After Mutation**:
  - **Balance Modified**: `balance = 500`
  - **Memory Address**: `1000` (unchanged)

### Definitions

- **Mutable Objects**:
  - Objects whose internal state **can** be changed.
  
- **Immutable Objects**:
  - Objects whose internal state **cannot** be changed.

### Examples of Immutable Objects

- **Numbers**: 
  - Integers (`int`), floats (`float`), booleans (`bool`), complex numbers (`complex`).
  - **Note**: When a number's value is changed, the reference points to a **new object**.

- **Strings**: 
  - Strings cannot be modified after creation. A new string must be created for any change.

- **Tuples**:
  - Containers that cannot have elements added, removed, or replaced.

- **Frozen Sets**: 
  - Immutable versions of sets.

- **User-Defined Classes**:
  - Can be designed to be immutable by not allowing changes to the internal state.

### Examples of Mutable Objects

- **Lists**:
  - Can have elements added, removed, or replaced.

- **Sets**: 
  - Can be modified by adding or removing elements.

- **Dictionaries**: 
  - Can have keys and values added, removed, or changed.

- **User-Defined Classes**:
  - Can be designed to allow modifications to the internal state.

### A Subtle Point: Immutability in Collections

- **Tuple with Immutable Elements**:
  - **Example**: `t = (1, 2, 3)`
  - All elements are immutable, so the tuple is completely immutable.

- **Tuple with Mutable Elements**:
  - **Example**: 
    ```python
    a = [1, 2]
    b = [3, 4]
    t = (a, b)
    ```
  - The tuple itself is immutable, but the **elements** (`a` and `b`) are mutable.
  - **Mutation Example**:
    ```python
    a.append(3)
    ```
    - Now `t` appears different, but the tuple's immutability is not violated.

### Code Demonstrations

- **Lists**:
  ```python
  my_list = [1, 2, 3]
  my_list.append(4)
  # Memory address of my_list remains the same
  ```

- **List Reassignment**:
  ```python
  my_list_1 = [1, 2, 3]
  my_list_1 = my_list_1 + [4]
  # Memory address of my_list_1 changes
  ```

- **Dictionaries**:
  ```python
  my_dict = dict(key1=1, key2='a')
  my_dict['key3'] = 3.14
  # Memory address of my_dict remains the same
  ```

- **Tuples with Immutable Elements**:
  ```python
  t = (1, 2, 3)
  # IDs of elements inside the tuple are different and fixed
  ```

- **Tuples with Mutable Elements**:
  ```python
  t = ([1, 2], [3, 4])
  t[0].append(3)
  # Tuple t now contains ([1, 2, 3], [3, 4])
  ```

### Conclusion

- **Key Takeaway**:
  - **Immutability** refers to the inability to change the internal state of an object itself.
  - However, **mutable objects** within an immutable container (like a tuple) can still change.