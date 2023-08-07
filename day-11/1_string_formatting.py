# we can format using f-strings
name = input("enter your name ")
age  = int(input("enter your age  "))
language  = input("enter the language you are learning ")
message = f"hello i am {name} .I am learning {language} "
print(message)
message = 'I am %s and I am %d years old' % (name,age)
print(message)
message = f"I am {name} and I am {age} years old"
print(message)

##### using format() method
message = "I am {} and I am {} years old."
formatted_message = message.format(name,age)
print(formatted_message)

message = "I have {1},{0} and {2} in my bag .".format('book','pen','copy')
print(message)

# message = "I have {1},{0} and {2} in my bag .".format('book','pen') # it raises error
message = "I have {1} and {2} in my bag .".format('book','pen','copy','pencil')
print(message) # here first place holder takes 'book' secong placeholder takes pen  and other are ignored.