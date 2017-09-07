import os
import time
import sys
import tty
import termios
import hero_creator
import hero_inventory
import hot_warm_cold
import win
import loose
import random
import export_score



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

        for i in range(len(imported_list)):
            for x in range(len(imported_list[i])):
                if imported_list[i][x] == "#":
                    imported_list[i][x] = imported_list[i][x].replace("#", "\033[95m#\33[0m")
                elif imported_list[i][x] == "$":
                    imported_list[i][x] = imported_list[i][x].replace("$", "\033[93m$\33[0m")
                elif imported_list[i][x] == "^":
                    imported_list[i][x] = imported_list[i][x].replace("^", "\033[32m^\033[0m")
                elif imported_list[i][x] == "=":
                    imported_list[i][x] = imported_list[i][x].replace("=", "\033[34m=\033[0m")
                elif imported_list[i][x] == "B":
                    imported_list[i][x] = imported_list[i][x].replace("B", "\033[96mB\033[0m")
                elif imported_list[i][x] == "|":
                    imported_list[i][x] = imported_list[i][x].replace("|", "\033[31m|\033[0m")
                elif imported_list[i][x] == "_":
                    imported_list[i][x] = imported_list[i][x].replace("_", "\033[31m_\033[0m")

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
        time.sleep(0.2)
    print('')


def insert_player_to_game_board(player, imported_list):

    position_x = 1
    position_y = 1
    imported_list[position_y][position_x] = player
    print_map(imported_list)


def check_collision(imported_list, next_x, next_y):

    interactive_symbols = ["\033[31m|\033[0m", "\033[93m$\33[0m", ".", "A", "S", "\033[96mB\033[0m", "M", ">"]
    if imported_list[next_y][next_x] in interactive_symbols:
        return True
    else:
        return False


def begin_fight(is_fight):
    if is_fight is True:
        print("You are facing an enemy! Only one of you will survive!")
        time.sleep(2)


def fight_mechanic(imported_list):

    hero_lifes = 10
    enemy_lifes = 5
    os.system('clear')
    print("Bandit: Come and face your destiny poor hero!")

    while True:
        decision = input("Press A to attack enemy! ")
        if decision == "A":
            hero_roll = random.randint(0, 10)
            enemy_roll = random.randint(0, 10)
            print("Your attack power: %s" % hero_roll)
            print("Enemy attack power: %s" % enemy_roll)
            if hero_roll > enemy_roll:
                print("You hardly wounded the enemy!")
                enemy_lifes -= 1
                print("Enemy lifes left: %s" % enemy_lifes)
                print("")
                if enemy_lifes == 0:
                    print("You killed the enemy!")
                    time.sleep(1)
                    break
            elif hero_roll == enemy_roll:
                print("Duce! Enemy parried your attack!")
                print("")
            elif hero_roll < enemy_roll:
                print("You lost one life!")
                hero_lifes -= 1
                print("Lifes left %s" % hero_lifes)
                print("")
                if hero_lifes == 0:
                    print("You died!!")
                    time.sleep(2)
                    loose.main()
                    play_again()
            else:
                continue


def player_actions(player, imported_list, next_y, next_x, player_stats, inventory):

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
            elif imported_list[next_y][next_x] == "\033[93m$\33[0m" :
                hero_inventory.add_to_inventory(inventory,'Gold coin', 1, 1, 'Collectable')
            elif imported_list[next_y][next_x] == "A":
                hero_inventory.add_to_inventory(inventory, 'Axe', 1, 12, 'Weapon')
            elif imported_list[next_y][next_x] == "S":
                hero_inventory.add_to_inventory(inventory,'Staff', 1, 5, 'Weapon')
            elif imported_list[next_y][next_x] == "\033[96mB\033[0m":
                hero_inventory.add_to_inventory(inventory,'Bow', 1, 7, 'Weapon')
            elif imported_list[next_y][next_x] == "M":
                begin_fight(True)
                fight_mechanic(imported_list)

            elif imported_list[next_y][next_x] == "\033[31m|\033[0m":
                hot_warm_cold.main()
                break

            imported_list[position_y][position_x] = "."
            imported_list[next_y][next_x] = "@"
            position_y = next_y
            position_x = next_x
            print_map(imported_list)
            time.sleep(0.1)

        elif check_collision(imported_list, next_x, next_y) is False and control in "wasd":
            print("You cant move there!")
            next_x = position_x
            next_y = position_y


def display_key_tips():
    print("W,S,A,D - move hero  ||  X - quit game  ||  I - inventory  || Q - statistics ")
    print(" ")


def how_to_play():
    how_to_play = open("how_to_play.txt").read()
    print(how_to_play)

def play_again():
    again = input("Do you want to play again? y or n: ")
    if again == "y":
        os.system("clear")
        game_core()
    elif again == "n":
        print("Goodbye")
    else:
        "Enter correct answer!"
        play_again()

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
    start_time = time.time()

    insert_player_to_game_board(player, imported_map_1)
    player_actions(player, imported_map_1, next_y, next_x, player_stats, inventory)

    insert_player_to_game_board(player, imported_map_2)
    player_actions(player, imported_map_2, next_y, next_x, player_stats, inventory)
    stop_time = time.time()
    game_time = stop_time - start_time
    export_score.export_statistics('hallOfFame.txt', player_stats, inventory, game_time)


def main():
    game_core()
    play_again()

if __name__ == '__main__':
    main()
