# Tetris AI

This project is a Tetris game implemented in Python using Pygame, with additional AI functionalities that will be implemented over time. The game includes standard Tetris features, along with visual enhancements such as shadow pieces and held piece display.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Controls](#controls)
4. [File Overview](#file-overview)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To run this project, you'll need to have Python installed along with the Pygame library. Follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/tetris-ai.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd tetris-ai

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the game, run the `main.py` file:
```bash
python main.py
```
## Controls
- **Left Arrow**: Move piece left
- **Right Arrow**: Move piece right
- **Down Arrow**: Move piece down faster
- **Up Arrow**: Rotate piece
- **Space**: Instant drop
- **C**: Hold current piece

## File Overview
- **constants.py**: Defines various constants used across the game, such as screen dimensions and colors.
- **drawing.py**: Contains functions for drawing the game state on the screen, including the grid, current piece, shadow piece, next piece, and held piece.
- **game.py**: Implements the main game logic, handling piece movements, collision detection, and game state transitions.
- **grid.py**: Functions for creating the game grid, clearing rows, and updating locked positions.
- **helpers.py**: Utility functions for shape formatting, checking valid positions, and handling game-over conditions.
- **main.py**: Initializes Pygame and starts the game by calling the main menu function.
- **piece.py**: Defines the Piece class, representing a Tetris piece with attributes like position, shape, color, and rotation.
- **shadow_piece.py**: Defines the ShadowPiece class, which extends the Piece class to implement shadow piece functionality.
- **shapes.py**: Contains the definitions of all Tetris shapes in various rotations.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
