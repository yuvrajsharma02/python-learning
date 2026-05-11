#*args = allow to you pass multiple non- key arguments
#keyward args = allow to you pass multiple keyward - arguments
#       unpacking operator
#  1. positional  2. default  3. keyward  4.ARBITARY


# 1. positional argument = kisi bhi variable ka order important hota hai ....

# def add(a, b):
#     return a + b

# print(add(1, 2))     # here a = 1, b = 2 yaha oeder badal bhi sakta hai ...

# 2. keyward argument = isme order important nahi hota kyuki  hum para meter ka name likh ke  value dete hai 

# def student(name, age):
#     print(name, age)

# student(age = 20, name = "yuvraj") #ye order me nahi hai but fir bhi order me ayega

# key ward argument pass multiple argument....

def shipping_label(*args, **kwargs):
    for arg in args:
       print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')},{kwargs.get('state')},{kwargs.get('zip')}")
    
shipping_label("DR.", "spoogeboob","squarepanets",
               Street= "123jkskwwhdw",
               city="detroit",
               state= "mi")





