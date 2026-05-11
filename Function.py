#function = A block of reusable code
# ek function ko create karne ke liye hum "def" keyword ka istemal karte hai ..

# def happy_birthday(name, age):
#  print(f"Happy bithday to you {name}")    # ab ye ek function ban gaya hai 
#  print(f"you are {age} old")   # jo bhi function banaya uske variable ko assign kar diya ....unke bich me
#  print("Happy birthday to you")

# happy_birthday("yuvraj", 20)

#=====================================================================================

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("yuvraj sharma", 23000, "23.2.2025")

#=============================================================================
# now make an function of add, subtracting , multiply or divide two numbers..........

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(sub(1,2))
print(multiply(1,2))
print(divide(1,2))

#============================================================================

# now we write a program for capitalize the name and create a name

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)