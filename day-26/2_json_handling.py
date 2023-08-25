# JSON handling for JavaScript Object Notation
# It is one of the file format to transfer data around the web or system
# It is very famous way of file transfer in the REST APIs
# Python has a built-in support for json handling


# Rules in a json file
# 1. keys and values must be enclosed in double quotes
# 2. Information can be enclosed in an array
# 3. Double quotes are not required for the number datatype
# 4. Extension of the Json file is .json
# for example:
# student =  {"name":"jon", "address": "KTM"} # This can be a valid JSON
# student =  {'name':'jon', 'address':'KTM'} # Invalid JSON. JSON must have double quotes

students =[
    {"name":"jon", "address": "KTM", "phone": 9845677891},
    {"name":"jane", "address": "BKT","phone": 9834589767},
    {"name":"harry", "address": "PKT", "phone": 9834567991},
    ] # Valid JSON

import json
filename = "students.json"
with open(filename, "w+") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)
    fp.seek(0)
    data = fp.read()
    data = json.loads(data)
name = data[0]["name"]
print(name)

#{
#    "error":"Unsthenticated" # json
#}
#<error>Unauthenticated</error> # xml