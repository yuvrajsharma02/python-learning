#Python writing files (.txt, .json, .csv)

# is code se hamne file create ki hai.......
# or threw code hamne us file me kuch likha ...

#----------------------------txt--------------------------------
# employees = ["Eugene", "Squidward", "Spoongebob", "Patrick"]

# file_path = "output.txt"

# try:
#     with open(file_path, "w") as file:
#          for employee in employees:
#           file.write(employee + "\n")
#          print(f"txt file '{file_path}' was created ")
# except FileExistsError:
#      print("That file is already exists!")

#---------------------------json-----------------------------


# import json

# employee = {
#     "name " : "Spoongbob",
#     "age " : 30,
#     "job " : "cook"
# }

# file_path = "output.txt"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print(" that file already exists!")

#---------------------------------------------------------------------------

import csv

employees = [["Name", "Age", "job"],
             ["spoongbob", 30, "cook"],
             ["patrick", 37, "unemployed"],
             ["sandy", 27, "scientist"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
