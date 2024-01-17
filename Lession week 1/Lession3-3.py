#!/usr/bin/env python3

#3-3

print("Change Calculator")
i = int(input("Enter a number 1-100\n"))
coin_q = 25 * 
coin_d = 10 
coin_n = 5 
coin_p = 1
close = "y"

while close == "y":

    print(f"\nQuarters {i / 25}")
    change_left = (i - (q*25)*100)
    print(f"Dimes {change_left // 10}")
    change_left %= 10
    print(f"nickles { change_left }")
    print(f"peneeins {change_left}")

    close = input("\nwould u like to do another ")
    