squared = {data: data**2 for data in range (1,13)}
print(squared)

student_list =[("name", "jon"), ("age", 25), ("address", "KTM")]
student = dict(student_list)
print(student)

# Create dictionary of the above data using dictionary comprehension
student = {key:value for key, value in student_list}
print(student)


############ enumerate() ############
# enumerate() funtion can take 2 parameters, iterable and start_value
vowels = ["a", "e", "i", "o", "u"]
print(enumerate(vowels)) # enumerate object
print(list(enumerate(vowels)))

for index, value in enumerate(vowels):
    print(index) # 0, 1
    print(value) # a, e


for index, value in enumerate(vowels, start=1):
    print(index) #  1,2,3,4,5
    print(value) #  a,e,i,o,u
    