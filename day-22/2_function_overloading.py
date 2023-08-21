# Function / Method overloading
# If the function define inside the class then the function is called the methods.
# Methods are called using object

# Function overloading is a term used in python if the same function definition is repeated multiple times
# Python doesn't support function overloading or method overloading


def addition(a, b):
    return a + b

def addition(a, b, c):
    return a + b + c

# r1 = addition(2, 6) # it raises error
# r2 = addition(3, 5, 8)
# print(r1)
# print(r2)

# Even we have defined teo addition functions with different numbers of parameters, but the atest one is
# only considered by python

# This problem in pyhton can be solved in a tricky way

def addition(a, b, c=0, **kwargs):
    return a+b+c+sum(kwargs.values())
r1 = addition(2, 3)
r2 = addition(2, 3, 4, p=2, q=3)
print(r1) # 5
print(r2) # 14

class A:
    def test_fxn(self):
        return "I'm learning python"
    def test_fxn(self):
        return "Hello World"
obj =A()
print(obj.test_fxn()) # Hello World

# Like function overloading, method overloading is also not possible in python
