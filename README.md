# Rock Paper Scissor AI Referee

#overview

This project implements a minimal AI referee chatbot for a Rock–Paper–Scissors–Plus game.
The bot enforces rules, tracks state and manages game flow across a
best of 3 rounds match using tools and state transitions.

The focus of the implementation is correctness, clarity, and agent-oriented design..


#State model
The game state is represented using a 'Gamestate' dataclass, which persists across turns.
It tracks:
- Current round and maximum rounds
- User and bot scores
- Bomb usage for both players
- game termination ('game_over')

The state contains no logic and serves as a single source of truth.


##Tool design
Game logic is implemented using 4 tools:
1. Validate_move : validates user input and bomb constraints
2. Select_bot_move: selects a bot move using constrained randomness
3. Resolve_round: determines round outcome and score deltas
4. Advance_round: applies state conversions and decides game termination

Only tools are allowed to mutate state, preventing hallucination or implicit logic for the LLM to not create any bias.


##Agent flow
The agent loop:
1. Explains rules once
2. Prompts for user input
3. Calls tools in a fixed sequence
4. Prints round-by-round feedback
5. Ends automatically after 3 rounds

cleanly separates intent understanding, game logic, and response generation.


##Tradeoffs and future improvements
- The current implementation uses a CLI loop; it can be easily wrapped in a formal ADK Agent.
- Additional UX improvements could include better input hints or replay options.
- More advanced bot strategies could be added without changing core architecture.


##How to run
```bash
python game_agent.py
