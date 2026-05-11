# Indexing = acessing element of a sequence using [] (indexing operator 
#   in indexing = [start :  end : step]

credit_number = "1234-5678-9012-3456"  # isme har string ke har ek variable ko ek digit de di jati hai jise hum indexing khete


#print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:-1])
# print(credit_number[:5])
# print(credit_number[-1])
# print(credit_number[::3])


# lets take an example of last digit of your credit card number....

last_digit = credit_number[-4:]    # it can be possible from indexing ......
print(f"XXXX-XXXX-XXXX-XXXX-{last_digit}")  
