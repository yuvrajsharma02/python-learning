#membership operator = used to test wheather a value or variable is found in a sequene
# कोई चीज़ किसी group / collection के अंदर है या नहीं
#            (string,list,tuple,set and dictionary)
#types----->               IN  and NOT-IN   




#                              IN ---> पूछता है: “ये अंदर है क्या?”
# word = "APPLE"

# letter = input("guess a letter in a screet word:  ")

# if letter in word:
#     print(f"Yes, There is a {letter}")
# else:
#     print(f"{letter} was not found")




#                         NOT IN ----> पूछता है: “ये अंदर नहीं है क्या?”

# students = {"spongebag","patrick","sandy"}

# student = input("Enter the name of a student : ")
# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")


# lets take an example of dictionary ---->
grades = {"sandy": "A",
          "squidward": "B",
           "spongebob": "C",
           "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")




