import random
from colorama import Fore, Back, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)


def get_feedback(guess, secret):
    """
    Compares the guess with the secret word and returns a colored string.
    """
    result = [""] * 5
    secret_list = list(secret)
    guess_list = list(guess)

    # First pass: Find the Greens (Correct position)
    for i in range(5):
        if guess_list[i] == secret_list[i]:
            result[i] = Back.GREEN + Fore.WHITE + f" {guess_list[i]} " + Style.RESET_ALL
            secret_list[i] = None  # Mark as used so it's not counted for yellow
            guess_list[i] = None

    # Second pass: Find the Yellows (Wrong position)
    for i in range(5):
        if guess_list[i] is not None:  # Skip if already marked Green
            if guess_list[i] in secret_list:
                result[i] = (
                    Back.YELLOW + Fore.BLACK + f" {guess_list[i]} " + Style.RESET_ALL
                )
                # Remove the first occurrence of this letter from secret_list
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = (
                    Back.RESET + Fore.WHITE + f" {guess_list[i]} " + Style.RESET_ALL
                )
                # In most terminals, Back.RESET isn't "grey",
                # so we can use a different approach for grey if needed.
                # On many terminals, the default background is dark enough.
                # To make it look like Wordle, let's use a dark grey background:
                result[i] = (
                    Back.BLACK + Fore.WHITE + f" {guess_list[i]} " + Style.RESET_ALL
                )

    return "".join(result)


def play_game():
    # A small sample word list. In a real game, you'd load a large text file.
    word_bank = [
        "APPLE",
        "BEACH",
        "BRAIN",
        "CLOUD",
        "DRIVE",
        "EARTH",
        "FLAME",
        "GRAPE",
        "HOUSE",
        "INDEX",
        "JUICE",
        "KNIFE",
        "LEMON",
        "MOUSE",
        "NIGHT",
        "OCEAN",
        "PIANO",
        "QUEEN",
        "RIVER",
        "SNAKE",
        "TABLE",
        "UNION",
        "VOICE",
        "WATER",
        "YACHT",
        "ZEBRA",
    ]

    secret_word = random.choice(word_bank).upper()
    attempts = 6
    guessed_words = []

    print("\n" + "=" * 30)
    print("  WELCOME TO CLI WORDLE!  ")
    print("=" * 30)
    print("Guess the 5-letter word. You have 6 tries.\n")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").upper()
            if len(guess) == 5 and guess.isalpha():
                break
            print("Invalid input! Please enter exactly 5 letters.")

        feedback = get_feedback(guess, secret_word)
        guessed_words.append(feedback)

        # Clear screen (simulated) and print board
        print("\n" * 2)
        for g in guessed_words:
            print(g)
        print("\n")

        if guess == secret_word:
            print(
                Fore.GREEN + f"Congratulations! You guessed it in {attempt} tries! 🎉"
            )
            return

    print(Fore.RED + f"Game Over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()
