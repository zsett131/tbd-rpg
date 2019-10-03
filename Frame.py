from MakeButton import MakeButton
import GameBase
import pygame

class Frame:

    down = 0
    right = 0
    mainGame = 0


    def __init__(self, down, right, gamebase):
        self.down = down
        self.right = right
        self.mainGame = gamebase
        self.display = self.mainGame.display

    def efill(self, color):
        self.display.fill(color)

    def makeRect(self, color, width, depth):
        pygame.draw.rect(self.display, color, (self.right, self.down, width, depth))

    def addButtons(self, args): #TODO
        for buttons in args:
            pass




