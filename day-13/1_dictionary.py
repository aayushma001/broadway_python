# Dictionary are the mutable datatypes in python
# They have the elements in key-value pair format
# It is also the sequential datatype like list and tuple.


# Creating an empty dictionary
a = dict() # empty dictionary
a = {} # This is also an empty dictionary

# Creating a non-empty dictionary
student = {"name": "jon", "age": 25, "department": "CS"}
print(student) # {"name": "jon", "age": 25, "department": "CS"}
student = dict(name="jon", age=25, department="CS")
print(student)

student = dict([("name", "jon"), ("age", 25), ("department", "CS")])
print(student)  # {"name": "jon", "age": 25, "department": "CS"}

# Creating a list of dictionaries
students = [
    {"name": "jon", "age": 25, "department": "CS"},
    {"name": "jane", "age": 32, "department": "IT"},
    {"name": "Harry", "age": 21, "department": "Physics"},
]
print(students)