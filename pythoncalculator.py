#python calculator

operator = input("Enter a operator (+ - * /) :  ")
num1 = float(input("Enter a 1st number:  "))
num2 = float(input("Enter a 2nd number:  "))

if operator == "+":
    result = num1 + num2  # here we  add both of number and print a simple result.....
    print(result)    
elif operator == "-":
    result = num1 - num2  # here we  sum both of number and print a simple result.....
    print(result)
elif operator == "*":
    result = num1 * num2  # here we  multiple both  of number and print a simple result.....
    print(result)
elif operator == "/":
    result = num1 / num2  # here we  divide both of number and print a simple result.....
    print(result)
else:
    print(f"the {operator} is nnot valid operator ")

# if we want an answer in a main or two digit then we simply use the round function.....
