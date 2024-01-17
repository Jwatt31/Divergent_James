#!/usr/bin/env python3

#4-3 feet - meter converter

# Make Title
def display_title():
    print("feet to meter conversion")

# TODO: make a numberd menue option for feet to meters vvs with a select conversion 1/2
def menue():
    print("A. feet - meters")
    print("B. meters - feet")
    pick = input("select a conversion a/b ")
    if pick == "a":
        feet = float(input("eneter the feet\n"))
        meters = feet * 0.3048
        print(f"{meters}meters")
    else:
        meters2 = input("eneter the meters\n")
        feet2 = meters2 / 0.3048
        print(f"{ feet2}feet")


# TODO: all in a while loop to see if u want to go again in the main functio
def main():
    display_title()
    menue()
    again = "y"
    while again == "y":
        again = input("would u like to enter another y/n") 
    print("bye")

main()