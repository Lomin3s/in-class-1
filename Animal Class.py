def main():

    legs = str(input("Does it have legs [y/n]: "))
    land = str(input("Does it live on land [y/n]: "))

    if legs == "n" and land == "n":
        print("It's a shark!")
    elif legs == "n" and land == "y":
        print("It's a snake!")
    elif legs == "y" and land == "n":
        print("It's a gator!")
    elif legs == "y" and land == "y":
        print("It's a cat!")

main()
