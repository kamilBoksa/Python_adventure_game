<<<<<<< HEAD
from time import sleep
import sys

def import_map(filename):
    imported_list = []
=======
def getkey():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    key = getkey()
    return key
>>>>>>> 9d03774aef8da518bf940b0f57c43e009ccd3354


def import_map(filename, imported_list):

    with open(filename) as board:
        for item in board:
            item = item.strip('\n')
            item = list(item)
            imported_list.append(item)

    return imported_list


def print_map(imported_list):
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

    lines = ["======================================================================",
            "|                                                                    |",
            "|   You were born in a small village Miskolc as a farmer's son.      |",
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

    for line in lines:      # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            time.sleep(0.02)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)

def insert_player_to_game_map(player, imported_list):
    position_column = 1
    position_row = 1
    imported_list[position_column][position_row] = player


def move_player(player, imported_list):
    pass


def main():
    imported_list = []
    player = '@'
    show_title('game_title.txt')
<<<<<<< HEAD
    story_printer()
    import_map('game_board.txt')
=======
    import_map('game_board.txt', imported_list)
    insert_player_to_game_map(player, imported_list)
    print_map(imported_list)
>>>>>>> 9d03774aef8da518bf940b0f57c43e009ccd3354

main()
