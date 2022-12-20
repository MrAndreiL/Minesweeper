import pygame


class InfoBoard:
    """The initial board that gather prerequisite board info.

    Displays info fields to be completed by the player.
    Displays a button to start the game with the given settings.

    Attributes:
        board_width: An integer representing the width of the board.
        board_height: An integer representing the height of the board.
        board: A pygame.display object representing the initial info board.
    """

    def __init__(self):
        """Inits InfoBoard with board information

        Sets up the main configuration for the starting board
        and initializes the framework.
        """
        self.board_width = 400
        self.board_height = 400

        pygame.init()

        self.board = pygame.display.set_mode((
            self.board_width,
            self.board_height)
        )

        pygame.display.set_caption('Minesweeper')

    def display_loop(self):
        """Creates and maintains the main display loop.

        Builds up the infinite loop, manages events and
        updates graphical table constantly."""
        running = True
        while running:
            # Loop through the event list.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with white.
            self.board.fill((255, 255, 255))

            # Update the display.
            pygame.display.flip()
