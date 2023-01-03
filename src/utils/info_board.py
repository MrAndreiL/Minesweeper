import pygame
import utils.text as text
import utils.input_box as input_box
import os


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
        self.__LGRAY = (211, 211, 211)
        self.__DGRAY = (169, 169, 169)

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

        # User input defaults.
        self.rows = 8
        self.columns = 8
        self.bombs = 10
        self.seconds = 120

        # CPU clock of the game.
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Minesweeper')

    def display_loop(self):
        """Creates and maintains the main display loop.

        Builds up the infinite loop, manages events, displays
        text blocks and buttons and
        updates graphical table constantly."""

        # Create labels and input spaces, group them and display them.
        rows_label = text.TextLabel("Number of rows:", self.__BLACK,
                                    self.font, self.font_size)
        rows_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                100
        )
        rows_input = input_box.InputBox(
                rows_label.rect.w + rows_label.rect.x + 10,
                100,
                50,
                20,
                self.__LGRAY,
                self.__DGRAY,
                self.font,
                self.font_size,
                '9'
        )
        col_label = text.TextLabel("Number of columns:", self.__BLACK,
                                   self.font, self.font_size)
        col_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                150
        )
        col_input = input_box.InputBox(
                col_label.rect.w + col_label.rect.x + 10,
                150,
                50,
                20,
                self.__LGRAY,
                self.__DGRAY,
                self.font,
                self.font_size,
                '9'
        )

        bomb_label = text.TextLabel("Number of bombs:", self.__BLACK,
                                    self.font, self.font_size)
        bomb_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                200
        )
        bomb_input = input_box.InputBox(
                bomb_label.rect.w + bomb_label.rect.x + 10,
                200,
                50,
                20,
                self.__LGRAY,
                self.__DGRAY,
                self.font,
                self.font_size,
                '10'
        )

        sec_label = text.TextLabel("Number of seconds:", self.__BLACK,
                                   self.font, self.font_size)
        sec_label.set_rectangle(
                (self.board_width // 3) - (rows_label.rect.w // 2),
                250
        )
        sec_input = input_box.InputBox(
                sec_label.rect.w + sec_label.rect.x + 10,
                250,
                50,
                20,
                self.__LGRAY,
                self.__DGRAY,
                self.font,
                self.font_size,
                '120'
        )

        # Create sprite label groups for better management.
        labels = pygame.sprite.Group()
        labels.add(rows_label)
        labels.add(col_label)
        labels.add(bomb_label)
        labels.add(sec_label)

        # Create sprite input groups for better management.
        inputs = pygame.sprite.Group()
        inputs.add(rows_input)
        inputs.add(col_input)
        inputs.add(bomb_input)
        inputs.add(sec_input)

        # Import start image from assets folder as object surface.
        try:
            base_path = os.path.dirname(__file__)
            start_path = os.path.join(base_path, "assets/start_button.png")
            start_img = pygame.image.load(start_path).convert()
            start_rect = start_img.get_rect()
        except Exception as exp:
            print("Exception occrrend when importing asset", exp)
        start_rect = pygame.Rect(
                self.board_width // 2 - start_rect.w // 2,
                300,
                start_rect.w,
                start_rect.h
        )

        # Import game icon.
        try:
            base_path = os.path.dirname(__file__)
            icon_path = os.path.join(base_path, "assets/icon.png")
            icon_img = pygame.image.load(icon_path).convert()
        except Exception as exp:
            print("Cannot import game icon", exp)
        # Set game icon.
        pygame.display.set_icon(icon_img)

        running = True
        while running:
            # Loop through the event list.
            for event in pygame.event.get():
                # If the user presses the OS' exit button.
                if event.type == pygame.QUIT:
                    running = False
                # Input handling.
                for inp in inputs:
                    inp.handle_event(event)
                # Test if start button was pressed correctly.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_rect.collidepoint(event.pos):
                        running = False

            # Fill the screen with white.
            self.board.fill(self.__WHITE)

            # Draw all text labels.
            for label in labels:
                self.board.blit(label.text_object, label.rect)

            # Draw all input spaces.
            for inp in inputs:
                pygame.draw.rect(self.board, self.__LGRAY, inp.rect)
                self.board.blit(inp.text_surf, inp.rect)

            # Display start image.
            self.board.blit(start_img, start_rect)

            # Update the display.
            pygame.display.flip()

            # Ensure cpu clock frame.
            self.clock.tick(self.__FRAMES)

        # Cleanup.
        pygame.quit()
