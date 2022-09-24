import math
import random

def game_header():
    """
    Prints the game title and rules to the board
    """
    title = "\n** Maths Hangman **\n"
    rules = "Game Rules are.....\n"
    print(title)
    print(rules)

def game_menu():
    """
    Prints the game menu options to the board
    """
    menu = ["1. Addition"]
    print("Game options:\n")
    print(menu[0])

def get_game_type():
    """
    Asks the user for their choice of game type and validates the data
    """
    while True:
        try:
            game_type = int(input("\nEnter an option to play: "))
            if game_type <= 0 or game_type > 4:
                print("\nNot a valid game option.")
            else:
                return game_type
        except ValueError:
            print("\nNot a valid game option.")

def get_answer(question):
    """
    Asks the user for their answer
    """
    print("Answer:")
    result = int(input(""))
    return result

def check_solution(user_solution, solution, increment):
    """
    Checks the users answer and returns correct or incorrect
    """
    if user_solution == solution:
        print("\nCorrect")
        increment = increment + 1
        return increment
    else:
        print(f"\nIncorrect. The correct answer is {solution}.")
        return increment

def game_play(index, increment):
    """
    Gets 2 random numbers between 1 and 25 and
    prints the appropriate maths question
    """
    number_one = random.randrange(1, 26)
    number_two = random.randrange(1, 26)
    if index == 1:
        print("\nQuestion:")
        question = str(number_one) + " + " + str(number_two) + " =\n"
        solution = number_one + number_two
        print(question)
        user_solution = get_answer(question)
        increment = check_solution(user_solution, solution, increment)
        return increment
        


def main():
    """
    Run all program functions
    """
    total = 0
    correct = 0
    incorrect = 0
    game_header()
    game_menu()
    choice = get_game_type()
    while incorrect <=5 and total < 15:
        total = total + 1
        correct = game_play(choice, correct)
        incorrect = total - correct
        print(f"Score: {correct}/{total}")
        print(f"Incorrect: {incorrect}")
    if incorrect == 6:
        percentage = round((correct / total) * 100)
        print(f"\nYou lost! Better luck next time!")
        print(f"Final score: {correct}/{total}. Percentage: {percentage}%.")
    else:
        percentage = round((correct / total) * 100)
        print(f"\nCongratulations! You beat The Hangman!")
        print(f"Final score: {correct}/{total}. Percentage: {percentage}%")

    



main()

