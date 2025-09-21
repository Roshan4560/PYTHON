# WAP to play stone paper scissor game


import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for stone, p for paper, c for scissor): ").lower()
youdict = {"s": 1, "p": 0, "c": -1}
reversedict = {1: "stone", 0: "paper", -1: "scissor"}

if youstr in youdict:
    you = youdict[youstr]
    print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

    if computer == you:
        print("Match draw")
    elif (computer == 1 and you == -1) or (computer == 0 and you == 1) or (computer == -1 and you == 0):
        print("COMPUTER WON")
    else:
        print("YOU WON")
else:
    print("Invalid choice. Please enter s, p, or c.")
