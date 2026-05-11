#match-case-statement in python is used for match pattern in python 
# एक value को अलग-अलग cases से match करना और जो match हो, वही code चलाना।
# एक ही variable की अलग-अलग values चेक करनी हों then we use match case
# basic syntax ===  match variable:
#    case value1:
#       # code
#    case value2:
#        # code
#    case _:
#        # default case


# lets take an example ---->

# def day_of_week(day):                                    # ye to ho gaya purana elif method lets take an new method
#     if day == 1:
#         return "It is a Sunday"
#     elif day == 2:
#         return "it is a monday"
#     elif day == 3:
#         return "it is a tuesday"
#     elif day == 4:
#         return "it is a wednesday"
#     elif day == 5:
#         return "it is a thrusday"
#     elif day == 6:
#         return "it is a friday"
#     elif day == 7:
#         return "it is a saturday"
    
# print(day_of_week(1))
    

#--------------------------------------------------------------------------------------------------

def day_of_week(day):  
 match day:                                 
    case 1:
         return "It is a Sunday"
    case 2:
        return "it is a monday"
    case 3:
        return "it is a tuesday"
    case 4:
        return "it is a wednesday"
    case 5:
        return "it is a thrusday"
    case 6:
        return "it is a friday"
    case 7:
        return "it is a saturday"
    case _:
        return "not a valid day"

print(day_of_week(2))
    
#-------------------------------------------------------------------------------------------------------

def is_weekend(day):
    match day:
        case "saturday" | "sunday" :
            return True
        case "Monday" | "Tuesday" |"wednesday" |"thrusday" |"friday":
            return False
        case _ :
            return False
        
print(is_weekend("saturday"))   #jo case daloge uske hissab se answer milega ......