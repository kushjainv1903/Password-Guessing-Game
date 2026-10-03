import random  # noqa


class PasswordGame:
    """Core password guessing game logic - API-friendly, no input() calls."""

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

    def __init__(self, difficulty: str):
        """Initialize a new game with the given difficulty."""
        if difficulty not in self.WORD_BANK:
            raise ValueError(f"Invalid difficulty: {difficulty}. Choose easy, medium, or hard.")

        self.difficulty = difficulty
        self.password = random.choice(self.WORD_BANK[difficulty])
        self.max_attempts = self.MAX_ATTEMPTS[difficulty]
        self.attempts = 0
        self.is_won = False
        self.is_over = False
        self.score = 0

    def make_guess(self, guess: str) -> dict:
        """
        Process a guess and return the result.

        Returns:
            dict with keys: valid, correct, attempts_used, remaining_attempts,
            correct_letters_count, position_hint, message, is_over, score
        """
        # Normalize input
        guess = guess.strip().lower()

        # Validate input
        if not guess:
            return {
                "valid": False,
                "message": "Empty guess! Type a word.",
            }

        if not guess.isalpha():
            return {
                "valid": False,
                "message": "Letters only! No numbers or special characters.",
            }

        # Game already over
        if self.is_over:
            return {
                "valid": False,
                "message": "Game is already over!",
                "is_over": True,
            }

        # Process the guess
        self.attempts += 1
        remaining = self.max_attempts - self.attempts

        # Check if correct
        if guess == self.password:
            self.is_won = True
            self.is_over = True
            self.score = self._calculate_score()
            return {
                "valid": True,
                "correct": True,
                "attempts_used": self.attempts,
                "remaining_attempts": remaining,
                "password": self.password,
                "score": self.score,
                "is_over": True,
                "message": f"Congratulations! You guessed it in {self.attempts} attempts!",
            }

        # Check if out of attempts
        if self.attempts >= self.max_attempts:
            self.is_over = True
            return {
                "valid": True,
                "correct": False,
                "attempts_used": self.attempts,
                "remaining_attempts": 0,
                "password": self.password,
                "is_over": True,
                "message": f"Game Over! You ran out of attempts. The password was: {self.password}",
            }

        # Generate hints
        correct_count = self._count_correct_letters(guess)
        position_hint = self._generate_position_hint(guess)

        return {
            "valid": True,
            "correct": False,
            "attempts_used": self.attempts,
            "remaining_attempts": remaining,
            "correct_letters_count": correct_count,
            "position_hint": position_hint,
            "is_over": False,
            "message": f"Not the password! {remaining} attempts left.",
        }

    def get_game_state(self) -> dict:
        """Return the current game state."""
        return {
            "difficulty": self.difficulty,
            "word_length": len(self.password),
            "max_attempts": self.max_attempts,
            "attempts_used": self.attempts,
            "remaining_attempts": self.max_attempts - self.attempts,
            "is_won": self.is_won,
            "is_over": self.is_over,
            "score": self.score if self.is_won else 0,
        }

    def _generate_position_hint(self, guess: str) -> str:
        """Show which characters match at the correct position."""
        hint = ""
        for i in range(len(self.password)):
            if i < len(guess) and guess[i] == self.password[i]:
                hint += self.password[i]
            else:
                hint += "_"
        return hint

    def _count_correct_letters(self, guess: str) -> int:
        """Count how many letters in the guess exist in the password."""
        password_letters = list(self.password)
        count = 0
        for letter in guess:
            if letter in password_letters:
                count += 1
                password_letters.remove(letter)
        return count

    def _calculate_score(self) -> int:
        """Calculate final score based on difficulty and attempts used."""
        speed_bonus = (self.max_attempts - self.attempts) * 10
        multiplier = self.SCORE_MULTIPLIER[self.difficulty]
        return (self.BASE_SCORE + speed_bonus) * multiplier


# ============================================================
# CLI Wrapper - For terminal play
# ============================================================

class PasswordGameCLI:
    """CLI wrapper for playing the game in the terminal."""

    def __init__(self):
        self.game = None

    def select_difficulty(self) -> str:
        """Get and validate difficulty level from the player."""
        while True:
            choice = input("\nChoose difficulty level (easy, medium, hard): ").strip().lower()
            if choice in PasswordGame.WORD_BANK:
                return choice
            else:
                print("Invalid choice! Please enter easy, medium, or hard.")

    def display_game_header(self, difficulty: str):
        """Display the game settings."""
        max_attempts = PasswordGame.MAX_ATTEMPTS[difficulty]
        multiplier = PasswordGame.SCORE_MULTIPLIER[difficulty]
        print(f"\n{'='*45}")
        print(f"  Difficulty : {difficulty.upper()}")
        print(f"  Max Attempts : {max_attempts}")
        print(f"  Score Multiplier : {multiplier}x")
        print(f"{'='*45}")

    def play(self):
        """Run one round of the game."""
        difficulty = self.select_difficulty()
        self.display_game_header(difficulty)

        self.game = PasswordGame(difficulty)
        state = self.game.get_game_state()
        print(f"\n  The password has {state['word_length']} letters. Start guessing!\n")

        while not self.game.is_over:
            guess = input(f"  Attempt {self.game.attempts + 1}/{self.game.max_attempts} → Guess: ")
            result = self.game.make_guess(guess)

            if not result["valid"]:
                print(f"  ⚠ {result['message']}")
                continue

            if result["correct"]:
                print(f"\n  {'='*45}")
                print(f"  🎉 Congratulations! You guessed it!")
                print(f"  🔑 Password : {result['password']}")
                print(f"  🎯 Attempts  : {result['attempts_used']}/{self.game.max_attempts}")
                print(f"  ⭐ Score     : {result['score']} points")
                print(f"  {'='*45}\n")
                return

            if result["is_over"]:
                print(f"\n  {'='*45}")
                print(f"  💀 Game Over! You ran out of attempts.")
                print(f"  🔑 The password was: {result['password']}")
                print(f"  {'='*45}\n")
                return

            print(f"  ✅ Correct letters in word: {result['correct_letters_count']}")
            print(f"  🔡 Position hint: {result['position_hint']}")
            print(f"  ❌ {result['message']}\n")

    def play_again(self) -> bool:
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
    cli = PasswordGameCLI()
    cli.run()
