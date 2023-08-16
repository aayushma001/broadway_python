# WAP to delete all the occurrances of a specified character in given string
#S = "All the occurances of a specifiedcharacter in a given string"
# input = "a"
# output = "ll the occurrances of  specified character in  given string"
S = "All the occurrances of a specified character in a given string"
char = input("pick a Character : ")
result = ""
for each in S:
    if each.lower() == char.lower():
        continue
    result += each
print(result)