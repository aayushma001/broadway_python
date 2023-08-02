# we can concatenate strings

m1 = "Hello"
m2 = "World"
message = m1 + m2
print(message) # HelloWorld

# Repetation operation

message = "HelloWorld"
print(message * 3) # "Hello WorldHello WorldHello World"



# Membership operation
message = "Hello World"
print("H" in message) # True
print("W" not in message) # False




##### Built-in functions that can be used in string #####
message ="Hello World"
print(len(message)) # 11 works only in list datatypes like tuple,list
print(bool(message)) # True
print(type(message)) # <Class 'str'>


x = slice(2,6)
print(message[x]) # "llo "