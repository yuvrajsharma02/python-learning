# validate user input exercise
# 1. username is no morethan 12 characters
#2. username must not contain space
#3. username must not contain digit

username = input("Enter a username :  ")

if len(username) > 12:
    print("this use name more than 12 chataracter")
elif not username.find(" ") == -1:              # username ke anadr find karega ki khai index value -1 to nahi hai 
    print("your user name can't contain space")
elif not username.isalpha():
    print("your username can't contain numbers")
else:
    print(f"welcome {username}")