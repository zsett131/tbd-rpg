"""
This class sets up all the battles and works together with the Frame class
to establish all the graphics and numerical aspects
__author__: Jairo Garciga
"""

from game.base.PlayerBase import PlayerBase
from game.battle.Frame import Frame
from game.base import GameBase
import Images
import pygame


class Battle:
    """
    Sets up all the variables and contains all the functions necessary for
    doing battles
    """
    pygame.init()
    thePlayer = PlayerBase
    theEnemy = PlayerBase
    isPlayerDead = False
    isEnemyDead = False
    bottomFrame = None
    topFrame = None
    location = None
    my_font = pygame.font.SysFont('comicsansms', 16)
    button_font = pygame.font.SysFont('comicsansms', 25)
    enemy_health_bar_length = 150
    enemy_health_bar_color = (0, 0, 0)
    player_health_bar_length = 150
    player_health_bar_color = (0, 0, 0)
    enemyHealthBar = pygame.Rect(125, 60, enemy_health_bar_length, 25)
    playerHealthBar = pygame.Rect(600, 235, player_health_bar_length, 25)

    character_bar = pygame.image.load("Images/Character_Bar.png")

    def __init__(self, player, enemy, main_game):
        """
        Sets up the player, enemy, and the GameBase object to access
        and set their variables in battle.
        :param player: The main player object
        :param enemy: The specific enemy
        :param main_game: The GameBase object
        """
        self.thePlayer = player
        self.theEnemy = enemy
        self.bottom_battle_frame(main_game)
        self.top_battle_frame(main_game)

    def bottom_battle_frame(self, main_game):
        """
        Creates the bottom half of the battle screen
        :param main_game: The GameBase object
        """
        self.bottomFrame = Frame(300, 0, main_game, self)
        self.bottomFrame.make_rect(GameBase.blue, 800, 300)
        self.bottomFrame.add_buttons()

    def top_battle_frame(self, main_game):
        """
        Establishes the top frame including: the player and it's attributes,
        the enemy and it's attributes, the background, and draws the health
        bars
        :param main_game: GameBase object
        """
        self.topFrame = Frame(0, 0, main_game, self)
        self.topFrame.make_rect(GameBase.light_blue, 800, 300)
        self.topFrame.display.blit(self.character_bar, (25, 25))
        self.topFrame.display.blit(self.character_bar, (500, 200))
        self.topFrame.display.blit(self.theEnemy.enemy_icon, (550, 20))
        self.topFrame.display.blit(self.thePlayer.playerIcon, (25, 140))

        # Creates the Font and renders them.
        text = self.my_font.render(self.theEnemy.get_name(), True,
                                   GameBase.black)
        self.topFrame.display.blit(text, (54, 35))
        text = self.my_font.render("Level: " + str(self.theEnemy.get_level()),
                                   True, GameBase.black)
        self.topFrame.display.blit(text, (220, 35))
        text = self.my_font.render(self.thePlayer.get_player_name(), True,
                                   GameBase.black)
        self.topFrame.display.blit(text, (530, 210))
        text = self.my_font.render(
            "Level: " + str(self.thePlayer.get_player_level()), True,
            GameBase.black)
        self.topFrame.display.blit(text, (696, 210))

        # Draws the Player and Enemy Health Bars
        self.draw_health_bars()

    def draw_health_bars(self):
        """
        The most complicated of all the functions in this class.
        Draws the colored portion of the health bar and redraws it
        continuously whenever the enemy or the player takes damage.
        Colors of the bar change depending on the amount of health that the
        enemy or player have
        """
        # Sets the pixel amount of the bar
        self.player_health_bar_length = int(
            150 * self.thePlayer.get_player_health_percentage())
        self.enemy_health_bar_length = int(
            150 * self.theEnemy.get_enemy_health_percentage())

        # Draws a white rectangle over the hp, allowing for a green
        # rectangle to be put on top
        pygame.draw.rect(self.topFrame.display, GameBase.white,
                         (125, 60, 150, 25))
        pygame.draw.rect(self.topFrame.display, GameBase.white,
                         (600, 235, 150, 25))

        # Sets the color of the Player and Enemies health bar
        if self.thePlayer.get_player_current_health() <= 0.0:
            self.player_health_bar_color = GameBase.white
        elif self.thePlayer.get_player_health_percentage() <= 1 / 3:
            self.player_health_bar_color = GameBase.red
        elif self.thePlayer.get_player_health_percentage() <= 2 / 3:
            self.player_health_bar_color = GameBase.orange
        else:
            self.player_health_bar_color = GameBase.green

        if self.theEnemy.get_hp() <= 0.0:
            self.enemy_health_bar_color = GameBase.white
        elif self.theEnemy.get_enemy_health_percentage() <= 1 / 3:
            self.enemy_health_bar_color = GameBase.red
        elif self.theEnemy.get_enemy_health_percentage() <= 2 / 3:
            self.enemy_health_bar_color = GameBase.orange
        else:
            self.enemy_health_bar_color = GameBase.green

        # Creates the new player and enemy hp bar
        self.playerHealthBar = pygame.Rect(600, 235,
                                           self.player_health_bar_length, 25)
        self.enemyHealthBar = pygame.Rect(125, 60,
                                          self.enemy_health_bar_length, 25)
        print("Player hp: ", self.thePlayer.get_player_current_health())
        print("Enemy hp: ", self.theEnemy.get_hp())

        # Draws both the enemy and player hp arb
        if self.player_health_bar_length != 0:
            pygame.draw.rect(self.topFrame.display,
                             self.player_health_bar_color,
                             self.playerHealthBar)
        if self.enemy_health_bar_length != 0:
            pygame.draw.rect(self.topFrame.display,
                             self.enemy_health_bar_color, self.enemyHealthBar)

        text = self.my_font.render(
            str(self.theEnemy.get_hp()) + "/" + str(
                self.theEnemy.get_max_hp()),
            True,
            GameBase.black)
        text_rect = text.get_rect()
        self.topFrame.display.blit(text, (130,
                                          self.enemyHealthBar.y -
                                          text_rect.height / 2 +
                                          self.enemyHealthBar.height / 2))
        text = self.my_font.render(
            str(self.thePlayer.get_player_current_health()) + "/" +
            str(self.thePlayer.get_player_max_health()), True, GameBase.black)
        text_rect = text.get_rect()
        self.topFrame.display.blit(text, (605,
                                          self.playerHealthBar.y -
                                          text_rect.height / 2 +
                                          self.playerHealthBar.height / 2))

    def damage_player(self):
        """
        Function that is called to deal damage to the player
        """
        if self.thePlayer.get_player_current_health() <= 0:
            self.isPlayerDead = True
        self.thePlayer.player_take_damage(self.theEnemy.get_damage())

    def damage_enemy(self):
        """
        Deals damage to the player
        """
        if self.theEnemy.get_hp() <= 0:
            self.isEnemyDead = True
        self.theEnemy.enemy_take_damage(
            self.thePlayer.get_player_damage())
