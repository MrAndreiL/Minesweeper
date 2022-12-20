#!/usr/bin/python3
from utils import info_board


def info_display():
    # Create the info board object.
    board = info_board.InfoBoard()

    # Open up the game/display loop.
    board.display_loop()


def game_display():
    pass


def end_display():
    pass


def main():
    """Start the game's development.

    Opens up flow control to the two main subsections of the game.
    The first one, a starting window that deals with receiving
    information from the user, such as the number of columns, rows,
    bombs or the number of seconds.
    The second one, the minesweeper game ready to be played.
    """
    info_display()

    game_display()

    end_display()


if __name__ == "__main__":
    main()
