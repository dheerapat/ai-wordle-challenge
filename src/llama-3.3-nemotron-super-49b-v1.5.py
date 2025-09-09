import random

def check_guess(guess, target):
    """
    Compares the guess with the target word and returns feedback.
    
    Feedback symbols:
    - '✓' = Correct letter in correct position
    - '!' = Correct letter in wrong position
    - '.' = Incorrect letter
    """
    result = [None] * 5
    target_letters = list(target)
    guess_letters = list(guess)

    # First pass: Check for correct letters in correct positions
    for i in range(5):
        if guess_letters[i] == target_letters[i]:
            result[i] = '✓'
            target_letters[i] = None  # Mark as used

    # Second pass: Check for correct letters in wrong positions
    for i in range(5):
        if result[i] is None and guess_letters[i] in target_letters:
            result[i] = '!'
            # Find and mark the first occurrence in target_letters
            j = target_letters.index(guess_letters[i])
            target_letters[j] = None

    return result

def display_result(guess, result):
    """
    Displays the guess and its feedback in a readable format.
    """
    for letter, feedback in zip(guess, result):
        symbol = '✓' if feedback == '✓' else '!' if feedback == '!' else '.'
        print(f"{letter} {symbol}", end=' ')
    print()

def main():
    # List of 5-letter words (can be expanded or read from a file)
    words = ["apple", "basic", "crate", "dance", "elate", "flame", "grape", "honey", "ideal", "jolly"]
    target = random.choice(words)
    max_attempts = 6
    attempts = 0

    print("Welcome to Wordle CLI!")
    print("Guess the 5-letter word. You have 6 attempts.")
    print("✓ = Correct letter in correct position")
    print("! = Correct letter in wrong position")
    print(". = Incorrect letter")
    print("-" * 30)

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: Enter your 5-letter guess: ").lower()

        # Input validation
        if len(guess) != 5:
            print("Error: Please enter a 5-letter word.")
            continue
        if not guess.isalpha():
            print("Error: Please enter only alphabetic characters.")
            continue

        # Check the guess
        result = check_guess(guess, target)
        display_result(guess, result)

        # Check for win
        if all(r == '✓' for r in result):
            print("Congratulations! You guessed the word!")
            break

        attempts += 1
    else:
        print(f"Game over! The word was '{target}'.")

if __name__ == "__main__":
    main()
