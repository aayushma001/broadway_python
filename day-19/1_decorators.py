def decorate_me(func):
    def inner_func(a, b):
        print("This is executed before the main function !")# we can keep here the code we want
        return func(a, b)  # here func is addition
    return inner_func
@decorate_me
def addition(a, b):
    return a + b


# addition= decorate_me(addition) # here the result calls inner function the name of function may be same sometimes
another_return = addition(2, 3)
print(another_return)