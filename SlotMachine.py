#Python Slot Machine

import random      # sabse phele import kiya random because ye help karega random choice generate karne me 

def spin_row():    # ye ek function define kara hua hai jisme random choice function hai jo randomly choice dega given symbols me 
    Symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"] # ye symbol create kiye hue hai "5"

    return [random.choice(Symbols) for _ in range(3)]  # return karo random choice given symbol me se 3 ki range me 
 
def print_row(row):   # ye function define kiya hai print row naam ka jisme ek parameter define kiya hai (row)
    print("*****************")  # only for design
    print("  |  ".join(row))   #join() list ke elements ko string bana kar jodta hai
    print("*****************")

def get_payout(row, bet): #ek function define kiya hai 
    if row[0] == row[1] == row[2]:  #aagr 3 row ek dusre ek equal aati hai 
          if row [0] == "🍒":  
               return bet * 3
          elif row [0] == "🍉":        # man lo watermelon aya to jitne ki bet hai uska 4 into milega 
               return bet * 4
          elif row [0] == '🍋':
               return bet * 5
          elif row [0] == '🔔':
               return bet * 6
          elif row [0] == '⭐':
               return bet * 10
    return 0
    
def main(): #function define kiya ..... ye main function hai isliye program yahi se start hoga 
    balance = 100   # ye balance variable define kiya hai jiski value hai 100
    print("***********************************")  # ye first interface hai 4 line..
    print("welcome to a slot machine project")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***********************************")
     #yaha kuch essential condition lagayi hai taki hum loop me har condition provide kar sake 
    while balance > 0:   # aagr balance bada hai 0 se then ye curret balance print kar dega 
        print(f"Current balance: ${balance}") #yaha balance variable ko call kar diya jo value hai vo print ho jayegi 


        bet = input("Place your bet amount: ")   # yha hum user se uski bet value ka input le rahe hai 

        if not bet.isdigit():  # aagr bet digit nahi hai kuch or hai to print karo invalid number
             print("Plese enter a valid number")
             continue
        
        bet = int(bet)  # yaha humne bet variable ko integr dife kiya hai type casting se 

        if bet > balance:  # aagr bet greater hai balance se to print kardo insufficiant balance 
               print("Insufficant fund")
               continue
        
        if bet <= 0:   # aagr bet small hai 0 se ya uske equal hai to print kardo given statement
            print("bet must be greater than 0")
            continue

        balance -= bet  # balance me se bet ko - kardo 

        row = spin_row()   # yaha spin row function ko call kiya hai 
        print("Spinning...\n")
        print_row(row)

        payout =get_payout(row, bet) #yaha get payout funtion ko call kiya hai 

        if payout > 0:  # agar payout 0 se bada hai to given statement print karo 
             print(f"you won ${payout}")
        else:     # verna ye statement print karo 
             print("Sorry you lost this round ")

        balance += payout  # payout variable ke chalne ke bad kuch value mili hai to usko balance me add kardo

if __name__ == '__main__':
    main()