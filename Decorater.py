#property = Decorater used to define  a method as property (it cab be accessed like an attribute)
#           Benefit : add additional logic when read, write, or delete attribute
#           Give you getter , setter and deleter method 

class Rectangle:
    def __init__(self, width, height):
        self._width = width  #underscore private dikhane ke liye use hota hai ..ye bolta hai   ये internal variable है, बाहर से direct मत छेड़ो
        self._height = height 

        
        #🔥 इसलिए property का काम है
        #   function को simple बनाना
        #   variable जैसा access देना
        #   data को control/format करना

    @property   #--> Function को variable की तरह इस्तेमाल करना
    def width(self):  
        return f"{self._width:.1f}cm"
    
    @property  
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Width must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")    

rectangle = Rectangle(3, 4)

print(rectangle.width)  #humne ise variable ki tarah use kiya hai kyuki hum @property use kar rahe hai
print(rectangle.height)
del rectangle.width  


