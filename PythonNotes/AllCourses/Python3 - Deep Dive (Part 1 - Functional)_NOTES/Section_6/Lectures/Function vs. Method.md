#python #general_knowledge 

---
## ⚙️ 1. **Function**

A **function** is a block of code that is **independent** and can be called anywhere in your program. Functions are defined using the `def` keyword and can be used to encapsulate reusable logic.

### **Example:**

```python
def my_function(x):
    return x * 2

print(my_function(5))  # Output: 10
```

- **Standalone**: Functions are not bound to any object or class.
- **Can be called anywhere**: Functions can be called using their name and passed arguments.

---

## 🛠️ 2. **Method**

A **method** is a **function that belongs to an object** (usually an instance of a class). It is called on an instance of a class and can access the data of that instance.

### **Example:**

```python
class MyClass:
    def my_method(self, x):
        return x * 2

obj = MyClass()
print(obj.my_method(5))  # Output: 10
```

- **Bound to an object**: Methods are defined inside a class and need to be called on an object (instance of the class).
- **`self` parameter**: Methods have access to the object’s data via the `self` parameter, which refers to the instance calling the method.

---

## 🔑 Key Differences

| Aspect               | Function                           | Method                             |
|----------------------|------------------------------------|------------------------------------|
| **Definition**        | Defined independently using `def`  | Defined within a class using `def` |
| **Call**              | Can be called directly             | Called on an instance (`object.method()`) |
| **Access to Data**    | Cannot access object data          | Can access and modify object data using `self` |
| **Type**              | Standalone function                | Function that is bound to a class |

---

### 🔍 Example Side-by-Side:

```python
# Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Function call

# Method
class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"

greeter = Greeter()
print(greeter.greet("Bob"))  # Method call on an object
```

---

## 📌 Summary

- **Functions** are independent blocks of reusable code, while **methods** are functions that belong to a class and work with object data.
- Methods use the `self` parameter to refer to the instance they are called on, while functions do not need this.