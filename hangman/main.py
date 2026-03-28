import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo)

# A random word will be chosen from the word list. Chosen word is printed for the ease of testing.
chosen_word = random.choice(word_list)
print(chosen_word)

# This prints out the spaces in underscores, denoting the number of characters in the chosen word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# this is the main engine of the game - this While Loop that keeps the user guessing until the game is over.
game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, we will print the letter and let them know.
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    # this For Loop ensures that when the correct letter is guessed, it will be displayed, otherwise it will still be underscores.
    # to ensure that previous correctly guessed words are also displayed, we created a list called correct_letters. We will append correct guesses in this list and make them appear again in subsequent guesses
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter is not in the chosen_word, we will print out the letter and let them know it's not in the word.

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed the letter {guess}, it is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}!,YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # this prints out the hangman ascii art with the stages corresponding the number of lives.
    print(stages[lives])


# Learning outcomes
# combining previous lessons: importing list from another python document, random function, for loop, for loop with range, if/elif, while loop.
# the use of an empty place holder in combination with loops.