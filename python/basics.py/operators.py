'''def arithmetic_operations(a, b):
    operations = {
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else "Undefined (division by zero)"
    }
    
    for op, result in operations.items():
        print(f"{op}: {result}")

# Example
arithmetic_operations(10, 5)
# another model for arthemetic operations
# Performing arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = float(a) + float(b)  # Addition
sub = float(a) - float(b)  # Subtraction
mul = float(a) * float(b)  # Multiplication
div = float(a) / float(b) if b != 0 else "Undefined (division by zero)"  # Division with zero check

# Printing the results
print(f"Addition of {a} and {b} = {add}")
print(f"Subtraction of {a} and {b} = {sub}")
print(f"Multiplication of {a} and {b} = {mul}")
print(f"Division of {a} by {b} = {div}")

# 2nd question
# increment and decrement
n = int(input())
# Increment operation
n += 1
print("After increment:", n)
# Decrement operation
n -= 1
print("After decrement:", n)

#3rd question
a = int(input())  
b = int(input())  
if a == b:
    print("Equal")
else:
    print("Not Equal")
#4th question
a = int(input())  
b = int(input())  

print(a < b)    # Less than
print(a <= b)   # Less than or equal to
print(a > b)    # Greater than
print(a >= b)   # Greater than or equal to'''
#5th question
a = int(input())  
b = int(input())  
print("Smaller:", min(a, b))  
print("Larger:", max(a, b))



