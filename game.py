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




def main():
    show_title('game_title.txt')
    import_map('game_board.txt')

main()
