import random      # import random number libarary

lowest_num = 1      # here we assign a variable with the name a (lowest_num) and give value = 1
highest_num = 100   # here we assign a variable with the name a (highest_num) and give value = 100
answer = random.randint(lowest_num, highest_num)   # here we assign a variable "answer" and import a fuction --> which can generate random integer 
guesses = 0    # here we assign a guess name variable which start from 0 
is_running = True   # is_running is assign for running status of an loop if its true it will running

print("Python number guessing game")     # when we enter in output screen we this prompt
print(f"select a number between {lowest_num} and {highest_num}")  # after that it will an choice by this f-string

while is_running:     # is runnning is true so loop is  starting
    guesses = input ("Enter your guess: ")  # it can take an input from user of its guess

    if guesses.isdigit():    # this condition says that user can write an digit of a string ...  validation check 
        guesses = int(guesses)  # guess is an integer so it will type cast it as an integer 
        guesses += 1   # how many time user an do this it will count that 
           
           
        if guesses < lowest_num or guesses > highest_num:   # it will check that number is in limit or out of limit
            print("that number is out of range")  
            print(f"pease select a num betwenn {lowest_num} and {highest_num}")
        elif guesses < answer:  # it will say that user ansewer is low from correct ans..
            print("to low! try again")
        elif guesses > answer:  # it will say that user answer is high from guess 
            print("to high! try again")
        else:     # other wise answer ....
            print(f"CORRECT! the answer was {answer}")
            print(f"number of guess: {guesses}")
            is_running = False  # if answer is right than it will stop the loop bu false
    
    else:
        print("Invalid guess")  # if all condition are false then it print this statement 
        print(f"please select a number between {lowest_num} and {highest_num}")


#        Code Line,Kaam (Purpose),Logic (Piche ki wajah)

# if guesses.isdigit():,Validation Check,"Yeh check karta hai ki user ne ""Number"" (0-9) enter kiya hai ya koi galat cheez (jaise ABC)."

# guesses = int(guesses),Data Conversion,Input hamesha Text (string) hota hai. Maths karne ke liye ise Integer (number) mein badalna zaroori hai.

# guesses += 1,Counter,"User ne kitni baar koshish ki, yeh use count karta hai. Har guess par +1 hota hai."

# if guesses < lowest_num or guesses > highest_num:,Range Check,Yeh dekhta hai ki number limit ke bahar to nahi (Maano limit 1-100 hai aur user ne 500 likha).

# elif guesses < answer:,Hint (Low),"Agar user ka number sahi jawab se chota hai, to use ""Too Low"" ka message milta hai."

# elif guesses > answer:,Hint (High),"Agar user ka number sahi jawab se bada hai, to use ""Too High"" ka message milta hai."

# else:,Success Case,"Agar upar ki koi condition match nahi hui, matlab user ne sahi number guess kar liya hai!"

# is_running = False,Stop Game,Sahi jawab milne par game ka loop rokne ke liye ise 'False' kiya gaya hai.

# else: (Invalid guess),Error Handling,"Agar shuruat mein .isdigit() fail ho jaye (user ne text daala ho), to yeh message dikhata hai."