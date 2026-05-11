#Key argument = an argument preceded by an identifier
#   help with readability
#  order of argument doesn't matter....   <------------------------------

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# hello("Hello", "Mr.", "Yuvraj", "Sharma")
hello("hello", title= "mr", last= "yuvraj", first= "sharma") 

# ========================================================

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=789)

print(phone_num)