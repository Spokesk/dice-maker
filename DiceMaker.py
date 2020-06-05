"""Dice Generator

Description: Dice Generator with starting prompt.

Author: Spokesk

"""

from random import randint

maxInt = 0
createdInt = 0

def carryOn():
    # Continue prompt
    try:
        continuePrompt = input("Would thou feel my generosity again? Y/N \n").upper()
    except ValueError:
        print("Please Enter a Y/N!")

    if continuePrompt == "Y":
        return True
    elif continuePrompt == "N":
        return False
    else:
        carryOn()

def start():
    """
    Random integer generator with user defined upper limit.
    Initiates with y/n prompt.
    """

    # Greeting
    print("Greetings lamb, I am RNGesus.")

    # Initiatation Prompt
    while True:
        try:
            maxInt = int(input("What die will thou bequeth upon me? "))
        except ValueError:
            print("Please enter a number!")
            continue

        # Random number generation from user defined limit
        createdInt = randint(0, maxInt)
        print(createdInt)

        if carryOn():
            continue
        else:
            break

start()                        
