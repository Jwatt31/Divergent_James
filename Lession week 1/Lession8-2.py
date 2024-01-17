import random
#8-2 wizerd inventory

FLOOR_ITEMS = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

# checke files functins
def check_file_inventory():
    try:
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "") 
    except FileNotFoundError:
        print(f"{INVENTORY_FILENAME} cant be found ")


def check_file_floor_items():
    try:
        with open(FLOOR_ITEMS) as file:
            for line in file:
                line = line.replace("\n", "")
    except FileNotFoundError:
        print(f"{FLOOR_ITEMS} cant be found ")


#functions for show, walk, drop, exit, read floor items and inventory

#iteams on the ground
def read_floor_items():
    floor_items = []
    try:

        with open(FLOOR_ITEMS) as file:
            for line in file:
                line = line.replace("\n", "")
                floor_items.append(line)
    except FileNotFoundError:
     print(f"{FLOOR_ITEMS} cant be found ")
    return floor_items

#inventory on u
def read_inventory():
    inventory = []
    try:
    
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
    except FileNotFoundError:
         print(f"{INVENTORY_FILENAME} cant be found ")           
    return inventory

def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")

#show function
def u_show(inventory):
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
    print()


#walk function
def u_grab(inventory):
    itemes = read_floor_items()
    still_left = [i for i in itemes if i not in inventory]
    item = random.choice(still_left)
    print(f"you see {item} in a bag.\n")
    try:
        choice = input("Do you want to grab it? (y/n): ")
        if choice == 'y':
            if len(inventory) >= 4:
                print("You can't carry any more items. Drop something first.\n")
            else:
                inventory.append(item)
                print(f"you picked up {item}.\n")
                write_inventory(inventory)
    except ValueError:
        print("Invalid input try again.\n")

#drop function
def u_drop(inventory):
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(inventory):
            print("Invalid item number.\n")
        else:
            item = inventory.pop(number-1)
            print(f"You dropped {item}.\n")
            write_inventory(inventory)
    except ValueError:
        print("Invalid item number.\n")


# menu options
def display_menu():
    print("show - show all items")
    print("walk - walk into the sun set")
    print("drop - fell out of your bag we know u arent dropping the 40 cheese wheeles")
    print("exit - closes")

# main and title

def main():
    #list in the invatory
    inventory = read_inventory()

    print("wizerd inventory program\n")

    display_menu()

    check_file_inventory()
    check_file_floor_items()
    
    while True:
        try:
            comm = input("Command\n")
            #print("Command was valid.)\n")
            if comm == "show":
                u_show(inventory)
            elif comm == "drop":
                u_drop(inventory)
            elif comm == "walk":
                u_grab(inventory)
            elif comm == "exit":
                break
            else:
                print("Not a valid command. Please try again.\n")
        except ValueError:
            print("Not a valid command. Please try again.\n")
    print("good bye")


if __name__ == "__main__":
    main()