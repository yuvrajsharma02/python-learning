#Super() Function = FUNCTION used is child class to class to call method from a parent class (superclass)
#        Allow you to extend the functionilty of the inherited method 

class Shape:    #here we make an parent class and give it an important function
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):  #here we make an child class and inherit it with parent class
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  #here we init the super function so the important function will auctomatically called from the parent class
        self.radius = radius 


class Square(Shape): #here we make an child class and inherit it with parent class 
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):  #here we make an child class and inherit it with parent class
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled= True, radius=5)
square = Square(color="blue", is_filled= True, width=5)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

circle.describe()
