# Encapsulation is the process of data hiding in OOP approach of Programming.
# Using this feature we make our attributes(variable inside class) private, public or/and  protected

# Public Attributes
# These attributes are accessible from both inside the class and outside the class

class Vehicle:
    engine_type = "Petrol"
    def description(self):
        return f"The vehicle has {self.engine_type} engine"

v = Vehicle()
print(v.engine_type) # petrol

# Protected Attributes
# These attributes should accessible from the same class or the child class only
class Vehicle:
    _color = "Blue"
    def color_desc(self):
        print(f"The color of the vehicle is {self._color}")

class Bike(Vehicle):
    def color_desc(self):
        print(f"The color of bike is {self._color}")
b = Bike()
print(b._color) # Blue . Python is flexible so it also allows the protected embers to be accessible
                # from outside the class . But, it is not recommend to do so

# Private Attributes
class Vehicle:
    __color = "red" # Private member because of the double underscore in the beginning of the variable
    def color_desc(self):
        return f"the color of the vehicle is {self.__color}"
v = Vehicle()
# print(v.__color) # attribute error
print(v.color_desc())