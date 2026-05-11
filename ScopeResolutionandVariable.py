# variable scope = where a variable is visible and accessible
#Scope resolution = (LEGB) Local -> Enclosed -> Global ->Built-in

# --------------> 1. Local scope = the variable is in function Localy.....

# def func1():
#     a = 1     # variable  is in function.............
#     print(a)


#----------------> 2. Enclosed scope = nested function (function ke andar function )
# isme varibale outer function ka hai to bhi inner function bhi ushe use kar sakta hai 

# def outer():                                               #function banaya outer 
#     a = 5                                                  # variable define kara hai 
#     def inner():                                           # fir inner banaya 
#         print(a)                                           # print kar diya "A" jo ki outer function me available hai 
#     inner()                                                # call kiya inner 

# outer()                                                    # call kiya outer

#1️⃣ Local → inner() ke andar
#❌ a nahi mila

# 2️⃣ Enclosing → outer() ke andar
# ✅ a = 5 mil gaya

#---------------------> 3. global scope =  use the variable all over the code
# x = 10                    #global variable
# def show():
#     print(x)

# show()

# global can access from everywhere 

# x = 10

# def show():
#     print(x)

# show()
# print(x)

#----------------------------------> buit-in 
# print()

# len()

# type()
                            #   these are allready  given in python so they are built-in scope 
# input()

# int()

# str()

# range()

#------------------------------------>example

from math import e

def func1():
    print(e)

e = 3

func1()










        