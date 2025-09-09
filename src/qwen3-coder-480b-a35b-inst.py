import random
import os

# Predefined 5-letter words
WORDS = [
    "APPLE",
    "BRAVE",
    "CLIMB",
    "DREAM",
    "EARTH",
    "FLAME",
    "GLASS",
    "HONEY",
    "IGLOO",
    "JUMBO",
    "KNIFE",
    "LEMON",
    "MAGIC",
    "NIGHT",
    "OCEAN",
    "PIANO",
    "QUILT",
    "RIVER",
    "SNAKE",
    "TIGER",
    "ULTRA",
    "VIVID",
    "WATER",
    "XENON",
    "YACHT",
    "ZEBRA",
]


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def get_feedback(guess, target):
    """
    Generate feedback for the guess:
    - Green: Correct letter in correct position
    - Yellow: Correct letter in wrong position
    - Gray: Letter not in target word
    """
    feedback = ["GRAY"] * 5
    target_letters = list(target)

    # First pass: Check for exact matches (Green)
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = "GREEN"
            target_letters[i] = None  # Mark as used

    # Second pass: Check for partial matches (Yellow)
    for i in range(5):
        if feedback[i] != "GREEN" and guess[i] in target_letters:
            feedback[i] = "YELLOW"
            target_letters[target_letters.index(guess[i])] = None  # Mark as used

    return feedback


def print_colored_guess(guess, feedback):
    """Print the guess with color-coded feedback"""
    colors = {
        "GRAY": "\033[90m",  # Dark gray
        "YELLOW": "\033[93m",  # Yellow
        "GREEN": "\033[92m",  # Green
        "RESET": "\033[0m",  # Reset to default
    }

    colored_output = ""
    for i in range(5):
        colored_output += f"{colors[feedback[i]]}{guess[i]}{colors['RESET']}"

    print(colored_output)


def main():
    target_word = random.choice(WORDS)
    attempts = 6
    guessed_correctly = False

    clear_screen()
    print("Welcome to PyWordle!")
    print("Guess the 5-letter word. You have 6 attempts.")
    print("Feedback: GREEN=Correct position, YELLOW=Wrong position, GRAY=Not in word\n")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").strip().upper()
            if len(guess) != 5:
                print("Please enter exactly 5 letters.")
            elif not guess.isalpha():
                print("Please enter only letters.")
            else:
                break

        feedback = get_feedback(guess, target_word)
        print_colored_guess(guess, feedback)

        if guess == target_word:
            guessed_correctly = True
            print("\nCongratulations! You've guessed the word!")
            break

    if not guessed_correctly:
        print(f"\nGame over! The word was: {target_word}")


if __name__ == "__main__":
    main()
