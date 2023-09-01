from estd_connection import estd_connection

def create_student():
    cursor = estd_connection()
    id = input("enter student id ")
    name = input("create student name ")
    age = input("enter student age ")
    address = input("enter student address")

    sql = f"""
    INSERT INTO STUDENTINFO (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', {age}, '{address}')
    """
    cursor.execute(sql)
    print("Student added Sucessfully")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == "y" else False
