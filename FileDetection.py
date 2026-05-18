# Python file Detection

import os

file_path = "C:\\vs-code data\\PythonPractice\\test.txt"
 
if os.path.exists(file_path):
    print(f"The Location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")