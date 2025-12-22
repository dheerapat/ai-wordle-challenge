import random

# A small list of 5-letter words for the game. In a real implementation, you'd want a more comprehensive list.
WORD_LIST = [
    "CRANE",
    "GRIND",
    "AUDIO",
    "WIDER",
    "SHEEP",
    "PLUMB",
    "FOCUS",
    "HONEST",
    "MINIM",
    "EXIST",
    "APPLE",
    "BEACH",
    "CITY",
    "DANCE",
    "EARTH",
    "FROST",
    "GRASS",
    "HOUSE",
    "ISLAND",
    "JOY",
]


def get_feedback(target_word, guess):
    """
    Generate feedback for a guess compared to the target word.
    Returns a string with colored letters indicating correct positions (green),
    correct letters in wrong positions (yellow), and incorrect letters (gray).
    """
    # Initialize all letters as gray
    feedback = ["\033[90m" + letter + "\033[0m" for letter in guess]

    target_list = list(target_word)

    # First pass: mark exact matches (green)
    correct_positions = set()
    for i, letter in enumerate(guess):
        if letter == target_list[i]:
            feedback[i] = f"\033[92m{letter}\033[0m"
            correct_positions.add(i)
            # Mark this position as used by setting it to None
            target_list[i] = None

    # Count remaining letters in the target word (excluding greens)
    from collections import defaultdict

    remaining_counts = defaultdict(int)
    for letter in target_list:
        if letter is not None:  # Not already matched by green
            remaining_counts[letter] += 1

    # Second pass: mark yellows and grays
    for i, letter in enumerate(guess):
        if i not in correct_positions and letter in remaining_counts:
            if remaining_counts[letter] > 0:
                feedback[i] = f"\033[93m{letter}\033[0m"
                remaining_counts[letter] -= 1
            # else: remains gray (no action needed as it's already gray)
        # Green positions are already handled

    return "".join(feedback)


def validate_guess(guess):
    """Validate that the guess is exactly 5 letters and all alphabetic."""
    if len(guess) != 5:
        return False
    if not guess.isalpha():
        return False
    return True


def play_wordle():
    print("Welcome to Wordle!")
    print("Guess the word. You have 6 attempts.")
    print("Each letter will be marked as follows:")
    print("- Green: correct letter in the correct position")
    print("- Yellow: correct letter but wrong position (and not duplicated elsewhere)")
    print("- Gray: incorrect letter or already used correctly")
    print("\nEnter your guesses one at a time. You can see previous attempts.")
    print("Type 'quit' to exit the game.\n")

    target_word = random.choice(WORD_LIST).upper()
    attempts_left = 6
    attempts = []

    while attempts_left > 0:
        if not attempts:
            print(
                f"Attempt {len(attempts) + 1} of {attempts_left}: ", end="", flush=True
            )
        else:
            # Print previous attempt(s) for reference
            for i, attempt in enumerate(attempts):
                print(f"{i + 1}. {attempt}")
            print(
                f"Attempt {len(attempts) + 1} of {attempts_left}: ", end="", flush=True
            )

        guess = input().strip().upper()

        if guess.lower() == "quit":
            print("\nThanks for playing!")
            return

        if not validate_guess(guess):
            print("Invalid input. Please enter exactly 5 letters.")
            continue

        feedback = get_feedback(target_word, guess)
        attempts.append(feedback)

        # Print the feedback with proper spacing
        print(f"  {feedback}")

        if target_word == guess:
            print("\nCongratulations! You guessed the word correctly!")
            return

        attempts_left -= 1
        if attempts_left == 0:
            print("\nGame over! The word was:", target_word)
            return

    # This line is theoretically unreachable due to the above returns, but included for completeness.
    print("Thanks for playing!")


if __name__ == "__main__":
    play_wordle()
