### list indexing ###
# list indexing starts from 0 for forward indexing and -1 for the backward indexing .
#indexes must be provided in big brackets

vowels  = ['a','e','i','o','u']

print(vowels[0])  # => 'a'
print(vowels[2])  # => 'i'
# print(vowel[5]) # => it raises Index error


print(vowels[-1])  # =>'u'
print(vowels[-3])  # => 'i'
# print(vowels[-6]) # => it raises index error

vowels[2] ="I" # assigning item to the list at 2nd position
print(vowels)

vowels[-1] = "U" # assigning item to the list at last position using negative indexing.
print(vowels)


####### List slicing ########
# in slicing the first index is including but the second index is always exclusive.
a = ['a','b','c','d','e','f','g','h','i','j']
print(a[:])

print(a[0:7])  # ['a','b','c','d','e','f','g']
print(a[:7])   #  ['a','b','c','d','e','f','g']
print(a[3:])  # [d,e,f,g,h,i,j]

print(a[2:6]) # [c,d,e,f]
print(a[6:2]) # []

print(a[-2,-7]) #[d,e,f,g,h]
print(a[-2:-7]) # []
print(a[:-2]) #[a,b,c,d,e,f,g,h]
print(a[2:-2]) # [c,d,e,f,g,h]
print(a[-3:]) # [h,i,j]



# in every data-types operations, methods and built-in functions should be studied carefully
