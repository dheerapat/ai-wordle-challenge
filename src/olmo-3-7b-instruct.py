import random

# List of short words (5 letters), you can expand this!
WORDS = ["crane", "stone", "flint", "glade", "beach", "march", "plump", "slate"]
SECRET_WORD = random.choice(WORDS).lower()

guesses_left = 6  # Like original Wordle: 6 tries

print("🎲 WORDLE-STYLE CLI GAME 🧠")
print("Guess a 5-letter word. After each try, you'll get feedback:")
print(
    "• 🔵 : correct letter in the right place\n"
    "• ⚪ : wrong or not in word\n"
    "• 🟡 : correct letter in the wrong place (but exists elsewhere)"
)

while guesses_left > 0:
    guess = (
        input(f"\nYour turn! Guess a 5-letter word (#{'*'*(guesses_left)}): ")
        .lower()
        .strip()
    )

    if len(guess) != 5 or not guess.isalpha():
        print("Please enter a valid 5-letter word with only letters!")
        continue

    feedback = ["🟨"] * 5  # Start all as gray (not in word yet)

    # Check for correct letters in the right places (green)
    for i in range(5):
        if guess[i] == SECRET_WORD[i]:
            feedback[i] = "🔵"

    # Remove already green letters from consideration for yellow
    used = [i for i, c in enumerate(feedback) if c == "🔵"]
    temp_feedback = ["⚪"] * 5

    # Check for correct letter in wrong places (yellow)
    for i in range(5):
        if SECRET_WORD[i] not in used and guess[i] in SECRET_WORD:
            for j in range(5):
                if SECRET_WORD[j] == guess[i] and j not in used:
                    temp_feedback[j] = "🟡"
                    break  # Mark only one yellow per letter (simple version)

    # Replace any remaining ⚪ with nothing (or just keep as ⚪)
    for i in range(5):
        if feedback[i] == "⚪" and temp_feedback[i] != "🟡":
            temp_feedback[i] = ""  # Or leave blank, or you can use space

    # Display feedback
    print("".join([f"{feedback[i]}{' ' if c else ''}" for i, c in enumerate(feedback)]))
    print(
        "".join([f"{temp_feedback[i]} " if temp_feedback[i] else "" for i in range(5)])
    )

    # Give hints to user
    correct = sum(1 for a, b in zip(feedback, SECRET_WORD) if a == "🔵")
    wrong_right_letter = sum(
        1 for a, b in zip(guess, SECRET_WORD) if b in guess and a != "🔵"
    )
    print(
        f"\nFeedback: {correct} correct letters in the right place. {wrong_right_letter} correct letter(s) elsewhere."
    )

    # Check win or lose
    if guess == SECRET_WORD:
        print("✅ You guessed it! 🎉")
        break

    guesses_left -= 1
    print(f"Guesses left: {guesses_left}\n")

else:
    print(f"\nGame over. The word was: {SECRET_WORD}")
