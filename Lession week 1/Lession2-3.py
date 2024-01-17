#!/usr/bin/env python3

#2-3 tipcal

print("Tips Calculator")
print("")
cost_meal= (float(input("Cost of Meal: ")))
tip_pre= (float(input("tips ammount:  ")))
print("")
tip_cost = cost_meal * (tip_pre/100)
total_cost = tip_cost + cost_meal
print(f"Tip Amount: {tip_cost}")
print(f"Total: {total_cost} ")
