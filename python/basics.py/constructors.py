## 1. Class with Default Constructor, One Argument Constructor, and Two Argument Constructor
class Student:
    # Default constructor
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
        print("Default Constructor Called")
    
    # One argument constructor
    def __init__(self, name):
        self.name = name
        self.age = 0
        print("One Argument Constructor Called")
    
    # Two argument constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Two Argument Constructor Called")
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Instantiate and call the constructor (Python only uses the last defined __init__)
student1 = Student("Renuka", 19)  # Calls the two-argument constructor
student1.display()

# 2. Call the constructors (both default and argument constructors) of superclass from a child class
class Parent:
    def __init__(self, name="Parent"):
        self.name = name
        print(f"Parent Constructor Called: {self.name}")

class Child(Parent):
    def __init__(self, name="Child", age=10):
        super().__init__(name)  # Calls Parent constructor
        self.age = age
        print(f"Child Constructor Called: Age = {self.age}")

# Instantiate the Child class
child = Child("Shiv", 25)

print()

# 3. Apply private, public, protected, and default access modifiers to the constructor
class AccessModifiers:
    def __init__(self):
        self.public_var = "Public"  # Public variable
        self._protected_var = "Protected"  # Protected variable (convention)
        self.__private_var = "Private"  # Private variable
    
    def display(self):
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")

# Instantiate the class
access = AccessModifiers()
access.display()

# Accessing private variable (will raise an error)
# print(access.__private_var)  # Uncommenting this line will raise an AttributeError

print()

# 4. Program illustrating the concept of attributes in a constructor
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute: name
        self.age = age  # Attribute: age
        print(f"Constructor with attributes: Name = {self.name}, Age = {self.age}")

# Instantiate the class
person = Person("Ram", 25)
