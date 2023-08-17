# Create a class person with instance attributes name and age. Create a method get_details in this class to print name and age.
class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"Name is {self.name} and age is  {self.age}"


v1 = Person("Ryna", 23)
print(v1.name)
print(v1.age)
print(v1.description())
