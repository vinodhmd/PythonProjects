# 🐍 Python Features Short Notes (Cheat Sheet)

A quick-reference guide compiling the core Python features from your mastery series.

## 1. Basics & Data Types
- **Variables**: Containers for storing data (`int`, `float`, `str`, `bool`).
- **Typecasting**: Converting one data type to another (e.g., `int("10")`, `str(10)`, `float(10)`).
- **Format Specifiers**: Using f-strings (`f"Hello {name}"`) or format modifiers (`f"{value:.2f}"`) to inject variables into strings.

## 2. Operators & Math
- **Arithmetic**: `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `//` (floor division), `%` (modulo), `**` (exponent).
- **Logical**: `and`, `or`, `not` Used to combine conditional statements.
- **Membership**: `in`, `not in` Used to check if a sequence is present in an object.
- **Math Module**: Import `math` for advanced mathematical operations (`math.pi`, `math.sqrt()`, `math.ceil()`).
- **Random Module**: Import `random` for random number generation (`random.randint()`, `random.choice()`).

## 3. Control Flow
- **If Conditionals**: `if`, `elif`, `else` Used for decision making.
- **While Loops**: Execute a block of statements repeatedly as long as a condition is true.
- **For Loops**: Iterate over a sequence (list, tuple, dictionary, set, or string).

## 4. Collections
- **Lists (`[]`)**: Ordered, mutable collections of items. Can contain duplicates.
- **Dictionaries (`{k: v}`)**: Ordered (in modern Python), mutable collections of key-value pairs. Keys must be unique.
- **Strings**: Ordered, immutable sequences of characters. Supports highly useful methods like `.upper()`, `.replace()`, `.split()`.

## 5. Functions & Advanced Concepts
- **Functions (`def`)**: Reusable blocks of code that run when called. Can take arguments and return values.
- **Keyword Arguments**: Identifying function arguments by their parameter name `func(name="Alice")` rather than position.
- **Iterators & Iterables**: Objects that can be iterated upon. An iterable (like a list) contains an `__iter__()` method, which returns an iterator.
- **Modules**: Code libraries (a file containing Python code) that you can include in your project using `import`.

## 6. Scope & Object-Oriented Principles
- **LEGB Scope Rule**: The order Python resolves variables:
  - **L**ocal: Inside the current function.
  - **E**nclosing: Inside enclosing functions.
  - **G**lobal: At the top level of a module.
  - **B**uilt-in: Predefined Python names.
- **Static Methods**: Bound to the class and not the object (`@staticmethod`). Doesn't require a `self` parameter.
- **Extending/Inheritance**: Allowing one class to inherit the properties and methods of another.

## 7. Concurrency
- **Threading**: Using the `threading` module (`threading.Thread(target=func)`) to run code concurrently to improve execution time of I/O bound tasks.
