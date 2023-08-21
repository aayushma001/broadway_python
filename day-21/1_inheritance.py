# inheritance is the transfer of properties and methods to the child class
# from the parent class
# Types of inheritance in python
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel
# 4. Hierarchical
# 5. Hybrid

class Vehicle:
    engine_type = "petrol_engine"

class Bike(Vehicle): # child
    wheels = "two"
class Car(Vehicle):# child because vehicle is kept inside bracket we can also make further child
    wheels = "four"





car = Car()
print(car.engine_type) # petrol_engine
print(car.wheels) # four


# Single inheritance
class A:
    pass
class B(A):
    pass

# Multiple inheritance
class A:
    pass
class B:
    pass

class C(A, B): #Multiple inheritance
    pass

# Multilevel inheritance
class A:
    pass

class B(A):
    pass
class C(B):
    pass

# Hierarchical inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

# mro => mro stands for method resolution order. it is the order in which attributes in inheritance
# is searched
# hybrid inheritance
class A:
    pass

class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E(D):
    pass

e = E()
print(E.mro())

