# lambda in python are the elegant to create the functions
# These function do not have name . So, they are also called anonymous function

def sum_all(x, y):
    return x + y

sum = lambda a, b: a + b
print(sum(4, 5))

is_even = lambda x: x % 2 == 0
print(is_even(4))


