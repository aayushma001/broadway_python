# add()
s = {1,2,3}
result =s.add(4)
print(s)  # {1,2,3,4}
# print(result) because add method return nothing none

# update()
s = {1, 2, 3}
s.update([4, 5, 6, 7, 8])
print(s)  # {1,2,3,4,5,6,7,8}

# discard()
s = {1,2,3,4}
s.discard(4)
print(s)
s = {1,2,3,4}
s.discard(5)
print(s) # it doesnot raises error

# remove()
s = {1,2,3,4}
s.remove(3)
print(s)


# s = {1,2,3,4}
# s.remove(6) # it raises error
# print(s)

# pop()
s = {1,2,3,4}
print(s.pop()) # it randomly pops out any one value of that set


# difference()
a = {1,2,3,4}
b = {3,4,5,6}
result = a.difference(b) # a-b
print(result) # {1,2}
print(a - b) # - operator is used for set difference
# intersection()
a = {1,2,3,4}
b = {3,4,5,6}
print(a.intersection(b)) # {3,4}
print(a & b) # & operator is used for set intersection

# union()
a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b)) # {1,2,3,4,5,6}
print(a | b) # | operator is used for set union
# isdisjoint()
a = {1,2,3,4}
b = {3,4,5,6}
print(a.isdisjoint(b)) # False

# issubset()
a = {1,2,3,4}
b = {3,4}
print(b.issubset(a)) #True

# issuperset()
a = {1,2,3,4}
b = {3,4}
print(a.issuperset(b)) # True


# symmetric_difference()
a = {1,2,3,4}
b = {3,4,5,6}
result = (a.symmetric_difference(b))
print(result) # {1,2,5,6}
print(a ^ b) # ^ operator is used for set intersection

 # symmetric_difference_update()
a = {1,2,3,4}
b = {3,4,5,6}
result = a.symmetric_difference_update(b)
print(result) # none
print(a)  #{1,2,5,6}
