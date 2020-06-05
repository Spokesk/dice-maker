"""Dice Generator

Description: 

Author:

"""

from random import randint

maxInt = 0
genedInt = 0

def start():
    """
        Function Description
    """
    
    # Greeting
    print("Greetings, I am the RNGesus") 

    # Prompt user for sides of dice
    maxInt = int(input("Dice Type: "))

    # Randomly Generate Number
    while True:
        genedInt = randint(1, maxInt)
        break

    # Display Results
    print(genedInt)

start()