#Magic Method = Dunder method (double underscore) __init__, __str__, __eq__
#               They are automatically called by many of Python's built-in operation
#               They allow developer to define or cusomize the behavior of object 

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name : {self.name} gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
student1 = Student("Spoongebob", 3.2)
student2 = Student("Patrick", 2.0)

print(student1)
print(student1 == student2)
print(student1 > student2)
