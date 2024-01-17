#!/usr/bin/env python3

#3-4 Shipping cal

print("Shipping cal\n")

shipping_cost = 0
close = "y"
i = float(input("what is the cost of the order"))

while close == "y":

    print(f"cost of the order: {i}")

    if i <= 30:
        shipping_cost = 5.95
    elif 31 <= i <= 49:
        shipping_cost = 7.95
    elif 50 <= i <= 74:
        shipping_cost = 9.95
    else:
        shipping_cost = 0
    total = shipping_cost + i

    print(f"Shipping cost: {shipping_cost}")
    print(f"the total cost : {total}")

    close = input("would u like to do another y/n\n")

