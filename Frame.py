from MakeButton import MakeButton
import GameBase
import pygame

class Frame:

    down = 0
    right = 0
    mainGame = 0


    def __init__(self, down, right, gamebase, battle):
        self.down = down
        self.right = right
        self.mainGame = gamebase
        self.battle = battle
        self.display = self.mainGame.display
        self.buttons = []
        self.attackButton = None
        self.runButton = None
        self.itemButton = None
        self.cringeButton = None

    def efill(self, color):
        self.display.fill(color)

    def makeRect(self, color, width, depth):
        pygame.draw.rect(self.display, color, (self.right, self.down, width, depth))

    def uniqueRect(self, color, right, down, width, depth):
        pygame.draw.rect(self.display, color, (right, down, width, depth))

    def addButtons(self):
        self.attackButton = MakeButton(self.mainGame, callback=self.destroyUniverse, width=250, height=100, desired_x=200, desired_y=375, standard_img=None, hover_img=None)
        self.attackButton.show()
        self.runButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '2'), width=250, height=100, desired_x=600, desired_y=375, standard_img=None, hover_img=None)
        self.runButton.show()
        self.itemButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '3'), width=250, height=100, desired_x=200, desired_y=525, standard_img=None, hover_img=None)
        self.itemButton.show()
        self.cringeButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '4'), width=250, height=100, desired_x=600, desired_y=525, standard_img=None, hover_img=None)
        self.cringeButton.show()

    def destroyUniverse(self):
        raise



