Rock Paper Scissors Plus (AI Bot)

This is a command-line Rock Paper Scissors game with a simple AI bot.
Along with the usual rock, paper, and scissors, the game also includes a special move called bomb, which can be used only once in the entire game.

The goal of this project is not just to make the game work, but to show clean logic, clear rules, and proper separation between decision-making and game rules.

Game Rules

The game is played for 3 rounds (best of 3)

Allowed moves are: rock, paper, scissors, and bomb

Bomb can be used only once per game

Bomb beats all other moves

If the user enters an invalid move, that round is wasted

After all rounds are completed, the final winner is announced

How the Game Is Designed

The game is built in a structured way so that:

Rules are always followed

The bot does not cheat

The game state is always clear

The AI bot does not directly change scores or end the game.
Instead, all important logic is handled using fixed rules inside tools, and the agent only reads the results and displays them.

This avoids bias, mistakes, or random behavior where it should not exist.

State Model

The game keeps track of the following information:

Current round number

Maximum number of rounds

User score

Bot score

Whether the user has used the bomb

Whether the bot has used the bomb

Whether the game is over or not

Because all this information is stored clearly, the full game progress can be understood at any point.

Tools Used in the Game

Each tool has only one job:

validate_move
Checks if the user’s move is valid and makes sure the bomb is not used more than once.

select_bot_move
Chooses the bot’s move using limited randomness.
It does not look at the user’s score to avoid unfair advantages.

resolve_round
Decides who wins the round and returns how the scores should change.

advance_round
Updates the round number, applies score changes, and decides when the game is over.
This is the only place where the game ending is decided.

Why Randomness Is Used Carefully

Randomness is used only when the bot selects its move, so the game feels natural and not predictable.

Randomness is never used in score calculation or deciding the winner, because those parts must always be correct and fair.

Project Structure

rock_paper_scissors_bot

game_agent.py : main file that runs the game

tools.py : contains all the game logic and rules

README.md : project explanation

How to Run the Game

Run the following command in the project folder:

python game_agent.py


Final Note

This project focuses on clean design, clear rules, and correct logic rather than a fancy interface.
The structure makes the game easy to understand, debug, and explain.
