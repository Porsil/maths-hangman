import random

def game_header():
    """
    Prints the game title and rules to the board
    """
    print("\n*******************")
    print("*  MATHS HANGMAN  *")
    print("*******************\n")
    print("How to play:")
    print("   Select desired maths questions from the game options")
    print("   You will be given 15 questions to answer")
    print("   Each incorrect answer will add to the hangman")
    print("   Answer all questions before the hangman is complete to win")


def game_menu():
    """
    Prints the game menu options to the board
    """
    menu_1 = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Quit"]
    print("\nGame options:")
    print("   " + menu_1[0])
    print("   " + menu_1[1])
    print("   " + menu_1[2])
    print("   " + menu_1[3])
    print("   " + menu_1[4])


def get_game_type():
    """
    Asks the user for their choice of game type and validates the data
    """
    while True:
        try:
            game_type = int(input("\nEnter an option to play: "))
            if game_type <= 0 or game_type > 5:
                print("\nNot a valid game option. Enter a number between 1 and 5.")
            else:
                return game_type
        except ValueError:
            print("\nNot a valid game option. Enter a number between 1 and 5.")


def difficulty_menu():
    """
    Prints the game difficulty options to the board
    """
    menu_2 = ["1. Easy", "2. Medium", "3. Hard", "4. Quit"]
    print("\nDifficulty options:")
    print("   " + menu_2[0])
    print("   " + menu_2[1])
    print("   " + menu_2[2])
    print("   " + menu_2[3])


def get_game_difficulty():
    """
    Asks the user for their choice of game difficulty and validates the data
    """
    while True:
        try:
            game_difficulty = int(input("\nEnter an option to play: "))
            if game_difficulty <= 0 or game_difficulty > 4:
                print("\nNot a valid game option. Enter a number between 1 and 4.")
            else:
                return game_difficulty
        except ValueError:
            print("\nNot a valid game option. Enter a number between 1 and 4.")


def game_message(game_type, game_difficulty):
    """
    Displays a message to inform user of game choices
    """
    if game_type == 1 and game_difficulty == 1:
        print("\nYou have selected Addition - Easy")
    elif game_type == 1 and game_difficulty == 2:
        print("\nYou have selected Addition - Medium")
    elif game_type == 1 and game_difficulty == 3:
        print("\nYou have selected Addition - Hard")
    elif game_type == 2 and game_difficulty == 1:
        print("\nYou have selected Subtraction - Easy")
    elif game_type == 2 and game_difficulty == 2:
        print("\nYou have selected Subtraction - Medium")
    elif game_type == 2 and game_difficulty == 3:
        print("\nYou have selected Subtraction - Hard")
    elif game_type == 3 and game_difficulty == 1:
        print("\nYou have selected Multiplication - Easy")
    elif game_type == 3 and game_difficulty == 2:
        print("\nYou have selected Multiplication - Medium")
    elif game_type == 3 and game_difficulty == 3:
        print("\nYou have selected Multiplication - Hard")
    elif game_type == 4 and game_difficulty == 1:
        print("\nYou have selected Division - Easy")
    elif game_type == 4 and game_difficulty == 2:
        print("\nYou have selected Division - Medium")
    elif game_type == 4 and game_difficulty == 3:
        print("\nYou have selected Division - Hard")


def ask_question(game_type, game_difficulty, increment, total):
    """
    Gets 2 random numbers from get_numbers functions,
    prints the appropriate maths question
    and calculates the correct answer
    """
    if game_type == 1:
        number_one = get_numbers_add_sub(game_difficulty)
        number_two = get_numbers_add_sub(game_difficulty)
        question = str(number_one) + " + " + str(number_two) + " ="
        solution = number_one + number_two
    elif game_type == 2:
        number_one = get_numbers_add_sub(game_difficulty)
        number_two = get_numbers_add_sub(game_difficulty)
        question = str(max(number_one, number_two)) + " - " + str(min(number_one, number_two)) + " ="
        solution = max(number_one, number_two) - min(number_one, number_two)
    elif game_type == 3:
        number_one = get_numbers_mult_div(game_difficulty)
        number_two = get_numbers_mult_div(game_difficulty)
        question = str(number_one) + " x " + str(number_two) + " ="
        solution = number_one * number_two
    elif game_type == 4:
        number_one = get_numbers_mult_div(game_difficulty)
        number_two = get_numbers_mult_div(game_difficulty)
        question = str(number_one * number_two) + " / " + str(number_two) + " ="
        solution = (number_one * number_two) / number_two
    user_solution = get_answer(total, question)
    increment = check_solution(user_solution, solution, increment)
    return increment


