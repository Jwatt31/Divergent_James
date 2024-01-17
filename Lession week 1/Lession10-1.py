GROCRYS = "grocrecy.html"

# TODO: Create func that reads the grocrecy.html file
def read_grocrecy():

# TODO: Create function that writes the grocrecy.html file
def write_grocrecy(grocrecy):
    with open(GROCRYS, "w") as file:
        for item in grocrecy:
            file.write(item + "\n")


# TODO: Create main function 

def main():
    print("your list of grocrecy")
    grocrecy = read_grocrecy()
    for item in grocrecy:
        print(item)
        write_grocrecy(grocrecy)

if __name__ == "__main__":
    main()
