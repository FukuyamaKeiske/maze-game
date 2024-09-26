import random
import numpy as np

class Maze:
    def __init__(self, width, height):
        """
        Initialize a new maze with the given width and height.
        The maze is represented as a 2D numpy array, where 0 represents a path and 1 represents a wall.
        The start position is set at the bottom of the maze, and the exit position is set at the top.
        The time limit for solving the maze is set to 60 seconds.

        Parameters:
        width (int): The width of the maze.
        height (int): The height of the maze.
        """
        self.width = width
        self.height = height
        self.maze = np.ones((height, width), dtype=int)
        self.start_pos = (height - 1, random.choice(range(1, width, 2)))
        self.exit_pos = self.generate_exit_pos()
        self.generate_maze()
        self.time_limit = 60

    def generate_exit_pos(self):
        """
        Generate a random exit position for the maze.
        The exit position is set at the top of the maze, and it must be on an odd-numbered column.

        Returns:
        tuple: The coordinates of the exit position (row, column).
        """
        return (0, random.choice(range(1, self.width, 2)))

    def generate_maze(self):
        """
        Generate a random maze using Prim's algorithm.
        The maze is represented as a 2D numpy array, where 0 represents a path and 1 represents a wall.
        The start position is set at the bottom of the maze, and the exit position is set at the top.
        """
        self.maze = np.ones((self.height, self.width), dtype=int)
        stack = [self.start_pos]
        visited = set(stack)

        while stack:
            cx, cy = stack[-1]
            self.maze[cx][cy] = 0
            directions = [(-2, 0), (0, 2), (2, 0), (0, -2)]
            random.shuffle(directions)
            found = False

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                between_x, between_y = cx + dx // 2, cy + dy // 2

                if 0 <= nx < self.height and 0 <= ny < self.width and (nx, ny) not in visited:
                    if 0 <= between_x < self.height and 0 <= between_y < self.width:
                        self.maze[between_x][between_y] = 0
                    self.maze[nx][ny] = 0
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                    found = True
                    break

            if not found:
                stack.pop()

        self.maze[self.exit_pos[0]][self.exit_pos[1]] = 0

    def is_valid_move(self, x, y):
        """
        Check if a move to the given coordinates is valid.
        A move is valid if it is within the maze boundaries and the destination cell is a path (0).

        Parameters:
        x (int): The row coordinate of the destination cell.
        y (int): The column coordinate of the destination cell.

        Returns:
        bool: True if the move is valid, False otherwise.
        """
        return 0 <= x < self.height and 0 <= y < self.width and self.maze[x][y] == 0

    def print_maze(self, stdscr, player_pos, time_left):
        """
        Print the maze to the given screen using ncurses library.
        The maze is displayed with walls represented by "██", paths represented by " ",
        the player represented by "P", the start position represented by "S", and the exit position represented by "E".
        The remaining time is displayed at the top of the screen.

        Parameters:
        stdscr: The ncurses screen object.
        player_pos (tuple): The coordinates of the player's current position (row, column).
        time_left (int): The remaining time for solving the maze in seconds.
        """
        stdscr.clear()
        stdscr.addstr(0, 0, f"Time left: {time_left} seconds\n\n")

        for i in range(self.height + 2):
            for j in range(self.width + 2):
                if i == 0 or i == self.height + 1 or j == 0 or j == self.width + 1:
                    stdscr.addstr(i + 1, j * 2, "██")
                else:
                    if (i - 1, j - 1) == player_pos:
                        stdscr.addstr(i + 1, j * 2, "P")
                    elif (i - 1, j - 1) == self.exit_pos:
                        stdscr.addstr(i + 1, j * 2, "E")
                    elif (i - 1, j - 1) == self.start_pos:
                        stdscr.addstr(i + 1, j * 2, "S")
                    elif self.maze[i - 1][j - 1] == 1:
                        stdscr.addstr(i + 1, j * 2, "██")
                    else:
                        stdscr.addstr(i + 1, j * 2, " ")
        stdscr.refresh()