# map()
# map() is a built-in function that takes two parameters as an input, first parameter is function and second
# parameter is an iterable
# map() function changes every element in an iterable in some other form
nums = [1, 2, 3, 4, 5]

def increase_by_10(data):
    return data + 10



result = map(increase_by_10, nums)
print(nums)
print(list(result))


##########lambda#########
result = map(lambda x: x+10, nums)
print(list(result))


def power_by_3(data):
    return data ** 3


result = map(power_by_3, nums)
print(nums)
print(list(result))  # can be changes into tuple or set also

#####lambda######
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # all the given nums are truthy so it prints the same given input
result = filter(lambda x: x**3, nums)
print(list(result))