#Python quiz game

questions = (
    "HOW MANY ELEMENTS ARE IN THE PERIODIC TABLE?: ",   # yaha hamne question liya....
    "WHICH ANIMAL LAYS THE LARGEST EGGS?: ",
    "WHAT IS THE MOST ABUNDANT GAS IN EARTH'S ATMOSPHERE?: ",
    "HOW MANY BONES ARE IN THE HUMAN BODY?: ",
    "WHICH PLANET IN THE SOLAR SYSTEM IS HOTTEST?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),      # yaha options liyeee
    ("A. WHALE", "B. CROCODILE", "C. ELEPHANT", "D. OSTRICH"),
    ("A. NITROGEN", "B. OXYGEN", "C. CARBON-DIOXIDE", "D. HYDROGEN"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. MERCURY", "B. VENUS", "C. EARTH", "D. MARS")
)

answers = ("C", "D", "A", "A", "B")          # answer ye rahe.........

guesses = []     # guess karna hai isliye ek khali list banayi
score = 0        # ye control variable hai jo 0 se ye bata hai ki kitne sawal sahi diye theee
question_num = 0  # question_num bhi "0" se count hoga

for q in questions:       
    print("--------------------------------")
    print(q)

    for option in options[question_num]:
        print(option)

    guess = input("ENTER (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("✅ CORRECT!")
    else:
        print("❌ INCORRECT!")
        print(f"Correct answer is: {answers[question_num]}")

    question_num += 1

print("--------------------------------")
print("RESULT")
print("--------------------------------")
print("Your guesses:", guesses)
print("Correct answers:", answers)
print(f"Your score is: {score}/{len(questions)}")


