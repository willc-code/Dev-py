print('''Welcome to the Treasure Island!
Your mission is to find the treaure!''')

# Asking the user to choose the direction to take

path = input("Let's begin! There are two paths ahead of you, which one do you take? L or R?: ").upper()

if path == "R":
    print("Sorry that leads you straight into a trap! Game over!")
elif path == "L":
    water = input('You\'re now at a jetty, there is an island not far away. ' \
    'Do you want to swim or wait for the boat to get to the island? Please input "swim" or "wait": ').lower()

    if water == "swim":
        print("Sorry the crocs got the better of you, game over!")
    elif water == "wait":
        door = input("You got on the last boat of the day, how lucky! " \
        "Now you are at the island and there are three doors: red, yellow and blue. " \
        "Which door Lcolour do you choose to go into?: ").lower()
        if door == "red":
            print("it's a room full of venomous snakes, game over!")
        elif door == "yellow":
            print("Thats where the treasure is, you found it! Congratulations, you won!")
        elif door == "blue":
            print("It's a room full of spiders, yikes! game over!")
        else:
            print("wrong input, game over!")
    else:
        print("Wrong input, game over!")
else:
    print("Wrong direction, game over!")