# remove() method
# remove method takes list item as parameter


vowels = ["a","e","i","o","u"]
vowels.remove('e')
print(vowels)


# if we pass a parameter not present in the list then it raises error
# vowels.remove("p") # it raises valueerror

# pop() method
# pop takes index as parameter
vowels = ["a","e","i","o","u"]
result =  vowels.pop(2)
print(result )  # 'i'
print(vowels)

# pop() method also returns a value from the index passed as the parameter
# in the above example result gives 'i' because 'i' is at the 2nd index. And,finally 'i'
# is also removed from the list vowels



# clear() method.It clears the list
vowels = ["a","e","i","o","u"]
vowels.clear() # it clears the list
print(vowels) # []


# index() method. It takes list item as an argument
vowels = ["a","e","i","o","u"]
result = vowels.index("o")
print(result) # 3

# index() method also takes start and end as parameters
vowels = [5,4,10,"o","u",10,4]
result = vowels.index(4,2,8) # (2,8) are ranges from positions and 4 is the value
print(result) # 6

# vowels = [5,4,10,"o","u",10,4]
# result = vowels.index(2,4,8)
# print(result) it raises error


# count() method takes list item as a parameter and returns the number of repetation
# of that item
vowels = ["a","e","i","o","u","o","o","a","i"]
result = vowels.count("a")
print(result) #2


# reverse() method .It reverses the item of the list
fruits = ["banana","apple","mango"]
fruits.reverse()
print(fruits)












