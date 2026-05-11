#while loop = execute some code while some condition remain true 
# yaar while loop is all about the condition check 
# mtlb jab tak conditionn true hai ye chalta rahega ise hum iteration bhi khete hai
#  lets take an example -->
# i = 1

# while i <= 5:
#     print(i)
#     i += 1

# ab kya hua jab tak condition true thi ye chalta raha mtlb 5 ke ane tak it will be running 
# jese hi condition false hui ye stop ho gaya ........


#  mtlb if me ye tha ------>

  # name = input("Enter your name :  ")

# if name == "":
#     print(" you not write anything..")   # isme ye hua ki hamare kuch na likhne par print ho gayi statement
# else:
#     print(f" Hello {name}")


#while loop me dekhte hai ab --->

# name = input("Enter your name :  ")

# while name =="":
#     print("you did not enter your name")  # isme jab tak hamne kuch nahi likha tab tak loop chalta rahega or 
#     name = input("Enter your name : ")  # or name mangta rahega 
# print(f"Hello {name}")



# ab manke chalo vo if statement vali statement isme hoti to hum loop me hi atak jate --->

# name = input("Enter your name:  ")

# while name == "":
#     print("you did'nt  not enter  your name ")

# print(f"Hello {name} ")

#----------------------------------------

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age:   "))

# print(f" you are {age} year old")

# food = input("Enter a food you like (q to quit):  ")  

# while not food == "q":     # jab tak loop "q"  na ho jaye tab tak ...
#     print(f"You like {food}")
#     food = input("Enter another food like you  (q to quit):  ")
# print("bye")

# num = int(input("Enter a # between 1- 10:  "))

# while num < 1 or num  > 10:
#     print(f"{num} is not valid")
#     num = int(input("enter a # between 1 -  10:  "))

# print(f"your number is {num}")




