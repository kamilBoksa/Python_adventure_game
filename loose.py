import game
import os


def loose_display():
    loose_screen = open("loose_screen.txt").read()
    loose_screen = loose_screen.replace("=", "\033[31m=\033[0m")
    print(loose_screen)
    again = input("Do you want to play again? y or n")
    if again == "y":
        os.system("clear")
        game.main()
    elif again == "n":
        print("Goodbye")
        quit()
    else:
        loose_display()


def main():
    loose_display()


if __name__ == "__main__":
    main()
