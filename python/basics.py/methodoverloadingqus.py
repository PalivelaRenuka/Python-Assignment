# 1. Two Methods with the Same Name but Different Number of Parameters of the Same Type

def greet(name, times=1):  # Default parameter for 'times'
    for _ in range(times):
        print(f"Hello, {name}!")

# Calling the method with one parameter
greet("Renuka")

# Calling the method with two parameters
greet("Anjnai", 3)

print()

# 2. Two Methods with the Same Name but Different Number of Parameters of Different Data Types

def display(*args):
    if len(args) == 1 and isinstance(args[0], str):
        print(f"Hello, {args[0]}!")
    elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
        print(f"Age: {args[0]}, Name: {args[1]}")
    else:
        print("Invalid arguments!")

# Calling the method with one parameter (string)
display("Renuka")

# Calling the method with two parameters (int and string)
display(25, "Anjnai")

# Calling the method with invalid parameters
display("Hello", 123)

print()

# 3. Two Methods with the Same Name and Same Number of Parameters of the Same Type

# Methods with the same name and same number of parameters (same type)
def multiply(a, b):
    return a * b

# This will override the first 'multiply' method
def multiply(a, b):
    return a * b * 2

# Calling the multiply method
result = multiply(5, 3)
print(f"Result: {result}")
