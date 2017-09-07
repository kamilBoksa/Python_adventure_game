def win_display():

    file = open("win_screen.txt")
    win_screen = file.read()
    win_screen = win_screen.replace("=", "\033[32m=\033[0m")
    win_screen = win_screen.replace("|", "\033[32m=\033[0m")
    print(win_screen)
    file.close()


def main():
    win_display()


if __name__ == "__main__":
    main()
