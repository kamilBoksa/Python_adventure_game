import os


def create_hero():
    """ Creates hero with class defined by player, returns list with saved hero statistics"""

    name = input("Tell me your name: ")
    os.system('clear')
    print("You have 3 paths to choose", name)
    classes = open("classes.txt").read()
    print(classes)


    while True:
        choice = input("If you like to be mage press M, for archer A and for warrrior W: ")
        choice = choice.upper()

        if choice == "M":
            profession = "Mage"
            strength = 3
            intelligence = 10
            lifes = 5
            agility = 2
            hero_stats = [name, strength, lifes, intelligence, agility, profession]
            break
        elif choice == "A":
            profession = "Archer"
            strength = 3
            lifes = 7
            intelligence = 2
            agility = 10
            hero_stats = [name, strength, lifes, intelligence, agility, profession]
            break
        elif choice == "W":
            profession = "Warrior"
            strength = 8
            lifes = 8
            intelligence = 2
            agility = 5
            hero_stats = [name, strength, lifes, intelligence, agility, profession]
            break
        else:
            print("Wrong input! Please enter: M, A or W")

    return hero_stats


def get_hero_statistics(hero_stats):
    """Takes hero statistics and returns them in a tuple"""

    name = hero_stats[0]
    strength = hero_stats[1]
    lifes = hero_stats[2]
    intelligence = hero_stats[3]
    agility = hero_stats[4]
    profession = hero_stats[5]

    return name, strength, lifes, intelligence, agility, profession


def print_hero_statistics(hero_stats):

    print("")
    print("_____________________")
    print("Name: %s" % hero_stats[0])
    print("Profession: %s" % hero_stats[5])
    print("Strenght: %s" % hero_stats[1])
    print("Intelligence: %s" % hero_stats[3])
    print("Agility: %s" % hero_stats[4])
    print("Lifes: %s" % hero_stats[2])
    print("_____________________")
