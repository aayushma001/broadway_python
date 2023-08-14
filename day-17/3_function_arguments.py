# Arguments in the funtion are the elements that are send in the function cell
# parameters in the functions are the elements that are present in the function definition

# Types of argument in function
# 1. Positional/required arguments
# 2. Default
# 3. Arbitrary

def addition(a, b, c=5):
    return a+b+c


result = addition(2, 3, 10)
print(result)  # 15
# Here "a" and "b" are positional arguments and "c" is a default argument
# Positional arguments must be sent during a function call i.e, they are the required arguments
# Default arguments are not required in a function call.
