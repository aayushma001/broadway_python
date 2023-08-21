# OOP stands for object-oriented programming
# It is the way of the modelling the real world problems into a program.
# It has two important components;Class and objects

# Classes are the blueprints of an object
# objects are the instance of the class

# Major features of object-oriented programming
# 1. Inheritance
# 2. encapsulation
# 3. Polymorphism
# 4. abstraction

class Vehicle:
    category = "car" # This is a class attribute

v = Vehicle()  # This is creating an object of class Vehicle
print(v.category) # Car # This is getting class attribute using an object
print(Vehicle.category) # Car # This is getting class attribute using a class

v.category = "Truck"
print(v.category) # Truck
print(Vehicle.category) # Car
class Vehicle:


    category = "Bus"

    def __init__(self, doors, color): # This is a constructor
        self.doors = doors # instance attribute
        self.color = color # instance attribute

    def description(self): # a method inside Vehicle class
        return f"Vehicle is {self.category}.Color is {self.color} and doors are {self.doors}"

    def change_color(self, color): # This is also a method
        self.color = color
v1 = Vehicle(4, "red")
print(v1.category)
print(v1.doors)
print(v1.color)

v1.category = "bike" # set_data
print(Vehicle.category) # bus
print(v1.category) # bike # get_data


v2 = Vehicle(2, "green")
print(v2.doors) # 2
print(v2.color) # green

print(v2.description())
v2.change_color = Vehicle(4, "Yellow")
print(v2.change_color.color)

# function inside a class is called method of that class and can be called with the object of that class only.