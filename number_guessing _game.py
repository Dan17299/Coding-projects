import random
low = 1
high = 100
number = random.randint(low, high)

print(f"In this game, you will attempt guess a number from {low} - {high}")
attempt = 0
guess = input(f"Please enter a number from {low} - {high}: (press q to quit)")

while True:
    while guess != "q" and (not guess.isdigit() or not low <= int(guess) <= high):
        guess = input(f"{guess} is a invalid guess, please enter another: (press q to quit)")
    if guess == "q":
        print("You quit the game.\nHave a nice day!") 
        break
    guess = int(guess)
    if guess == number:
        print(f"Well done, you guessed the number in {attempt} guesses")
        break
    elif guess < number:
        guess = input(f"{guess} is too low!\nHave another guess: (press q to quit)")
    else:
        guess = input(f"{guess} is too high!\nHave another guess: (press q to quit)")
