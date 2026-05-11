#Multiple inheritance = inherit more than one parent class
#                       C(A, B)

#Multi-level inheritance = inherit from a parent which inherit from another parent 
#                          c(b)  <- b(a) <-A


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is spleepig")

class Prey(Animal):           #HERE WE CAN MAKE AN CLASS NAME PRAY 
    def flee(self):     #MAKE AN FUNCTION IN AN CLASS 
        print("This animal is feeling")   

class Predator(Animal):         # SAME HERE AS WE MAKE AN 2ND CLASS HERE 
    def hunt(self):     #MAKE AN FUNCTION IN AN CLASS 
        print("This animal is hunting")

class Rabbit(Prey):     #HERE WE CAN MAKE AN CLASS RABBIT BUT INHERIT WITH THE RECENT CLASS "PREY"
    pass

class Hawk(Predator):    #HERE WE CAN MAKE AN CLASS HAWK BUT INHERIT WITH THE RECENT CLASS "PREDICTOR"
    pass

class Fish(Prey, Predator):  #HERE WE MAKE AN CLASS FISH BUT HERE WE MULTI-INHERIT WITH PREY AND PRIDICTOR BOTH
    pass

# NOW OVERALL WE CAN MAKE 5 CLASSES
# PREY 
# PREDICTOR
# RABBIT  --> PREY 
# HAWK --> PREDICTOR
# FISH --> PREY AND PREDATOR

rabbit = Rabbit("susa")   #HERE WE DEFINE A VARIABLE TO CALL A CLASS
hawk = Hawk("lolu")
fish = Fish("machli")


rabbit.eat()





