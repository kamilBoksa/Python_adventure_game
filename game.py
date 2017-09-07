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
    """Reads key in terminal without pressing Enter button"""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def import_map(filename, imported_list):
    """Imports game board from file and colours specific characters"""

    with open(filename) as board:
        for element in board:
            element = element.strip('\n')
            element = list(element)
            imported_list.append(element)

        for row in range(len(imported_list)):
            for column in range(len(imported_list[row])):
                if imported_list[row][column] == "#":
                    imported_list[row][column] = imported_list[row][column].replace("#", "\033[95m#\33[0m")
                elif imported_list[row][column] == "$":
                    imported_list[row][column] = imported_list[row][column].replace("$", "\033[93m$\33[0m")
                elif imported_list[row][column] == "^":
                    imported_list[row][column] = imported_list[row][column].replace("^", "\033[32m^\033[0m")
                elif imported_list[row][column] == "=":
                    imported_list[row][column] = imported_list[row][column].replace("=", "\033[34m=\033[0m")
                elif imported_list[row][column] == "B":
                    imported_list[row][column] = imported_list[row][column].replace("B", "\033[96mB\033[0m")
                elif imported_list[row][column] == "|":
                    imported_list[row][column] = imported_list[row][column].replace("|", "\033[31m|\033[0m")
                elif imported_list[row][column] == "_":
                    imported_list[row][column] = imported_list[row][column].replace("_", "\033[31m_\033[0m")

    return imported_list


def print_map(imported_list):
    """Displays game board"""

    os.system('clear')
    display_key_tips()
    for element in imported_list:
        print(''.join(element))


def show_game_title():
    """Displays game title"""

    title = []

    file_name = open('game_title.txt')

    for line in file_name:
        line = line.strip('\n')
        title.append(line)

    for line in title:
        print(''.join(line))

    file_name.close()


def story_printer():
    """Displays game story"""

    file_name = open("story.txt")
    lines = file_name.readlines()
    for char in lines:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.2)
    print('')

    file_name.close()


def insert_player_to_game_board(player, imported_list):
    """Sets player to the starting position on the map"""

    position_x = 1
    position_y = 1
    imported_list[position_y][position_x] = player
    print_map(imported_list)


def check_collision(imported_list, next_x, next_y):
    """Informs about the symbols after which player can move"""

    interactive_symbols = ["\033[31m|\033[0m", "\033[93m$\33[0m", ".", "A", "S", "\033[96mB\033[0m", "M", ">"]
    if imported_list[next_y][next_x] in interactive_symbols:
        return True
    else:
        return False


def begin_fight(is_fight):

    if is_fight is True:
        print("You are facing an enemy! Only one of you will survive!")
        time.sleep(2)


def fight_mechanic(player_stats):
    """Carries out the mechanics of fighting with the enemy
    Indexes description:
    1 == hero_strength
    2 == hero_lifes
    3 == hero_intelligence
    4 == hero_agility
    5 == hero_profession"""

    hero_lifes = player_stats[2]
    if player_stats[5] == "Mage":
        bonus_attack = player_stats[3]
    elif player_stats[5] == "Archer":
        bonus_attack = player_stats[4]
    elif player_stats[5] == "Warrior":
        bonus_attack = player_stats[1]

    enemy_lifes = 5
    os.system('clear')
    print("Bandit: Come and face your destiny poor hero!")

    while True:
        perform_attack = input("Press A to attack enemy! ")
        if perform_attack == "A" or perform_attack == "a":
            hero_roll = random.randint(0, 10) + bonus_attack
            enemy_roll = random.randint(0, 15)
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


def player_actions(player, imported_list, next_y, next_x, player_stats, inventory):
    """Carries out the mechanics of player moving, collecting items and displaying inventory and  hero statistics
    Indexes description:
    1 == hero_strength
    3 == hero_intelligence
    4 == hero_agility"""

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
            elif imported_list[next_y][next_x] == "\033[93m$\33[0m":
                hero_inventory.add_to_inventory(inventory, 'Gold coin', 1, 1, 'Collectable')
            elif imported_list[next_y][next_x] == "A":
                hero_inventory.add_to_inventory(inventory, 'Axe', 1, 12, 'Weapon')
                player_stats[1] += 3
            elif imported_list[next_y][next_x] == "S":
                hero_inventory.add_to_inventory(inventory, 'Staff', 1, 5, 'Weapon')
                player_stats[3] += 3
            elif imported_list[next_y][next_x] == "\033[96mB\033[0m":
                hero_inventory.add_to_inventory(inventory, 'Bow', 1, 7, 'Weapon')
                player_stats[4] += 3
            elif imported_list[next_y][next_x] == "M":
                begin_fight(True)
                fight_mechanic(player_stats)

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


def display_how_to_play():

    file_name = open("how_to_play.txt")
    how_to_play = file_name.read()
    print(how_to_play)
    file_name.close()


def play_again():
    """Allows user to repeat the game"""

    again = input("Do you want to play again? y or n: ")
    again = again.lower()
    if again == "y":
        os.system("clear")
        game_core()
    elif again == "n":
        print("Goodbye")
        file_name = open("credits.txt")
        credits = file_name.read()
        print(credits)
        file_name.close()
        quit()
    else:
        "Enter correct answer!"
        play_again()


def game_core():
    """Conducts the main gameplay process"""

    imported_map_1 = []
    imported_map_2 = []
    player = '@'
    show_game_title()
    import_map('game_board.txt', imported_map_1)
    import_map('game_board2.txt', imported_map_2)
    next_y = 1
    next_x = 1
    inventory = []

    story_printer()
    display_how_to_play()
    player_stats = hero_creator.create_hero()
    start_time = time.time()
    # Gameplay on the first map
    insert_player_to_game_board(player, imported_map_1)
    player_actions(player, imported_map_1, next_y, next_x, player_stats, inventory)
    # Gameplay on the second map
    insert_player_to_game_board(player, imported_map_2)
    player_actions(player, imported_map_2, next_y, next_x, player_stats, inventory)
    # End game
    stop_time = time.time()
    game_time = stop_time - start_time
    export_score.export_statistics('hallOfFame.txt', player_stats, inventory, game_time)


def main():

    game_core()
    play_again()


if __name__ == '__main__':
    main()
