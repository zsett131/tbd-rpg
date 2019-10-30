from game.base.PlayerBase import PlayerBase
from game.battle.Frame import Frame
from game.base import GameBase
import pygame


class Battle:

    pygame.init()
    thePlayer = PlayerBase
    theEnemy = PlayerBase
    isPlayerDead = False
    isEnemyDead = False
    bottomFrame = None
    topFrame = None
    myfont = pygame.font.SysFont('comicsansms', 16)
    buttonfont = pygame.font.SysFont('comicsansms', 25)
    enemy_health_bar_length = 150
    enemy_health_bar_color = (0,0,0)
    player_health_bar_length = 150
    player_health_bar_color = (0,0,0)
    enemyHealthBar = pygame.Rect(125, 60, enemy_health_bar_length, 25)
    playerHealthBar = pygame.Rect(600, 235, player_health_bar_length, 25)

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
        self.topFrame.display.blit(self.theEnemy.icon, (550, 20))
        self.topFrame.display.blit(self.thePlayer.playerIcon, (25, 140))

        # Creates the Font and renders them.
        text = self.myfont.render(self.theEnemy.getName(), True, GameBase.black)
        self.topFrame.display.blit(text, (54, 35))
        text = self.myfont.render(self.thePlayer.getPlayerName(), True, GameBase.black)
        self.topFrame.display.blit(text, (530, 215))


        # Draws the Player and Enemy Health Bars
        self.drawHealthBars()

    def drawHealthBars(self):
        # Sets the pixel amount of the bar
        self.player_health_bar_length = int(150 * self.thePlayer.getPlayerHealthPercentage())
        self.enemy_health_bar_length = int(150 * self.theEnemy.getEnemyHealthPercentage())

        # Draws a white rectangle over the hp, allowing for a green rectangle to be put on top
        pygame.draw.rect(self.topFrame.display, GameBase.white, (125, 60, 150, 25))
        pygame.draw.rect(self.topFrame.display, GameBase.white, (600, 235, 150, 25))

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
        self.playerHealthBar = pygame.Rect(600, 235, self.player_health_bar_length, 25)
        self.enemyHealthBar = pygame.Rect(125, 60, self.enemy_health_bar_length, 25)
        print("Player hp: ", self.thePlayer.getPlayerCurrentHealth())
        print("Enemy hp: ", self.theEnemy.getHp())

        # Draws both the enemy and player hp arb
        if self.player_health_bar_length != 0:
            pygame.draw.rect(self.topFrame.display, self.player_health_bar_color, self.playerHealthBar)
            self.battleComplete()
        if self.enemy_health_bar_length != 0:
            pygame.draw.rect(self.topFrame.display, self.enemy_health_bar_color, self.enemyHealthBar)
            self.battleComplete()

        text = self.myfont.render(str(self.theEnemy.getHp()) + "/" + str(self.theEnemy.getMaxHp()), True,
                                  GameBase.black)
        textRect = text.get_rect()
        self.topFrame.display.blit(text, (130, self.enemyHealthBar.y - textRect.height / 2 + self.enemyHealthBar.height / 2))
        text = self.myfont.render(str(self.thePlayer.getPlayerCurrentHealth()) + "/" +
                                  str(self.thePlayer.getPlayerMaxHealth()), True, GameBase.black)
        textRect = text.get_rect()
        self.topFrame.display.blit(text, (605, self.playerHealthBar.y - textRect.height / 2 + self.playerHealthBar.height / 2))

    def damagePlayer(self):
        if self.thePlayer.getPlayerCurrentHealth() <= 0:
            self.isPlayerDead = True
        return self.thePlayer.playerTakeDamage(self.theEnemy.getDamage())


    def damageEnemy(self):
        if self.theEnemy.getHp() <= 0:
            self.isEnemyDead = True
        return self.theEnemy.enemyTakeDamage(self.thePlayer.playerAttack())


    def battleComplete(self):
        if self.thePlayer.isPlayerAlive() and not self.theEnemy.isAlive():
            self.thePlayer.getBattleDrops(self.theEnemy.died())
            return self.thePlayer
        else:
            return self.thePlayer

