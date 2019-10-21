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
        self.buttons = []
        self.attackButton = None
        self.runButton = None

    def efill(self, color):
        self.display.fill(color)

    def makeRect(self, color, width, depth):
        pygame.draw.rect(self.display, color, (self.right, self.down, width, depth))

    def uniqueRect(self, color, right, down, width, depth):
        pygame.draw.rect(self.display, color, (right, down, width, depth))

    def addButtons(self):
        self.attackButton = MakeButton(self.mainGame, callback=lambda: print('1'), width=250, height=100, desired_x=200, desired_y=400, standard_img=None, hover_img=None)
        self.attackButton.show()
        self.runButton = MakeButton(self.mainGame, callback=lambda: print('2'), width=250, height=100, desired_x=600, desired_y=400, standard_img=None, hover_img=None)
        self.runButton.show()



