# fruits = ["apple","orange","banana","cococunt"]
# vegetable = ["celery","carrots","patatoes"]
# meats = ["chicken","fish","turkeys"]

# groceries = [fruits, vegetable, meats]

# print(groceries[0][0])
# so here wee print three list by the one variable groceries...


#----------------------------------------------------------------
# groceries = [["apple","orange","banana","cococunt"],
# ["celery","carrots","patatoes"],
# ["chicken","fish","turkeys"]]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")

# here we can iterate the element of groceries......


num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
        


