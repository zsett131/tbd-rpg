import pygame
import sys
BUTTONS = []
class MakeButton:

    x_position = 0
    y_position = 0
    img_width = 0
    img_height = 0
    standard_img = ''
    hover_img = ''
    clicked_img = ''
    resolution_width = 800
    resolution_height = 600

    def __init__(self, base, width, height, desired_x, desired_y, img_one, img_two, callback=None):
        self.base = base
        self.img_width = width
        self.img_height = height
        self.x_position = desired_x-width//2
        self.y_position = desired_y-height//2
        self.standard_img = pygame.image.load(img_one)
        self.hover_img = pygame.image.load(img_two)
        self.callback = callback
        self.pressed = False

    def getXPosition(self):
        return self.x_position

    def getYPosition(self):
        return self.y_position

    def getXY(self):
        return self.getXPosition(), self.getYPosition()

    def imgStandard(self):
        return self.standard_img

    def imgHover(self):
        return self.hover_img

    def show(self):
        self.base.display.blit(self.imgStandard(), self.getXY())
        BUTTONS.append(self)

    def hide(self):
        BUTTONS.remove(self)

    def process(self):
        mouse = pygame.mouse.get_pos()
        x, y = self.standard_img.get_size()
        hovered = False
        if self.getXPosition() < mouse[0] < self.getXPosition() + x and \
                self.getYPosition() < mouse[1] < self.getYPosition() + y:
            if not self.base.CLICK_STATE or self.pressed:
                self.base.display.blit(self.imgHover(), self.getXY())
                hovered = True
        else:
            self.base.display.blit(self.imgStandard(), self.getXY())

        if pygame.mouse.get_pressed()[0] and hovered:
            self.pressed = 1
        elif self.pressed and not hovered and not pygame.mouse.get_pressed()[0]:
            self.pressed = 0
        elif not pygame.mouse.get_pressed()[0] and hovered and self.pressed:
            self.pressed = 0
            if self.callback:
                self.callback()
