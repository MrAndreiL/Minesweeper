import pygame


class InputBox(pygame.sprite.Sprite):
    """Creates box for user input.

    Create and store user input information
    necessary for the configuration and construction
    of the minesweeper table in the next phase.

    Attributes:
        x: x position
        y: y position
        width: width of the rectangle
        heigth: height of the rectangle
        text: text currently displayed.
        font: text font.
        font_size: text font size.
        active: control variable to monitor if the box is currently used.
        active_color: color for when the box is used.
        inactive_color: color for when the box is not used.
        current_color: either active or inactive.
    """

    def __init__(self, x, y, width, height, active_color,
                 inactive_color, font, font_size, text=''):
        """Inits the InputBox object with necessary data.

        Creates the rectangle, text and font objects used
        to dinamically display the input text.
        """
        super(InputBox, self).__init__()
        # Input box configuration info.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.font_size = font_size
        self.active = False  # active when pressed.
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.current_color = inactive_color

        # Create rect and text to be displayed.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font_surf = pygame.font.Font(self.font, self.font_size)
        self.text_surf = self.font_surf.render(self.text,
                                               True,
                                               (0, 0, 0))

    def handle_event(self, event):
        """Handles events specific to the text input object.

        Based on the type of the incoming events, changes the
        current state of the input box into either active or inactive.
        Moreover, makes sure only digits are allowed to be written and
        dynamically changes the displayed text.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            if self.active:
                self.current_color = self.active_color
            else:
                self.current_color = self.inactive_color
        # count only digit entries.
        if event.type == pygame.KEYDOWN and event.unicode.isdigit():
            if self.active and len(self.text) <= 2:
                self.text += event.unicode
            # Re-render the text.
            self.text_surf = self.font_surf.render(self.text,
                                                   True,
                                                   (0, 0, 0))
        # allow backspace.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            if self.active and len(self.text) > 0:
                self.text = self.text[:-1]
            # Re-render the text.
            self.text_surf = self.font_surf.render(self.text,
                                                   True,
                                                   (0, 0, 0))

    def get_text(self):
        """Returns an integer form of the current displayed text."""
        return int(self.text)
