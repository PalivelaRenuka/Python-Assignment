#1st -Define a static variable and access it through a class
class MyClass:
    static_var = 10  
print("Access through class:", MyClass.static_var)

#2ndDefine a static variable and access it through an instance
class MyClass:
    static_var = 10  
obj = MyClass()
print("Access through instance:", obj.static_var)

#3rd Define a static variable and change it within an instance
class MyClass:
    static_var = 10  
obj1 = MyClass()
obj1.static_var = 20 
print("Static variable from class:", MyClass.static_var)  
print("Modified static variable in obj1:", obj1.static_var)

#4th- Define a static variable and change it within the class
class MyClass:
    static_var = 10  
MyClass.static_var = 30  
print("Modified static variable in class:", MyClass.static_var)