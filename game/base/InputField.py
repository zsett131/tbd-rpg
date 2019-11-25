"""
This is used for creating input fields that text can be typed into.
__author__: Zachary Setterquist
"""
import pygame

from game.base import GameBase
from game.thirdparty.TextInput import TextInput

SELECTED = None
FIELDS = []


class InputField:
    """
    This is a class for creating text entry input fields.
    """

    def __init__(self, base, x_pos, y_pos, width, height, font_size,
                 initial_string='', max_length=-1, space=True, callback=None):
        self.base = base
        self.xPos = x_pos - width // 2
        self.yPos = y_pos - height // 2
        self.width = width
        self.height = height
        self.fontSize = font_size
        self.initialString = initial_string
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.textInput = TextInput(initial_string=initial_string,
                                   font_size=font_size,
                                   max_string_length=max_length)
        self.space = space
        self.callback = callback

    def draw(self):
        """
        Draws the white field input box.
        """
        pygame.draw.rect(self.base.display, GameBase.white, self.rect)
        surface = self.textInput.get_surface()
        surface_y = self.rect.centery - surface.get_height() / 2
        self.base.display.blit(surface, (self.rect.x + 1, surface_y))

    def show(self):
        """
        Begins processing the input field every frame.
        """
        FIELDS.append(self)

    def hide(self):
        """
        Stops processing the input field every frame.
        """
        FIELDS.remove(self)

    def process(self, events):
        """
        Processes the key events for typing into the input field.
        :param events: All the events for the current frame.
        :return: None
        """
        if self == SELECTED:
            for event in events:
                if not self.space:
                    if event.type == pygame.KEYDOWN and \
                            event.key == pygame.K_SPACE:
                        events.remove(event)
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_RETURN:
                    if self.callback:
                        self.callback()
                        return

            self.textInput.update(events)

        self.draw()
