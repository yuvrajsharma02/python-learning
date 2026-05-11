#default argument = a defult value for certain parameter........
#Default Argument ---->  वह पैरामीटर होता है जिसे फ़ंक्शन बनाते समय पहले से कोई मान (value) दे दी जाती है।
# यदि फ़ंक्शन को कॉल करते समय उस पैरामीटर के लिए कोई मान नहीं दिया जाता, तो फ़ंक्शन उसी डिफ़ॉल्ट मान का उपयोग करता है

# def greet(name = "guest"):
#     print("Hello", name)

# greet()
# greet("yuvraj")

#=============================================================================================

# def net_price(list_price, discount, tax):   # ye ek function create kiya ....or usme kuch argument kiya
#     return list_price * (1 - discount) * (1 + tax)  # yaha hamne un argument ka behaviour define kiya hai 

# print(net_price(500, 0, 0.05))   # ab jo argument behaviour hamne define kiya uske hisaab se hame output milega 

#======================================================================================================

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500)) # yaha hamne sirf list price define kiya baki sab uper hi kar diya .......

#======================================================================================================

import time

def count(start, end):     #ek function banaya count name se then we will give two arrgument start and end 
    for x in range(start, end+1):  # then loop chalaya "x" with these arrgument 
        print(x)          # print kar diya "x"
        time.sleep(1)    # 1 sec ke gap se loop chalega 
    print("DONE!")    # sab kuch hone ke ba done print hoga 

count(0, 10)  # yaha hamne jo argument define kiye the loop me unki value dali hai 

