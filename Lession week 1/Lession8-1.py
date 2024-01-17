#8-1

# print("Tip Cal")

# meal = float(input("Plz enter the cost of the meal"))
# print("The coast of the meal is")
# print("")

# print("15%")
# tip = meal * (15 / 100)
# print(f"The tip amount: {tip}")
# low_tip = meal + tip
# print(f"total {low_tip}\n")

# print("20%")
# tip = meal * (20 / 100)
# print(f"The tip amount: {tip}")
# mid_tip = meal + tip
# print(f"total {mid_tip}\n")

# print("25%")
# tip = meal * (25 / 100)
# print(f"The tip amount: {tip}")
# high_tip = meal + tip
# print(f"total {high_tip}\n")

def meal_cost():
    try:
        meal = float(input("Plz enter the cost of the meal"))
        print("The coast of the meal is")
    except ValueError:
        print("Please enter a number")


def tip_cost(meal):
    try:
        tip = float(input("Plz enter the tip  % "))
        tips = meal * (tip/100)
        total = meal + tips
        print(f"total {total}")
    except ValueError: 
        print("Please enter a number")


def main():
    print("Tip Cal")
    while True:
        meal= meal_cost()
        tip_cost(meal)
    print("good bye")

if __name__ == "__main__":
    main()
