#python #coding-lesson 

---
### Decimals in Python: Understanding the `decimal` Module

#### 1. **Importing the `decimal` Module**
   - To work with decimals in Python, you first need to import the `decimal` module and specifically the `Decimal` class.
   - Example:
     ```python
     import decimal
     from decimal import Decimal
     ```
   - You can refer to the `Decimal` class directly after importing, avoiding the need to use `decimal.Decimal`.

#### 2. **Understanding Context in Decimals**
   - **Context**: Specifies certain properties that affect how decimals operate, particularly precision and rounding.
   - Retrieve the current default context using:
     ```python
     decimal.getcontext()
     ```
   - **Default Context Example**:
     - **Precision**: Default is 28.
     - **Rounding**: Default is "ROUND_HALF_EVEN".

   - Accessing specific context values:
     ```python
     # Get precision
     precision = decimal.getcontext().prec
     
     # Get rounding
     rounding = decimal.getcontext().rounding
     ```

#### 3. **Modifying the Global Context**
   - You can change the global precision and rounding:
     ```python
     # Set precision to 6
     decimal.getcontext().prec = 6
     
     # Change rounding mode
     decimal.getcontext().rounding = decimal.ROUND_HALF_UP
     ```
   - To avoid repeatedly calling `decimal.getcontext()`, assign it to a variable:
     ```python
     global_context = decimal.getcontext()
     ```

#### 4. **Local Contexts**
   - **Local Context**: Used for temporarily changing the decimal context within a specific block of code.
   - **Creating a Local Context**:
     ```python
     with decimal.localcontext() as local_ctx:
         local_ctx.prec = 6
         local_ctx.rounding = decimal.ROUND_HALF_UP
     ```
   - **Key Points**:
     - **Local context** is created using `decimal.localcontext()`, which returns a context manager.
     - Context managers clean up after themselves; when the `with` block ends, the local context is disposed of.
     - Inside the `with` block, the local context overrides the global context.

   - **Difference between Global and Local Contexts**:
     - `decimal.getcontext()` returns the current context, which could be the global or local context depending on where it's called.

#### 5. **Rounding Mechanisms**
   - Example of using `ROUND_HALF_UP`:
     ```python
     x = Decimal('1.25')
     y = Decimal('1.35')
     
     print(round(x, 1))  # Outputs 1.3
     print(round(y, 1))  # Outputs 1.4
     ```
   - **Inside Local Context**:
     - Using `ROUND_HALF_UP` would round `.5` up, as seen in the examples above.
   - **Outside Local Context (Global Context)**:
     - Default rounding (`ROUND_HALF_EVEN`) would round `1.25` to `1.2`.

#### 6. **Practical Example: Global vs Local Context**
   - **Module Level (Global Context)**:
     - Default rounding: `ROUND_HALF_EVEN`
     - Example:
       ```python
       # This will round 1.25 to 1.2
       print(round(Decimal('1.25'), 1))  # Outputs 1.2
       ```

   - **Inside Local Context**:
     - Custom rounding: `ROUND_HALF_UP`
     - Example:
       ```python
       with decimal.localcontext() as local_ctx:
           local_ctx.rounding = decimal.ROUND_HALF_UP
           print(round(Decimal('1.25'), 1))  # Outputs 1.3
       ```