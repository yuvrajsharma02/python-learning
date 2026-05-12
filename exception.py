#exception = An event that interrupt the flow of program
#           (ZerroDivisionError, TypeError, ValueError)
#            1.try 2.except 3.finally

# kaffi tarah ki error hoti hai program me jaise 
# zero division error = 1/0
# TypeError = int(Pizza)
# value Error = 1 + " 1"

# ab inko handel karne ke liye python hume kuch 3 steps deta hai --> try --> except ---> finally

try:
    number = int(input("Enter a number:  "))
    print(1 / number)
except ZeroDivisionError:    # iske threw user ko massage jayegi ki vo galti kar raha hai or kya galti kar raha hai 
    print("You can't divide by zero IDIOT!")
except ValueError:           # iske threw user ko massage jayegi ki vo value sahi nahi dal raha 
    print("Enter only number please")

 # ab hum chahte to direct Exception bhi use kar sakte the but it was an bad practice 

finally:
    print("do some cleanup here ")  # finally का use उस code को चलाने के लिए होता है जो हर हालत में execute होना chahiye

