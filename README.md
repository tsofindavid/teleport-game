# PROG1: Projekt – Teleporty

## Overview

This project simulates a tabletop game called **Teleporty** in Python. The game can accommodate 1 to 4 players and
features a customizable square game board (5x5 to 10x10) filled with **positive and negative teleports**. Players race
to move their pieces from the starting position to the target while navigating teleports and using strategic dice rolls.

---

## Demos

[Demo with One Player](https://2ly.link/21k8r)

[Demo with Two Players](https://2ly.link/21k94)

---

## Features

- Simulates **Teleporty** game mechanics for 1-4 players.
- Customizable game board size: `n x n` (5 ≤ n ≤ 10).
- **Randomly placed teleports**:
    - **Positive teleports**: Move the piece forward.
    - **Negative teleports**: Move the piece backward.
- Supports **dice-based movement** with cumulative rolls when landing a 6.
- Outputs game progress and board updates after every turn.
- Enforces the rule of exact movement to win the game.

---

## How to Play

1. **Game Board**:
    - The board is a 2D grid where:
        - `+`: Start position
        - `*`: Target position
        - Uppercase letters (e.g., `A`): Positive teleport (start → end)
        - Lowercase letters (e.g., `a`): Negative teleport (end → start)
        - `.`: Regular grid cell
2. **Player Moves**:
    - Players roll a 6-sided die to determine the number of steps to move their piece.
    - Rolling a 6 grants an extra roll.
    - Pieces navigate row-by-row, alternating left-to-right and right-to-left directions.
    - Players must land on the target position with an exact roll to win.

---

## Running the Program

1. **Prerequisites**:
    - Python 3.x is required.
    - No third-party libraries are used.

2. **Setup and Execution**:
    - Ensure you have Python 3.x installed on your Unix-based system.
    - Clone the repository:
      ```bash
      git clone https://github.com/tsofindavid/teleports-game.git
      cd teleport-game
      ```
    - Run the script:
      ```bash
      python3 main.py
      ```

3. **User Input**:
    - Enter the size of the game board.
    - Enter the number of players.
    - Enter the players names.
    - The game runs automatically, displaying moves and board updates after each turn.

---

## Game Logic

### Part A: Generating the Board

- Randomly generates positive and negative teleport positions.
- Rules for placing teleports:
    - Positive teleports move pieces forward (end below start).
    - Negative teleports move pieces backward (end above start).
    - Teleports cannot overlap with the start (`+`) or target (`*`) positions.

### Part B: Simulating the Game (1 Player)

- Rolls a die and moves the player's piece accordingly.
- Applies teleport rules if landing on a teleport's starting position.
- Displays:
    - Player's dice roll and resulting position.
    - Updated game board after each turn.
    - A message when the player reaches the target.

### Part C: Multiplayer Simulation (1-5 Players)

- Turns alternate between players.
- Displays:
    - Each player's dice roll and resulting position.
    - Updates for teleport events.
    - An updated game board after each turn.
    - Announces the winner when a player reaches the target.