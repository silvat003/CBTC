def take_num(player1_id):
    while True:
        num = input(f"Enter the number, {player1_id}: ")
        if num.isdigit() and len(num) >= 2:
            return num
        else:
            print("Invalid input.Please enter a valid number.")

def guess_num(player2_id, num):
    while True:
        guess = input(f"Enter your guess, {player2_id}: ")
        if guess.isdigit() and len(guess) >= 2 and len(num)==len(guess):
            return guess
        else:
            print("Invalid input.Please enter a valid guess.")

def hint_num(num, guess):
    hint = ""
    print("X means the element is present in the same index, O means the element is present but in a different index, - means the element is not present.")
    for i in range(len(num)):
        if num[i] == guess[i]:
            hint += "X"
        elif guess[i] in num:
            hint += "O"
        else:
            hint += "-"
    return hint

def play_game(player1_id, player2_id):
    num1 = take_num(player1_id)
    player2_guess = 0
    print(f"{player1_id} has entered the number.")
    
    
    while True:
        guess = guess_num(player2_id, num1)
        player2_guess += 1
        if num1 == guess:
            print("Congrats!! You have guessed the number.")
            break
        else:
            print("Hint:", hint_num(num1, guess))
    
    num2 = take_num(player2_id)
    player1_guess = 0
    print(f"{player2_id} has entered the number.")
    
    while True:
        guess = guess_num(player1_id, num2)
        player1_guess += 1
        if num2 == guess:
            print("Congrats!! You have guessed the number.")
            break
        else:
            print("Hint:", hint_num(num2, guess))

    if player1_guess < player2_guess:
        print(f"{player1_id} wins.")
    elif player2_guess < player1_guess:
        print(f"{player2_id} wins.")
    else:
        print("It's a tie!")

player1_id = input("Enter the name of player1: ")
player2_id = input("Enter the name of player2: ")
print(f"{player1_id} is setting the number and {player2_id} is guessing it")
play_game(player1_id, player2_id)