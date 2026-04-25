import random
import sys

# ANSI escape codes for terminal colors
GREEN  = '\033[92m'
YELLOW = '\033[93m'
GRAY   = '\033[90m'
RESET  = '\033[0m'

# Sample word list (expand or load from a file for production)
WORDS = [
    "APPLE", "BEACH", "BRAIN", "BREAD", "BRUSH", "CHAIR", "CHEST", "CHORD", "CLICK", "CLOCK",
    "CLOUD", "DANCE", "DIARY", "DRINK", "DRIVE", "EARTH", "FEAST", "FIELD", "FRUIT", "GLASS",
    "GRAPE", "GREEN", "GHOST", "HEART", "HOUSE", "JUICE", "LIGHT", "LEMON", "MELON", "MONEY",
    "MUSIC", "NIGHT", "OCEAN", "PARTY", "PIANO", "PHONE", "PILOT", "PLANE", "PLANT", "PLATE",
    "POUND", "POWER", "RADAR", "RADIO", "RIVER", "ROBOT", "ROCKY", "SHADE", "SHAPE", "SHEEP",
    "SHIRT", "SHOES", "SHOOT", "SKULL", "SLICE", "SMILE", "SMOKE", "SNAKE", "SPACE", "SPOON",
    "SPORT", "STORM", "STORY", "STOVE", "SUGAR", "SWEET", "TABLE", "TASTE", "TIGER", "TRAIN",
    "TRUCK", "WATCH", "WATER", "WHIST", "WHITE", "WOMAN", "WORLD", "WRITE", "YOUTH"
]

def get_feedback(target, guess):
    """
    Generate Wordle-style feedback.
    Returns a list of 5 colored characters matching the guess.
    """
    feedback = [''] * 5
    target_counts = {}
    for char in target:
        target_counts[char] = target_counts.get(char, 0) + 1

    # First pass: mark exact matches (green)
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = f"{GREEN}{guess[i]}{RESET}"
            target_counts[guess[i]] -= 1

    # Second pass: mark present but wrong position (yellow) or absent (gray)
    for i in range(5):
        if feedback[i]:  # Already marked green
            continue
        if guess[i] in target_counts and target_counts[guess[i]] > 0:
            feedback[i] = f"{YELLOW}{guess[i]}{RESET}"
            target_counts[guess[i]] -= 1
        else:
            feedback[i] = f"{GRAY}{guess[i]}{RESET}"

    return feedback

def play():
    """Main game loop."""
    target = random.choice(WORDS)
    max_attempts = 6
    attempts = 0
    won = False

    print("🎯 WELCOME TO CLI WORDLE 🎯")
    print("Guess the hidden 5-letter word in 6 attempts.\n")
    print(f" {GREEN}█{RESET} = Correct letter & position")
    print(f" {YELLOW}█{RESET} = Correct letter, wrong position")
    print(f" {GRAY}█{RESET} = Letter not in word\n")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: ").strip().upper()

        # Input validation
        if not (len(guess) == 5 and guess.isalpha() and guess.isascii()):
            print("❌ Invalid input. Please enter exactly 5 English letters.\n")
            continue

        feedback = get_feedback(target, guess)
        print(' '.join(feedback))
        print()

        attempts += 1

        if guess == target:
            won = True
            break

    if won:
        print(f"🎉 Congratulations! You guessed '{target}' in {attempts} attempt(s)!")
    else:
        print(f"😞 Game Over! The word was '{target}'")

    # Replay option
    while True:
        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay in ('y', 'yes'):
            play()
            return
        elif replay in ('n', 'no'):
            print("Thanks for playing! Goodbye! 👋")
            return
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\n👋 Game interrupted. Thanks for playing!")
        sys.exit(0)
