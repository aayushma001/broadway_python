
import json
filename = "student.json"
def update_student(student_id):
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())
        with open(filename, 'r') as fp:
            students = json.loads(fp.read())
        if student:
            student = student[0]
            key = input("enter the info you want to update ")
            if key.lower() not in ["name", "age", "address"]:
                print("Invalid user info")
            value = input("enter the new value ") # jane
            student[key] =value
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
        else:
            print("please enter a valid student id ")
    repeat = input("Do you want to continue (y/n)")
    return True if repeat.lower() == "y" else False