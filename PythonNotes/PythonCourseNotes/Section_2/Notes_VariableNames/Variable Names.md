#python #general_knowledge

---
### Key Points on Variable Names and Conventions:

1. **Case Sensitivity**:
   - Identifiers in Python are case-sensitive. For instance, `myVar` and `MyVar` are different identifiers.
   - While technically possible, it's not recommended to use identifiers that differ only by case, as it can be confusing.

2. **Rules for Variable Names**:
   - **Must Start With**: An identifier must start with either a letter (A-Z, a-z) or an underscore (_).
   - **Followed By**: After the initial character, an identifier can contain letters, digits (0-9), or underscores.
   - **Cannot Start With a Digit**: An identifier cannot begin with a digit.
   - **Examples of Legal Names**: `var`, `myVar`, `index_1`, `_var`, `__var__`.

3. **Reserved Words**:
   - Identifiers cannot be Python reserved words (keywords) like `if`, `else`, `while`, `for`, `def`, etc.

4. **Naming Conventions**:
   - **Single Underscore Prefix (_var)**: This indicates that the variable is intended for internal use. It’s a convention to signal that it's private, though Python doesn’t enforce privacy.
   - **Double Underscore Prefix (__var)**: Triggers name mangling, which helps avoid name clashes in inheritance scenarios.
   - **Double Underscore Surrounding (__var__)**: Reserved for special use in Python’s system-defined names. Avoid creating such names yourself.

5. **PEP 8 Naming Conventions**:
   - **Packages**: Should have short, all-lowercase names, ideally without underscores. E.g., `utilities`.
   - **Modules**: Short, all-lowercase names, underscores are allowed. E.g., `db_utils`.
   - **Classes**: Use CapWords or UpperCamelCase, where each word starts with a capital letter, no underscores. E.g., `BankAccount`.
   - **Functions & Variables**: Use snake_case, which is lowercase words separated by underscores. E.g., `open_account`, `account_id`.
   - **Constants**: Should be all uppercase letters, with words separated by underscores. E.g., `MIN_APR`.

6. **Consistency and Best Practices**:
   - PEP 8 is a guideline to make your code readable and standardized, which helps others (and yourself) understand the structure of your code more easily.
   - You can deviate from these conventions when necessary, but consistency within your codebase is key.

7. **PEP 8 Style Guide**:
   - You can find more details by searching for "PEP 8" online. It’s a relatively short and informative document that outlines these conventions and more.