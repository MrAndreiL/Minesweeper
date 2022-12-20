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

    def set_rectangle(self, x, y):
        """Positions the rectangle to a newer spot."""
        self.rect.x = x
        self.rect.y = y
