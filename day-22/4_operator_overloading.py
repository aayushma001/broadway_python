# operator overloading is a way of defining how an operator behaves in it's operation
# For example '+' in the integer operator behaves different from the string operation
a = 3
b = 2
print(a + b) # 5
m1 = "hello"
m2 ="world"
print(m1 + m2) # helloworld
# Such operator functions are defined in the built-in classes of python.These methods are called
# magic methods. __add__(), __mul__(), __gt__(), __lt__(), __sub__() etc. are the examples of magic methods

a = 1
b = 2
print(a.__add__(b)) # 3