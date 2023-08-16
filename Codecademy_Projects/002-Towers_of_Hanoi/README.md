# Towers of Hanoi

Towers of Hanoi is an ancient mathematical puzzle that involves moving a stack of disks from one stack to another while following specific rules. In this project, we implement the Towers of Hanoi game using stacks in Python.

## Project Description

The Towers of Hanoi puzzle consists of three rods and a number of disks of different sizes which can be slid onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

## Getting Started

To run the Towers of Hanoi game, follow these steps:

1. Clone this repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Run the Python script using the command: `python towers_of_hanoi.py`

## How to Play

1. When you run the script, you will be prompted to enter the number of disks you want to play with.
2. Follow the on-screen instructions to make legal moves and solve the puzzle.
3. The game will provide feedback on your moves and let you know when you have successfully solved the puzzle.

Have fun playing the Towers of Hanoi puzzle and honing your problem-solving skills!

## Implementation Details

The game is implemented using stacks to represent the rods and disks. The `Stack` class provides methods for pushing and popping disks, and the `TowersOfHanoi` class contains the main game logic to solve the puzzle.