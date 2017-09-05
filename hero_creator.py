import os

def create_hero():
    name = input("Tell me your name: ")
    os.system('clear')

    print("You have 3 paths to choose", name)
    classes = open("classes.txt").read()
    print(classes)

    while True:
        choice = input("If you like to be mage press M, for archer A and for warrrior W: ")
        if choice == "M":
            print("You are a mage!")
            streght = 3
            lifes = 5
            inteligence = 10
            break
        elif choice == "A":
            print("You are an archer!")
            streght = 5
            lifes = 10
            inteligence = 7
            break
        elif choice == "W":
            print("You are a warrior!")
            streght = 7
            lifes = 8
            inteligence = 5
            break
        else:
            print("Wrong input! Please enter: M, A or W")

    return name, streght, lifes, inteligence
