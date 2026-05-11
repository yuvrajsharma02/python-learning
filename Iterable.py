#ITERABLE = An object / collection that can return its elementone at time, allowing it to be iterated over a loop 
# Jis cheez par hum for loop chala sakein, wo iterable hoti hai ✅
#list , tuple, string, set, dictionary,range  ye sab iterable hai 
# जिस चीज़ के अंदर से Python एक-एक item निकाल सके, वही Iterable है  ex--> "RAM" beacause R-A-M 
# Non-Iterable == x= 10 beacuse उसके अंदर से एक-एक चीज़ नहीं निकाल सकते


#lets take an example of list and tuple--->  both are printed so this are iterables 
number =(1,2,3,4,5) #[1,2,3,4,5]

for number in number:
    print(number)

# now take an example of set {}
fruits = {"apple", "banana", "coconout", "dragon" }

for fruits in fruits:
    print(fruits)

#now take an example of string
name = "Yuvraaj Shrama"  # this iterate easily so  string are iterable ....

for character in name:
        print(character) # if we want to print string in a single horizontal line we can easily use ' end=" " '

# lets take an example of dictionary ......---->

my_dictionary = {"A":1, "B":2, "C":3}

for key,value in my_dictionary.items():
     print(key, value)

#for key in my_dictionary:
#    print(key, value)

#for key in my_dictionary.value():
#     print(value)
