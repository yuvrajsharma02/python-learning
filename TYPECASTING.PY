#Typecasting = the process of converting one data type into another data type str(), int(), float(), Bool()

name = " "
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


# now we convert a data type into another .....



is_student = str(is_student) # we can change the data type in this line into another data type ......
print(is_student)

print(type(is_student))

#now take an example 

age = str(age)
age += "1"  # here we convert interger in string so +- is not working without "" this coluns if it was an integer than it will work without that 

print(age) 

#this is use for handling user inputs 


name = " "
name = bool(name)

print(name)