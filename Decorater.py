#Decorator = A function that extends the behaviour of another function
#            without modify that base function
#            Pass the base function as a argument to the decorator

#            @add_sprinkle
#            get_ice_cream("vanilla")

def add_sprinkles(func):  # make an function and call a parameter func...
    def wrapper():   
        print("*sprinkles*")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("*You add fudge*")
        func()
    return wrapper

@add_sprinkles
@add_fudge

def get_ice_cream():
    print("here is your ice-cream")

get_ice_cream()