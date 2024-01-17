#6-2 wizerd inventory


#have 5 functions for show, grab, drop, edit, exit

def u_show(invatory):
    if len(invatory) == 0:
        print("your a poor poor adventure")
    else:
        for i, stash in enumerate(invatory, start=1):
            print(f"{i}. {stash[0]}")
    print()

def u_grab(invatory):
    item = input("whatss in the box")
    invatory.append(item)
    item <= 4
    print(f"{item[0]} was added.\n")

def u_drop(invatory):
    num= input("what number is the item in 'hint: you can check your invantory for the number on the side'")
    if num > 1 or num < len(invatory):
        print("it looks like its been stolen or u lost it u cluts")
    else:
        stash = invatory.pop(num-1)
        print(f"{stash[0]} was deleted.\n")
    print()
        

# def u_edit(invatory):
#     item = input("what item number u wish to change")
#     if item [1:len(invatory)]:


# menu options
def display_menu():
    print("show - show all items")
    print("grab - add to inventory")
    print("drop - fell out of your bag we know u arent dropping the 40 cheese wheeles")
    print("edit - move iteas around for better accsess in combat")
    print("exit - closes")

# main and title

def main():
    #list in the invatory
    invatory = ["sword", "gold", "rope"]

    print("wizerd inventory program\n")

    display_menu()
    while True:
        comm = input("Command\n")
        if comm.lower == "show":
            u_show(invatory)
        elif comm.lower == "grab":
            u_grab(invatory)
        elif comm.lower == "drop":
            u_drop(invatory)
        #elif comm.lower == "edit":
        #   u_edit(invatory)
        elif comm.lower == "exit":
            break
        # else:
        #     print("plz enter a vaild command")


    



if __name__ == "__main__":
    main()