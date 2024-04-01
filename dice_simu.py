import random

x = "y"

# Define the number of dice and the number of sides on each die.
num_dice = 1
num_sides = 6

# Create a list of weights for the dice.
weights = [1, 1, 1, 1, 1, 2]

# Add a bias to the dice.
bias = 1

while x == "y":

    # Generates a random number
    # between 1 and 6 (including
    # both 1 and 6
    # Roll the dice and print the results.
    rolls = random.choices(range(1, num_sides + 1), weights=weights, k=num_dice)

    if rolls[0] == 1:
        print("-------")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("-------")
    if rolls[0] == 2:
        print("-------")
        print("| 0   |")
        print("|     |")
        print("|   0 |")
        print("-------")
    if rolls[0] == 3:
        print("-------")
        print("|     |")
        print("|0 0 0|")
        print("|     |")
        print("-------")
    if rolls[0] == 4:
        print("-------")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("-------")
    if rolls[0] == 5:
        print("-------")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
        print("-------")
    if rolls[0] == 6:
        print("-------")
        print("|0 0 0|")
        print("|     |")
        print("|0 0 0|")
        print("-------")
    x=input("press y to roll again and n to exit:")
    print("\n")
