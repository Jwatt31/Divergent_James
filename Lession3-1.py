#!/usr/bin/env python3

#3-1

print("Letter grade converter")

grade = 0
i= "y"

while i=="y" :
    grade = float(input("Plz enter the grade -"))
    if 90 <= grade <=100:
        print("A")
    elif 80 <= grade <=89:
        print("B")
    elif 70 <= grade <=79:
        print("C")
    elif 60 <= grade <=69:
        print("D")
    elif 0 <= grade <=59:
        print("F")
    else:
        print("plz enter a valid number")
    i= input("would u like to enter another -")


duck = ''' 22 if grade >= 90\n
tttftvojjp:'''

split([duck][, num])