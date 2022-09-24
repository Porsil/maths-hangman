import random

def game_header():
    """
    Prints the game title and rules to the board
    """
    print("*******************")
    print("*  MATHS HANGMAN  *")
    print("*******************\n")
    print("How to play:")
    print("   Select desired maths questions from the game options")
    print("   You will be given 15 questions to answer")
    print("   Each incorrect answer will add to the hangman")
    print("   Answer all questions before the hangman is complete to win\n")


def game_menu():
    """
    Prints the game menu options to the board
    """
    menu = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Quit"]
    print("Game options:")
    print("   " + menu[0])
    print("   " + menu[1])
    print("   " + menu[2])
    print("   " + menu[3])
    print("   " + menu[4])


def get_game_type():
    """
    Asks the user for their choice of game type and validates the data
    """
    while True:
        try:
            game_type = int(input("\nEnter an option to play: "))
            if game_type <= 0 or game_type > 5:
                print("\nNot a valid game option.")
            else:
                return game_type
        except ValueError:
            print("\nNot a valid game option.")


def game_play(index, increment, total):
    """
    Gets 2 random numbers between 1 and 25 and
    prints the appropriate maths question
    """
    if index == 1:
        number_one = random.randrange(1, 26)
        number_two = random.randrange(1, 26)
        question = str(number_one) + " + " + str(number_two) + " ="
        solution = number_one + number_two
    elif index == 2:
        number_one = random.randrange(1, 26)
        number_two = random.randrange(1, 26)
        question = str(max(number_one, number_two)) + " - " + str(min(number_one, number_two)) + " ="
        solution = max(number_one, number_two) - min(number_one, number_two)
    elif index == 3:
        number_one = random.randrange(1, 13)
        number_two = random.randrange(1, 13)
        question = str(number_one) + " x " + str(number_two) + " ="
        solution = number_one * number_two
    elif index == 4:
        number_one = random.randrange(1, 13)
        number_two = random.randrange(1, 13)
        question = str(number_one * number_two) + " / " + str(number_two) + " ="
        solution = (number_one * number_two) / number_two
    user_solution = get_answer(total, question)
    increment = check_solution(user_solution, solution, increment)
    return increment


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
    print(f"\nPlay Again? (y/n)", end = " ")
    play_again = (input(""))
    if play_again == "y" or play_again == "Y":
        return True
    else:
        play_game = end_game()

def end_game():
    print("\nThank-you for playing Maths Hangman!\n")
    return False

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
        choice = get_game_type()
        if choice == 5:
            play_game = end_game()
        else:
            while incorrect < 6 and total < 15:
                total = total + 1
                correct = game_play(choice, correct, total)
                incorrect = total - correct
                hangman(incorrect)
                if incorrect == 6 or total == 15:
                    give_results(total, correct, incorrect)
                else:
                    print(f"Score: {correct}/{total}")
            play_game = play_again()

    



main()

