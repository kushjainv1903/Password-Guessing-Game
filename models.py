from pydantic import BaseModel, Field, field_validator


class StartGameRequest(BaseModel):
    """Request model for starting a new game."""
    difficulty: str = Field(..., description="Difficulty level: easy, medium, or hard")

    @field_validator('difficulty')
    @classmethod
    def validate_difficulty(cls, v):
        allowed = ['easy', 'medium', 'hard']
        if v.lower() not in allowed:
            raise ValueError(f"Difficulty must be one of {allowed}")
        return v.lower()


class StartGameResponse(BaseModel):
    """Response model for starting a new game."""
    game_id: str
    difficulty: str
    word_length: int
    max_attempts: int
    message: str


class GuessRequest(BaseModel):
    """Request model for making a guess."""
    guess: str = Field(..., min_length=1, description="The guessed word")


class GuessResponse(BaseModel):
    """Response model for a guess."""
    valid: bool
    correct: bool | None = None
    attempts_used: int | None = None
    remaining_attempts: int | None = None
    correct_letters_count: int | None = None
    position_hint: str | None = None
    is_over: bool | None = None
    score: int | None = None
    password: str | None = None
    message: str


class GameStateResponse(BaseModel):
    """Response model for game state."""
    game_id: str
    difficulty: str
    word_length: int
    max_attempts: int
    attempts_used: int
    remaining_attempts: int
    is_won: bool
    is_over: bool
    score: int
