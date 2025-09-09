#!/usr/bin/env python3
"""
Wordle-like CLI Game
A command-line version of the popular word guessing game.
"""

import random
import sys
from typing import List, Tuple


class WordleGame:
    def __init__(self):
        # Common 5-letter words for the game
        self.word_list = [
            "ABOUT",
            "ABOVE",
            "ABUSE",
            "ACTOR",
            "ACUTE",
            "ADMIT",
            "ADOPT",
            "ADULT",
            "AFTER",
            "AGAIN",
            "AGENT",
            "AGREE",
            "AHEAD",
            "ALARM",
            "ALBUM",
            "ALERT",
            "ALIEN",
            "ALIGN",
            "ALIKE",
            "ALIVE",
            "ALLOW",
            "ALONE",
            "ALONG",
            "ALTER",
            "AMBER",
            "AMID",
            "AMONG",
            "ANGER",
            "ANGLE",
            "ANGRY",
            "APART",
            "APPLE",
            "APPLY",
            "ARENA",
            "ARGUE",
            "ARISE",
            "ARRAY",
            "ARROW",
            "ASIDE",
            "ASSET",
            "AUDIO",
            "AUDIT",
            "AVOID",
            "AWAKE",
            "AWARD",
            "AWARE",
            "BADLY",
            "BAKER",
            "BASES",
            "BASIC",
            "BEACH",
            "BEGAN",
            "BEGIN",
            "BEING",
            "BELOW",
            "BENCH",
            "BILLY",
            "BIRTH",
            "BLACK",
            "BLAME",
            "BLIND",
            "BLOCK",
            "BLOOD",
            "BOARD",
            "BOOST",
            "BOOTH",
            "BOUND",
            "BRAIN",
            "BRAND",
            "BRAVE",
            "BREAD",
            "BREAK",
            "BREED",
            "BRIEF",
            "BRING",
            "BROAD",
            "BROKE",
            "BROWN",
            "BUILD",
            "BUILT",
            "BUYER",
            "CABLE",
            "CALIF",
            "CARRY",
            "CATCH",
            "CAUSE",
            "CHAIN",
            "CHAIR",
            "CHAOS",
            "CHARM",
            "CHART",
            "CHASE",
            "CHEAP",
            "CHECK",
            "CHEST",
            "CHIEF",
            "CHILD",
            "CHINA",
            "CHOSE",
            "CIVIL",
            "CLAIM",
            "CLASS",
            "CLEAN",
            "CLEAR",
            "CLICK",
            "CLIMB",
            "CLOCK",
            "CLOSE",
            "CLOUD",
            "COACH",
            "COAST",
            "COULD",
            "COUNT",
            "COURT",
            "COVER",
            "CRAFT",
            "CRASH",
            "CRAZY",
            "CREAM",
            "CRIME",
            "CROSS",
            "CROWD",
            "CROWN",
            "CRUDE",
            "CURVE",
            "CYCLE",
            "DAILY",
            "DANCE",
            "DATED",
            "DEALT",
            "DEATH",
            "DEBUT",
            "DELAY",
            "DEPTH",
            "DOING",
            "DOUBT",
            "DOZEN",
            "DRAFT",
            "DRAMA",
            "DRANK",
            "DRAWN",
            "DREAM",
            "DRESS",
            "DRILL",
            "DRINK",
            "DRIVE",
            "DROVE",
            "DYING",
            "EAGER",
            "EARLY",
            "EARTH",
            "EIGHT",
            "ELITE",
            "EMPTY",
            "ENEMY",
            "ENJOY",
            "ENTER",
            "ENTRY",
            "EQUAL",
            "ERROR",
            "EVENT",
            "EVERY",
            "EXACT",
            "EXIST",
            "EXTRA",
            "FAITH",
            "FALSE",
            "FAULT",
            "FIBER",
            "FIELD",
            "FIFTH",
            "FIFTY",
            "FIGHT",
            "FINAL",
            "FIRST",
            "FIXED",
            "FLASH",
            "FLEET",
            "FLOOR",
            "FLUID",
            "FOCUS",
            "FORCE",
            "FORTH",
            "FORTY",
            "FORUM",
            "FOUND",
            "FRAME",
            "FRANK",
            "FRAUD",
            "FRESH",
            "FRONT",
            "FRUIT",
            "FULLY",
            "FUNNY",
            "GIANT",
            "GIVEN",
            "GLASS",
            "GLOBE",
            "GOING",
            "GRACE",
            "GRADE",
            "GRAND",
            "GRANT",
            "GRASS",
            "GRAVE",
            "GREAT",
            "GREEN",
            "GROSS",
            "GROUP",
            "GROWN",
            "GUARD",
            "GUESS",
            "GUEST",
            "GUIDE",
            "HAPPY",
            "HARRY",
            "HEART",
            "HEAVY",
            "HENCE",
            "HENRY",
            "HORSE",
            "HOTEL",
            "HOUSE",
            "HUMAN",
            "IDEAL",
            "IMAGE",
            "INDEX",
            "INNER",
            "INPUT",
            "ISSUE",
            "JAPAN",
            "JIMMY",
            "JOINT",
            "JONES",
            "JUDGE",
            "KNOWN",
            "LABEL",
            "LARGE",
            "LASER",
            "LATER",
            "LAUGH",
            "LAYER",
            "LEARN",
            "LEASE",
            "LEAST",
            "LEAVE",
            "LEGAL",
            "LEVEL",
            "LEWIS",
            "LIGHT",
            "LIMIT",
            "LINKS",
            "LIVES",
            "LOCAL",
            "LOGIC",
            "LOOSE",
            "LOWER",
            "LUCKY",
            "LUNCH",
            "LYING",
            "MAGIC",
            "MAJOR",
            "MAKER",
            "MARCH",
            "MARIA",
            "MATCH",
            "MAYBE",
            "MAYOR",
            "MEANT",
            "MEDIA",
            "METAL",
            "MIGHT",
            "MINOR",
            "MINUS",
            "MIXED",
            "MODEL",
            "MONEY",
            "MONTH",
            "MORAL",
            "MOTOR",
            "MOUNT",
            "MOUSE",
            "MOUTH",
            "MOVED",
            "MOVIE",
            "MUSIC",
            "NEEDS",
            "NEVER",
            "NEWLY",
            "NEWS",
            "NIGHT",
            "NOISE",
            "NORTH",
            "NOTED",
            "NOVEL",
            "NURSE",
            "OCEAN",
            "OFFER",
            "OFTEN",
            "ORDER",
            "OTHER",
            "OUGHT",
            "PAINT",
            "PANEL",
            "PAPER",
            "PARTY",
            "PEACE",
            "PETER",
            "PHASE",
            "PHONE",
            "PHOTO",
            "PIANO",
            "PIECE",
            "PILOT",
            "PITCH",
            "PLACE",
            "PLAIN",
            "PLANE",
            "PLANT",
            "PLATE",
            "POINT",
            "POUND",
            "POWER",
            "PRESS",
            "PRICE",
            "PRIDE",
            "PRIME",
            "PRINT",
            "PRIOR",
            "PRIZE",
            "PROOF",
            "PROUD",
            "PROVE",
            "QUEEN",
            "QUICK",
            "QUIET",
            "QUITE",
            "RADIO",
            "RAISE",
            "RANGE",
            "RAPID",
            "RATIO",
            "REACH",
            "READY",
            "REALM",
            "REBEL",
            "REFER",
            "RELAX",
            "REPAY",
            "REPLY",
            "RIGHT",
            "RIVAL",
            "RIVER",
            "ROBIN",
            "ROGER",
            "ROMAN",
            "ROUGH",
            "ROUND",
            "ROUTE",
            "ROYAL",
            "RURAL",
            "SCALE",
            "SCENE",
            "SCOPE",
            "SCORE",
            "SENSE",
            "SERVE",
            "SEVEN",
            "SHALL",
            "SHAPE",
            "SHARE",
            "SHARP",
            "SHEET",
            "SHELF",
            "SHELL",
            "SHIFT",
            "SHINE",
            "SHIRT",
            "SHOCK",
            "SHOOT",
            "SHORT",
            "SHOWN",
            "SIGHT",
            "SINCE",
            "SIXTH",
            "SIXTY",
            "SIZED",
            "SKILL",
            "SLEEP",
            "SLIDE",
            "SMALL",
            "SMART",
            "SMILE",
            "SMITH",
            "SMOKE",
            "SOLID",
            "SOLVE",
            "SORRY",
            "SOUND",
            "SOUTH",
            "SPACE",
            "SPARE",
            "SPEAK",
            "SPEED",
            "SPEND",
            "SPENT",
            "SPLIT",
            "SPOKE",
            "SPORT",
            "STAFF",
            "STAGE",
            "STAKE",
            "STAND",
            "START",
            "STATE",
            "STEAM",
            "STEEL",
            "STEEP",
            "STEER",
            "STICK",
            "STILL",
            "STOCK",
            "STONE",
            "STOOD",
            "STORE",
            "STORM",
            "STORY",
            "STRIP",
            "STUCK",
            "STUDY",
            "STUFF",
            "STYLE",
            "SUGAR",
            "SUITE",
            "SUPER",
            "SWEET",
            "TABLE",
            "TAKEN",
            "TASTE",
            "TAXES",
            "TEACH",
            "TEAM",
            "TERRY",
            "TEXAS",
            "THANK",
            "THEFT",
            "THEIR",
            "THEME",
            "THERE",
            "THESE",
            "THICK",
            "THING",
            "THINK",
            "THIRD",
            "THOSE",
            "THREE",
            "THREW",
            "THROW",
            "THUMB",
            "TIGHT",
            "TIRED",
            "TISSUE",
            "TITLE",
            "TODAY",
            "TOPIC",
            "TOTAL",
            "TOUCH",
            "TOUGH",
            "TOWER",
            "TRACK",
            "TRADE",
            "TRAIL",
            "TRAIN",
            "TREAT",
            "TREND",
            "TRIAL",
            "TRIBE",
            "TRICK",
            "TRIED",
            "TRIES",
            "TRUCK",
            "TRULY",
            "TRUNK",
            "TRUST",
            "TRUTH",
            "TWICE",
            "TWIST",
            "TYLER",
            "UNDER",
            "UNDUE",
            "UNION",
            "UNITY",
            "UNTIL",
            "UPPER",
            "UPSET",
            "URBAN",
            "USAGE",
            "USUAL",
            "VALUE",
            "VIDEO",
            "VIRUS",
            "VISIT",
            "VITAL",
            "VOCAL",
            "VOICE",
            "WASTE",
            "WATCH",
            "WATER",
            "WAVE",
            "WAYS",
            "WEARS",
            "WEIRD",
            "WELSH",
            "WHOLE",
            "WHOSE",
            "WOMAN",
            "WORLD",
            "WORRY",
            "WORSE",
            "WORST",
            "WORTH",
            "WOULD",
            "WRITE",
            "WRONG",
            "WROTE",
            "YIELD",
            "YOUNG",
            "YOUTH",
        ]

        # Valid words for guessing (includes word_list + additional common words)
        self.valid_words = set(
            self.word_list
            + [
                "ABACK",
                "ABATE",
                "ABBEY",
                "ABIDE",
                "ABLED",
                "ABODE",
                "ABORT",
                "ABOUND",
                "ABHOR",
                "ACHES",
                "ACIDS",
                "ACORN",
                "ACRES",
                "ACTED",
                "ACTOR",
                "ADDED",
                "ADDER",
                "ADEPT",
                "ADMIN",
                "ADOPT",
                "ADULT",
                "AFAR",
                "AFTER",
                "AGAPE",
                "AGENT",
                "AGING",
                "AGONY",
                "AGREE",
                "AHEAD",
                "AIDED",
                "AIDER",
                "AIMED",
                "AIRED",
                "AISLE",
                "ALARM",
                "ALBUM",
                "ALERT",
                "ALIAS",
                "ALIBI",
                "ALIEN",
                "ALIGN",
                "ALIKE",
                "ALIVE",
                "ALLEY",
                "ALLOT",
                "ALLOW",
                "ALLOY",
                "ALONE",
                "ALONG",
                "ALOOF",
                "ALOUD",
                "ALPHA",
                "ALTAR",
                "ALTER",
                "AMBER",
                "AMEND",
                "AMISS",
                "AMONG",
                "AMPLE",
                "AMPLY",
                "AMUSE",
                "ANGEL",
                "ANGER",
                "ANGLE",
                "ANGRY",
                "ANKLE",
                "ANNOY",
                "ANTIC",
                "APART",
                "APHID",
                "APING",
                "APRON",
                "APTLY",
                "ARBOR",
                "ARDOR",
                "ARENA",
                "ARGUE",
                "ARISE",
                "ARMED",
                "ARMOR",
                "AROMA",
                "AROSE",
                "ARRAY",
                "ARROW",
                "ARSON",
                "ARTSY",
                "ASCOT",
                "ASHEN",
                "ASIDE",
                "ASSET",
                "ATOLL",
                "ATOMS",
                "ATONE",
                "ATTIC",
                "AUDIO",
                "AUDIT",
                "AUGUR",
                "AUNTY",
                "AVAIL",
                "AVERT",
                "AVIAN",
                "AVOID",
                "AWAKE",
                "AWARD",
                "AWARE",
                "AWASH",
                "AWFUL",
                "AWOKE",
                "AXIAL",
                "AXIOM",
                "AXION",
                "AZURE",
                "BACON",
                "BADGE",
                "BADLY",
                "BAGEL",
                "BAKER",
                "BALLS",
                "BALMY",
                "BANAL",
                "BANJO",
                "BARGE",
                "BARON",
                "BASIL",
                "BASIN",
                "BASIS",
                "BASTE",
                "BATCH",
                "BATHE",
                "BATON",
            ]
        )

        self.target_word = random.choice(self.word_list)
        self.guesses = []
        self.max_guesses = 6
        self.game_over = False
        self.won = False

    def display_instructions(self):
        print("🟩 WORDLE CLI 🟩")
        print("=" * 50)
        print("Guess the 5-letter word in 6 tries!")
        print("After each guess, the color will show how close you are:")
        print("🟩 Green: Letter is correct and in the right position")
        print("🟨 Yellow: Letter is in the word but in the wrong position")
        print("⬜ Gray: Letter is not in the word")
        print("=" * 50)
        print()

    def is_valid_word(self, word: str) -> bool:
        return word.upper() in self.valid_words

    def get_feedback(self, guess: str) -> List[Tuple[str, str]]:
        """Returns list of (letter, color) tuples for each position"""
        guess = guess.upper()
        target = self.target_word.upper()
        feedback = []

        # Count letters in target word for yellow logic
        target_counts = {}
        for letter in target:
            target_counts[letter] = target_counts.get(letter, 0) + 1

        # First pass: mark green letters
        result = [""] * 5
        used_positions = set()

        for i in range(5):
            if guess[i] == target[i]:
                result[i] = "🟩"
                target_counts[guess[i]] -= 1
                used_positions.add(i)

        # Second pass: mark yellow and gray letters
        for i in range(5):
            if i in used_positions:
                continue

            letter = guess[i]
            if letter in target_counts and target_counts[letter] > 0:
                result[i] = "🟨"
                target_counts[letter] -= 1
            else:
                result[i] = "⬜"

        # Create feedback with letters and colors
        for i in range(5):
            feedback.append((guess[i], result[i]))

        return feedback

    def display_guess(self, guess: str, feedback: List[Tuple[str, str]]):
        """Display a guess with color feedback"""
        display_line = ""
        for letter, color in feedback:
            display_line += f"{color} {letter} "
        print(display_line)

    def display_board(self):
        """Display all guesses made so far"""
        print("\nCurrent Board:")
        print("-" * 30)

        for i, (guess, feedback) in enumerate(self.guesses):
            print(f"Guess {i+1}: ", end="")
            self.display_guess(guess, feedback)

        # Show remaining empty rows
        remaining = self.max_guesses - len(self.guesses)
        for i in range(remaining):
            print(f"Guess {len(self.guesses)+i+1}: ⬜ _ ⬜ _ ⬜ _ ⬜ _ ⬜ _")

        print("-" * 30)

    def get_guess(self) -> str:
        """Get a valid guess from the player"""
        while True:
            try:
                guess = (
                    input(
                        f"\nEnter your guess ({len(self.guesses)+1}/{self.max_guesses}): "
                    )
                    .strip()
                    .upper()
                )

                if len(guess) != 5:
                    print("❌ Please enter exactly 5 letters!")
                    continue

                if not guess.isalpha():
                    print("❌ Please enter only letters!")
                    continue

                if not self.is_valid_word(guess):
                    print("❌ Not a valid word! Try again.")
                    continue

                return guess

            except KeyboardInterrupt:
                print("\n\nThanks for playing! 👋")
                sys.exit(0)

    def check_win(self, guess: str) -> bool:
        """Check if the guess is correct"""
        return guess.upper() == self.target_word.upper()

    def play(self):
        """Main game loop"""
        self.display_instructions()

        while not self.game_over and len(self.guesses) < self.max_guesses:
            if self.guesses:
                self.display_board()

            guess = self.get_guess()
            feedback = self.get_feedback(guess)
            self.guesses.append((guess, feedback))

            print(f"\nGuess: {guess}")
            self.display_guess(guess, feedback)

            if self.check_win(guess):
                self.won = True
                self.game_over = True
            elif len(self.guesses) >= self.max_guesses:
                self.game_over = True

        self.display_board()
        self.show_result()

    def show_result(self):
        """Display the final result"""
        print("\n" + "=" * 50)
        if self.won:
            print("🎉 Congratulations! You guessed the word! 🎉")
            print(f"You won in {len(self.guesses)}/{self.max_guesses} guesses!")
        else:
            print("😞 Game Over! Better luck next time!")
            print(f"The word was: {self.target_word}")
        print("=" * 50)

    def play_again(self) -> bool:
        """Ask if player wants to play again"""
        while True:
            try:
                choice = (
                    input("\nWould you like to play again? (y/n): ").strip().lower()
                )
                if choice in ["y", "yes"]:
                    return True
                elif choice in ["n", "no"]:
                    return False
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                return False


def main():
    """Main function to run the game"""
    print("Welcome to Wordle CLI! 🎮")

    while True:
        game = WordleGame()
        game.play()

        if not game.play_again():
            print("\nThanks for playing Wordle CLI! 👋")
            break

        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
