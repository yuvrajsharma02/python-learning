#import math

#x = 9.8

# print(math.pi)
# print(math.e)

#result = math.sqrt(x)
# result = math.ceil(x)   /its up the value of float
# result = math.floor(x)   /its less the value


#print(result)


# --------------------------------------------------------------
    #  circumference of circle

# import math

# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {circumference}")   # here if we want to answer in simple digit with 2 point digit we use a 'round' function
# print(f"The circumference is: {round(circumference, 2)}")

#-----------------------------------------------------------

#      area of cirle   = pi.r^2

# import math

# radius = float(input('Enter The Radius of a Circle: '))
# area = math.pi * pow(radius ,2)

# print(f"the area of the circle is: {area}cm^2 ")  now here we use the round function and make  result shorter
                                #    |
                                #    |
                                #    \/ 
# print(f"the area of the circle is: {round (area) }cm^2 ")


# -------------------------------------------------------------

# find side of a triangle

import math

a = float(input("Enter side A:  "))
b = float(input("Enter side B:   "))

# the formula is sqrt of a+b

c = math.sqrt (pow(a, 2) + pow(b, 2))

print(f" side c = {c}")

