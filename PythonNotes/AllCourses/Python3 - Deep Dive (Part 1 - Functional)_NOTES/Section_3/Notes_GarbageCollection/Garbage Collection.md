#python #general_knowledge 

---
## Garbage Collection

### Reference Counting
- **Definition**: Python tracks the number of references to each object.
- **Mechanism**:
  - Each object has a reference count.
  - When the reference count drops to zero, the object is destroyed, and memory is reclaimed.

### Circular References
- **Problem**: When two or more objects reference each other, creating a loop, reference counting fails to reclaim the memory.
- **Example**:
  ```python
  class A:
      def __init__(self):
          self.b = B(self)
  
  class B:
      def __init__(self, a):
          self.a = a
  ```
  - **Circular Reference**: `A` -> `B` -> `A`.

### Garbage Collection
- **Purpose**: Handles circular references and frees memory that cannot be reclaimed by reference counting alone.
- **Module**: `gc` (Garbage Collector module)
  - **Control**:
    - **Disable GC**: `gc.disable()`
    - **Manual Collection**: `gc.collect()`
  - **Default**: Enabled

### Interacting with the Garbage Collector
- **Checking Object Existence**:
  ```python
  def object_by_id(obj_id):
      for obj in gc.get_objects():
          if id(obj) == obj_id:
              return "Object exists"
      return "Not found"
  ```
- **Example Code**:
  ```python
  import ctypes
  import gc

  def ref_count(address):
      return ctypes.c_long.from_address(address).value

  class A:
      def __init__(self):
          self.b = B(self)
          print(f"A: {hex(id(self))}, B: {hex(id(self.b))}")

  class B:
      def __init__(self, a):
          self.a = a
          print(f"B: {hex(id(self))}, A: {hex(id(self.a))}")

  # Disable garbage collector
  gc.disable()

  my_var = A()
  a_id = id(my_var)
  b_id = id(my_var.b)

  print("Reference count for A:", ref_count(a_id))
  print("Reference count for B:", ref_count(b_id))

  print(object_by_id(a_id))
  print(object_by_id(b_id))

  # Removing reference to my_var
  my_var = None

  # Force garbage collection
  gc.collect()

  print(object_by_id(a_id))
  print(object_by_id(b_id))
  ```

### Important Notes
- **Memory Addresses**: 
  - After objects are collected, their memory addresses may be reused or become unreliable.
  - Caution is needed when working with memory addresses for debugging purposes.
- **Version Compatibility**:
  - Issues with destructors in circular references are resolved in Python 3.4 and above.