#!/usr/bin/env python3

#4-2 Hike calculator

# TODO:make title
def display_title():
    print("Hike Calcutation mile to feet\n")
 
# TODO: ask for input and display its conversion from miles to feet
def how_far():
    miles = float(input("How far did u go in miles"))
    feet = int(5280/miles)
    print(f"you walked {feet} feet")


# TODO: Main
def main():
    display_title()
    how_far()
    again = "y"
    while again.lower() == "y":
        again = input("would u like to enter another y/n\n")
    print("bye")
main()
