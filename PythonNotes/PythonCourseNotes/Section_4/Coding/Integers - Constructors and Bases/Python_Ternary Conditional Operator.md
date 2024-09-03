#python #coding-lesson 

---

### Python: Ternary Conditional Operator

**Syntax:**
```python
x = a if condition else b
```

**Description:**
The ternary conditional operator evaluates `condition` and assigns `a` to `x` if the condition is `True`. Otherwise, it assigns `b` to `x`.

**Example:**
```python
sign = -1 if number < 0 else 1
```
- **`condition`:** `number < 0`
- **`a`:** `-1`
- **`b`:** `1`

**Explanation:**
- If `number` is less than 0, `sign` is set to `-1`.
- If `number` is 0 or positive, `sign` is set to `1`.

**Usage:**
- Provides a concise way to handle conditional assignments.
- Useful for simple conditional logic within expressions.