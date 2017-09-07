import random
import win
import loose


def print_instruction():

    print("Hey little Hero ! Wan't to play a game?")
    print("Here are the rules:")
    print("I will think of 3-digits number")
    print("If none of the digits is in the number the hint is cold")
    print("If the digit is in in the number - the hint is warm")
    print("If the digit is in the number and on a correct spot - the hint is hot")
    print("You will die anyway.....but take a try")
    print("")


def get_random_digits():
    correct_answer = []
    while len(correct_answer) < 3:
        digit = random.randint(0, 9)
        if digit not in correct_answer:
            correct_answer.append(digit)
    return correct_answer


def get_user_input():
    while True:
        user_guess = input("Enter number: ")
        if user_guess.isalpha():
            print("Enter digits only!")
        elif len(user_guess) != 3:
            print("You have to enter exactly 3 digits!")
        else:
            return list(user_guess)


def compare_user_input_with_answer(user_guess, correct_answer):
    index = 0
    hint_list = []
    for digit in correct_answer:
        if str(digit) == user_guess[index]:
            hint_list.insert(0, 'Hot')
        elif str(digit) in user_guess:
            hint_list.append("Warm")
        index += 1
    if not hint_list:
        hint_list.append("Cold")
    return hint_list


def check_result(hint_list):
    if hint_list == ["Hot"] * 3:
        return True


def main():
    print_instruction()
    correct_answer = get_random_digits()
    lifes_left = 10
    while lifes_left > 0:
        print("You have %s lifes left!" % lifes_left)
        user_guess = get_user_input()
        result = compare_user_input_with_answer(user_guess, correct_answer)
        print(result)
        if check_result(result):
            print("VICTORY")
            win.main()
            break
        lifes_left -= 1
        if lifes_left == 0:
            print("DEFEAT!")
            print("Correct answer was: %s" % correct_answer)
            loose.main()


if __name__ == '__main__':
    main()
