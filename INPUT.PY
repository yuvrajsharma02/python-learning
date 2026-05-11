 #INPUT() = A FUNCTION THAT PROMPTS  THE USER TO ENTER DATA 
#           RETURN  THE ENTERED DATA AS A STRING 

name = input("what is your name?: ")
age = int(input("how old are you?:"))

 # here i typecast the datatype because it can not accept string as a number
age = age + 1

#yaha hum user se input le rahe hai ....
print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"you are {age} year old")

#yaha humne user se name or age ka input liya question karke
# fir print karwa diya usko apne content ke sath .... thats called input method in string.



