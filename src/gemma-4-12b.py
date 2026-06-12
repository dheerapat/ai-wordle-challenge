import random

# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
RESET = '\033[0m'

# A small sample word list (In a real game, you'd load a .txt file with thousands of words)
WORDS = ["APPLE", "BEACH", "BRAIN", "CLOUD", "DANCE", "EARTH", "FLAME",
          "GRAPE", "HOUSE", "INDEX", "JUICE", "KNIFE", "LIGHT", "MUSIC",
          "NIGHT", "OCEAN", "PIANO", "QUEEN", "RIVER", "SMILE", "TIGER",
          "UNDER", "VOICE", "WATER", "YOUNG", "ZEBRA"]

def get_feedback(guess, secret):
    """
    Compares guess to secret word and returns a list of colored letters.
    Handles duplicate letters correctly.
    """
    result = [""] * 5
    secret_list = list(secret)
    guess_list = list(guess)

    # First pass: Find Greens (Correct letter, correct spot)
    for i in range(5):
        if guess_list[i] == secret_list[i]:
            result[i] = f"{GREEN}{guess_list[i]}{RESET}"
            secret_list[i] = None  # Mark as used so it's not counted for yellow
            guess_list[i] = None

    # Second pass: Find Yellows (Correct letter, wrong spot)
    for i in range(5):
        if guess_list[i] is not None:
            if guess_list[i] in secret_list:
                result[i] = f"{YELLOW}{guess_list[i]}{RESET}"
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = f"{GRAY}{guess_list[i]}{RESET}"

    return "".join(result)

def play_game():
    secret_word = random.choice(WORDS).upper()
    attempts = 6

    print("--- PYTHON WORDLE CLI ---")
    print("Guess the 5-letter word in 6 tries.")
    print("Colors: Green (Right spot), Yellow (Wrong spot), Gray (Not in word)\n")

    for i in range(1, attempts + 1):
        guess = input(f"Attempt {i}/{attempts}: ").upper()

        # Validation
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue

        # Get feedback
        feedback = get_feedback(guess, secret_word)
        print(feedback)

        if guess == secret_word:
            print(f"\n🎉 Congratulations! You guessed it: {secret_word}")
            break

        if i == attempts:
            print(f"\n GAME OVER. The word was: {secret_word}")

if __name__ == "__main__":
    play_game()
