try:
    num1 = int(input("enter a number : "))
    num2 = int(input("enter another number : "))


except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Please provide a number other than zero")
else:
    sum = num1 + num2

    print(sum)
