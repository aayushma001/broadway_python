message = "hello World"

##### string methods #####
# Capatalize()

result = message.capitalize()
print(result)

# Title()
result = message.title()
print(result)

# upper()
result = message.upper()
print(result)

# lower()
result = message.lower()
print(result)

# split()
result = message.split()
print(result) # ["Hello","World"]

result = message.split('o')
print(result) #['hell', ' W', 'rld']

message = "I,am,learning,python"
result = message.split(",")
print(result) # ['I', 'am', 'learning', 'python']

# join()
message = ['I', 'am', 'learning', 'python']
result = " ".join(message)
print(result) # I am learning python
# message.split("") # it raises error.


# result => I, am, Learning, Python
message = ['I', 'am', 'learning', 'python']
result = ", ".join(message)
print(result)

# find()
message = "Hello World "
result = message.find("l")
print(result) # 2

result = message.find("Wor")
print(result) # 6

result = message.find("wor")
print(result) # -1 default value


# replace()
message = "Hello World"
result = message.replace("Hello","HELLO") # ("old" ,"new")
print(result)

