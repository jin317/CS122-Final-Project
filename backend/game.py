import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    return choice == 'y'

class HangmanGame:
    def __init__(self):
        self.difficulty_levels = {
            'easy': 'easy_words.txt',
            'medium': 'medium_words.txt',
            'hard': 'hard_words.txt'
        }

        self.max_attempts = 6
        self.word = ""
        self.guessed_letters = set()
        self.word_display = []
        self.attempts_left = self.max_attempts

        self.hangman_stages = [
            """
            -----
            |   |
                |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            --------
            """
        ]

    def load_word(self, difficulty):
        try:
            with open(self.difficulty_levels[difficulty], 'r') as f:
                words = f.read().strip().split('\n')
                return random.choice(words).lower()
        except FileNotFoundError:
            print(f"Word file for {difficulty} difficulty not found. Creating files...")
            return self.load_word(difficulty)

    def display_game_state(self):
        clear_screen()
        print("\n" + self.hangman_stages[self.max_attempts - self.attempts_left])
        print("\nWord: " + " ".join(self.word_display))
        print("\nGuessed letters: " + ", ".join(sorted(self.guessed_letters)) if self.guessed_letters else "None")
        print(f"Attempts left: {self.attempts_left}")

    def update_word_display(self):
        self.word_display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                self.word_display.append(letter)
            else:
                self.word_display.append("_")

    def is_word_guessed(self):
        return "_" not in self.word_display

    def make_guess(self, guess):
        guess = guess.lower()

        if guess in self.guessed_letters:
            return "You've already guessed that letter!"

        self.guessed_letters.add(guess)

        if guess in self.word:
            self.update_word_display()
            if self.is_word_guessed():
                return "win"
            return "Good guess!"
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                return "lose"
            return "Incorrect guess!"

    def play(self):
        clear_screen()
        print("Welcome to Hangman!")
        print("\nChoose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in ['1', '2', '3']:
                difficulty = {
                    '1': 'easy',
                    '2': 'medium',
                    '3': 'hard'
                }[choice]
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        self.word = self.load_word(difficulty)
        self.guessed_letters = set()
        self.attempts_left = self.max_attempts
        self.update_word_display()

        while True:
            self.display_game_state()

            guess = input("\nGuess a letter: ").strip()

            if not guess:
                print("Please enter a letter.")
                input("Press Enter to continue...")
                continue

            if len(guess) > 1:
                print("Please enter only one letter.")
                input("Press Enter to continue...")
                continue

            if not guess.isalpha():
                print("Please enter a valid letter.")
                input("Press Enter to continue...")
                continue

            result = self.make_guess(guess)

            if result == "win":
                self.display_game_state()
                print(f"\nCongratulations! You've guessed the word: {self.word}")
                break

            elif result == "lose":
                self.display_game_state()
                print(f"\nGame Over! The word was: {self.word}")
                break

            else:
                print(result)
                input("Press Enter to continue...")


def main():
    game = HangmanGame()

    while True:
        game.play()
        if not play_again():
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()