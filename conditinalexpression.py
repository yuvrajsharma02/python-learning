#conditional expression = A one line shortcut for the if-else statement (ternary operator
#                         print  or assign one of two value based on a condition
#                         X if condition else Y

# num = 5

# print("positive"  if  num > 0 else "Negetive")
# result = "EVEN" if num % 2 == 0 else "odd"


# print(result)


# num = 5
# a = 6
# b = 7

# max_num = a if a > b else b
# min_num = a if a > b else b

# print(max_num)


num = 5
a = 6
b = 7
temprature = 20
user_role = "Limited access"

#weather = "HOT" if temprature > 20 else "COLD"

access_level = "Full Access" if user_role == "admin" else "Limited access"


print(access_level)