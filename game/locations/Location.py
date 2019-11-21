import pygame
from game.base import GameBase
from game.battle import Battle
from game.enemy.EnemyList import EnemyList

"""
This class is the parent for each location class.
__author__ = Jairo Garciga
"""

class Location:

    pygame.init()
    screen = None
    the_Player = None
    enemies = None
    battle = None
    locationMap = None

    def __init__(self, player, base, mapp):
        self.the_Player = player
        self.screen = base
        self.enemies = EnemyList(self.the_Player.get_player_level())
        self.locationMap = pygame.image.load(mapp)
        self.display = self.screen.display
        self.display.blit(self.locationMap, (0,0))

    def addButtons(self):
        None

    def showMainButtons(self):
        None

    def hideMainButtons(self):
        None