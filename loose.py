def loose_display():

    file = open("loose_screen.txt").read()
    loose_screen = file.read()
    loose_screen = loose_screen.replace("=", "\033[31m=\033[0m")
    loose_screen = loose_screen.replace("|", "\033[31m|\033[0m")
    print(loose_screen)
    file.close()


def main():
    loose_display()


if __name__ == "__main__":
    main()
