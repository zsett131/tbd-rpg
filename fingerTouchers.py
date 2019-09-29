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
        self.x_position = desired_x-width//2
        self.y_position = desired_y-height//2
        self.standard_img = pygame.image.load(img_one)
        self.hover_img = pygame.image.load(img_two)

    def getXPosition(self):
        return self.x_position

    def getYPosition(self):
        return self.y_position