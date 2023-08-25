# Different modes in which files can be opened
# r => Read Mode
# w => Write Mode
# a => append mode
# r+ => Read and Write Mode
# w+ => Write and Read Mode
# a+ => append and read mode
# x => write exclusively mode

filename = "message.txt"
fp = open(filename, "w")
fp.write("helloworld")
fp.close()


fp = open(filename, "r")
data = fp.read()
print(data)
fp.close()

fp = open(filename, "a")
fp.write("\nI'm Learning Python")
fp.close()

# file handling with context manager
with open(filename, "r") as fp:
    data = fp.read()
print(data)

# with open(filename, "r+") as fp:
#   data = fp.read() # first read
#    fp.write("\nPython is a high level language") #  and then write
# print(data)

with open(filename, "w+") as fp:
    fp.write("I'm Learning Python Language")
    data = fp.read()
print(data)

# Exclusive mose doesn't create a file if the file already exist.It raises error in such case
# with open(filename, "x") as fp:
#   fp.write("Hello World ")
