import random
import win
import loose

def instruction():
    print("Welcome to boss fight")
    print("The rules are like this")
    print("I will think of 3-digits number")
    print("If none of the digits is in the numer the hint is cold")
    print("If the digit is in in the number - the hint is warm")
    print("If the digit is in the number and on a correct spot - the hint is hot")
    print("You will die anyway")


def choosing():
    first_digit = random.randint(1, 9)
    second_digit = random.randint(0, 9)
    third_digit = random.randint(0, 9)
    while (first_digit == second_digit) or (second_digit == third_digit) or (first_digit == third_digit):
        first_digit = str(random.randint(1, 9))
        second_digit = str(random.randint(0, 9))
        third_digit = str(random.randint(0, 9))
    return first_digit, second_digit, third_digit


def user_guessing(first_digit, second_digit, third_digit):
    tries = 10
    while tries > 0:
        user_guess = input("Enter the number")

        if user_guess.isalpha():
            print("Enter only digits")
        elif len(user_guess) != 3:
            print("try again")
        else:
            user_guess = list(user_guess)
            print(user_guess)
            if (int(user_guess[0]) == first_digit) and (int(user_guess[1])==second_digit) and (int(user_guess[2]) == third_digit):
                print("You win")
                win.main()
            if (int(user_guess[0]) == first_digit) or (int(user_guess[1]) == second_digit) or (int(user_guess[2]) == third_digit):
                print("Hot")
            if (str(first_digit) in user_guess) or (second_digit in user_guess) or (third_digit in user_guess):
                print("warm")
            else:
                print("cold")
        tries -= 1
    else:
        print("You loose")
        loose.main()


def main():
    instruction()
    first_digit, second_digit, third_digit = choosing()
    user_guessing(first_digit, second_digit, third_digit)

if __name__ == '__main__':
    main()
