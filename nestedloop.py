# nested loop = A loop within another loop  (outer, innerloop)
#      outer loop :
#              inner loop :

# EX of for loop in for loop ....

# for x in range(3):   # iska mtlb hai ki iteation 3 bar chalega 
#  for y in range(1, 10):  # iska mtlb hai ki range 1 se 10 hogi jo ki 0 se 9 hogi...
#     print(y, end=" ")   # iska mtlb hai ki ab print kardo lekin " " iske bich ke gap ko darshata hai ..

rows = int(input("Enter a # of rows:  "))
columns = int(input("Enter the # of columns: "))
symbol= input("Enter a symbol to use :  ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
# so this is called loop in another loop ..