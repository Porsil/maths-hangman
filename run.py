"""
Python code for Maths Hangman:
A terminal based maths game
"""

# Import libraries
import random
import time


def game_header():
    """
    Prints the game title and rules to the board
    """
    # Game title generated using
    # https://patorjk.com/software/taag/#p=display&f=Standard&t=
    # %20%20%20%20%20%20Maths%0AHangman
    game_title = ("                 __  __       _   _                      \n"
                  "                |  \/  | __ _| |_| |__  ___              \n"
                  "                | |\/| |/ _` | __| '_ \/ __|             \n"
                  "           _   _| |  | | (_| | |_| | | \__ \             \n"
                  "          | | | |_|_ |_|\__,_|\__|_| |_|___/  __ _ _ __  \n"
                  "          | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n"
                  "          |  _  | (_| | | | | (_| | | | | | | (_| | | | |\n"
                  "          |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n"
                  "                             |___/\n")
    game_rules = ("How to play: \n"
                  "   Select desired maths questions from the options given\n"
                  "   Select desired difficulty from the options given\n"
                  "   You will be given 15 questions to answer\n"
                  "   Each incorrect answer will add to the hangman\n"
                  "   Answer all questions before the hangman is"
                  " complete to win")
    print(game_title + game_rules)
    print_line()


def print_line():
    print("___________________________________________________________________"
          "____________")


def game_menu():
    """
    Prints the game menu options to the board
    """
    types = ["1. Addition", "2. Subtraction", "3. Multiplication",
             "4. Division", "5. Quit"]

    print("Game options:")
    for type in types:
        print("   " + type)


def get_game_type():
    """
    Asks the user for their choice of game type and validates the data
    """
    while True:
        try:
            game_type = int(input("\nEnter an option to play: "))
            if game_type <= 0 or game_type > 5:
                print("\nNot a valid game option. "
                      "Enter a number between 1 and 5.")
            else:
                return game_type
        except ValueError:
            print("\nNot a valid game option. Enter a number between 1 and 5.")


def difficulty_menu():
    """
    Prints the game difficulty options to the board
    """
    difficulties = ["1. Easy", "2. Medium", "3. Hard", "4. Quit"]

    print("Difficulty options:")
    for difficulty in difficulties:
        print("   " + difficulty)


def get_game_difficulty():
    """
    Asks the user for their choice of game difficulty and validates the data
    """
    while True:
        try:
            game_difficulty = int(input("\nEnter an option to play: "))
            if game_difficulty <= 0 or game_difficulty > 4:
                print("\nNot a valid game option."
                      "Enter a number between 1 and 4.")
            else:
                return game_difficulty
        except ValueError:
            print("\nNot a valid game option. Enter a number between 1 and 4.")


def game_message(game_type, game_difficulty):
    """
    Retrieves the game type and difficulty and
    displays a message to inform user of game choices
    """
    if game_type == 1:
        game_type = "Addition"
    elif game_type == 2:
        game_type = "Subtraction"
    elif game_type == 3:
        game_type = "Multiplication"
    elif game_type == 4:
        game_type = "Division"

    if game_difficulty == 1:
        game_difficulty = "Easy"
    elif game_difficulty == 2:
        game_difficulty = "Medium"
    elif game_difficulty == 3:
        game_difficulty = "Hard"

    print(f"\nYou have selected {game_type} - {game_difficulty}")


def game_play(game_type, game_difficulty, total, correct, incorrect):
    """
    Loops through questions until the hangman is full
    or 15 questions have been answered and
    calculates the time taken to play the game
    """
    start_time = time.time()
    while incorrect < 6 and total < 15:
        total = total + 1
        correct = ask_question(game_type, game_difficulty, correct, total)
        incorrect = total - correct
        hangman(incorrect)
        if incorrect == 6 or total == 15:
            give_results(total, correct, incorrect)
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
        else:
            print(f"Score: {correct}/{total}\n")
            print_line()


def ask_question(game_type, game_difficulty, increment, total):
    """
    Gets 2 random numbers from get_numbers functions,
    prints the appropriate maths question
    and calculates the correct answer
    """
    number_one, number_two = get_numbers(game_type, game_difficulty)

    if game_type == 1:
        question = str(number_one) + " + " + str(number_two) + " ="
        solution = number_one + number_two
    elif game_type == 2:
        question = (str(max(number_one, number_two)) + " - " +
                    str(min(number_one, number_two)) + " =")
        solution = max(number_one, number_two) - min(number_one, number_two)
    elif game_type == 3:
        question = str(number_one) + " x " + str(number_two) + " ="
        solution = number_one * number_two
    elif game_type == 4:
        question = (str(number_one * number_two) + " / " +
                    str(number_two) + " =")
        solution = (number_one * number_two) / number_two

    user_solution = get_answer(total, question)
    increment = check_solution(user_solution, solution, increment)

    return increment


