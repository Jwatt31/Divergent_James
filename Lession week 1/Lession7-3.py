#7-3 contact manager


# title with menu
def title():
    print("contact manager\n")
    print("list - Display Contacts\n"
          "view - view a contact\n"
          "add  - add to it\n"
          "del  - delete\n"
          "exit - leave"
          )

# function for user input command (list, view, add, del, exit)

def list():
    with open("contacts.csv", "r") as f:
        for line in f:
            print(line[1], end="")
        print()

# function for user input numbers
def view(contacts):
    num = int(input("pick the number assocated with who u want to call \n "))
    if num < 0 or num> 5:
        print("plz enter a valid number")
    else:
        contact = contacts[num-1]
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Phone: {contact[2]}")
        print("")

# function to add
def add(contacts):
    name = input("Name: ")
    email = input("Email: ") 
    phone = input("Phone: ")

    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    print(list)

    
def main():
    contacts = [["dave von vot","daveTHEBA45", 236346784],
            ["jaen man vot","yoohud34", 2129638784]]

    title()
    command = input("command: ")
    list()
    view(contacts)
    return 0

if __name__ == "__main__":
    main()