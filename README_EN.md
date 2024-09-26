# Maze Game

[![Русский](https://img.shields.io/badge/lang-Русский-blue)](README.md)

## Description

"Maze Game" is a console game written in Python where the player must find the exit from a randomly generated maze. The player controls the character using the WASD keys. The time to complete the maze is limited to one minute.

## Requirements

- Python 3.6 or higher
- Operating System: Windows, Linux, macOS

## Installation

To run the game, you need to clone the repository and run `__main__.py`. Here are the steps for installation:

1. Clone the repository:
   ```sh
   git clone https://github.com/FukuyamaKeiske/maze-game.git
   cd maze-game
   ```

2. (Optional) Install dependencies if you are using Windows:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Game

The game can be launched by running the following command in the terminal, FULL SCREEN:

```sh
python __main__.py
```

## Controls

Use the following keys to control the character:

- `W` - move up
- `A` - move left
- `S` - move down
- `D` - move right

## Game Rules

The player must find the exit from the maze within the allotted time:

- If the player finds the exit in less than a minute, the game displays the completion time and offers to restart.
- If the player fails to find the exit within the allotted time, the game offers to restart.

## Screenshots
![Screenshot](https://github.com/user-attachments/assets/0a1ac12d-2da2-4a57-993c-6c749427c117)
