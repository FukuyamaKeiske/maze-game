class Player:
    def __init__(self, maze):
        """
        Initialize a new Player instance.

        Parameters:
        maze (Maze): The maze in which the player will move.

        Attributes:
        maze (Maze): The maze in which the player is currently located.
        player_pos (tuple): The current position of the player in the maze.
        directions (dict): A dictionary mapping movement keys to their corresponding directional changes.
        """
        self.maze = maze
        self.player_pos = maze.start_pos
        self.directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }

    def move(self, direction):
        """
        Move the player in the specified direction if the move is valid.

        Parameters:
        direction (str): The direction in which the player wants to move.

        Returns:
        None
        """
        dx, dy = self.directions[direction]
        new_x, new_y = self.player_pos[0] + dx, self.player_pos[1] + dy
        if self.maze.is_valid_move(new_x, new_y):
            self.player_pos = (new_x, new_y)