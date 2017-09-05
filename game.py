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

    lines = open("historia.txt").readlines()
    for c in lines:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.2)
    print('')


def insert_player_to_game_board(player, imported_list):
    position_x = 1
    position_y = 1
    imported_list[position_y][position_x] = player
    print_map(imported_list)


def check_collision(imported_list, next_x, next_y):

    if imported_list[next_y][next_x] == "." or imported_list[next_y][next_x] == ">":
        return True
    else:
        return False


def switch_board1_to_board2(imported_list, position_x, position_y):
    if imported_list[position_y, position_x] == ">":
        return True
    else:
        return False


def move_player(player, imported_list, next_y, next_x):
    position_y = 1
    position_x = 1

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
    os.system('clear')
    print("You have 3 paths to choose", name)
    classes = open("classes.txt").read()
    print(classes)
    choice = input("If you like to be mage press m, for archer a and for warrrior")
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
    imported_map_1 = []
    imported_map_2 = []
    player = '@'
    show_title('game_title.txt')
    import_map('game_board.txt', imported_map_1)
    import_map('game_board2.txt', imported_map_2)
    next_y = 1
    next_x = 1

    story_printer()
    name, streght, lifes, inteligence = create_hero()

    insert_player_to_game_board(player, imported_map_1)
    move_player(player, imported_map_1, next_y, next_x)
    print_map(imported_map_1)

    if switch_board1_to_board2(imported_map1, next_y, next_x):
        insert_player_to_game_board(player. imported_map_2)
        move_player(player, imported_map_2)
        print_map(imported_map_2)


main()
