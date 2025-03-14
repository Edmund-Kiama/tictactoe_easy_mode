# Tic-Tac-Toe Game

This is a simple text-based Tic-Tac-Toe game in Python. The game supports two modes: Player vs. Player (Multiplayer) and Player vs. Computer.

## Features
- Play against another player (Multiplayer mode)
- Play against the computer (AI makes random moves)
- Simple text-based board display
- Automatic win and tie detection

## Requirements
- Python 3.x

## Installation
1. Clone this repository:
   ```sh
   git clone git@github.com:Edmund-Kiama/tictactoe_easy_mode.git
   cd <repository_directory>
   ```
2. Run the script:
   ```sh
   python main.py
   ```

## How to Play
- At the start, choose a mode:
  - `A` for Multiplayer (two players take turns)
  - `B` for Player vs. Computer
- Players take turns selecting a position (1-9) to place their mark (`X` or `O`).
- The game checks for a winner after every move.
- The game ends when a player wins or all slots are filled (tie).

## Controls
- Enter a number (1-9) corresponding to the board position.
- Invalid inputs will prompt re-entry.

## Future Improvements
- Implement a smarter AI with minimax algorithm.
- Add a GUI version using Pygame or Tkinter.

## License
This project is open-source and available under the MIT License.

