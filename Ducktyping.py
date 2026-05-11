#duck typing is an another way to achive polymorphism beside Inheritance
#     object must have the minimum neccesary attribute/method

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF !")

class Cat(Animal):
    def speak(self):
        print("MEOW !")

class Car:

    alive = True

    def speak(self):
        print("HONK!")

animal = [Dog(), Cat(), Car()]

for animal in animal :  
    animal.speak()
    print(animal.alive)

