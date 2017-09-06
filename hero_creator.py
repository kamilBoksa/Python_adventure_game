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
            strenght = 3
            inteligence = 10
            lifes = 5
            agility = 2
            break
        elif choice == "A":
            print("You are an archer!")
            strenght = 3
            lifes = 7
            inteligence = 2
            agility = 10
            break
        elif choice == "W":
            print("You are a warrior!")
            strenght = 8
            lifes = 8
            inteligence = 2
            agility = 5
            break
        else:
            print("Wrong input! Please enter: M, A or W")

    return name, strenght, lifes, inteligence, agility

def save_hero_statistics():
    pass

def print_hero_statistics(stats):
    print("Name: %s" % stats[0])
    print("Strenght: %s" % stats[1])
    print("Intelligence: %s" % stats[2])
    print("Agility: %s" % stats[3])
    print("Lifes: %s" % stats[4])
