# 🚀 OOP Concepts in Python

This repository demonstrates core **Object-Oriented Programming (OOP)** concepts in Python with practical examples.

---

## 📁 Project Structure

### 1. Classes and Methods

**File:** `atm.py`
Demonstrates how to define classes, create objects, and implement instance methods to model real-world behavior.

---

### 2. Magic Methods (Dunder Methods)

**File:** `fraction.py`

Magic methods (also known as _dunder methods_) are special methods in Python that start and end with double underscores (`__`).
They allow objects to interact with built-in operators and functions.

### Example:

- `__add__` → `+`
- `__sub__` → `-`
- `__mul__` → `*`

```python
f1 + f2  # Internally calls f1.__add__(f2)
```

You can explore available magic methods using:

```python
dir(int)
```

---

## 🧠 Variables in Python Classes

### Instance Variables

- Defined per object
- Value differs for each instance

### Class (Static) Variables

- Shared across all objects
- Example: IFSC code for a bank branch

---

## 🔗 Class Relationships

Real-world applications require multiple interacting classes.

### Types of Relationships:

- **Aggregation (Has-A)**
  Example: `Customer` has an `Address`

- **Inheritance (Is-A)**
  Example: `Smartphone` is a `Product`

---

## 🔄 Polymorphism (Multiple Forms)

Polymorphism allows the same operation to behave differently.

### Types:

- Method Overriding
- Method Overloading _(handled via default arguments in Python)_
- Operator Overloading _(via magic methods)_

---

## 🧬 Types of Inheritance

1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance _(one parent, multiple children)_
4. Multiple Inheritance _(multiple parents, one child)_
5. Hybrid Inheritance _(combination of above)_

---

## 📌 Summary

This project helps in understanding:

- Core OOP principles in Python
- Real-world class design
- Operator overloading using magic methods
- Relationships between classes

---
