import time
from maze import Maze
from player import Player
from threading import Thread

def timer_thread(maze, timer_data):
    """
    This function is a thread that counts down the time left in the maze game.

    Parameters:
    maze (Maze): The maze object representing the game level.
    timer_data (dict): A dictionary containing the time left and a flag indicating if the time is up.

    Returns:
    None
    """
    start_time = time.time()
    while time.time() - start_time < maze.time_limit:
        time.sleep(1)
        timer_data["time_left"] = int(maze.time_limit - (time.time() - start_time))
    timer_data["time_left"] = 0
    timer_data["time_up"] = True

def main(stdscr):
    """
    The main function of the maze game. It handles the game loop, player input, and game state.

    Parameters:
    stdscr (curses.window): The curses window object used for rendering the game.

    Returns:
    None
    """
    while True:
        width, height = 31, 31
        maze = Maze(width, height)
        player = Player(maze)

        timer_data = {"time_left": maze.time_limit, "time_up": False}
        timer = Thread(target=timer_thread, args=(maze, timer_data))
        timer.start()

        start_time = time.time()
        stdscr.nodelay(1)
        game_over = False

        while not game_over:
            maze.print_maze(stdscr, player.player_pos, timer_data["time_left"])
            if timer_data["time_up"]:
                stdscr.clear()
                stdscr.addstr(0, 0, "Time's up! Press \"r\" to restart or \"q\" to quit.")
                stdscr.refresh()
                game_over = True

            key = stdscr.getch()
            if key != -1:
                key = chr(key).lower()
                if key in ("w", "a", "s", "d"):
                    player.move(key)

                if player.player_pos == maze.exit_pos:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    stdscr.clear()
                    stdscr.addstr(0, 0, f"Congrats! You have won in {elapsed_time:.2f} seconds! Press \"r\" to restart or \"q\" to quit.")
                    stdscr.refresh()
                    game_over = True

        while game_over:
            key = stdscr.getch()
            if key != -1:
                key = chr(key).lower()
                if key == "q":
                    return
                elif key == "r":
                    game_over = False
                    break