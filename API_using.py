#API = how to connect to an  api using python

import requests  #import the request ..

base_url = "https://pokeapi.co/api/v2/"  # the url where from we retrive a data ......

def get_pokemon_info(name):      #here we define the function which have url and response method from api
    url = f"{base_url}/pokemon/{name}"   # here url....
    response = requests.get(url)    # a variable function call requests which call by us for get info... from url
    
    if response.status_code == 200:   # here the html code = 200  mean mission okkk
       pokemon_data = response.json() # API से जो data आया है उसे Python dictionary में convert करो। json me
       return pokemon_data  # we can use the pokemon data at outside also by use return function
    else:
        print(f"failed to retrive data {response.status_code}")  # aagr  nahi ye ye print kardo

pokemon_name = "typhlosion"  # kis pokemon ki info chahiye 
pokemon_info = get_pokemon_info(pokemon_name)  # yaha pokemon info variable define karke kha ki get_pokemon call kiya or usme particular pokemon_name ki detail mangi

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")  # agar print (pokemon_info) karte to saari info print ho jati isliye F-string use karke particular jaise  "name"  print kara diya 
    print(f" Id : {pokemon_info["id"]}")
    print(f" Height :{pokemon_info["height"]}")
    print(f" weight :{pokemon_info["weight"]}")