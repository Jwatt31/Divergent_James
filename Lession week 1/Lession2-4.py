#!/usr/bin/env python3

#2-4 Price  compare

print("Price Compare")
print("")
big_oz=64
smol_oz=32
big= (float(input("price of 64oz: ")))
smol= (float(input("price of 32oz:  ")))
print("")
price_64= big / big_oz
price_32= smol / smol_oz
print(f"price per ounce of a 64oz: {price_64}")
print(f"price per ounce of a 32oz: {price_32}")