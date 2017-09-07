def win_display():

    win_screen = open("win_screen.txt").read()
    win_screen = win_screen.replace("=", "\033[32m=\033[0m")
    print(win_screen)


def main():
    win_display()


if __name__ == "__main__":
    main()
