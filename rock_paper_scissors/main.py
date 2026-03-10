import random

# ASCII Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# ASCII Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# ASCII Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


print("Welcome to the python rock, paper, scissors game! " \
"")

# asking for user input
user = int(input("What do you choose? enter 0 for Rock, 1 for Paper and 2 for Scissors: \n"))

print("You chose: ")

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print("you entered an invalid number, you lose!")


# generating computer input
comp = random.randint(0, 2)

print(f"Computer chose {comp}: ")

if comp == 0:
    print(rock)
elif comp == 1:
    print(paper)
elif comp == 2:
    print(scissors)

if user == 0 and comp == 1:
    print("you lose!")
elif user == 0 and comp == 2:
    print("you win!")
elif user == 1 and comp == 0: 
    print("you win!")
elif user == 1 and comp == 2:
    print("you lose!")
elif user == 2 and comp == 0:
    print("you lose!")
elif user == 2 and comp == 1:
    print("you win!")
elif user == comp:
    print("draw!")
else:
    print("you entered an invalid number, you lose!")



