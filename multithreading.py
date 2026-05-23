#MultiThreading = used to perform multiple task concurrently (Multitasking)
#                 Good for I/O bound task like reading file or fething data from APIs
#                 threading . thread (target = My_function)

import threading
import time     

def walk_dog(first,last):
    time.sleep(8)
    print(f"you finish walking {first} {last} ")

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_mail():
    time.sleep(4)
    print("you get the mail ")


# walk_dog()     inse to mai sequencly call kar sakta hu mtlb phele 8,2,4 sequencly    
# take_out_trash()
# get_mail()

#now ab hum according to time period call karenge

chore1 = threading.Thread(target = walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target = take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()
