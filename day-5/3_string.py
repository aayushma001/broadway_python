# Strings are immutable and sequence datatype in python
# creating an empty string
a = "" # empty string
b = '' #empty string
c = """""" #empty string
d = str() #empty string
# creating a non empty string
a = "hello world"
b ='python is a high level language'
c = """
hello world
Python is awesome.
"""



# Quote characters
a = "i'm learning python"
b = 'he said,"python is easy to learn"'

# we can also use escape characters for in strings with quote
a = 'I\'m learning python'
b = "he said,\"python is easy to learn\""

# Escape characters are the characters in python which supress the actual python
# meaning and gives new meaning to that character.
# \'.\",\n,\t etc are the examples of escape characters.

print("hello\nworld") # prints hello in first line and hello in second line
print("hello\tworld") # prints hello, a tab, world


# Python also has triple quoted strings
message = """
I'm Learning python
"""
message = '''
I'm learning python
'''
# There is no need for \' (escape sequence) for triple quoted strings
# Triple quoted strings are not only used as normal strings, but are also used to
# add code description in function,classes and as multiple comments

def addition(a,b):
    """

    :param a: any integer value
    :param b: any integer value
    :return: sum of a and b
    """
    return a + b

help(addition)