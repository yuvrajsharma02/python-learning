#format specifer = {value: flag}  format a value based on what flag are inserted 

price1 = 3.14159
price2 = -987.65
price3 = 12.34


# print(f"Price 1 is {price1:.2f}")   # ye value ko specify karta hai extra digit specify ho jate hai 
# print(f"Price 2 is {price2:.2f}")   #  different way se value ko specify kiya jata jaise space ke liye :2  ese
# print(f"print 3 is {price3:.2f}")

# print(f"Price 1 is {price1:10}")   # ab is se ye hua ki space aa gaya mtlb pura output 10 indexing me khatam hoga
# print(f"price 2 is {price2:010}")  # is se ye hua ki jo space tha uski jagah 0  aa gaya ..
# print(f"price 3 is {price3:<10}") # is se ye hoga ki jo space aage aa raha tha vo piche chala gaya ....

# to kull mila ke format specifer value ko justify karne ke kam  ata hai .....


# print(f"price 1 is {price1:+,.2f}")   # to kul mil ke is tarah hum value ko justify karte hai ...