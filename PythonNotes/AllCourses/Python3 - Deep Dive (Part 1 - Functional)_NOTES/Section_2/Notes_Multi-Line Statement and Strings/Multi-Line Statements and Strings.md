#python #summary #general_knowledge 

---

### Multi-line Statements and Multi-line Strings in Python

#### **Overview**
- Python code is written as physical lines in a text file, which the Python compiler then processes to create logical lines of code. These logical lines are then tokenized for execution.
- It's important to distinguish between physical newline characters (actual line breaks) and logical newline tokens (used by Python to identify the end of a statement).

#### **Multi-line Statements**
- **Implicit Line Continuation:** 
  - Python allows you to split long expressions across multiple lines using implicit line continuation. This works when using brackets (`[]`, `{}`, `()`) in lists, tuples, dictionaries, set comprehensions, function arguments, etc.
  - Example:
    ```python
    my_list = [
        1,  # item one
        2,  # item two
        3   # item three
    ]
    ```
  - Python will automatically combine these lines into a single logical line.

- **Explicit Line Continuation:**
  - When you need to split statements that are not within brackets across multiple lines, use the backslash `\` as a continuation character.
  - Example:
    ```python
    if (a > 5 and b > 10 and 
        c > 20):
        print("Yes")
    ```
  - Comments cannot be placed after a backslash; they must be on a separate line.

#### **Multi-line Strings**
- Multi-line strings can be created using triple quotes (`'''` or `"""`).
- These strings preserve all whitespace, including newlines, tabs, and spaces.
- Example:
  ```python
  multi_line_str = '''This is a string
  that spans multiple
  lines.'''
  ```
  - When printed, it will appear exactly as it is formatted, with the included newlines.

#### **Important Notes**
- Multi-line strings should not be confused with comments. Although they can be used similarly to comments (e.g., docstrings), they are still part of the code and get compiled, unlike comments which are ignored by Python.

#### **Practical Tips**
- Use multi-line formatting for better readability, especially in complex expressions or when defining functions with many parameters.
- Be careful with indentation in multi-line strings, especially within functions, as it will affect how the string is displayed when printed.