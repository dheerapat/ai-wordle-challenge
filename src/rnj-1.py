import random

def choose_word(word_list, length):
    """Choose a random word from the list with the correct length."""
    filtered_words = [word for word in word_list if len(word) == length]
    return random.choice(filtered_words)

def get_feedback(guess, secret_word):
    """Get feedback about the guess compared to the secret word."""
    # Correct letters in the right position
    green_letters = []
    # Correct letters in the wrong position
    yellow_letters = []

    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            green_letters.append(letter)
        elif letter in secret_word:
            yellow_letters.append(letter)

    return green_letters, yellow_letters

def display_feedback(green_letters, yellow_letters):
    """Display the feedback to the user."""
    print("Green letters (correct position):", " ".join(set(green_letters)))
    print("Yellow letters (wrong position):", " ".join(set(yellow_letters)))

def play_wordle(word_list, word_length=5, max_attempts=6):
    """Main function to play Wordle-like game."""
    secret_word = choose_word(word_list, word_length)
    attempts = 0

    print(f"Welcome to the Wordle-like game! You have {max_attempts} attempts to guess a {word_length}-letter word.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()

        if len(guess) != word_length:
            print(f"Word must be {word_length} letters long. Try again.")
            continue

        green_letters, yellow_letters = get_feedback(guess, secret_word)
        display_feedback(green_letters, yellow_letters)

        attempts += 1

        if set(secret_word) == set(guess):
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The word was: {secret_word}")

if __name__ == "__main__":
    # A small list of words to choose from for simplicity.
    word_list = ["apple", "grape", "peach", "melon", "berry", "lemon", "mango"]

    play_wordle(word_list)
