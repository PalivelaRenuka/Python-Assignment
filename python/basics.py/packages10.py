#1 
class ClassOne:
    def __init__(self):
        print("Constructor of ClassOne")

    def show(self):
        print("Method of ClassOne")
#1.1
class ClassTwo:
    def __init__(self):
        print("Constructor of ClassTwo")

    def display(self):
        print("Method of ClassTwo")

# Import classes from package
import sys
sys.path.append('./')  # Add the current directory to Python path


from my_package.class1 import ClassOne
from my_package.class2 import ClassTwo

# Create objects and call methods
obj1 = ClassOne()
obj1.show()

obj2 = ClassTwo()
obj2.display()
