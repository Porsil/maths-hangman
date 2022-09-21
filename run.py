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
    Asks the user for their choice of game type
    """
    game_type = int(input("\nEnter an option to play: "))
    return game_type

def game_option(index):
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




def main():
    """
    Run all program functions
    """
    game_header()
    game_menu()
    choice = get_game_type()
    game_option(choice)



main()

