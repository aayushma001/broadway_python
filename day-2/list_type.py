# Python list are mutable objects
# We can create a list by enclosing a sequence in big
# Brackets[]

# We can also create the list using the list() built-in function.
a = [] # An empty set
b = list() # an empty list using list() function

a = [1,2,3] #mNon-empty list
# in this list all data are of integer data-type .But list can also
#have heterogenous type
a = [1,"hello",2.1,{1,2,3},{"a":1,"b":2}]
#in this list the data are of different types which is also supported by a python list
#We can use built-in type function to check the type of an object
type([1,2,3]) #list
type((1,2,3)) #tuple
type(1) #int
# and so on....