def loose_display():

    loose_screen = open("loose_screen.txt").read()
    loose_screen = loose_screen.replace("=", "\033[31m=\033[0m")
    print(loose_screen)


def main():
    loose_display()


if __name__ == "__main__":
    main()
