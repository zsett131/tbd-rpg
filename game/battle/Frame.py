from game.base.MakeButton import MakeButton
from game.base import GameBase
from game.base.Animation import TextWriter
import time
import pygame

class Frame:

    pygame.init()
    down = 0
    right = 0
    mainGame = 0
    myfont = pygame.font.SysFont('Comic Sans TM', 25)

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
        self.color = None
        self.width = None
        self.depth = None
        self.textWriter = None
        self.playerDialogText = ''
        self.enemyDialogText = ''

    def efill(self, color):
        self.display.fill(color)

    def makeRect(self, color, width, depth):
        self.color = color
        self.width = width
        self.depth = depth
        pygame.draw.rect(self.display, color, (self.right, self.down, width, depth))

    def uniqueRect(self, color, right, down, width, depth):
        pygame.draw.rect(self.display, color, (right, down, width, depth))

    def addButtons(self):
        self.attackButton = MakeButton(self.mainGame, callback=self.enterAttack, width=250, height=100, desired_x=200,
                                       desired_y=375, standard_img=None, hover_img=None, text=self.battle.buttonfont.render('Attack', True, GameBase.black))
        self.runButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '2'), width=250, height=100,
                                    desired_x=600, desired_y=375, standard_img=None, hover_img=None, text=self.battle.buttonfont.render('Run', True, GameBase.black))
        self.itemButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '3'), width=250, height=100,
                                     desired_x=200, desired_y=525, standard_img=None, hover_img=None, text=self.battle.buttonfont.render('Item', True, GameBase.black))
        self.cringeButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '4'), width=250, height=100,
                                       desired_x=600, desired_y=525, standard_img=None, hover_img=None)
        self.backButton = MakeButton(self.mainGame, callback=self.exitAttack, width=25, height=25, desired_x=25,
                                     desired_y=325, standard_img='exit_normal.png', hover_img='exit_hover.png')
        self.attack1 = MakeButton(self.mainGame, callback=self.doAttack, width=250, height=100,
                                  desired_x=200, desired_y=375, standard_img=None, hover_img=None)
        self.attack2 = MakeButton(self.mainGame, callback=lambda: print(self.battle, 'attack-2'), width=250, height=100,
                                  desired_x=600, desired_y=375, standard_img=None, hover_img=None)
        self.attack3 = MakeButton(self.mainGame, callback=lambda: print(self.battle, 'attack-3'), width=250, height=100,
                                  desired_x=200, desired_y=525, standard_img=None, hover_img=None)
        self.attack4 = MakeButton(self.mainGame, callback=lambda: print(self.battle, 'attack-4'), width=250, height=100,
                                  desired_x=600, desired_y=525, standard_img=None, hover_img=None)
        self.showMain()

    def showMain(self):
        self.makeRect(self.color, self.width, self.depth)
        self.attackButton.show()
        self.runButton.show()
        self.itemButton.show()
        self.cringeButton.show()

    def enterAttack(self):
        self.attackButton.hide()
        self.runButton.hide()
        self.itemButton.hide()
        self.cringeButton.hide()
        self.makeRect(self.color, self.width, self.depth)
        self.backButton.show()
        self.attack1.show()
        self.attack2.show()
        self.attack3.show()
        self.attack4.show()

    def exitAttack(self):
        self.backButton.hide()
        self.attack1.hide()
        self.attack2.hide()
        self.attack3.hide()
        self.attack4.hide()
        self.makeRect(self.color, self.width, self.depth)
        self.showMain()

    def doAttack(self):
        self.backButton.hide()
        self.attack1.hide()
        self.attack2.hide()
        self.attack3.hide()
        self.attack4.hide()
        self.makeRect(self.color, self.width, self.depth)
        self.doPlayerDialog()

    def setPlayerDialog(self, text):
        self.playerDialogText = text
        self.makeRect(self.color, self.width, self.depth)
        text = self.myfont.render(self.playerDialogText, True, GameBase.white)
        self.display.blit(text, (20, 310))
        if self.playerDialogText == self.textWriter.text:
            self.battle.theEnemy.enemyTakeDamage(self.battle.thePlayer.getPlayerDamage())
            self.battle.drawHealthBars()
            self.mainGame.updateDisplay()
            self.doEnemyDialog()

    def setEnemyDialog(self, text):
        self.enemyDialogText = text
        self.makeRect(self.color, self.width, self.depth)
        text1 = self.myfont.render(self.playerDialogText, True, GameBase.white)
        text2 = self.myfont.render(self.enemyDialogText, True, GameBase.white)
        self.display.blit(text1, (20, 310))
        self.display.blit(text2, (20, 340))
        if self.enemyDialogText == self.textWriter.text:
            self.battle.thePlayer.playerTakeDamage(self.battle.theEnemy.getDamage())
            self.battle.drawHealthBars()
            self.mainGame.updateDisplay()
            time.sleep(1)
            self.textWriter = None
            self.playerDialogText = None
            self.enemyDialogText = None
            self.showMain()

    def doPlayerDialog(self):
        firstAttack = self.battle.thePlayer.getPlayerName() + " has dealt " + \
                      str(self.battle.thePlayer.getPlayerDamage()) + " to " + self.battle.theEnemy.getName()
        self.textWriter = TextWriter(self.mainGame, 15, firstAttack, self.setPlayerDialog)
        self.textWriter.start()

    def doEnemyDialog(self):
        secondAttack = self.battle.theEnemy.getName() + " has dealt " + \
                      str(self.battle.theEnemy.getDamage()) + " to " + self.battle.thePlayer.getPlayerName()
        self.textWriter = TextWriter(self.mainGame, 15, secondAttack, self.setEnemyDialog)
        self.textWriter.start()

