# Note: This was my second attempt after learning from the weaknesses in my draft version in main.py
# This version was also done without looking at tutorials or suggested solution, except for the list of cards.
# After realising that the completed solution contains card number 11, I briefly looked at the suggested solution.
# I took the list of cards from the suggested solution which mirrors the card deck better and improve the odds more realistically.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Alas, this version of mine still has a weakness and I have missed out an important part of the real Blackjack game:
# That if 11 is in cards and the sum of cards is above 21, 11 will be counted as 1:
# if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
# It is structurally difficult to include this feature without a major revamp.
# Therefore I am keeping this version here as a testament to writing them without looking at the solution.
# Possibility of revisiting and rewriting this in the future.
# For future solution, Claude has suggested: Rewrite just the score calculation — add a calculate_score() function to your existing code that handles the ace rule. You don't need to restructure everything.

from blackjack_art import logo
import random

print(logo)

# Asks user to start game or otherwise.
game_on = input("Do you want to play a game of Blackjack? type 'y' or 'n': \n")

# Storing cards in a list, which starts empty.
your_cards = []
comp_cards = []

# Defining drawing cards.
# The list of points mirrors the deck from Ace to King.
# Randomly selected card will be appended to the list.
def you_draws_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    your_cards.append(card)

def comp_draws_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    comp_cards.append(card)

# If user chooses to start game, two cards will be drawn each for computer and user.
# Immediately the computer will draw further cards if the score is less than 12.
if game_on == "y":
    you_draws_card()
    you_draws_card()
    your_score = sum(your_cards)

    comp_draws_card()
    comp_draws_card()
    comp_score = sum(comp_cards)
    if comp_score < 12:
        comp_draws_card()
        comp_score = sum(comp_cards)
    else:
        pass

    print(f"Your cards are: {your_cards}, current score: {your_score}.")
    print(f"Computer's first card: {comp_cards[0]}")

    # This is the while loop on adding cards or drawing more cards.
    continue_adding = True

    while continue_adding:
        another_card = input("Type 'y' to get another card, type 'n' to pass: \n")
        if another_card == "y":
            you_draws_card()
            your_score = sum(your_cards)

            if comp_score < 17:
                comp_draws_card()
                comp_score = sum(comp_cards)
            else:
                pass

            # The while loop continues only if user's and computer's score are both below 21.
            # Otherwise while loop breaks immediately.
            if comp_score < 21 and your_score < 21:
                print(f"Your cards are: {your_cards}, current score: {your_score}.")
                print(f"Computer's first card: {comp_cards[0]}")

            elif comp_score > 21 or your_score > 21:
                break


        elif another_card == "n":
            break

    # When exited the while loop -
    print(f"Your final hand: {your_cards}, final score: {your_score}.")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}.")

    if comp_score > 21 and your_score <= 21:
        print("The computer went over. You win!")
    elif your_score > 21 and comp_score <= 21:
        print("You went over. You lose!")
    elif your_score > comp_score:
        print("You win!")
    elif comp_score > your_score:
        print("You lose!")
    elif comp_score == your_score:
        print("Draw!")


elif game_on == "n":
    print("\n" * 20)
    pass

else:
    print("Invalid input.")
    pass






