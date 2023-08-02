##### Accessing characters in a string ###
# we access characters from string using indexing. indexing in string is similar to that of list
# Forward indexing starts from 0 and reverse indexing starts from -1.

message ="hello world"
print(message[0]) # h
print(message[3]) # l
print(message[5]) # <space>
print(message[-3]) # r
print(message[-1]) # d

# if we try to access index not present in the string it raises error
#print(message[15]) # it raises index error


#### string slicing ####
# string slicing is also similar to list slicing
message ="hello world"
print(message[:3]) # Hell
print(message[4:]) # o world
print(message[2:5])  # llo
print(message[5:2]) # " "

print(message[:-2]) # hello worl
print(message[-4:]) # orld
print(message[-2:-6]) # " "
print(message[-6:-2]) # <space>wor
print(message[3:-2]) # lo<space>wor


# operating and deleting string item
m = "hello world"
# m[2] = "L" # it raises error because string is immutable and item assignment is not possible

# del m[6] # this is also not possible
# but we can entirely delete the string object
del m # it deletes the string object m


# iterating string using for loop
message = "Hello World"
for i in message:
    print(i) # H,e,l,l,o,w,o,r,l,d

for i in message[2:7]:
    print(i) # l,l, ,o,w
















