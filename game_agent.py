from state import GameState
from tools import (
    validate_move,
    select_bot_move,
    resolve_round,
    advance_round,
)


def explain_rules():
    print(
        "\nRules:\n"
        "• Best of 3 rounds\n"
        "• Moves: rock, paper, scissors, bomb (once per game)\n"
        "• Bomb beats everything\n"
        "• Invalid input wastes the round\n"
    )


def run_game():
    state = GameState()
    explain_rules()

    while not state.game_over:
        print(f"\n--- Round {state.current_round} ---")
        user_input = input("Your move: ")

        validation = validate_move(state, user_input)

        if not validation["valid"]:
            print(validation["reason"])
            state.current_round += 1
            if state.current_round > state.max_rounds:
                state.game_over = True
            continue

        user_move = validation["normalized_move"]
        bot_move = select_bot_move(state)

        round_result = resolve_round(user_move, bot_move)

        state = advance_round(
            state=state,
            user_move=user_move,
            bot_move=bot_move,
            round_result=round_result,
        )

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")
        print(f"Result: {round_result['result']}")
        print(f"Score → You: {state.user_score} | Bot: {state.bot_score}")

    print("\n=== GAME OVER ===")
    if state.user_score > state.bot_score:
        print("Final Result: You win!")
    elif state.bot_score > state.user_score:
        print("Final Result: Bot wins!")
    else:
        print("Final Result: Draw!")


if __name__ == "__main__":
    run_game()
