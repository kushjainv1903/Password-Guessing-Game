import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Password_Guess import PasswordGame
from models import (
    StartGameRequest,
    StartGameResponse,
    GuessRequest,
    GuessResponse,
    GameStateResponse,
)

app = FastAPI(
    title="Password Guessing Game API",
    description="A fun word-guessing game with difficulty levels, hints, and scoring",
    version="1.0.0",
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory game storage (no database needed)
games = {}


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {
        "message": "Password Guessing Game API is running!",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.post("/game/start", response_model=StartGameResponse)
def start_game(request: StartGameRequest):
    """
    Start a new game with the specified difficulty.

    Returns a unique game_id to use for subsequent guesses.
    """
    try:
        game = PasswordGame(request.difficulty)
        game_id = str(uuid.uuid4())
        games[game_id] = game

        return StartGameResponse(
            game_id=game_id,
            difficulty=game.difficulty,
            word_length=len(game.password),
            max_attempts=game.max_attempts,
            message=f"Game started! Guess the {len(game.password)}-letter word.",
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/game/{game_id}/guess", response_model=GuessResponse)
def make_guess(game_id: str, request: GuessRequest):
    """
    Submit a guess for the specified game.

    Returns hints, attempts remaining, and score if the game is won.
    """
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")

    game = games[game_id]
    result = game.make_guess(request.guess)

    return GuessResponse(**result)


@app.get("/game/{game_id}/status", response_model=GameStateResponse)
def get_game_status(game_id: str):
    """
    Get the current state of the specified game.
    """
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")

    game = games[game_id]
    state = game.get_game_state()

    return GameStateResponse(
        game_id=game_id,
        **state,
    )


@app.delete("/game/{game_id}")
def delete_game(game_id: str):
    """
    Delete a game from memory.
    """
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")

    del games[game_id]
    return {"message": f"Game {game_id} deleted successfully"}


@app.get("/stats")
def get_stats():
    """
    Get stats about active games.
    """
    return {
        "active_games": len(games),
        "games": [
            {
                "game_id": game_id,
                "difficulty": game.difficulty,
                "attempts_used": game.attempts,
                "is_over": game.is_over,
            }
            for game_id, game in games.items()
        ],
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
