## OOP Concepts in Python

1. **Classes and Methods**  
   **File:** `atm.py`

2. **Magic Methods (`__add__`, `__sub__`, `__mul__`)**  
   **File:** `fraction.py`

   Magic methods (also called _dunder methods_) are special methods in Python that start and end with double underscores.  
   They allow you to define how objects behave with built-in operations like `+`, `-`, `*`, etc. :contentReference[oaicite:0]{index=0}

   👉 Refer to the official Python documentation or explore using:

   ```python
   dir(int)
   ```

3. **Instance variable** is for which the value is different for different objects
   Class variable / Static variable ( ex Ifsc code is same one bank branch ) is value which is same for different objects

4. Class RelationShips:
   Aggregation: _Has-A_
   Inheritance: _Is-A_
   class relationship is needed because real applications use different classes not one class
   inheritance example : Product <- Smartphone
   Aggregation example : customer -> Addresss
