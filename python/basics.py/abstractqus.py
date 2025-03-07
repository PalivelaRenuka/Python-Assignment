from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    
    # Non-abstract method
    def speak(self):
        print("Animal speaks")

    # Abstract method
    @abstractmethod
    def sound(self):
        pass

# Subclass of Animal
class Dog(Animal):
    
    # Implementing the abstract method
    def sound(self):
        print("Dog barks")

# Creating an object of the child class
dog = Dog()

# 1. Accessing the non-abstract method from the parent class (Animal)
dog.speak()  # Calling non-abstract method

# 2. Accessing the abstract method (which is implemented in the child class)
dog.sound()  # Calling abstract method (implemented in Dog)

# 3. Creating an instance of the child class inside itself and calling the abstract method
class Dog2(Dog):
    def make_sound(self):
        # Instance of the child class inside itself
        dog_instance = Dog()
        dog_instance.sound()

dog2 = Dog2()
dog2.make_sound()

# 4. Creating an instance of the child class inside itself and calling the non-abstract method
class Dog3(Dog):
    def make_speak(self):
        # Instance of the child class inside itself
        dog_instance = Dog()
        dog_instance.speak()

dog3 = Dog3()
dog3.make_speak()
