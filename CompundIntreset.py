#Intreset 
#yaha hum python se intreset nikalne ka program banayenge .....

# print("LETS CALCULATE")

# principle = 0
# rate = 0
# time = 0
# amount = 0

# while principle <= 0:
#     principle = float(input("Enter a principle amount:  "))
#     if principle <= 0:
#         print("principle can't be less than  '0' ")

  
# while rate <= 0:
#     rate = float(input("Enter a Intreset rate amount:  "))
#     if rate <= 0:
#         print(" Intreset rate (%) can't be less than  '0' or equal")

  
# while time <= 0:
#     time = int(input("Enter a time in years:  "))
#     if time <= 0:
#         print("time can't be less than  '0' ")


# total = principle * pow((1 + rate/ 100),  time)        #formula of compund intreset...
# print(f"Balance after {time} year's : {total:.2f}")

# now we calculate the rate (%) on principle amount

# while amount <= 0:
#     amount = float(input("Enter a amount  :  "))
#     if amount <= 0:
#         print("amount can't be less than  '0' ")

# total1 = (pow(amount/principle, 1/time) - 1) * 100
# print(f"the rate of intreset on your amount is {total1:.2f}")



#  now the different way of while loop is --->

print("LETS CALCULATE")

principle = 0
rate = 0
time = 0

while True:        #true is an boolean so 
    principle = float(input("Enter a principle amount:  "))
    if principle < 0:
        print("principle can't be less than  '0' ")
    else:
        break

  
while True:
    rate = float(input("Enter a Intreset rate amount:  "))
    if rate < 0:
        print(" Intreset rate (%) can't be less than  '0' or equal")
    else:
        break

  
while True:
    time = int(input("Enter a time in years:  "))
    if time < 0:
        print("time can't be less than  '0' ")
    else:
        break


total = principle * pow((1 + rate/ 100),  time)        #formula of compund intreset...
print(f"Balance after {time} year's : {total:.2f}")




  
