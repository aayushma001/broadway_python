import json
import os
filename ="student.json"


def create_student():
    id = input("enter student id ")
    name = input("create student name ")
    age = input("enter student age ")
    address = input("enter student address")
    student = dict(id=id, name=name, age=age, address=address)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([student])
            fp.write(data)
    else:
        with open(filename, "r+") as fp:
            students = json.loads(fp.read())
            students.append(student)
            fp.seek(0)
            data = json.dumps(students, indent=2)
            fp.write(data)
    print("Student added Sucessfully")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == "y" else False
