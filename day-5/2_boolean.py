# True and false are the boolean datatype.True or false are also keywords in python
# Boolean type in python is the subclass of the integer class
# where false represents 0 and true represents 1.

# Relational operators yield boolean type
a = 5
b = 3
print(a > b) # True
print(b > a) # false
print(b == a) # false
print(b != a) # true

# logical operators yield bollen type
print(a>b and a!=b) # true
print(b>a and a!=b) # true
print(a==b or a<b) # false
print(not a) # false
print(not b) # false
c = None
print(not c) #true
print(not[]) # true
print(not"") # true
print(not{}) # true
print(not()) # true
print(not False) # true
print(not True) # false


# membership operations yield boolean
print(2 in [1,2,3]) #true
print("a" not in ["a","e","i","o","u"]) # false

#identity operations yield boolean
a = [1,2,3]
b = a
print(a is b) #true
print(id(a) == id(b)) # false
print(a is not b) #false

b = a.copy()
print(a is b) # false
print(a is not b) #true


# we have already mentioned , boolean is a subclass of int type
# let's see some examples
print(True + 2) # 1+2=3
print(70*False) # 70*0=0
print(True+False) # 1+0=0
print(True +True) # 1+1=2

# we have bool() builtin function for the boolean type
# Anything truthy inside the bool() function gives true and whereas anything falsy inside
# bool() gives false

# Any non-empty datatypes are considered truthy.Examples of truthy(except 0 all values) are :
a = 23
b =12.1
c = [1,2,3] # it is a non-empty list
d = {1,2,3} # it is a non-empty set
e = (1,2,3) # it is a non-empty tuple
f = {"name":"jon","age:23"} # it is a non-empty dictionary
g = True
print(bool(a)) # true
print(bool(b)) # true
print(bool(c)) # true
print(bool(d)) # true
print(bool(e)) # true
print(bool(f)) # true
print(bool(g)) # true

# All empty datatypes ,None and false are falshy values
a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = ""
h = None
i = False
bool() # falshy
print(bool(a)) # false
print(bool(b)) # false
print(bool(c)) # false
print(bool(d)) # false
print(bool(e)) # false
print(bool(f)) # false
print(bool(g)) # false
print(bool(h)) # false
print(bool(i)) # false





