import random
import sys
from termcolor import colored

# List of 5-letter words for the game
WORD_LIST = [
    "apple", "beach", "crane", "dance", "eagle", "flame", "grape", "happy",
    "igloo", "jolly", "knight", "lemon", "mango", "noble", "ocean", "pizza",
    "queen", "river", "sunny", "tiger", "unity", "vivid", "water", "xenon",
    "youth", "zebra", "abide", "baker", "candy", "daisy", "ember", "fable",
    "glory", "haste", "image", "jewel", "kiosk", "laugh", "merry", "nurse",
    "olive", "pearl", "quiet", "rider", "swift", "toast", "umbra", "vague",
    "witty", "xerox", "yacht", "zesty"
]

class WordleGame:
    def __init__(self):
        self.secret_word = random.choice(WORD_LIST).lower()
        self.max_attempts = 6
        self.attempts = 0
        self.guessed_words = []
        
    def is_valid_word(self, word):
        """Check if the word is valid (5 letters, alphabetic)"""
        return len(word) == 5 and word.isalpha() and word.lower() in WORD_LIST
    
    def get_feedback(self, guess):
        """Provide feedback on the guess with color coding"""
        guess = guess.lower()
        feedback = []
        secret_list = list(self.secret_word)
        
        # First pass: mark correct letters in correct position
        for i, (g, s) in enumerate(zip(guess, self.secret_word)):
            if g == s:
                feedback.append(colored(g.upper(), 'green'))
                secret_list[i] = None  # Mark as used
            else:
                feedback.append(g.upper())
        
        # Second pass: mark correct letters in wrong position
        for i, (g, s) in enumerate(zip(guess, self.secret_word)):
            if g != s and g in secret_list:
                feedback[i] = colored(g.upper(), 'yellow')
                secret_list[secret_list.index(g)] = None  # Mark as used
            elif g != s:
                feedback[i] = colored(g.upper(), 'red')
        
        return ' '.join(feedback)
    
    def play(self):
        """Main game loop"""
        print("Welcome to Wordle CLI!")
        print(f"Guess the 5-letter word. You have {self.max_attempts} attempts.")
        print("Feedback: Green = correct letter & position, Yellow = correct letter wrong position, Red = incorrect letter")
        
        while self.attempts < self.max_attempts:
            guess = input(f"\nAttempt {self.attempts + 1}/{self.max_attempts}. Enter your guess: ").strip().lower()
            
            if not self.is_valid_word(guess):
                print("Invalid word. Please enter a valid 5-letter word from our dictionary.")
                continue
            
            self.attempts += 1
            self.guessed_words.append(guess)
            
            feedback = self.get_feedback(guess)
            print(f"Feedback: {feedback}")
            
            if guess == self.secret_word:
                print(f"\n🎉 Congratulations! You guessed the word '{self.secret_word.upper()}' in {self.attempts} attempts!")
                return True
        
        print(f"\n💀 Game over! The word was '{self.secret_word.upper()}'. Better luck next time!")
        return False

def main():
    game = WordleGame()
    game.play()


if __name__ == "__main__":
    main()
