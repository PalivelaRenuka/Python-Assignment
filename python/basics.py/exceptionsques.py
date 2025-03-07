'''#1st: Generate Arithmetic Exception without exception handling
x = 10
y = 0  # Zero causes the error
print(x / y)


#2nd-Handle the Arithmetic Exception using try-except block
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

    
#3rd Write a method that throws an exception and call it without try block
def raise_exception():
    raise ValueError("This is an exception")
raise_exception()  # No try block used


#4th Program with multiple except blocks
try:
    a = int("abc")  # Causes ValueError
except ZeroDivisionError:
    print("Zero Division Error Occurred")
except ValueError:
    print("Value Error Occurred")
except Exception:
    print("Some other error occurred")
#another model
a = [1, 2, 3]
try:
    print ("Second element = ",a[1])
    # Throws error since there are only 3 elements in array
    print ("Fourth element = ",a[3])   
except:
    print ("An error occurred")
print()
try:
    a = [1, 2]
    print(a[2])  # This will raise an IndexError
except IndexError:
    print("Index out of range!")
except Exception:
    print("Some other error occurred.")




#5th Throw an exception with your own message
raise Exception("This is my custom error message")

#6th Throw an exception with your own message
raise Exception("This is my custom error message")
#2nd type
class MyCustomException(Exception):
    pass

raise MyCustomException("This is my own exception type.")

#7th:  Program with finally block
try:
    num = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This is always executed.")

#8th : Generate Arithmetic Exception
print(10 / 0)

#9th : Generate FileNotFoundException
try:
    with open("noexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")

#10th :Generate ClassNotFoundException
try:
    import non_existent_module
except ModuleNotFoundError:
    print("The module could not be found.")

#11th :Generate IOException
import os
try:
    os.remove("noexistent_file.txt")  # Attempt to remove a non-existing file
except OSError as e:
    print(f"Error occurred: {e}")

'''
#12th:Generate NoSuchFieldException
class MyClass:
    def __init__(self):
        self.name = "Python"

obj = MyClass()
try:
    print(obj.age)  # This will cause AttributeError as 'age' doesn't exist
except AttributeError:
    print("The attribute does not exist.")