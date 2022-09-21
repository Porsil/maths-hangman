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




def main():
    """
    Run all program functions
    """
    game_header()
    game_menu()
    choice = get_game_type()
    game_option(choice)



main()

