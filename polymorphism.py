#polymorphism = greek word that means to "have many forms of faces"...

#two ways to achive ploymorphism
#-------->  Inheritance
#--------> "Duck typing"


from abc import ABC, abstractmethod   #ABC ka matlab hai Abstract Base Classes. Yeh Python ki ek library hai.

class Shape:    
     @abstractmethod   #@abstractmethod = ऐसा function जिसे child class को compulsory override करना पड़ेगा
     def area (self):   # yaha humne bola ki har class jo shape class ko own karti hai uska area hona compulsary 
         pass

class Circle(Shape):  # yaha ek class banayi Circle or vo own kar rahi hai shape ko 
    def __init__(self, radius): 
        self.radius = radius  

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2 

class Triangle(Shape):
    def __init__(self, base, height):
        self.base= base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("peppeoni",15)]

for shape in shapes:
    print(f"{shape.area()}cm2")



