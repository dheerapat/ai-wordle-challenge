import random
import sys

# --- Configuration ---
ATTEMPTS_ALLOWED = 6
WORD_LENGTH = 5

# A small list of common 5-letter words for the game
WORD_LIST = [
    "apple", "brave", "crane", "drain", "eager", "flame", "grape", "house",
    "index", "jolly", "knife", "lemon", "mango", "night", "ocean", "piano",
    "quiet", "river", "snake", "train", "unity", "vivid", "water", "xenon",
    "yacht", "zebra", "alert", "argue", "beach", "begin", "brain", "bread",
    "brush", "chair", "chest", "dance", "dress", "exist", "final", "focus",
    "force", "horse", "large", "laugh", "light", "money", "mount", "north",
    "paper", "party", "peace", "point", "power", "press", "price", "print",
    "quick", "raise", "ratio", "reply", "right", "round", "scene", "sense",
    "share", "sheet", "shift", "shirt", "shock", "sight", "skill", "sleep",
    "smile", "sound", "south", "space", "speed", "spend", "sport", "squad",
    "staff", "stage", "stand", "start", "state", "steam", "steel", "stick",
    "still", "stock", "stone", "store", "study", "stuff", "style", "sugar",
    "table", "teach", "thank", "theme", "thing", "title", "total", "touch",
    "trial", "trust", "truth", "uncle", "union", "value", "video", "virus",
    "visit", "voice", "waste", "watch", "wheel", "white", "woman", "world",
    "worry", "would", "write", "wrong", "young", "youth"
]

# --- ANSI Color Codes ---
class Colors:
    RESET = '\033[0m'
    GREEN = '\033[42m\033[30m'  # Green background, Black text
    YELLOW = '\033[43m\033[30m' # Yellow background, Black text
    GRAY = '\033[47m\033[30m'   # Light Gray background, Black text

def clear_screen():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def print_title():
    print(f"{Colors.GREEN} WORDLE CLI {Colors.RESET}")
    print(f"Guess the {WORD_LENGTH}-letter word in {ATTEMPTS_ALLOWED} attempts.")
    print("Green = Correct spot | Yellow = Wrong spot | Gray = Not in word\n")

def process_guess(target, guess):
    """
    Compares the guess against the target word.
    Returns a list of tuples: (letter, color_code)
    """
    result = []
    target_chars = list(target)
    guess_chars = list(guess)

    # Initialize result list with placeholders
    # 0 = gray (default), 1 = green, 2 = yellow
    statuses = [0] * WORD_LENGTH

    # 1. Check for exact matches (GREEN) first
    for i in range(WORD_LENGTH):
        if guess_chars[i] == target_chars[i]:
            statuses[i] = 1
            target_chars[i] = None  # Mark as used

    # 2. Check for misplaced letters (YELLOW)
    for i in range(WORD_LENGTH):
        if statuses[i] == 1:
            continue # Already marked green

        current_char = guess_chars[i]
        if current_char in target_chars:
            statuses[i] = 2
            # Remove the char from target pool so it isn't matched twice
            target_chars.remove(current_char)

    # Build the visual output
    for i, char in enumerate(guess):
        if statuses[i] == 1:
            result.append(f"{Colors.GREEN} {char.upper()} {Colors.RESET}")
        elif statuses[i] == 2:
            result.append(f"{Colors.YELLOW} {char.upper()} {Colors.RESET}")
        else:
            result.append(f"{Colors.GRAY} {char.upper()} {Colors.RESET}")

    return result

def validate_input(user_input):
    """Ensures input is a 5-letter alphabetic string."""
    if len(user_input) != WORD_LENGTH:
        print(f"Word must be exactly {WORD_LENGTH} letters.")
        return False
    if not user_input.isalpha():
        print("Input must only contain letters.")
        return False
    return True

def main():
    target_word = random.choice(WORD_LIST).lower()
    attempts = 0
    history = [] # To store the string blocks of previous guesses

    while attempts < ATTEMPTS_ALLOWED:
        clear_screen()
        print_title()

        # Print history
        for line in history:
            print(line)

        # Calculate remaining attempts
        remaining = ATTEMPTS_ALLOWED - attempts
        print(f"\nAttempts remaining: {remaining}")

        # Get user input
        try:
            guess = input(f"Enter guess ({WORD_LENGTH} letters): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGame exited.")
            return

        # Validate
        if not validate_input(guess):
            input("Press Enter to continue...")
            continue

        # Logic
        colored_result = process_guess(target_word, guess)
        result_str = "".join(colored_result)
        history.append(result_str)
        attempts += 1

        # Win condition
        if guess == target_word:
            clear_screen()
            print_title()
            for line in history:
                print(line)
            print(f"\n{Colors.GREEN}Congratulations! You won!{Colors.RESET}")
            return

    # Lose condition
    clear_screen()
    print_title()
    for line in history:
        print(line)
    print(f"\nGame Over. The word was: {target_word.upper()}")

if __name__ == "__main__":
    main()
