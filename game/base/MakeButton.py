import pygame
from game.base import GameBase

BUTTONS = []
class MakeButton:

    x_position = 0
    y_position = 0
    img_width = 0
    img_height = 0
    visible = None
    standard_img = ''
    hover_img = ''
    clicked_img = ''
    resolution_width = 800
    resolution_height = 600

    def __init__(self, base, width, height, desired_x, desired_y, visibility, standard_img, hover_img, press_img=None, text=None, callback=None):
        self.base = base
        self.img_width = width
        self.img_height = height
        self.x_position = desired_x-width//2
        self.y_position = desired_y-height//2
        self.standard_img = pygame.image.load(standard_img) if standard_img else None
        self.hover_img = pygame.image.load(hover_img) if hover_img else None
        self.press_img = pygame.image.load(press_img) if press_img else None
        self.callback = callback
        self.visible = visibility
        self.pressed = False
        self.rect = None
        self.text = text


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
        if not self.imgStandard():
            self.rect = pygame.Rect(self.x_position, self.y_position, self.img_width, self.img_height)
            if not self.visible:
                self.rect.set_alpha(0)
        BUTTONS.append(self)
        self.process()

    def hide(self):
        if self in BUTTONS:
            BUTTONS.remove(self)

    def process(self):
        hovered = False
        rect = self.rect
        if not rect:
            rect = self.imgStandard().get_rect()
        rect.x, rect.y = self.getXY()
        if rect.collidepoint(pygame.mouse.get_pos()):
            if not self.base.CLICK_STATE or self.pressed:
                if self.imgHover():
                    self.base.display.blit(self.imgHover(), self.getXY())
                else:
                    self.rectVis = pygame.draw.rect(self.base.display, GameBase.green, self.rect)
                hovered = True
        else:
            if self.imgStandard():
                self.base.display.blit(self.imgStandard(), self.getXY())
            else:
                self.rectVis = pygame.draw.rect(self.base.display, GameBase.white, self.rect)

        if self.text:
            textRect = self.text.get_rect()
            textWidth = textRect.width
            textHeight = textRect.height
            x, y = rect.center
            self.base.display.blit(self.text, (x - textWidth / 2, y - textHeight / 2))

        if pygame.mouse.get_pressed()[0] and hovered:
            self.pressed = 1
        elif self.pressed and not hovered and not pygame.mouse.get_pressed()[0]:
            self.pressed = 0
        elif not pygame.mouse.get_pressed()[0] and hovered and self.pressed:
            self.pressed = 0
            if self.callback:
                self.callback()
