
# TODO: makes a title 
def title():
    print("Pig Dice rules:")

# TODO: displays the rules of the game
def rules():
    with open("rules.txt", "r") as file:
        for line in file:
            print(line, end="")
    print() 

# TODO:make the main function and call it

def main():
    title()
    rules()
main()