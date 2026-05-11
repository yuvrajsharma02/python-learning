import random

options = ("rock", "paper", "scissors")
player = None
# Galti 1: Computer choice loop ke andar honi chahiye
running = True

while running:
    player = input("Enter a choice (rock, paper, scissors): ").lower() # Spelling sahi ki
    
    if player == "q":
        running = False
        break # Seedha bahar niklo

    if player not in options:
        print("invalid choice! please try again")
        continue
    
    # Correction: Computer har baar naya choose karega
    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Galti 2: Ye saara logic loop ke ANDAR hona chahiye (Indented)
    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "scissors" and computer == "rock":
        print("you loose")
    elif player == "paper" and computer == "scissors":
        print("you loose") # Spelling: lose
    elif player == "scissors" and computer == "paper":
        print("you win")
    elif player == "rock" and computer == "paper":
        print("you loose")
    elif player == "paper" and computer == "rock":
        print("you win")