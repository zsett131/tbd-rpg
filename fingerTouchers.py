import pygame
import sys

class fingerTouchers:

    x_position = 0
    y_position = 0
    img_width = 0
    img_height = 0
    standard_img = ''
    hover_img = ''
    clicked_img = ''
    resolution_width = 800
    resolution_height = 600

    def __init__(self, width, height, desired_x, desired_y, img_one, img_two):

        self.img_width = width
        self.img_height = height
        self.x_position = self.resolution_width-(desired_x//2)
        self.y_position = self.resolution_height-(desired_y//2)
        self.standard_img = pygame.image.load(img_one)
        self.hover_img = pygame.image.load(img_two)

    def setStandardImg(self):
        pygame.display.set_mode.blit(self.standard_img, (self.x_position, self.y_position))

    def setHoverImg(self):
        pygame.display.set_mode.blit(self.hover_img, (self.x_position, self.y_position))