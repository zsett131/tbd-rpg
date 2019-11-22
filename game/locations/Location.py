"""
This class is the parent for each location class.
__author__ = Jairo Garciga
"""

import pygame
from game.enemy.EnemyList import EnemyList


class Location:
    """
    Parent class for each location in the game
    """
    pygame.init()
    screen = None
    the_Player = None
    enemies = None
    battle = None
    locationMap = None

    def __init__(self, player, base, mapp):
        """
        The constructor sets up the player object so that the location can
        access certain attributes like health.
        The parameter base allows the buttons made in location and the
        picture of the location to be drawn onto the screen.
        :param player: the player
        :param base: GameBase object
        :param mapp: the picture of the location
        """
        self.the_Player = player
        self.screen = base
        self.enemies = EnemyList(self.the_Player.get_player_level())
        self.locationMap = pygame.image.load(mapp)
        self.display = self.screen.display
        self.display.blit(self.locationMap, (0, 0))

    def show_main_buttons(self):
        """
        A function that calls all the "show" functions for each button
        """
        pass

    def hide_main_buttons(self):
        """
        A function that calls all the "hide" functions for each button
        """
        pass
