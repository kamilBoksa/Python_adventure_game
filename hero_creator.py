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


def get_hero_statistics(hero_stats):
    hero_stats = create_hero()

    name = hero_stats[0]
    strength = hero_stats[1]
    lifes = hero_stats[2]
    intelligence = hero_stats[3]
    agility = hero_stats[4]

    return name, strength, lifes, intelligence, agility

def print_hero_statistics(hero_stats):
    print("")
    print("_____________________")
    print("Name: %s" % hero_stats[0])
    print("Strenght: %s" % hero_stats[1])
    print("Intelligence: %s" % hero_stats[3])
    print("Agility: %s" % hero_stats[4])
    print("Lifes: %s" % hero_stats[2])
    print("_____________________")
