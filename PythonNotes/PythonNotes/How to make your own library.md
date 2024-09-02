#python #libraries #modules 
## Making Your Own Libraries
- **Creating a Library**: Define functions in a `.py` file that can be imported into other Python scripts.
- **Example**:
  ```python
  # sayings.py
  def hello(name):
      print(f"hello, {name}")

  def goodbye(name):
      print(f"goodbye, {name}")
  ```
- **Using Your Library**: 
  ```python
  # say.py
  from sayings import goodbye
  goodbye("Alice")
  ```