def get_numbers_add_sub(game_difficulty):
    """
    Gets 2 random numbers for the addition and subtraction
    game types, dependant on the difficulty selected
    """
    if game_difficulty == 1:
        number = random.randrange(1, 26)
        return number
    elif game_difficulty == 2:
        number = random.randrange(1, 101)
        return number
    elif game_difficulty == 3:
        number = random.randrange(1, 501)
        return number


def get_numbers_mult_div(game_difficulty):
    """
    Gets 2 random numbers for the multiplication and division
    game types, dependant on the difficulty selected
    """
    if game_difficulty == 1:
        number = random.randrange(1, 13)
        return number
    elif game_difficulty == 2:
        number = random.randrange(1, 26)
        return number
    elif game_difficulty == 3:
        number = random.randrange(1, 51)
        return number


def get_answer(total, question):
    """
    Asks the user for their answer
    """
    print(f"\nQuestion {total}:   {question}", end=" ")
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
        solution = round(solution)
        print(f"\nIncorrect, the correct answer is {solution}.")
        return increment


def hangman(incorrect):
    """
    Prints the hangman with a new body part
    everytime an answer is incorrect
    """
    if incorrect == 1:
        print("_____")
        print("|   O")
        print("|")
        print("|")
        print("|_____")
    elif incorrect == 2:
        print("_____")
        print("|   O")
        print("|   |")
        print("|")
        print("|_____")
    elif incorrect == 3:
        print("_____")
        print("|   O")
        print("|  /|")
        print("|")
        print("|_____")
    elif incorrect == 4:
        print("_____")
        print("|   O")
        print("|  /|\ ")
        print("|")
        print("|_____")
    elif incorrect == 5:
        print("_____")
        print("|   O")
        print("|  /|\ ")
        print("|  /")
        print("|_____")
    elif incorrect == 6:
        print("_____")
        print("|   O")
        print("|  /|\ ")
        print("|  / \ ")
        print("|_____")


def give_results(total, correct, incorrect):
    """
    Gives the user the final scores at the end of game play
    """
    percentage = round((correct / total) * 100)
    if incorrect == 6:
        print(f"\nYou lost! Better luck next time!")
        print(f"Final score: {correct}/{total}. Percentage: {percentage}%.")
    else:
        print(f"\nCongratulations! You beat The Hangman!")
        print(f"Final score: {correct}/{total}. Percentage: {percentage}%")


def play_again():
    """
    Asks the user if they want to play the game again
    Re-plays the game is y is answered
    Ends the game if n is answered
    """
    while True:
        print(f"\nPlay Again? (y/n)", end = " ")
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


def game_play(game_type, game_difficulty, total, correct, incorrect):
    """
    Loops through questions until the hangman is full
    or 15 questions have been answered
    """
    while incorrect < 6 and total < 15:
        total = total + 1
        correct = ask_question(game_type, game_difficulty, correct, total)
        incorrect = total - correct
        hangman(incorrect)
        if incorrect == 6 or total == 15:
            give_results(total, correct, incorrect)
        else:
            print(f"Score: {correct}/{total}")


def main():
    """
    Run all program functions
    """
    play_game = True
    while play_game == True:  
        total = 0
        correct = 0
        incorrect = 0
        game_header()
        game_menu()
        game_type = get_game_type()
        if game_type == 5:
            play_game = end_game()
        else:
            difficulty_menu()
            game_difficulty = get_game_difficulty()
            if game_difficulty == 4:
                play_game = end_game()
            else:
                game_message(game_type, game_difficulty)
                game_play(game_type, game_difficulty, total, correct, incorrect)
                play_game = play_again()

    
main()

