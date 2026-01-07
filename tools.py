import random
from typing import Dict
from state import GameState

def validate_move(state: GameState, user_move: str) -> Dict:
    move = user_move.strip().lower()
    valid_moves = ["rock", "paper", "scissors", "bomb"]

    if move not in valid_moves:
        return {
            "valid": False,
            "reason": "Invalid move. Choose rock, paper, scissors, or bomb."
        }

    if move == "bomb" and state.user_bomb_used:
        return {
            "valid": False,
            "reason": "You have already used your bomb."
        }

    return {
        "valid": True,
        "normalized_move": move
    }

def select_bot_move(state: GameState) -> str:
    moves = ["rock", "paper", "scissors"]

    if not state.bot_bomb_used:
        moves.append("bomb")

    return random.choice(moves)


def resolve_round(
    user_move: str,
    bot_move: str
) -> Dict:
    if user_move == "bomb" and bot_move == "bomb":
        return {"user_delta": 0, "bot_delta": 0, "result": "Draw (bomb vs bomb)"}

    if user_move == "bomb":
        return {"user_delta": 1, "bot_delta": 0, "result": "User wins (bomb)"}

    if bot_move == "bomb":
        return {"user_delta": 0, "bot_delta": 1, "result": "Bot wins (bomb)"}

    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if user_move == bot_move:
        return {"user_delta": 0, "bot_delta": 0, "result": "Draw"}

    if wins_against[user_move] == bot_move:
        return {"user_delta": 1, "bot_delta": 0, "result": "User wins"}

    return {"user_delta": 0, "bot_delta": 1, "result": "Bot wins"}


def advance_round(
    state: GameState,
    user_move: str,
    bot_move: str,
    round_result: Dict
) -> GameState:

    state.user_score += round_result["user_delta"]
    state.bot_score += round_result["bot_delta"]

    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    state.current_round += 1

    if state.current_round > state.max_rounds:
        state.game_over = True

    return state
