import pygame
from game.base import GameBase
from game.thirdparty.TextInput import TextInput

SELECTED = None
FIELDS = []

class InputField:
    def __init__(self, base, xPos, yPos, width, height, fontSize, initialString='', maxLength=-1, space=True, callback=None):
        self.base = base
        self.xPos = xPos-width//2
        self.yPos = yPos-height//2
        self.width = width
        self.height = height
        self.fontSize = fontSize
        self.initialString = initialString
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.textInput = TextInput(initial_string=initialString, font_size=fontSize, max_string_length=maxLength)
        self.space = space
        self.callback = callback

    def draw(self):
        pygame.draw.rect(self.base.display, GameBase.white, self.rect)
        surface = self.textInput.get_surface()
        self.base.display.blit(surface, (self.rect.x + 1, self.rect.centery - surface.get_height() / 2))

    def show(self):
        FIELDS.append(self)

    def hide(self):
        FIELDS.remove(self)

    def process(self, events):
        if self == SELECTED:
            for event in events:
                if not self.space:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        events.remove(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.callback:
                        self.callback()
                        return

            self.textInput.update(events)

        self.draw()




