import pygame


class Game:
    """Minesweeper main board game.

    This class takes care of initiating, creating
    and updating the main pygame interface. It imports
    assets and deals with input from user.
    """

    def __init__(self, board):
        """Constructor method that builds up pygame instance.

        Establishes the main parameters that will be used
        throughout the whole game, initiates the pygame instance
        and sets up the window.

        Args:
            board: Info_Board type object that describes how to build
                the actual game board.
        """
        # Main board build-up information.
        self._BLOCK_WIDTH = 20
        self._BLOCK_HEIGHT = 20

        self._BOARD_WIDTH = self._BLOCK_WIDTH * board.columns
        self._BOARD_HEIGHT = self._BLOCK_HEIGHT * board.rows + 150

        # Commonly used color codes.
        self._WHITE = (255, 255, 255)

        # Input data.
        self._BOMBS = board.bombs
        self._SECONDS = board.seconds

        # Pygame init data and maintainance.
        pygame.init()

        pygame.display.set_caption("Minesweeper")

        self._BOARD = pygame.display.set_mode(
                (self._BOARD_WIDTH,
                 self._BOARD_HEIGHT)
        )

        self._FRAMES = 30

        self._CLOCK = pygame.time.Clock()

    def game_loop(self):
        """Interacts with the player and controls displaying.

        Through an infinite loop, provides the player with the
        minesweeper table and responds appropriately to their
        actions. Stops when the player exits the game.
        """

        # Infinite game loop.
        running = True
        while running:
            # Loop through the event list.
            for event in pygame.event.get():
                # If the user presses the OS' exit button.
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with white.
            self._BOARD.fill(self._WHITE)

            # Update the display.
            pygame.display.flip()

            # Ensure CPU clock-frame.
            self._CLOCK.tick(self._FRAMES)

        # End-game clean-up.
        pygame.quit()
