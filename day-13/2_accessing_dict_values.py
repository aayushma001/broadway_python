vowels =["a", "e", "i", "o", "u"]
print(vowels[4]) # u

# Acessing dictionary is similar to that of accessing list elements
student = {"name": "jon", "age": 25, "department": "CS"}
dept = student["department"]
print(dept) # CS

name = student["name"]
print(name) # jon

# print(student["DOB"]) # This raises KeyError

# Accessing values using get() method
department = student.get("department")
print(department) # CS
dob = student.get("dob")
print(dob) # None
######impppp in dictionary function gives none if the key is not given
###### if there is big bracket then the key is not given then it results error


# Adding key-value pair in a dictionary
vowels =["a", "e", "i", "o", "u"]
vowels.append("u")
vowels.insert(2, "A")
vowels[1] = "E"

student = {"name": "jon", "age": 25, "department": "CS"}
student["dob"] = "22 July"
print(student) # {"name": "jon", "age": 25, "department": "CS", "dob": "22 July"}

student.update(roll_no=12)
print(student) # {"name": "jon", "age": 25, "department": "CS", "dob": "22 July", "roll_no"=12}

student["name"] = "Jane"
print(student) # {"name": "jane", "age": 25, "department": "CS", "dob": "22 July", "roll_no": 12}
#### if the key is not there previously then the data is added but if the key resides there
# previously then it'll update.

# Removing a key-value pair from a dictionary
student = {"name": "jane", "age": 25, "department": "CS", "dob": "22 July", "roll_no": 12}
result = student.pop("dob")
print(result) # 22 July
print(student) # {"name": "jane", "age": 25, "department": "CS", "roll_no": 12}

# result = student.pop("address") # KeyError
# print(result)

result = student.popitem()
print(result) # ("roll_no", 12)
print(student) # {"name": "jane", "age": 25, "department": "CS"}


student.clear()
print(student) #{}

del student # deletes the object
