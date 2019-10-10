from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
from Frame import Frame
import GameBase
import pygame
from pygame import font
import time



class Battle:

    pygame.init()
    thePlayer = PlayerBase
    theEnemy = PlayerBase
    bottomFrame = 0
    topFrame = 0
    myfont = pygame.font.SysFont('Comic Sans TM', 25)
    enemy_health_bar_length = 150
    player_health_bar_length = 150
    enemyHealthBar = pygame.Rect(125, 50, enemy_health_bar_length, 25)
    playerHealthBar = pygame.Rect(600, 225, player_health_bar_length, 25)

    character_bar = pygame.image.load('Character_Bar.png')

    def __init__(self, Player, Enemy, mainGame):
        self.thePlayer = Player
        self.theEnemy = Enemy
        self.bottomBattleFrame(mainGame)
        self.topBattleFrame(mainGame)

    def bottomBattleFrame(self, mainGame):
        self.bottomFrame = Frame(300, 0, mainGame)
        self.bottomFrame.makeRect(GameBase.blue, 800, 300)

    def topBattleFrame(self, mainGame):
        self.topFrame = Frame(0, 0, mainGame)
        self.topFrame.makeRect(GameBase.lightblue, 800, 300)
        self.topFrame.display.blit(self.character_bar, (25, 25))
        self.topFrame.display.blit(self.character_bar, (500, 200))
        text = self.myfont.render(self.theEnemy.getName(), True, GameBase.black)
        self.topFrame.display.blit(text, (54, 43))
        text = self.myfont.render(self.thePlayer.getPlayerName(), True, GameBase.black)
        self.topFrame.display.blit(text, (530, 218))
        self.drawHealthBars()
        self.drawHealthBars()

    def drawHealthBars(self):
        # Sets the pixel amount of the bar
        self.player_health_bar_length = self.player_health_bar_length * self.thePlayer.getPlayerHealthPercentage()
        self.enemy_health_bar_length = self.enemy_health_bar_length * self.theEnemy.getEnemyHealthPercentage()
        # Draws a white rectangle over the hp, allowing for a green rectangle to be put on top
        pygame.draw.rect(self.topFrame.display, GameBase.white, (125, 50, 150, 25))
        pygame.draw.rect(self.topFrame.display, GameBase.white, (600, 225, 150, 25))
        # Creates the new player and enemy hp bar
        self.playerHealthBar = pygame.Rect(600, 225, self.player_health_bar_length, 25)
        self.enemyHealthBar = pygame.Rect(125, 50, self.enemy_health_bar_length, 25)
        # Draws both the enemy and player hp arb
        pygame.draw.rect(self.topFrame.display, GameBase.green, self.enemyHealthBar)
        pygame.draw.rect(self.topFrame.display, GameBase.green, self.playerHealthBar)

    def damagePlayer(self):
        return self.thePlayer.playerTakeDamage(10)


    def damageEnemy(self):
        return self.theEnemy.enemyTakeDamage(self.thePlayer.playerAttack())

    def battleComplete(self):
        if self.thePlayer.isPlayerAlive() and not self.theEnemy.isAlive():
            self.thePlayer.getBattleDrops(self.theEnemy.died())
            return self.thePlayer
        else:
            return self.thePlayer

