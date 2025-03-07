# 1. Print your name
print("Renuka")

# 2. Single-line and multi-line comments
# This is a single-line comment
'''
This is a 
multi-line comment
'''

# 3. Define variables for different data types and print them
integer_var = 10
boolean_var = True
char_var = 'A'  # Python does not have a separate char type, it uses strings of length 1
float_var = 10.5
double_var = 20.123456789  # Python's float is equivalent to double in other languages

print("Integer:", integer_var)
print("Boolean:", boolean_var)
print("Character:", char_var)
print("Float:", float_var)
print("Double:", double_var)

# 4. Local and Global variable with the same name
global_var = "I am a global variable"

def variable_scope():
    global_var = "I am a local variable"
    print("Inside function:", global_var)

variable_scope()
print("Outside function:", global_var)
a=-5
print("Type of a: ",type(a))
a=5
a = 5
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a) 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 4      #Value of 'a' modified
    print('Inside h() : ', a)  
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)