# oop-concepts-python
This project helps to understand all the basic concepts of object-oriented programming with the Python programming language. Each concept consists of a separate simple example file. 

---
## 🧱 1. Class and Object
**File:** `class_object.py`

### 📘 What is the concept?
A **class** is a blueprint for creating **objects**. It encapsulates (express the essential features of ) data for the object and defines behaviors (methods) that operate on the data.

### ✅ How it is used in the example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says woof!"
```
- `Dog` is a class.
- `dog = Dog("Buddy", 5)` creates an object.
- The method `speak()` defines a behavior of the object.

---

## 🧬 2. Inheritance
**File:** `inheritance.py`

### 📘 What is the concept?
**Inheritance** allows one class (child) to acquire properties and methods of another class (parent). It promotes reusability and hierarchy.

### ✅ How it is used in the example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
```
- `Dog` and `Cat` inherit from `Animal`.
- They reuse `Animal`'s `__init__` and define their own `speak()`.

---

## 🔒 3. Encapsulation
**File:** `encapsulation.py`

### 📘 What is the concept?
**Encapsulation** is the bundling of data and methods that act on that data, restricting direct access to internal variables.

### ✅ How it is used in the example:
```python
class Person:
    def __init__(self, name, age):
        self.__age = age

    def get_age(self):
        return self.__age
```
- `__age` is private.
- Access is controlled using `get_age()` and `set_age()`.

---

## 🎭 4. Abstraction
**File:** `abstraction.py`

### 📘 What is the concept?
**Abstraction** means hiding complex implementation details and showing only essential features. Python uses abstract base classes (ABCs) to define required methods.

### ✅ How it is used in the example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```
- `Shape` is an abstract class.
- `Rectangle` must implement the `area()` method.

---

## 🔁 5. Polymorphism
**File:** `polymorphism.py`

### 📘 What is the concept?
**Polymorphism** allows different classes to be used interchangeably if they implement the same method or interface.

### ✅ How it is used in the example:
```python
class Bird:
    def fly(self):
        print("Flying in the sky")
```
- Both `Bird` and `Airplane` implement `fly()`.
- Function `let_it_fly(obj)` works on any object with a `fly()` method.

---

## 🚗 6. Composition
**File:** `composition.py`

### 📘 What is the concept?
**Composition** means building classes using other classes by including them as attributes, forming a "has-a" relationship.

### ✅ How it is used in the example:
```python
class Car:
    def __init__(self):
        self.engine = Engine()
```
- A `Car` has an `Engine`.
- `Car.start()` calls `Engine.start()` internally.

---

## 🧾 7. Dataclasses
**File:** `dataclass_example.py`

### 📘 What is the concept?
**Dataclasses** are a Pythonic way to reduce boilerplate in classes that are mainly used to store data.

### ✅ How it is used in the example:
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```
- Python auto-generates `__init__`, `__repr__`, etc.
- We easily create and print data objects.

---

## 📚 8. Abstract Base Classes (ABCs)
**File:** `abc_example.py`

### 📘 What is the concept?
An **abstract base class** enforces that subclasses implement certain methods. It defines an interface contract.

### ✅ How it is used in the example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```
- `Animal` is abstract.
- `Dog` implements `sound()`, or else Python will throw an error.

---

## ✅ Getting Started
1. Clone the repo or copy the files.
2. Run any example with `python filename.py`.
3. Explore and extend each concept.

---

## 📎 References
- [Python Official Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python OOP Guide](https://realpython.com/python3-object-oriented-programming/)

---

Feel free to star ⭐ and fork 🍴 this repository if you found it helpful!
