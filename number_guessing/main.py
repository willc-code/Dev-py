import random
from number_guessing_art import logo

ATTEMPTS = 0
game_over = False
number = int(random.randint(1, 100))

def guess(num):
    global ATTEMPTS
    global number
    global game_over
    if num > number:
        ATTEMPTS -= 1
        print("Too high.")
    elif num < number:
        ATTEMPTS -= 1
        print("Too low.")
    elif num == number:
        print(f"Your guess is correct. The number is {number}. Good job!")
        game_over = True

def difficulty(level):
    global ATTEMPTS
    if level == "easy":
        ATTEMPTS = 10
    elif level == "hard":
        ATTEMPTS = 5

print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
choose_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if choose_level == "easy":
    difficulty("easy")
elif choose_level == "hard":
    difficulty("hard")

while game_over == False:
    your_guess = input("Your guess: ")
    guess(int(your_guess))
    if int(your_guess) == number:
        print("You won!")
    else:
        print(f"You have {ATTEMPTS} attempts left")

    if ATTEMPTS == 0:
        game_over = True
        print("You've run out of guesses. Refresh the page to run again.")
    else:
        pass