def get_numbers(game_type, game_difficulty):
    """
    Gets 2 random numbers for the addition and subtraction
    game types, dependant on the difficulty selected
    """
    if game_difficulty == 1:
        if game_type in (1, 2):
            number_one = random.randrange(1, 26)
            number_two = random.randrange(1, 26)
        else:
            number_one = random.randrange(1, 13)
            number_two = random.randrange(1, 13)
    if game_difficulty == 2:
        if game_type in (1, 2):
            number_one = random.randrange(51, 251)
            number_two = random.randrange(25, 251)
        else:
            number_one = random.randrange(6, 26)
            number_two = random.randrange(2, 26)
    if game_difficulty == 3:
        if game_type in (1, 2):
            number_one = random.randrange(101, 501)
            number_two = random.randrange(50, 501)
        else:
            number_one = random.randrange(11, 51)
            number_two = random.randrange(3, 51)

    return number_one, number_two


def get_answer(total, question):
    """
    Asks the user for their answer and validates the data
    """
    while True:
        try:
            print(f"\nQuestion {total}:   {question}", end=" ")
            result = int(input(""))
            return result
        except ValueError:
            print("\nNot a valid input. Answers should be a whole number:")


def check_solution(user_solution, solution, increment):
    """
    Checks the users answer and returns correct or incorrect
    """
    if user_solution == solution:
        print("\nCorrect")
        increment = increment + 1
        return increment
    else:
        solution = round(solution)
        print(f"\nIncorrect, the correct answer is {solution}.")
        return increment


def hangman(incorrect):
    """
    Prints the hangman with a new body part
    everytime an answer is incorrect
    """
    if incorrect == 0:
        print("_____\n"
              "|\n"
              "|\n"
              "|\n"
              "|_____")
    elif incorrect == 1:
        print("_____\n"
              "|   O\n"
              "|\n"
              "|\n"
              "|_____")
    elif incorrect == 2:
        print("_____\n"
              "|   O\n"
              "|   |\n"
              "|\n"
              "|_____")
    elif incorrect == 3:
        print("_____\n"
              "|   O\n"
              "|  /|\n"
              "|\n"
              "|_____")
    elif incorrect == 4:
        print("_____\n"
              "|   O\n"
              "|  /|\ \n"
              "|\n"
              "|_____")
    elif incorrect == 5:
        print("_____\n"
              "|   O\n"
              "|  /|\ \n"
              "|  /\n"
              "|_____")
    elif incorrect == 6:
        print("_____\n"
              "|   O\n"
              "|  /|\ \n"
              "|  / \ \n"
              "|_____")


def give_results(total, correct, incorrect):
    """
    Gives the user the final scores at the end of game play
    """
    percentage = round((correct / total) * 100)
    if incorrect == 6:
        print(f"\nYou lost! Better luck next time!\n"
              f"\nFinal score: {correct}/{total}\nPercentage: {percentage}%")
    else:
        print(f"\nCongratulations! You beat The Hangman!\n"
              f"\nFinal score: {correct}/{total}\nPercentage: {percentage}%")


def time_convert(sec):
    """
    Converts the time taken to play the game into hh:mm:ss
    """
    # Code adapted from
    # https://www.codespeedy.com/how-to-create-a-stopwatch-in-python/
    # and https://stackoverflow.com/questions/3505831/
    # in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
    mins = sec // 60
    sec = int(sec % 60)
    hours = int(mins // 60)
    mins = int(mins % 60)
    print(f"Time: {hours:02}:{mins:02}:{sec:02}")


def play_again():
    """
    Asks the user if they want to play the game again and validates the answer
    Re-plays the game is y is answered
    Ends the game if n is answered
    """
    while True:
        print(f"\nPlay Again? (y/n)", end=" ")
        play_again = (input(""))
        if play_again == "y" or play_again == "Y":
            play_again = True
            return play_again
        elif play_again == "n" or play_again == "N":
            play_again = end_game()
            return False
        else:
            print("\nNot a valid option. Please enter y for yes or n for no.")


def end_game():
    """
    Ends the game
    """
    print("\nThank-you for playing Maths Hangman!\n")
    return False


def main():
    """
    Run all program functions
    """
    play_game = True
    while play_game is True:
        total = 0
        correct = 0
        incorrect = 0
        game_header()
        game_menu()
        game_type = get_game_type()
        if game_type == 5:
            play_game = end_game()
        else:
            game_header()
            difficulty_menu()
            game_difficulty = get_game_difficulty()
            if game_difficulty == 4:
                play_game = end_game()
            else:
                game_header()
                game_message(game_type, game_difficulty)
                game_play(game_type, game_difficulty,
                          total, correct, incorrect)
                play_game = play_again()


if __name__ == '__main__':
    main()
