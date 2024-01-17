#!/usr/bin/env python3

#4-1 Even odd checker

# Make Title
def display_title ():
    print("Even Odd Checker\n")

# Have User Input
def num ():
    i = int(input("plz give me a number 1-100\n"))
    if i % 2 == 0:
        print("even") 
    else:
        print("odd")


# Create a Main Function 
def main():
    display_title()
    num()
    again = "y"
    while again.lower() == "y":
        again = input("would u like to enter another y/n")
    print("bye")
    
main()
