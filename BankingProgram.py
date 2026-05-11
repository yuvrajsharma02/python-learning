#Python Banking Program

def show_balance(balance):  #Define a function
    print(f"Your balance is ${balance:.2f}")  # we gave an output of print balance

def deposit():      #Define a Function
    amount = float(input("Enter an amount to be deposite:   "))  #take an input of balance deposit by user

    if amount < 0:        # if amount is less than 0 then print "0"
        print("this is not a valid amount") 
    else:                #if amount is bigger than 0 then return the value 
        return amount

def withdraw(balance):        # define a function
    amount = float(input("Enter amount to be written:  "))  # take an input from user of amount to be withdraw

    if amount > balance:       # here we can state an condition if amount is bigger than balance
        print("Insufficiant funds")   #then it saw an output insufficiant balance
        return 0                    # here we return an "0"
    elif amount < 0:              # here amount is lesser than 0 
        print(" Please Enter a valid amount! Amount  must be greater than 0")    # then it print this statement
        return 0
    else:
        return amount   


def main():       

    balance = 0       #here we can define a variable balance for all over code and it will be started from "0"
    is_running = True    # if this condition is true the program will be run continously
    
    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
    
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':      #if choice is 1 it call the function show balance 
            show_balance(balance)
        elif choice == '2':
            balance += deposit()   #choice is 2 then , balnce will be add with remaining balance 
        elif choice == '3':
            balance -= withdraw(balance)  # choice is 3 then , balance will be subtract with remaining balance
        elif choice == '4':
            is_running = False     # if choice is 4 then is_running will be false and the loop is stop 
        else:
            print("that is not a valid choice")   # otherwise this statement
    
    print("Thank you have a nice day")

if __name__ == '__main__':
    main()