import random

# Predefined list of 5-letter words (you can expand this)
WORD_LIST = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elder",
    "fudge",
    "grape",
    "honey",
    "juice",
    "kiwi",
    "lemon",
    "mango",
    "nectar",
    "orange",
    "peach",
    "quail",
    "raspberry",
    "strawberry",
    "tangerine",
    "watermelon",
]


def get_feedback(guess, target):
    """Return feedback for each letter in the guess"""
    feedback = ["gray"] * 5
    target_used = [False] * 5  # Track which letters in target are used

    # First pass: check for exact matches (green)
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = "green"
            target_used[i] = True

    # Second pass: check for correct letters in wrong position (yellow)
    for i in range(5):
        if feedback[i] == "gray":
            letter = guess[i]
            for j in range(5):
                if not target_used[j] and letter == target[j]:
                    feedback[i] = "yellow"
                    target_used[j] = True
                    break

    return feedback


def play_game():
    target = random.choice(WORD_LIST).lower()
    print("Welcome to Wordle!")
    print("Guess a 5-letter word. You have 6 attempts.")

    for attempt in range(1, 7):
        guess = input(f"\nAttempt {attempt}/6: ").strip().lower()

        # Validate input
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter a valid 5-letter word.")
            continue

        feedback = get_feedback(guess, target)

        # Display feedback
        for i, color in enumerate(feedback):
            if color == "green":
                print(f"\033[92m{guess[i]}\033[0m", end="")  # Green
            elif color == "yellow":
                print(f"\033[93m{guess[i]}\033[0m", end="")  # Yellow
            else:
                print(f"\033[90m{guess[i]}\033[0m", end="")  # Gray
        print()

        if guess == target:
            print("Congratulations! You guessed the word!")
            return

    print(f"\nSorry, you've used all attempts. The word was: {target}")


if __name__ == "__main__":
    play_game()
