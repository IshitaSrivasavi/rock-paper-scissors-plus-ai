from dataclasses import dataclass


@dataclass
class GameState:
    current_round: int = 1
    max_rounds: int = 3

    user_score: int = 0
    bot_score: int = 0

    user_bomb_used: bool = False
    bot_bomb_used: bool = False

    game_over: bool = False

#temp test

if __name__ == "__main__":
    state = GameState()
    print(state)
