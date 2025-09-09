#!/usr/bin/env python3
"""
wordle_cli.py
Simple Wordle-like command-line game.
Usage: python wordle_cli.py
"""
import random
import sys

# --- Small built-in lists (replace/expand as you like) ---
ANSWERS = [
    "crane","slice","trace","shard","grace","plane","flint","blaze","pride","smile",
    "cough","light","sound","cheap","beach","candy","swing","bloom","faint","scent",
    "stone","night","water","cloud","laugh","train","drive","build","watch","spark"
]

# allowed guesses - combine answers + some common 5-letter words
ALLOWED = sorted(set(ANSWERS + [
    "about","other","which","their","there","apple","match","bring","young","panel",
    "staff","again","under","could","where","house","brown","fight","worry","often",
    "piano","guilt","purge","spite","gamer","quiet","group","spend","study","glide"
]))

# ANSI color helpers
RESET = "\033[0m"
GREEN_BG = "\033[30;42m"   # black text on green background
YELLOW_BG = "\033[30;43m"  # black text on yellow background
GRAY_BG = "\033[37;100m"   # white text on bright black (gray) background

def print_colored(letters, statuses):
    """Print letters with colored backgrounds based on statuses list."""
    out = []
    for ch, s in zip(letters, statuses):
        if s == "green":
            out.append(f"{GREEN_BG} {ch.upper()} {RESET}")
        elif s == "yellow":
            out.append(f"{YELLOW_BG} {ch.upper()} {RESET}")
        else:
            out.append(f"{GRAY_BG} {ch.upper()} {RESET}")
    print(" ".join(out))

def evaluate_guess(solution, guess):
    """
    Returns statuses for each position: "green", "yellow", or "gray".
    Implements Wordle's letter-count-aware logic:
      1) Mark greens first.
      2) For remaining letters in guess, mark yellow only if that letter still
         appears unmatched in the solution.
    """
    assert len(solution) == len(guess) == 5
    statuses = ["gray"] * 5
    sol_chars = list(solution)
    # First pass: greens
    for i, (s_ch, g_ch) in enumerate(zip(sol_chars, guess)):
        if g_ch == s_ch:
            statuses[i] = "green"
            sol_chars[i] = None  # consume

    # Second pass: yellows
    for i, g_ch in enumerate(guess):
        if statuses[i] == "gray":
            try:
                j = sol_chars.index(g_ch)
            except ValueError:
                # not present (or already consumed)
                continue
            statuses[i] = "yellow"
            sol_chars[j] = None  # consume
    return statuses

def input_guess(allowed):
    """Prompt user for a guess; enforce 5 letters and membership in allowed list."""
    while True:
        guess = input("Enter your 5-letter guess: ").strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            print(" → Guess must be exactly 5 letters (a–z). Try again.")
            continue
        if guess not in allowed:
            print(" → Word not in allowed word list. Try another word.")
            # show a hint for user convenience:
            if guess not in ALLOWED:
                print("   (You can add more words to the ALLOWED list in the script.)")
            continue
        return guess

def play_round():
    solution = random.choice(ANSWERS)
    attempts = 6
    print("Welcome to Wordle-CLI! You have 6 attempts to guess the 5-letter word.")
    # Uncomment for debugging / testing:
    # print(f"(DEBUG: solution is {solution})")
    for turn in range(1, attempts + 1):
        print(f"\nAttempt {turn}/{attempts}")
        guess = input_guess(ALLOWED)
        statuses = evaluate_guess(solution, guess)
        print_colored(guess, statuses)
        if all(s == "green" for s in statuses):
            print(f"\n🎉 You got it in {turn} guess{'es' if turn>1 else ''}! The word was '{solution.upper()}'.")
            break
    else:
        print(f"\n☠️  Out of attempts — the word was '{solution.upper()}'.")
    print()

def main():
    try:
        while True:
            play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if not again.startswith("y"):
                print("Thanks for playing — bye!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
