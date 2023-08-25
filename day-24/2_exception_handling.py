# Exceptions in Python are handled using try.... except block

# Try.....except
try:
    num = int(input("enter a number : "))
    print(num)
except ValueError:
    print("enter a valid number")

# It is not mandatory to mention error type in except block.
# If it is not mentioned then it can handle all the exceptions
try:
    num = int(input("enter a number : "))
    print(num)
except:
    print("enter a valid number")

# We can handle as many errors as possible

try:
    num = int(input("enter a number"))
    result = 23/num
    print(result)
except ValueError:
    print("please provide a valid number")
except ZeroDivisionError:
    print("please provide a number other than zero")
#
try:
    num = int(input("enter a number"))
    result = 23/num
    print(result)
except ValueError:
    print("please provide a valid number")
except ZeroDivisionError:
    print("please provide a number other than zero")

# try....except...else...finally
# "finally" block is always executed regardless of error or not
try:
    f = open("test.txt", "w")
except:
    print("something went wrong")
else:
    print(f)
finally:
    f.close()