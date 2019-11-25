"""
This is used for creating buttons that can be clicked with events to be
triggered.
__authors__: Jairo Garciga and Zachary Setterquist
"""
import pygame

from game.base import GameBase

BUTTONS = []


class MakeButton:
    """
    This is a class for creating clickable button objects.
    """
    def __init__(self, base, width, height, desired_x, desired_y, visibility,
                 standard_img, hover_img, press_img=None, text=None,
                 callback=None):
        self.base = base
        self.img_width = width
        self.img_height = height
        self.x_position = desired_x - width // 2
        self.y_position = desired_y - height // 2
        self.standard_img = pygame.image.load(
            standard_img) if standard_img else None
        self.hover_img = pygame.image.load(hover_img) if hover_img else None
        self.press_img = pygame.image.load(press_img) if press_img else None
        self.callback = callback
        self.visible = visibility
        self.pressed = False
        self.rect = None
        self.text = text
        self.rectVis = None

    def get_x_position(self):
        """
        Returns the button's x position.
        :return: x position
        """
        return self.x_position

    def get_y_position(self):
        """
        Returns the button's y position.
        :return: y position
        """
        return self.y_position

    def get_xy(self):
        """
        Returns the button's position.
        :return: x and y position.
        """
        return self.get_x_position(), self.get_y_position()

    def img_standard(self):
        """
        Returns the default image of the button.
        :return: default image
        """
        return self.standard_img

    def img_hover(self):
        """
        Returns the button hover image.
        :return: hover image
        """
        return self.hover_img

    def show(self):
        """
        Starts processing for button visibility.
        """
        if not self.img_standard():
            self.rect = pygame.Rect(self.x_position, self.y_position,
                                    self.img_width, self.img_height)
        BUTTONS.append(self)
        self.process()

    def hide(self):
        """
        Stops processing for button visibility.
        """
        if self in BUTTONS:
            BUTTONS.remove(self)

    def process(self):
        """
        Processes the button visibility every frame.
        """
        hovered = False
        rect = self.rect
        if not rect:
            rect = self.img_standard().get_rect()
        rect.x, rect.y = self.get_xy()
        if rect.collidepoint(pygame.mouse.get_pos()):
            if not self.base.CLICK_STATE or self.pressed:
                if self.img_hover() and self.visible:
                    self.base.display.blit(self.img_hover(), self.get_xy())
                else:
                    if self.visible:
                        self.rectVis = pygame.draw.rect(self.base.display,
                                                        GameBase.green,
                                                        self.rect)
                hovered = True
        else:
            if self.img_standard() and self.visible:
                self.base.display.blit(self.img_standard(), self.get_xy())
            else:
                if self.visible:
                    self.rectVis = pygame.draw.rect(self.base.display,
                                                    GameBase.white, self.rect)

        if self.text and self.visible:
            text_rect = self.text.get_rect()
            text_width = text_rect.width
            text_height = text_rect.height
            x, y = rect.center
            self.base.display.blit(self.text,
                                   (x - text_width / 2, y - text_height / 2))

        if pygame.mouse.get_pressed()[0] and hovered:
            self.pressed = 1
        elif self.pressed and not hovered and \
                not pygame.mouse.get_pressed()[0]:
            self.pressed = 0
        elif not pygame.mouse.get_pressed()[0] and hovered and self.pressed:
            self.pressed = 0
            if self.callback:
                self.callback()
