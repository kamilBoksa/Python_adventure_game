from time import sleep
import sys

def import_map(filename):
    imported_list = []

    for item in open(filename):
        item = item.strip('\n')
        imported_list.append(item)

    for n in imported_list:
        print(''.join(n))


def show_title(filename):
    imported_list = []

    for item in open(filename):
        item = item.strip('\n')
        imported_list.append(item)

    for n in imported_list:
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



def main():
    show_title('game_title.txt')
    story_printer()
    import_map('game_board.txt')

main()
