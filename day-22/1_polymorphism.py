# Polymorphism means many forms of same the same function or object.
# We can take example of len, sum, max etc. built-in fucntion to observe polymorphism in python

#len() is a built-in function in python which can take any type of iterable as a parameter and gives
# the length of the iterable

print(len([1, 2, 3]) # 3(list)
print(len((1, 2, 3))) # 3(tuple)
print(len({"name":"jane", "address": "KTM"}))

# regardless of the datatype , len returns length of an iterable.

# We can classify polymorphism in three different variations in pyhton
# 1. Function / Method Overloading
# 2. method
# 3.