import random as ran

print("This is a ROCK-PAPER-SCISSOR game")
print("RULES:")
print("ROCK beats SCISSOR, SCISSOR beats PAPER, PAPER beats ROCK")
print("Enter 1 for ROCK, 2 for PAPER, 3 for SCISSOR")

choice_list = [1, 2, 3]
user_choice = int(input("Enter a choice: "))
machine_choice = ran.choice(choice_list)

if user_choice not in choice_list:
    print("Wrong choice")
else:
    choices = {1: "ROCK", 2: "PAPER", 3: "SCISSOR"}
    print(f"You chose {choices[user_choice]}")
    print(f"The machine chose {choices[machine_choice]}")

    if machine_choice == user_choice:
        print("It's a tie!!")
    elif (machine_choice == 1 and user_choice == 3) or (machine_choice == 2 and user_choice == 1) or (machine_choice == 3 and user_choice == 2):
        print("The machine wins. You're a loser.")
    else:
        print("Congrats!! You win.")