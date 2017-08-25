import os


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


def insert_player_to_game_map(player, imported_list):
    position_x = 1
    position_y = 1
    imported_list[position_y][position_x] = player
    print_map(imported_list)

def move_player(player, imported_list):
    position_x = 1
    position_y = 1
    key = getkey()

    if getkey == 's':
        imported_list[position_y][position_x] = '.'
        position_y += 1
        imported_list[position_y][position_x] = player
        print_map(imported_list)
    elif getkey == 'd':
    imported_list[position_y][position_x] = '.'
    position_x += 1
    imported_list[position_y][position_x] = player
    print_map(imported_list)



def main():
    imported_list = []
    player = '@'
    show_title('game_title.txt')
    import_map('game_board.txt', imported_list)
    insert_player_to_game_map(player, imported_list)
    move_player(player, imported_list)

main()
