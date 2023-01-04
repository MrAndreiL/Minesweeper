#!/usr/bin/python3
from utils import info_board
from utils import game


def info_display():
    """Provies the user with the initial display.

    Initially, a board is created to retrieve the user's
    options regarding the game's parameters(rows, columns, bombs and
    game seconds). Default values for these fields are provided.

    Returns:
        A board object with the filled in data.
    """
    # Create the info board object.
    board = info_board.InfoBoard()

    # Open up the game/display loop.
    board.display_loop()

    return board


def game_display(board):
    """Main game display with the actual minesweeper game.

    Using the information provided by the initial info board,
    the game board is then built up and the game is ready to be
    played.

    Args:
        board: A reference to the aforementioned info board.
            Contains input data necessary to build up the game board.
    """
    # Initiate pygame config info.
    game_board = game.Game(board)

    # Start the main game loop.
    game_board.game_loop()


def main():
    """Start the game's development.

    Opens up flow control to the two main subsections of the game.
    The first one, a starting window that deals with receiving
    information from the user, such as the number of columns, rows,
    bombs or the number of seconds.
    The second one, the minesweeper game ready to be played.
    The third one, a display that shows the games' result.
    """
    board = info_display()

    game_display(board)


if __name__ == "__main__":
    main()
