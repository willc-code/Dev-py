import random
from number_oracle_art import logo

# Placeholder for number of Attempts and game status.
ATTEMPTS = 0
game_over = False
# This is the randomly generated number that the user would have to guess.
number = int(random.randint(1, 100))

# Defining guess function.
# Since this guess function will update global variables, global variables are being declared using 'global'.
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

# Defining difficulty level selection, which determines the number of attempts that the user will start with.
def difficulty(level):
    global ATTEMPTS
    if level == "easy":
        ATTEMPTS = 10
    elif level == "hard":
        ATTEMPTS = 5

# The game begins by printing logo, welcome message and prompting user to input difficulty level.
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
choose_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

# if/elif statement to determine the difficulty level and the number of attempts.
if choose_level == "easy":
    difficulty("easy")
elif choose_level == "hard":
    difficulty("hard")

# while loop that will keep the game running as long as the guess is wrong and the number of attempts is not equals to zero, or that the correct number has been guessed.
while game_over == False:
    your_guess = input("Your guess: ")
    guess(int(your_guess))           # made a mistake here earlier by not declaring the type as integer.
    if int(your_guess) == number:
        print("You won!")
        break
    else:
        print(f"You have {ATTEMPTS} attempts left")

    if ATTEMPTS == 0:
        game_over = True
        print("You've run out of guesses. Refresh the page to run again.")
    else:
        pass


