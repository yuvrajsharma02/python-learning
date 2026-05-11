#class variable = shared among all the instance of a class
#    defined outside the constructor
#    allow you to share data among all object created from the class 

class Student:

    class_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("yuvraj sharma", 30)
student2 = Student("patrick", 35)
student3 = Student("squidward", 55)
student4 = Student("sandy", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students} student")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)