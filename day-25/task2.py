# Add two numbers input and divide a number by another number.
# Handle the possible exception
try:
    num1 = int(input("Enter a number :"))
    num2 = int(input("enter another number : "))
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Please provide a number other than zero")
else:
    result = num1 / num2
    print(result)