import game
import os


def win_display():

    win_screen = open("win_screen.txt").read()
    win_screen = win_screen.replace("=", "\033[32m=\033[0m")
    print(win_screen)
    again = input("Do you want to play again? y or n")
    
    if again == "y":
        os.system("clear")
        game.main()
    elif again == "n":
        print("Goodbye")
        quit()
    else:
        win_display()


def main():
    win_display()


if __name__ == "__main__":
    main()
