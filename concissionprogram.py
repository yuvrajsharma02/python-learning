

menu = {"pizza"        : 450,     #here we an add a dictionary
        "burgur"       : 50,
        "chowmein"     : 30,
        "french fries" : 40}

cart = []                             #here we can take an empty cart for a user in list form
total = 0                             #total is starting from "0"

print("--------MENU-----------")    # isne ek loop chalaya jaha sari chize jodi me print hui hai 
for key, value in menu.items():      # key ...me jitni bhi item hai unko print karo ..10 space leke or samne value rakho 
    print(f"{key:10}: {value}")
    print("-----------------------------")

while True:
 food = input("select an item(q to quit):  ") # jab tak loop chalega jab tak ki user "q" nahi deta 
 if food == "q":
    break
 elif menu.get(food) is not None:   #    # agar koi item menu me nahi hai tab bhi use likh lena 
    cart.append(food)

print("------your order--------")
for food in cart:                     # ab jo food cart m aya usko total kar do
   total += menu.get(food)             # yaha total kiya sabhi ka menu.get ki help se
   print(food, end=" ")                # jitne bhi food cart me aaye unke ek line me likho gap ke sath

print()
print(f"Total is : ${total:.2f}")     # ab yaha total likh do sabhi food ka 