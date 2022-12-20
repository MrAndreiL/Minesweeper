import pygame
import utils.text as text


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

        # Board build-up information.
        self.board_width = 400
        self.board_height = 400

        # Color codes used.
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)

        # Text info.
        self.font = 'freesansbold.ttf'
        self.font_size = 20

        # How many frames to bound to.
        self.__FRAMES = 30

        # Pygame internal config.
        pygame.init()

        self.board = pygame.display.set_mode((
            self.board_width,
            self.board_height)
        )

        # CPU clock of the game.
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Minesweeper')

    def display_loop(self):
        """Creates and maintains the main display loop.

        Builds up the infinite loop, manages events, displays
        text blocks and buttons and
        updates graphical table constantly."""

        # Create labels, group them and display them.
        labels = pygame.sprite.Group()

        rows_label = text.TextLabel("Number of rows:", self.__BLACK,
                                    self.font, self.font_size)
        rows_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                50
        )

        col_label = text.TextLabel("Number of columns:", self.__BLACK,
                                   self.font, self.font_size)
        col_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                100
        )

        bomb_label = text.TextLabel("Number of bombs:", self.__BLACK,
                                    self.font, self.font_size)
        bomb_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                150
        )

        sec_label = text.TextLabel("Number of seconds:", self.__BLACK,
                                   self.font, self.font_size)
        sec_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                200
        )

        labels.add(rows_label)
        labels.add(col_label)
        labels.add(bomb_label)
        labels.add(sec_label)

        running = True
        while running:
            # Loop through the event list.
            for event in pygame.event.get():
                # If the user presses the OS' exit button.
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with white.
            self.board.fill(self.__WHITE)

            # Draw all text labels.
            for label in labels:
                self.board.blit(label.text_object, label.rect)

            # Update the display.
            pygame.display.flip()

            # Ensure cpu clock frame.
            self.clock.tick(self.__FRAMES)
