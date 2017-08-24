def import_map(filename):
    imported_list = []
    flatted_list = []

    for item in open(filename):
        item = item.strip('\n')
        imported_list.append(item)

    for n in imported_list:
        print(''.join(n))


def main():

    import_map('game_board.txt')

main()
