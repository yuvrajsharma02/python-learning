# python weight converter

weight = float(input("Enter your weight:   "))  # here we take an input of wieght by user
unit = input("kilogram or pounds? (K or L):   ")  # here we can justify the input type

if unit == "K":
    weight = weight * 2.205   # we multiply the value for conversion into ponds
    unit = "Lbs."
    print(f"Your weight is : {round(weight, 1)} {unit}")
elif  unit == "L":
    weight = weight / 2.205   #we devide the value for converion into kilograms
    unit = "kgs."
    print(f"Your weight is : {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

# in this python file we can build an weight converter that can calculate the coversion by multiply and divide
