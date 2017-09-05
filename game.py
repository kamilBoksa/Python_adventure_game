import os
from time import sleep
import sys
import tty
import termios


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def import_map(filename, imported_list):

    with open(filename) as board:
        for item in board:
            item = item.strip('\n')
            item = list(item)
            imported_list.append(item)

    return imported_list


def print_map(imported_list):
    os.system('clear')
    for n in imported_list:
        print(''.join(n))


def show_title(filename):
    title = []

    for item in open(filename):
        item = item.strip('\n')
        title.append(item)

    for n in title:
        print(''.join(n))


def story_printer():

<<<<<<< HEAD
    lines = ["======================================================================",
            "|                                                                    |",
            "|   You were born in a small village Miszkolc as a farmer's son.      |",
            "|Your life was running smoothly from day to day until that happened! |",
            "|                                                                    |",
            "|   In the evening, coming back from hunting, you saw the smoke      |",
            "|rising in the distance over your village.                           |",
            "|On the spot you found your family and other people murdered.        |",
            "|                                                                    |",
            "|Among the fallen you recognized the bandits from the north.         |",
            "|Bloody Zorka is their leader.                                       |",
            "|                                                                    |",
            "|   You swore revenge, now you need to be prepared to face the       |",
            "|bandits and their boss. Get ready for the adventure!                |",
            "|                                                                    |",
            "======================================================================"]

    for line in lines:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.02)
        print('')
=======
    lines = open("historia.txt").readlines()
    for c in lines:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.2)
    print('')
>>>>>>> 1f4c30261b69e1c8660e188ad140247ddb1ff490


def insert_player_to_game_map(player, imported_list):
    position_x = 1
    position_y = 1
    imported_list[position_y][position_x] = player
    print_map(imported_list)


def check_collision(imported_list, next_x, next_y):

    if imported_list[next_y][next_x] == ".":
        return True
    else:
        return False


def move_player(player, imported_list):
    position_x = 1
    position_y = 1
    next_x = 1
    next_y = 1

    move = True
    while move:
        control = getch()
        if control == "a":
            next_x = next_x - 1
        elif control == "d":
            next_x = next_x + 1
        elif control == "w":
            next_y = next_y - 1
        elif control == "s":
            next_y = next_y + 1
        elif control == "x":
            exit()

        if check_collision(imported_list, next_x, next_y) is True:
            imported_list[position_y][position_x] = "."
            imported_list[next_y][next_x] = "@"
            position_y = next_y
            position_x = next_x
            print_map(imported_list)
            sleep(0.1)
        else:
            print("You cant move there!")
            next_x = position_x
            next_y = position_y


def create_hero():
    name = input("Tell me your name: ")
    print("You have 3 paths to choose", name)
    classes =open("classes.txt").read()
    print(classes)
    choice = input ("If you like to be mage press m, for archer a and for warrrio w")
    if choice == "m":
        print('You are a mage')
        streght = 3
        lifes = 5
        inteligence = 10
    elif choice == "a":
        print("You are an archer")
        streght = 5
        lifes = 10
        inteligence = 7
    elif choice == "w":
        print("You are a warrior")
        streght = 7
        lifes = 8
        inteligence = 5  
    else:
        create_hero()

    return name, streght, lifes, inteligence


def main():
    imported_list = []
    player = '@'
    show_title('game_title.txt')
<<<<<<< HEAD
    #story_printer()
=======
    name, streght, lifes, inteligence = create_hero()
    print(streght)
    story_printer()
>>>>>>> 1f4c30261b69e1c8660e188ad140247ddb1ff490
    import_map('game_board.txt', imported_list)
    insert_player_to_game_map(player, imported_list)
    move_player(player, imported_list)
    print_map(imported_list)


main()
