#inheritance = allows a class to inherit attribute and method from another class
# help with code reusability and extensibility

class Animal:  #HERE WE CAN CREATE A CLASS 
    def __init__(self, name):   # DEFINE THE CONSTRUCTOR OF CLASS
        self.name = name    #AUTOMATICALLY DEFINE THE NAME OF THE CONSTRUCTOR
        self.is_alive = True   

    def eat(self):     #HERE WE DEFINE THE FUNCTION EAT WITH SELF
        print(f"{self.name} is eating")   

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):   
    def speak(self):
        print("WOOF! ")

class Cat(Animal):
    def speak(self):
        print("MEAO! ")

class Mouse(Animal):
    def speak(self):
        print("SQEEK! ")

dog = Dog("kutta")
cat = Cat("billi")
mouse = Mouse(" cuhaa ")

dog.speak()
cat.sleep()
dog.sleep()


