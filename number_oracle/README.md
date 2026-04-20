# The Number Oracle. 

About: The Oracle has chosen a number between 1 and 100. You have limited attempts to uncover it — but how many guesses will it take? The fewer the better.

## How to use 

Run `python main.py` and follow the prompts to input the relevant responses. 

## What it does

Guess a number between 0 - 100. Select 'easy' and you will get 10 attempts, and 'hard' for 5 attempts. 

## Other files

number_oracle_art.py - contains the logo of the game in ASCII art, which is then imported to main.py
Learning_Note_Global_vs_Local_Variable.md - Learning notes on Global vs Local Variable. 

### Learning notes 

- There's a widely accepted convention for structuring Python scripts. Here's the standard order:

Imports
Constants / global variables
Function definitions
Main code (the code that actually runs when you execute the script)

- Global vs Local Variables and how to update/edit global variables in defined local functions (using the global keyword).
- The need to declare the global variable at the top of the defined function first: 
 def guess(num):
    global ATTEMPTS        # declare first
    if num > number:
        ATTEMPTS -= 1
        print("Too high.")
    elif num < number:
        ATTEMPTS -= 1
        print("Too low.")
    elif num == number:
        print("You got it!")

- 