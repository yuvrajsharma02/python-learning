# collection = single  "variable" used to store multiple value
#List = []  ordered and changeable. Duplicate OK
#set = {} unordered and immutable, but Add/Remove OK. No duplicate
#tuple= () ordered and unchangeable . duplicate ok. Faster

#LIST-------------------------------------------------------

#fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits[0:2])   #<---------

# LETS ITRATE OUR LIST 
# for x in fruits:
#     print(x)          

#now dekhte hai hum list ke sath kitne operation perform kar sakte hai 
# print(dir(fruits))
# konsa method kya kam karega ye help method bata dega 
# print(help(fruits))

 # if we want to find any variable  our list we can simple  use in ... fruit in fruit

# fruits[0] = "pineapple"   # it is used to replace an variable in a list
# for fruit in fruits:
#  print(fruit)

# fruits.append("pinapple") # it is used to add an extra variable in list 
# print(fruits)

# fruits.reverse()  # reverse the whole list
# print(fruits)

# fruits.clear()

# print(fruits.count("banana"))


#set------------------------------------------
# immutable or unordered but remove or add is ok

# fruits = {"apple","orange","banana","cocunut","pineapple"}
# fruits.remove("apple")
# print(fruits)

#tuples-----------------------------------
fruits = {"apple","orange","banana","cocunut","pineapple"}

for fruits in fruits :

    print(fruits)


