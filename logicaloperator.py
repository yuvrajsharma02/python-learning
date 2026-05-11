#logical operator = evaluate multiple codition  (or, and , not)
#               or= at least one condition must be true 
#               and = both condition must be true 
#               not = inverts the condition (not false, not true )

#---------------------  or -----------------------------

# temp = 0
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

#-------------------- And --------------------------------

temp = 29        #yaha hamre pass temprature hai....
is_sunny =  False   #yaha hamare pass hai ki temprature sunny hai ya nahi 

if temp >= 28 and is_sunny:      #aagr temp 28 ke equal ya us se jayda hai ...or sunny hai ...
 print("it is Hot outside🥵")
 print("It is sunny😓")
elif temp <= 0 and is_sunny:      # aagr temp 0 se jayada ya equal hai or sunny hai... 
 print("It is Cold outside")
 print("it is sunny")
elif 28> temp > 0 and is_sunny:    # aagr temp 0 se kam or 28 se jayda or sunny hai ...
 print("it is warm outside ")
 print("it is sunny ")
elif temp >= 28 and not is_sunny:   # aagr temp 28 ya us se jayda hai or not sunny hai ...
 print("it is Hot outside")
 print("it is cloudy")
elif temp <= 0 and not is_sunny:   # agar temp 0 ya se jayda equal or not sunny hai ...
 print("its is cloud outside")
 print(" it is cloudy")