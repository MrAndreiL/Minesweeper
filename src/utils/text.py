import pygame


class TextLabel(pygame.sprite.Sprite):
    """Text label to be attached to a display.

    Provides a text sprite label that can be displayed
    to the player. Can also be grouped into sprite groups
    for better management.

    Attriutes:
        text: the text to be written on the rectangle.
        color: text color.
        center_x: width centerpoint of the rectangle.
        center_y: height centerpoint of the rectangle
        font: text typeface.
        font_size: text size to be displayed.
        font_object: pygame type Font object
        text_object: rendering object for text formats.
        rect: rectangle object with the displaying text.
    """

    def __init__(self, text, color, font, font_size):
        """Inits TextLabel class and super class with config data."""
        super(TextLabel, self).__init__()
        # Parameter intake.
        self.text = text
        self.color = color
        self.font = font
        self.font_size = font_size

        # Generate text pattern.
        self.font_object = pygame.font.Font(self.font, self.font_size)
        self.text_object = self.font_object.render(text, True, self.color)

        # Create default rect object.
        self.rect = self.text_object.get_rect()

        # Input box associated with this label.
        self.inp = None

    def set_rectangle(self, x, y):
        """Positions the rectangle to a newer spot."""
        self.rect.x = x
        self.rect.y = y

    def update_color(self, color):
        """Updates label text color.

        Args:
            color: triple representing RGB color code.
        """
        self.text_object = self.font_object.render(self.text, True, color)

    def set_input_box(self, inp):
        """Receives the input box associated with this label.

        Args:
            inp: Input space that contains the actual number.
        """
        self.inp = inp

    def validate_rows(self):
        """Validates the input rows asssociated with this text label."""
        return (5 <= self.inp.get_text() and self.inp.get_text() <= 50)

    def validate_cols(self):
        """Validates the input columns associated with this label."""
        return (5 <= self.inp.get_text() and self.inp.get_text() <= 50)

    def validate_bombs(self, rows, cols):
        """Validates the number of bombs given as input.

        Makes sure that the number of bombs is appropiate.
        There has to be at least a bomb and at most the number
        of spots available.

        Args:
            rows: The number of rows given as input.
            cols: The number of columns given as input.

        Returns:
            A boolean value that represents the validaton.
        """ 
        return self.inp.get_text() <= (rows * cols)
    
    def validate_seconds(self):
        """Validates input seconds.

        Asserts whether the number of seconds is appropiate.
        It is expected that the number of seconds to be
        at least 30 seconds and at most 999.

        Returns:
            A boolean value that represents the assertion.
        """
        return self.inp.get_text() >= 30
