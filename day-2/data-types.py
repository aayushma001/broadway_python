# mutable and immutable objects
"""
mutable and immutable objects
if an object once created can be changed later then the object is mutable object

but if an object once created can never be changed throughout its life cycle then it is
an immutable object

List,Dictionary,Set are the example of mutable object
numbers,tuple,boolean,String are the example of immutable objects

"""
a = [1,2,3]
a[1] = 5
a
b = (1,2,3)
b[1] = 5 # it raises error because of tuple in immutable

