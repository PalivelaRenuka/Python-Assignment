'''#1st question
class A:
    def __init__(self):
        self.__private_field = "Private Field in A"  
    def __private_method(self):  
        print("Private method in A")
    
    def public_method(self):
        print("Public method in A")

# Subclass B
class B(A):
    def try_access_private(self):
        pass
a = A()
print(a._A__private_field)  
a.public_method()           
a._A__private_method()     

b = B()
b.try_access_private()



# 2nd -Protected fields and methods
# Class with protected fields and methods
class A:
    def __init__(self):
        self._protected_field = "Protected Field in A"  # Protected field
    
    def _protected_method(self):
        print("Protected method in A")


# In the same package (Same File)
class B:
    def access_protected(self):
        a = A()
        print(a._protected_field)  # Access protected field
        a._protected_method()      # Access protected method


# Different Package (Another File)
class C(B):
    def access_protected_in_child(self):
        b = B()
        b.access_protected()       # Access protected from parent class


# Driver Code
b = B()
b.access_protected()

c = C()
c.access_protected_in_child()

'''
# 3rd question Public Fields and Methods Output:
# Class with public fields and methods
# Class with public fields and methods
class A:
    def __init__(self):
        self.public_field = "Public Field in A"  # Public field
    
    def public_method(self):
        print("Public method in A")


# Driver Code
a = A()
print(a.public_field)   # Access public field
a.public_method()       # Access public method
