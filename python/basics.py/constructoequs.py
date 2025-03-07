# 1. Write a class with a default constructor, one argument constructor, and two argument constructors
class Person:
    # Default constructor
    def __init__(self, name="Renuka", age=19):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")

# Instantiate the class and call all constructors
person1 = Person()  # Default constructor
person2 = Person("Ram")  # One argument constructor
person3 = Person("Shiv", 25)  # Two arguments constructor

print()

# 2. Call the constructors (both default and argument constructors) of superclass from a child class
class Animal:
    def __init__(self, name="Animal", sound="Generic Sound"):
        self.name = name
        self.sound = sound
        print(f"{self.name} makes a {self.sound} sound.")

class Dog(Animal):
    def __init__(self, name="Dog", sound="Bark"):
        super().__init__(name, sound)  # Calling constructor of superclass

# Instantiate the child class and call both constructors
dog1 = Dog()  # Calls constructor of Dog class and superclass Animal
dog2 = Dog("Bulldog", "Growl")  # Custom Dog with sound

print()

# 3. Apply private, public, protected, and default access modifiers to the constructor
class AccessModifierExample:
    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"
        print(f"Public: {self.public_var}, Protected: {self._protected_var}, Private: {self.__private_var}")

# Instantiate and show access to variables with different access modifiers
example = AccessModifierExample()
print(f"Public: {example.public_var}")  # Public is accessible
print(f"Protected: {example._protected_var}")  # Protected can be accessed but should not be changed directly
# The following will throw an error since private variables can't be accessed outside the class
# print(f"Private: {example.__private_var}")  # Uncommenting this will throw an AttributeError

print()

# 4. Program which illustrates the concept of attributes of a constructor
class Car:
    def __init__(self, brand="Unknown", model="Unknown", year=0):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Car brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Instantiate the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)
