#!/usr/bin/env python3
import random

#4-5 Dice Roller

# TODO: make title

# TODO: add a random dice genarator and have 2 be displayed (if time allowe fo a change in the type of dice)

# TODO: show the total

# TODO: main with a while loop.

def rolldice():
    val = random.randint(1,6)
    return val

def main():
    while True:
        again = input("roll again? y/n\n")
        if again.lower()!='y':
            print("good bye")
            break

        print("dice roller")
        result1 = rolldice()
        result2 = rolldice()
        print(f"die 1: {result1}")
        print(f"die 2: {result2}")
        total = result1 + result2
        print(f"tatal:{total}")
        if total == 2:
            print("snake eyes")
        elif total ==12:
            print("boxcar")
main()