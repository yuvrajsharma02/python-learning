unit = input("Is this tempreature in calsius or Farahnite (C/F):   ")
temp = float (input("Enter the temprature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32,1)     # the formula is (`c * 9/5) + 32 = F` 
    print(f" The temperature in Fahrenheit is : {temp}  farahnite")
elif unit == "F":
    temp = round((temp - 32) * 5/9 , 1)
    print(f"The temperature in calsius is : {temp} celcius ")
else:
    print(f"{unit} is an invalid unit of measurement")  