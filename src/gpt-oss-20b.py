#!/usr/bin/env python3
"""
wordle.py – A tiny command‑line Wordle clone

Author:   ChatGPT (OpenAI) with a human tweak
License:  MIT (feel free to reuse)

Usage:
    python wordle.py          # play with the embedded word list
    WORDFILE=mydict.txt python wordle.py  # load words from another file
"""

import random
import os
import sys
from pathlib import Path
from collections import Counter

# ------------------------------------------------------------
# 1.  Word list handling
# ------------------------------------------------------------

# A very small built‑in list – replace or extend it as you wish
DEFAULT_WORD_LIST = [
    "apple", "brain", "candy", "delta", "eagle", "fancy", "giant",
    "hotel", "input", "joker", "knock", "lemon", "mango", "naval",
    "ocean", "piano", "queen", "robot", "sugar", "tiger", "ultra",
    "vivid", "whale", "xenon", "yield", "zebra",
]

def load_word_list(fname: Path | None = None) -> list[str]:
    """
    Load a list of 5‑letter words from `fname`.  If the file is missing
    or empty, return the default list.  All words are converted to
    lowercase and stripped of whitespace.
    """
    words = []

    # 1. Try user supplied file via WORDFILE env var
    word_file = os.getenv("WORDFILE")
    if word_file:
        fname = Path(word_file)

    # 2. Load from passed path if exists
    if fname and fname.is_file():
        with fname.open(encoding="utf-8") as f:
            for line in f:
                w = line.strip().lower()
                if len(w) == 5 and w.isalpha():
                    words.append(w)

    # 3. Fallback to defaults if nothing loaded
    if not words:
        words = DEFAULT_WORD_LIST.copy()

    return words

# ------------------------------------------------------------
# 2. Colour codes & helpers
# ------------------------------------------------------------

# ANSI escape sequences for green, yellow, gray, and reset
GREEN  = "\033[1;32m"   # bright green
YELLOW = "\033[1;33m"   # bright yellow
GRAY   = "\033[1;37m"   # bright white (treated as gray)
RESET  = "\033[0m"

# Unicode block characters to represent feedback
# (colour will be applied to the whole block)
SQUARE = "■"

def coloured_square(square: str, colour: str) -> str:
    return f"{colour}{square}{RESET}"

# ------------------------------------------------------------
# 3. Feedback generator
# ------------------------------------------------------------

def generate_feedback(guess: str, target: str) -> list[str]:
    """
    Returns a list of colour markers for a guess:
      GREEN   – correct letter, correct spot
      YELLOW  – correct letter, wrong spot
      GRAY    – letter not in the target
    """
    feedback = [''] * 5
    target_chars = list(target)

    # First pass – greens
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            feedback[i] = GREEN
            target_chars[i] = None  # Mark as used

    # Second pass – yellows
    for i, g in enumerate(guess):
        if feedback[i]:   # already green
            continue
        if g in target_chars:
            feedback[i] = YELLOW
            target_chars[target_chars.index(g)] = None
        else:
            feedback[i] = GRAY

    return feedback

# ------------------------------------------------------------
# 4. Game loop
# ------------------------------------------------------------

def play_wordle(word_list: list[str]) -> None:
    target = random.choice(word_list)
    attempts = 6

    print("Welcome to CLI‑Wordle!")
    print(f"You have {attempts} attempts to guess a 5‑letter word.\n")

    for attempt in range(1, attempts + 1):
        # Input loop – keep asking until a valid 5‑letter guess is supplied
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").lower().strip()
            if len(guess) != 5 or not guess.isalpha():
                print("❌ Please enter exactly 5 letters.")
                continue
            if guess not in word_list:
                print("❌ Not a recognised word. Try again.")
                continue
            break

        # Check guess vs target
        feedback = generate_feedback(guess, target)

        # Render the coloured feedback line
        line = " ".join(coloured_square(SQUARE, c) for c in feedback)
        sys.stdout.write(line + "\n")

        # Adjust terminal output flush for readability
        sys.stdout.flush()

        if guess == target:
            print(f"🎉 Congratulations! You guessed the word in {attempt} attempt(s).")
            return

    # If loop completes, user failed
    print(f"💀 Out of attempts! The word was '{target}'. Better luck next time.")

# ------------------------------------------------------------
# 5. Program entry point
# ------------------------------------------------------------

def main() -> None:
    word_list = load_word_list()
    play_wordle(word_list)

if __name__ == "__main__":
    main()
