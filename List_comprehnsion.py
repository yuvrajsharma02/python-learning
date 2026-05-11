#List Comprehension ==>   short + smart तरीका list बनाने का, जहाँ हम loop + condition एक ही line में लिख देते हैं

# ye to ho gaya long tarika print karne ka ......jo ki hum karte aaye hai 
doubles = []
for x in range (1,11):
    doubles.append(x * 2)

print(doubles)


# ab hum karenge list comprehension se....

doubles = [x * 2 for x in range (1,11)]  # isme humne direct hi likh diiya 
print(doubles)

triples = [y * 3  for y in range (1,11)] 
print(triples)


#--------------------------------------------------------------------
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0 ]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if  num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]

print(positive_nums)

#---------------------------------------------------------

grades = [85,42,79,90,56,61,30]

passing_grades = [grades for grades in grades if grades >= 60]

print(passing_grades)