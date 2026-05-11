#lets make an enryption program .....
#ENCRYPTION = means hide an important text or massage

import random   # we import the library
import string   

chars = string.punctuation + string.digits + string.ascii_letters  #all the things are add combine
chars = list(chars)  #char ko list me badal diya
key = chars.copy()   #char ki copy banayi

random.shuffle(key)  # key ko randomly suffer kiya...


print(f"chars : {chars}")  #print kar diye charachter
print(f"key : {key}")    #print kar diye key 

#ENCRYPT

plain_text = input("Enter a massage to encrypt: ")   #user se input liya
cipher_text = ""   

for letter in plain_text: 
    index = chars.index(letter)
    cipher_text += key[index]

print(f"origial message: {plain_text}")
print(f"encrypted message: {cipher_text}")


