import random
from collections import Counter

WORD_LENGTH = 5
MAX_GUESSES = 6

WORDS = [
    "apple", "grape", "lemon", "mango", "peach",
    "berry", "melon", "chair", "table", "plant",
    "house", "water", "light", "sound", "music",
    "stone", "bread", "flame", "cloud", "earth",
    "river", "smile", "dream", "heart", "train",
    "plane", "mouse", "brain", "green", "black",
    "white", "brown", "sugar", "spice", "candy"
]

GREEN = "\033[42m\033[30m"
YELLOW = "\033[43m\033[30m"
GRAY = "\033[47m\033[30m"
RESET = "\033[0m"


def print_intro():
    print("=" * 32)
    print("        WORDLE CLI GAME")
    print("=" * 32)
    print(f"Guess the {WORD_LENGTH}-letter word.")
    print(f"You have {MAX_GUESSES} guesses.")
    print()
    print("Colors:")
    print(f"{GREEN} A {RESET} Correct letter, correct spot")
    print(f"{YELLOW} A {RESET} Correct letter, wrong spot")
    print(f"{GRAY} A {RESET} Letter not in word")
    print()


def get_guess():
    while True:
        guess = input("Enter guess: ").lower().strip()

        if len(guess) != WORD_LENGTH:
            print(f"Your guess must be {WORD_LENGTH} letters long.")
            continue

        if not guess.isalpha():
            print("Your guess must contain only letters.")
            continue

        return guess


def color_guess(guess, answer):
    result = [None] * WORD_LENGTH
    answer_counts = Counter(answer)

    # First pass: mark correct letters in correct positions.
    for i in range(WORD_LENGTH):
        if guess[i] == answer[i]:
            result[i] = GREEN
            answer_counts[guess[i]] -= 1

    # Second pass: mark correct letters in wrong positions or absent letters.
    for i in range(WORD_LENGTH):
        if result[i] is not None:
            continue

        if guess[i] in answer_counts and answer_counts[guess[i]] > 0:
            result[i] = YELLOW
            answer_counts[guess[i]] -= 1
        else:
            result[i] = GRAY

    colored = ""
    for i in range(WORD_LENGTH):
        colored += f"{result[i]} {guess[i].upper()} {RESET}"

    return colored


def play_game():
    answer = random.choice(WORDS)

    print_intro()

    for attempt in range(1, MAX_GUESSES + 1):
        print(f"Guess {attempt}/{MAX_GUESSES}")
        guess = get_guess()

        print(color_guess(guess, answer))
        print()

        if guess == answer:
            print("You got it!")
            print(f"The word was: {answer.upper()}")
            return

    print("Game over!")
    print(f"The word was: {answer.upper()}")


if __name__ == "__main__":
    play_game()
