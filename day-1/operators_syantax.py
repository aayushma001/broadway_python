# operators are the special symbols in any programming language to carry out
# arthimetic and logical operations

a = 1
b = 2
c = a+b
# '=' is an argument and '+' is an argumetic operator

# arithemetic operators
# addition (+)
# subtraction(-)
# multiplication(*)
# division(/)
# floor division (//)=>floor division removes the decimal value only
# provides the integer towards floor.


print(3//2) # it gives 1
print(-3//2) # it gives -2

# exponential (**)
print(3**2) # it gives 9



# modulus (%) =>Gives remainder of a division
print(3%2) # it gives 1
print(4%2) # it gives 0



###### comparision/relational operators #######
# ==,<,>,!=,>=,<= are relational operators

print(4==5) # false
print(6!=3) #true

# logical operators
# and ,or,not are the logical operations and their operators are "and","or"
# and "not" respectively .The results in logical operations are either true or false


# identity operators
# identity operators check whether two operators are same or not .'is' and
# 'is not' are used for the identity check.
a = 1
b = 1
print(a is b) #true
print(id(a))
print(id(b)) # for the sam object id() gives equal value


# membership Operators
# it is used to check membership of an object in a sequence.'in' and 'not in' are
# used for membership check
print(2 in [1,2,3]) #true
print(3 not in [1,2,3]) #false


# Assignment operator
# The result of any operator can be assign to a variable using an assignment
# operator."=" is a basic assignment operator.
name="jon" # here = is an assignment operator

# +=,-=,*=./= are also some of the assignment operators
a = 1
a = a + 1 #this line can also be written as a += 1
print(a) #  2
a += 1 # 3
print(a)


# Presedence and Associativity
# presedence of the opertaors is the rule that determines which operator should be
# executed first
# if multiple operators in an operation have same precedence then the associativity
# determines the operation sequence


# Normally associativity is from left-right except for the case of '**'.
# for exponent (**), it is from right-left

print(2**3**2) #512


