#!/usr/bin/env python3

#2-4 Price  compare

print("Travel Time")
print("")
miles= (int(input("how many miles to go: ")))
mph= (int(input("how fast are u going in mph; ")))
print("")
print("estimated travle time")
hours=(miles / mph)
min =(miles % mph * 60 // mph)
print(f"hours {hours}")
print(f"min {min}")