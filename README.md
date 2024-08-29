# Sokoban Puzzle Solver

This project is an implementation of a Sokoban puzzle solver using Python, with libraries like `pygame` and `tkinter` for the graphical interface. The game uses TMX map files and implements A and A* search algorithms to simulate and solve the puzzles.

## Features

- Load and display a Sokoban puzzle from a `.tmx` map file.
- Simulate solving the puzzle using A and A* search algorithms.
- Display the number of iterations required to solve the puzzle via a simple graphical interface.

## Prerequisites

- **Python 3.x**
- **Python Libraries**:
  - `pygame`: For the graphical interface.
  - `pytmx`: For loading TMX map files.
  - `pyscroll`: For handling scrollable maps.
  - `numpy`: For numerical computations.
  - `tkinter`: For creating a simple GUI window.

## Installation

1. Clone this GitHub repository to your local machine:

    ```bash
    git clone https://github.com/nesrinenesrine/Sokoban-Puzzle-Solver
    cd your-project
    ```

2. Install the necessary dependencies:

    ```bash
    pip install pygame pytmx pyscroll numpy
    ```

## Usage

1. Ensure you have the map files (e.g., `interface2.tmx`, `interface4.tmx`, `interface5.tmx`).
2. Run the main script:

    ```bash
    python main.py
    ```

3. A window will open displaying the number of iterations needed to solve the puzzle.

## Project Structure

- **main.py**: The main script to load and run the game.
- **sokoPuzzle.py**: Class to manage the Sokoban puzzle.
- **node.py**: Node class to represent the game state.
- **Game.py**: Class to manage the game engine, including graphical rendering and simulation.
- **search.py**: Implementation of A and A* search algorithms to solve the puzzle.
- **player.py**: Manages player interactions and movements.
- **bloc.py**: Handles the block elements within the puzzle.
