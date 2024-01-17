import random
#7-2 wizerd inventory

FLOOR_ITEMS = "wisard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"


#functions for show, walk, drop, exit, read floor items and inventory

#iteams on the ground
def read_floor_items():
    floor_items = []
    with open(FLOOR_ITEMS) as file:
        for line in file:
            line = line.replace("\n", "")
            floor_items.append(line)
    return floor_items

#inventory on u
def read_inventory():
    inventory = []
    with open(INVENTORY_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            inventory.append(line)
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
    choice = input("Do you want to grab it? (y/n): ")
    if choice == 'y':
        if len(inventory) >= 4:
            print("You can't carry any more items. Drop something first.\n")
        else:
            inventory.append(item)
            print(f"you picked up {item}.\n")
            write_inventory(inventory)

#drop function
def u_drop(inventory):
    num= int(input("what number is the item in 'hint: you can check your invantory for the number on the side'"))
    if num > 1 or num < len(inventory):
        print("it looks like its been stolen or u lost it u cluts")
    else:
        stash = inventory.pop(num-1)
        print(f"{stash[0]} was deleted.\n")
    print()


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
    
    while True:
        comm = input("Command\n")
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
    print("good bye")



    



if __name__ == "__main__":
    main()