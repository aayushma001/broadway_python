# Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
# Add the radius of the circles and print the result. Do the above task using a method and
# then a magic method.Compare the size of the circle and print the result using magic method.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def add_radius(self, obj2):
        return obj2.radius+self.radius
    def __add__(self, other):
        return self.other + other.radius


c1 = Circle(3)
c2 = Circle(5)
result = c1.radius + c2.radius
print(result) # 8

result = c1.add_radius(c2)
print(result) # 8

result = c1+ c2
print(result) # 8
