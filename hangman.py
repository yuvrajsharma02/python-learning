# #Hangman in python
# import random 

# words = ("apple", "orange", "banana", "coconut", "pineapple")

# #dictionary of key: ()

# hangman_art = {1: ("  0  ",
#                    "     ",
#                    "     "),

#                2: ("  O  ",
#                    "  |  ",
#                    "     "),

#                3: ("  O  ",
#                    "  |\ ",
#                    "     "),

#                4: ("  O  ",
#                    " /|\\ ",
#                    "     "),

#                5: ("  O  ",
#                    " /|\\",
#                    " /   "),

#                6:("   O ",
#                    " /|\\",
#                    " / \\  "),}
            
# def display_man(wrong_guesses):
#     for line in hangman_art[wrong_guesses]:
#         print(line) 
#     print("*********")

# def display_hint(hint):
#     print(" ".join(hint))

# def display_answer(answer):
#     print(" ".join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 3
#     guessed_letter = set()
#     is_running = True

#     while is_running:
#       display_man(wrong_guesses)
#       display_hint(hint)
#       display_answer(answer)
#       guess = input("Enter a letter: ").lower()

#       if guess in answer :  
#         for i in range(len(answer)):
#           if answer[i] == guess:
#              hint[i] = guess


# if __name__== "__main__":
#  main()   

import random 

words = ("apple", "orange", "banana", "coconut", "pineapple")

# Dictionary me 0 key add ki hai kyunki game 0 galti se shuru hoga
hangman_art = {0: ("     ", "     ", "     "),
               1: ("  0  ", "     ", "     "),
               2: ("  O  ", "  |  ", "     "),
               3: ("  O  ", "  |\ ", "     "),
               4: ("  O  ", " /|\\ ", "     "),
               5: ("  O  ", " /|\\", " /   "),
               6: ("   O ", " /|\\", " / \\  ")}
            
def display_man(wrong_guesses):
    # Fixed: hangman_art[wrong_guesses] access logic
    for line in hangman_art[wrong_guesses]:
        print(line) 
    print("*********")

def display_hint(hint):
    print(" ".join(hint))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0 # 3 ki jagah 0 se shuru hoga
    is_running = True

    while is_running:
      # FIX 1: display_man()(wrong_guesses) se extra () hata diya
      display_man(wrong_guesses)
      display_hint(hint)
      
      guess = input("Enter a letter: ").lower()

      # FIX 2: Check agar guess sahi hai ya galat
      if guess in answer:  
        for i in range(len(answer)):
          if answer[i] == guess:
             hint[i] = guess
      else:
        # FIX 3: Galat guess par counter badhana zaroori hai
        wrong_guesses += 1

      # FIX 4: Game khatam hone ki conditions
      if "_" not in hint:
          print("Aap jeet gaye!")
          display_hint(hint)
          is_running = False
      elif wrong_guesses >= 6:
          display_man(wrong_guesses)
          print("Game Over!")
          is_running = False

if __name__== "__main__":
 main()