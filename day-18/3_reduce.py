# reduce()
# reduce () is a built-in function that takes two parameters as an input, first parameter is function
# and second parameter is an iterable
# reduce() function returns one element from the final computation in the iterable.


from functools import reduce
nums = [1, 2, 3, 4, 5]
def sum_all(x, y):
    return x + y

result = reduce(sum_all, nums)
print(nums)
print(result)  # 15

#### lambda####
nums = [1, 2, 3, 4, 5]
result = filter(lambda x: x**3 ,nums)
# usually used this rather than normal function
print(list(result))

