import os
from time import sleep
import sys
import tty
import termios
import hero_creator
import hero_inventory
import hot_warm_cold


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
        for element in board:
            element = element.strip('\n')
            element = list(element)
            imported_list.append(element)

    return imported_list


def print_map(imported_list):
    os.system('clear')
    display_key_tips()
    for element in imported_list:
        print(''.join(element))


def show_title(filename):
    title = []

    for line in open(filename):
        line = line.strip('\n')
        title.append(line)

    for line in title:
        print(''.join(line))


def story_printer():

    lines = open("story.txt").readlines()
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
    interactive_symbols = ".>|$MASB"
    if imported_list[next_y][next_x] in interactive_symbols:
        return True
    else:
        return False


def switch_board1_to_board2(imported_list, next_y, next_x):
    if imported_list[next_y][next_x] == ">":
        return True
    else:
        return False


def move_player(player, imported_list, next_y, next_x, player_stats, inventory):
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
        elif control == "q":
            hero_creator.print_hero_statistics(player_stats)
        elif control == "i":
            hero_inventory.print_table(inventory)
        elif control == "x":
            exit()

        if check_collision(imported_list, next_x, next_y) is True:
            if imported_list[next_y][next_x] == ">":
                break

            elif imported_list[next_y][next_x] == "$":
                hero_inventory.add_to_inventory(inventory,'Gold coin', 1, 1, 'Collectable')
            elif imported_list[next_y][next_x] == "A":
                hero_inventory.add_to_inventory(inventory,'Axe', 1, 12, 'Weapon')
            elif imported_list[next_y][next_x] == "S":
                hero_inventory.add_to_inventory(inventory,'Staff', 1, 5, 'Weapon')
            elif imported_list[next_y][next_x] == "B":
                hero_inventory.add_to_inventory(inventory,'Bow', 1, 7, 'Weapon')
            elif imported_list[next_y][next_x] == "|":
                hot_warm_cold.main()
                break

            imported_list[position_y][position_x] = "."
            imported_list[next_y][next_x] = "@"
            position_y = next_y
            position_x = next_x
            print_map(imported_list)
            sleep(0.1)
        elif check_collision(imported_list, next_x, next_y) is False and control in "wasd":
            print("You cant move there!")
            next_x = position_x
            next_y = position_y


def display_credits():
    credits = open("credits.txt").read()
    print(credits)


def display_key_tips():
    print("W,S,A,D - move hero  ||  X - quit game  ||  I - inventory  || Q - statistics ")
    print(" ")


def win_display():
    win_screen = open("win_screen.txt").read()
    print(win_screen)
    again = input("Do you want to play again? y or n")
    if again == "y":
        print("ok")
    elif again == "n":
        print("Goodbye")
    else:
        win_display()


def loose_display():
    loose_screen = open("loose_screen.txt").read()
    print(loose_screen)
    again = input("Do you want to play again? y or n")
    if again == "y":
        print("ok")  # wywolanie maina??
    elif again == "n":
        print("Goodbye")
    else:
        win_display()


def how_to_play():
    how_to_play = open("how_to_play.txt").read()
    print(how_to_play)


def game_core():
    imported_map_1 = []
    imported_map_2 = []
    player = '@'
    show_title('game_title.txt')
    import_map('game_board.txt', imported_map_1)
    import_map('game_board2.txt', imported_map_2)
    next_y = 1
    next_x = 1
    inventory = []

    story_printer()
    how_to_play()
    player_stats = hero_creator.create_hero()

    insert_player_to_game_board(player, imported_map_1)
    move_player(player, imported_map_1, next_y, next_x, player_stats, inventory)
    print_map(imported_map_1)

    insert_player_to_game_board(player, imported_map_2)
    move_player(player, imported_map_2, next_y, next_x, player_stats, inventory)

    print_map(imported_map_2)


def main():
    game_core()


if __name__ == '__main__':
    main()
