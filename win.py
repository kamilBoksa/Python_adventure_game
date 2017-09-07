def display_win_screen():

    file_name = open("win_screen.txt")
    win_screen = file_name.read()
    win_screen = win_screen.replace("=", "\033[32m=\033[0m")
    win_screen = win_screen.replace("|", "\033[32m=\033[0m")
    print(win_screen)
    file_name.close()


def main():
    display_win_screen()


if __name__ == "__main__":
    main()
