# create a dictionary student with keys id, name, age, department.Take
# a input from the user, which info(id, name, age or department) he wants
# to access and print the result.Handle the possible exceptions.
student = {"id": 1, "name": "jenny", "age":23, "department": "IT"}
try:
    key = input("enter the key you want to access ")
    data = student[key]
    print(f"The {key} of the student is {data}")
except KeyError:
    print("Please enter a valid key")
except ZeroDivisionError:
    print("Please provide a number other than zero")