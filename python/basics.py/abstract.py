'''
#1st question
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
dog = Dog()
dog.make_sound()
dog.move()
cat = Cat()
cat.make_sound()
cat.move()


#2nd question
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def dog_info(self):
        self.move()
dog = Dog()
dog.make_sound()
dog.dog_info()


# 3rd question
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def create_and_call(self):
        dog_instance = Dog()
        dog_instance.make_sound()
        dog_instance.move()
dog = Dog()
dog.create_and_call()
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def create_and_call(self):
        dog_instance = Dog()
        dog_instance.move()
dog = Dog()
dog.create_and_call()