def display_loose_screen():

    file_name = open("loose_screen.txt")
    loose_screen = file_name.read()
    loose_screen = loose_screen.replace("=", "\033[31m=\033[0m")
    loose_screen = loose_screen.replace("|", "\033[31m|\033[0m")
    print(loose_screen)
    file_name.close()


def main():
    display_loose_screen()


if __name__ == "__main__":
    main()
