#Module = module is file contaning code you want to include in your program
#         use 'import'  to include a module (built - in your own)
#         usefull  to break up  a large  program reusable seprate files 
#    aapni code ki file banao import karo use karo ...............that called module 


import examplemodule
# by this import i will use my own module which created by me 

result = examplemodule.pi
result = examplemodule.square(3)
result = examplemodule.cube(3)
result = examplemodule.circumference(3)
result = examplemodule.area(3)
print(result)

# if want to know any about module use print(help(module));