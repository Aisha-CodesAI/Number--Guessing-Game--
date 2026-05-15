import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

SCORE_FILE = "scores.txt"


def save_score(name, score, difficulty):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{name} | {difficulty} | Score: {score}\n")


def view_scoreboard():
    print(Fore.CYAN + "\n========== SCOREBOARD ==========\n")

    try:
        with open(SCORE_FILE, "r") as file:
            data = file.read()

            if data.strip() == "":
                print("No scores available yet.\n")
            else:
                print(data)

    except FileNotFoundError:
        print("Scoreboard file not found.\n")

    print("=" * 35)


def choose_difficulty():

    print(Fore.YELLOW + "\nSelect Difficulty:\n")

    print("1 -> Easy   (10 chances, range 1-50)")
    print("2 -> Medium (7 chances, range 1-100)")
    print("3 -> Hard   (5 chances, range 1-200)")

    while True:
        choice = input("\nEnter choice (1/2/3): ")

        if choice == "1":
            return "Easy", 50, 10, 10

        elif choice == "2":
            return "Medium", 100, 7, 20

        elif choice == "3":
            return "Hard", 200, 5, 30

        else:
            print(Fore.RED + "Invalid choice! Try again.")


def play_game():

    print(Fore.MAGENTA + "\n========== NUMBER NEXUS ==========\n")

    name = input("Enter your name: ")

    difficulty, max_range, chances, base_score = choose_difficulty()

    secret_number = random.randint(1, max_range)

    attempts = 0

    print(Fore.CYAN + f"\nHello {name}!")
    print(f"I'm thinking of a number between 1 and {max_range}")
    print(f"Difficulty: {difficulty}")
    print(f"You have {chances} chances.\n")

    start_time = time.time()

    while attempts < chances:

        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))

        except ValueError:
            print(Fore.RED + "Please enter a valid number!")
            continue

        attempts += 1

        difference = abs(secret_number - guess)

        if guess == secret_number:

            end_time = time.time()

            time_taken = round(end_time - start_time, 2)

            score = (base_score * 10) - (attempts * 2)

            if score < 0:
                score = 0

            print(Fore.GREEN + "\n🎉 CONGRATULATIONS 🎉")
            print(Fore.GREEN + f"You guessed the number {secret_number} correctly!")

            print(Fore.YELLOW + f"Attempts Taken : {attempts}")
            print(Fore.YELLOW + f"Time Taken     : {time_taken} seconds")
            print(Fore.YELLOW + f"Your Score     : {score}")

            save_score(name, score, difficulty)

            break

        elif guess < secret_number:

            if difference <= 5:
                print(Fore.BLUE + "Very Close! Just a little higher.")

            elif difference <= 15:
                print(Fore.BLUE + "Close! Try a higher number.")

            else:
                print(Fore.BLUE + "Too low!")

        else:

            if difference <= 5:
                print(Fore.MAGENTA + "Very Close! Just a little lower.")

            elif difference <= 15:
                print(Fore.MAGENTA + "Close! Try a lower number.")

            else:
                print(Fore.MAGENTA + "Too high!")

        print(Fore.CYAN + f"Remaining chances: {chances - attempts}\n")

    else:
        print(Fore.RED + "\n💀 GAME OVER 💀")
        print(Fore.RED + f"The correct number was: {secret_number}")


while True:

    print(Fore.GREEN + "\n===================================")
    print("         NUMBER NEXUS")
    print("===================================\n")

    print("1 -> Play Game")
    print("2 -> View Scoreboard")
    print("3 -> Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        play_game()

    elif choice == "2":
        view_scoreboard()

    elif choice == "3":
        print(Fore.YELLOW + "\nThank you for playing!")
        print("Exiting game...\n")
        break

    else:
        print(Fore.RED + "Invalid choice! Please try again.")
