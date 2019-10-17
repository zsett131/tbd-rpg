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
    enemy_health_bar_color = (0,0,0)
    player_health_bar_length = 150
    player_health_bar_color = (0,0,0)
    enemyHealthBar = pygame.Rect(125, 50, enemy_health_bar_length, 25)
    playerHealthBar = pygame.Rect(600, 225, player_health_bar_length, 25)

    character_bar = pygame.image.load('Character_Bar.png')

    def __init__(self, Player, Enemy, mainGame):
        self.thePlayer = Player
        self.theEnemy = Enemy
        self.bottomBattleFrame(mainGame)
        self.topBattleFrame(mainGame)

    def bottomBattleFrame(self, mainGame):
        self.bottomFrame = Frame(300, 0, mainGame, self)
        self.bottomFrame.makeRect(GameBase.blue, 800, 300)
        self.bottomFrame.addButtons()

    def topBattleFrame(self, mainGame):
        self.topFrame = Frame(0, 0, mainGame, self)
        self.topFrame.makeRect(GameBase.lightblue, 800, 300)
        self.topFrame.display.blit(self.character_bar, (25, 25))
        self.topFrame.display.blit(self.character_bar, (500, 200))

        # Creates the Font and renders them.
        text = self.myfont.render(self.theEnemy.getName(), True, GameBase.black)
        self.topFrame.display.blit(text, (54, 43))
        text = self.myfont.render(self.thePlayer.getPlayerName(), True, GameBase.black)
        self.topFrame.display.blit(text, (530, 218))

        # Draws the Player and Enemy Health Bars
        self.drawHealthBars()

    def drawHealthBars(self):
        # Sets the pixel amount of the bar
        self.player_health_bar_length = int(self.player_health_bar_length * self.thePlayer.getPlayerHealthPercentage())
        self.enemy_health_bar_length = int(self.enemy_health_bar_length * self.theEnemy.getEnemyHealthPercentage())

        # Draws a white rectangle over the hp, allowing for a green rectangle to be put on top
        pygame.draw.rect(self.topFrame.display, GameBase.white, (125, 50, 150, 25))
        pygame.draw.rect(self.topFrame.display, GameBase.white, (600, 225, 150, 25))

        # Sets the color of the Player and Enemies health bar
        if self.thePlayer.getPlayerCurrentHealth() <= 0.0:
            self.player_health_bar_color = GameBase.white
        elif self.thePlayer.getPlayerHealthPercentage() <= 1/3:
            self.player_health_bar_color = GameBase.red
        elif self.thePlayer.getPlayerHealthPercentage() <= 2/3:
            self.player_health_bar_color = GameBase.orange
        else:
            self.player_health_bar_color = GameBase.green

        if self.theEnemy.getHp() <= 0.0:
            self.enemy_health_bar_color = GameBase.white
        elif self.theEnemy.getEnemyHealthPercentage() <= 1/3:
            self.enemy_health_bar_color = GameBase.red
        elif self.theEnemy.getEnemyHealthPercentage() <= 2/3:
            self.enemy_health_bar_color = GameBase.orange
        else:
            self.enemy_health_bar_color = GameBase.green

        # Creates the new player and enemy hp bar
        self.playerHealthBar = pygame.Rect(600, 225, self.player_health_bar_length, 25)
        self.enemyHealthBar = pygame.Rect(125, 50, self.enemy_health_bar_length, 25)
        print("Player hp: ", self.thePlayer.getPlayerCurrentHealth())
        print("Enemy hp: ", self.theEnemy.getHp())

        # Draws both the enemy and player hp arb
        if self.player_health_bar_length != 0:
            pygame.draw.rect(self.topFrame.display, self.player_health_bar_color, self.playerHealthBar)
            self.battleComplete()
        if self.enemy_health_bar_length != 0:
            pygame.draw.rect(self.topFrame.display, self.enemy_health_bar_color, self.enemyHealthBar)
            self.battleComplete()

    def damagePlayer(self):
        return self.thePlayer.playerTakeDamage(self.theEnemy.getDamage())

    def damageEnemy(self):
        return self.theEnemy.enemyTakeDamage(self.thePlayer.playerAttack())

    def battleComplete(self):
        if self.thePlayer.isPlayerAlive() and not self.theEnemy.isAlive():
            self.thePlayer.getBattleDrops(self.theEnemy.died())
            return self.thePlayer
        else:
            return self.thePlayer

