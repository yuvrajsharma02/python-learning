# import time   # sabse phele time import kiya ...

# my_time = int(input("Enter the time in seconds:  "))  # yaha my_time name ka variable assign kiya or user se input liya


# for x in range(0, my_time):   # isme mene ka time ko 0 se or  jo user input dega tab tak chalao...
#  time.sleep(3)  # ye har iteration me time ko 3 sec ke liye pause karega 3 * 5 = 15...      


# print("Time's up!")   # mtlb ye program counter 15 sec me chalega 

# ab manke chalo ginti bhi chalani hai ...........--->

# import time

# my_time = int(input("Enter the time in second:   "))

# for x in range(0, my_time):  # ab isme counter time chalte hue dikhega kyuki mene print kar diya hai "x" ko..
#     print(x)                 # agar time revrse me chalana hai to in range me -1 aa jayega bss
#     time.sleep(1)

# print("Times up")


# ab thoda tagda vala karte hai 

import time

my_time = int(input("Enter the time in second:  "))

for x in range (my_time, 0, -1):
    second = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("Time's up!")


#------------------is pe ek or question karenge.....................................


