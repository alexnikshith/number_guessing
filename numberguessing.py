import random
from colorama import init, Fore, Style
import time

# Initialize colorama
init(autoreset=True)

# Global variables
high_score = None

def welcome():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*50)
    print("🎮 WELCOME TO THE ULTIMATE NUMBER GUESSING GAME 🎮".center(50))
    print("="*50)
    print(Fore.YELLOW + "\nInstructions:")
    print("→ I will think of a number, and you must guess it.")
    print("→ I will tell you if your guess is too high or too low.")
    print("→ Choose difficulty: Easy, Medium, or Hard.\n")

def choose_difficulty():
    print(Fore.MAGENTA + "\nSelect difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    while True:
        choice = input(Fore.CYAN + "\nEnter your choice (1/2/3): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print(Fore.RED + "Invalid input. Please choose 1, 2, or 3.")

def play_game():
    global high_score

    number = random.randint(1, 100)
    attempts_allowed = choose_difficulty()
    attempts_taken = 0

    print(Fore.YELLOW + f"\nI have picked a number between 1 and 100. Can you guess it? You have {attempts_allowed} attempts.")

    while attempts_taken < attempts_allowed:
        try:
            guess = int(input(Fore.GREEN + f"\n🔢 Attempt {attempts_taken + 1}/{attempts_allowed} - Enter your guess: "))
        except ValueError:
            print(Fore.RED + "❌ Invalid input! Please enter a number.")
            continue

        attempts_taken += 1

        if guess < number:
            print(Fore.BLUE + "📉 Too low! Try a higher number.")
        elif guess > number:
            print(Fore.MAGENTA + "📈 Too high! Try a lower number.")
        else:
            print(Fore.GREEN + Style.BRIGHT + f"\n🎉 Correct! You guessed it in {attempts_taken} attempts!")
            if high_score is None or attempts_taken < high_score:
                high_score = attempts_taken
                print(Fore.CYAN + "🏆 New High Score!")
            break
    else:
        print(Fore.RED + Style.BRIGHT + f"\n💥 You've used all your attempts. The number was {number}.")

def show_high_score():
    if high_score is not None:
        print(Fore.LIGHTYELLOW_EX + f"\n🔥 Current High Score: {high_score} attempts")
    else:
        print(Fore.LIGHTYELLOW_EX + "\n🚫 No high score yet. Play to set one!")

def main_menu():
    welcome()
    while True:
        print(Fore.LIGHTBLUE_EX + "\nMain Menu:")
        print("1. Play Game")
        print("2. Show High Score")
        print("3. Exit")

        choice = input(Fore.CYAN + "\nEnter your choice: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            show_high_score()
        elif choice == '3':
            print(Fore.YELLOW + "\nThanks for playing! Goodbye! 👋")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

        time.sleep(1)
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()
