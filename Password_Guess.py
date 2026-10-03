import random #noqa


class PasswordGame:
    """A password guessing game with difficulty levels, hints, and scoring."""

    WORD_BANK = {
        "easy": ["apple", "banana", "grape", "orange", "peach", "pear"],
        "medium": ["planet", "laptop", "coconut", "python", "bottle", "monkey"],
        "hard": ["computer", "programming", "umbrella", "function", "variable", "mountain"],
    }

    MAX_ATTEMPTS = {
        "easy": 10,
        "medium": 7,
        "hard": 5,
    }

    SCORE_MULTIPLIER = {
        "easy": 1,
        "medium": 2,
        "hard": 3,
    }

    BASE_SCORE = 100

    def __init__(self):
        self.difficulty = None
        self.password = None
        self.max_attempts = None
        self.attempts = 0
        self.score = 0

    def select_difficulty(self):
        """Get and validate difficulty level from the player."""
        while True:
            choice = input("\nChoose difficulty level (easy, medium, hard): ").strip().lower()
            if choice in self.WORD_BANK:
                self.difficulty = choice
                self.max_attempts = self.MAX_ATTEMPTS[choice]
                print(f"\n{'='*45}")
                print(f"  Difficulty : {self.difficulty.upper()}")
                print(f"  Max Attempts : {self.max_attempts}")
                print(f"  Score Multiplier : {self.SCORE_MULTIPLIER[choice]}x")
                print(f"{'='*45}")
                return
            else:
                print("Invalid choice! Please enter easy, medium, or hard.")

    def select_word(self):
        """Pick a random word based on the selected difficulty."""
        self.password = random.choice(self.WORD_BANK[self.difficulty])

    def generate_position_hint(self, guess):
        """Show which characters match at the correct position."""
        hint = ""
        for i in range(len(self.password)):
            if i < len(guess) and guess[i] == self.password[i]:
                hint += self.password[i]
            else:
                hint += "_"
        return hint

    def count_correct_letters(self, guess):
        """Count how many letters in the guess exist in the password."""
        password_letters = list(self.password)
        count = 0
        for letter in guess:
            if letter in password_letters:
                count += 1
                password_letters.remove(letter)
        return count

    def validate_guess(self, guess):
        """Validate the player's guess input."""
        if not guess:
            print("  ⚠ Empty guess! Type a word.")
            return False
        if not guess.isalpha():
            print("  ⚠ Letters only! No numbers or special characters.")
            return False
        return True

    def calculate_score(self):
        """Calculate final score based on difficulty and attempts used."""
        speed_bonus = (self.max_attempts - self.attempts) * 10
        multiplier = self.SCORE_MULTIPLIER[self.difficulty]
        self.score = (self.BASE_SCORE + speed_bonus) * multiplier
        return self.score

    def play(self):
        """Run one round of the game."""
        self.attempts = 0
        self.score = 0
        self.select_difficulty()
        self.select_word()

        print(f"\n  The password has {len(self.password)} letters. Start guessing!\n")

        while self.attempts < self.max_attempts:
            remaining = self.max_attempts - self.attempts
            guess = input(f"  Attempt {self.attempts + 1}/{self.max_attempts} → Guess: ").strip().lower()

            if not self.validate_guess(guess):
                continue

            self.attempts += 1

            if guess == self.password:
                self.calculate_score()
                print(f"\n  {'='*45}")
                print(f"  🎉 Congratulations! You guessed it!")
                print(f"  🔑 Password : {self.password}")
                print(f"  🎯 Attempts  : {self.attempts}/{self.max_attempts}")
                print(f"  ⭐ Score     : {self.score} points")
                print(f"  {'='*45}\n")
                return True

            correct_count = self.count_correct_letters(guess)
            position_hint = self.generate_position_hint(guess)

            print(f"  ✅ Correct letters in word: {correct_count}")
            print(f"  🔡 Position hint: {position_hint}")
            print(f"  ❌ Not the password! {remaining - 1} attempts left.\n")

        print(f"\n  {'='*45}")
        print(f"  💀 Game Over! You ran out of attempts.")
        print(f"  🔑 The password was: {self.password}")
        print(f"  {'='*45}\n")
        return False

    def play_again(self):
        """Ask the player if they want to play another round."""
        while True:
            choice = input("  Play again? (yes/no): ").strip().lower()
            if choice in ("yes", "y"):
                return True
            elif choice in ("no", "n"):
                return False
            else:
                print("  Please enter yes or no.")

    def run(self):
        """Entry point — loop of play + play_again."""
        print("\n" + "=" * 50)
        print("  🔐 Welcome to the Password Guessing Game! 🔐")
        print("=" * 50)
        print("  Guess the secret password based on your")
        print("  chosen difficulty. Use the hints wisely!")

        while True:
            self.play()
            if not self.play_again():
                print("\n  Thanks for playing! See you next time. 👋\n")
                break


if __name__ == "__main__":
    game = PasswordGame()
    game.run()
