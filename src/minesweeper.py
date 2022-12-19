#!/usr/bin/python3

def info_display():
    pass


def game_display():
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


if __name__ == "__main__":
    main()
