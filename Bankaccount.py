#BANK ACOUNT PROJECT........

import sys

#HERE I INTIALIZE MY VARIABLES AND VALUES..

Balance = 1000
pin = "1234"
Attempts = 0
Transaction_History = []
is_loggedin = False

#LOGIN LOGIC
print("-----Welcome To ATM Machine-----")


while Attempts < 3:
        user_pin = input("Enter Your ATM PIN:  ")

        if user_pin == pin:
            print("---Welcome----")
            print("your current balance is : ", Balance)
            is_loggedin = True
            break
        else:
            Attempts += 1
            remaining = 3 - Attempts
            if remaining > 0:
                 print(f"galat pin! {remaining} attemp bache hai ")
            else:
                 print("failed in 3 attemp")
if is_loggedin:
     while True:
          print("1. Check Balance")
          print("2. Deposit Money")
          print("3. Withdraw Money")
          print("4. Transaction History")
          print("5. Exit")

          choice = input("Choose an Option")

          if choice == "1":
               print(f"your current balance is: {Balance} ")
          elif choice == "2":      #-------------------------------------------> deposite
               amount = int(input("enter your deposit amount: "))
               Balance += amount
             
               Transaction_History.append(f"Deposit: {amount}")
               print(f"{amount} deposit in your account")
          elif choice == "3":    #-------------------------------------------------->withdraw
               amount = int(input("Enter an amount of withdraw: "))
               if amount > Balance:
                    print("itna paisa nahi hai account me")
               else:
                    Balance -= amount

                    Transaction_History.append(f"withdrew: {amount}")
                    print(f"{amount} is less from your account {Balance}")
          elif choice == "4": #-------------------------------------------------->history
               print("--Here your transation history ")
               if not Transaction_History:
                    print("koi transcation nahi hai ")
               for item in Transaction_History:
                    print("-", item)

          elif choice == "5":
               print("Thank you for using Smart ATM, Tata, bye bye")
               break
          else:
               print("invalid choice! sahi option chuno...")

               





        



