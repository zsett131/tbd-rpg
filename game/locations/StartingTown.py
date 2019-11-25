"""
First location that the player starts in, with the weakest enemies.
__author__ = Jairo Garciga
"""

from game.base import GameBase
from game.base.MakeButton import MakeButton
from game.locations.Location import Location
import pygame
import random


class StartingTown(Location):
    """
    The starting town
    The constructor sets up the font, enemy list, images, and the buttons
    for the class
    """

    def __init__(self, player, base, mapp):
        Location.__init__(self, player, base, mapp)
        pygame.init()
        self.hospitalImg = pygame.image.load('Images/hospital.png')
        self.myfont = pygame.font.SysFont('comicsansms', 26)

        self.battleButton = MakeButton(self.screen,
                                       callback=self.enter_battle,
                                       width=250, height=100,
                                       desired_x=200, desired_y=350,
                                       visibility=True, standard_img=None,
                                       hover_img=None,
                                       text=self.myfont.render(
                                           "To Battle!", True,
                                           GameBase.black))

        self.hospitalButton = MakeButton(self.screen,
                                         callback=self.go_hospital,
                                         width=250, height=100,
                                         desired_x=500, desired_y=200,
                                         visibility=True, standard_img=None,
                                         hover_img=None,
                                         text=self.myfont.render(
                                             "Hospital UWU", True,
                                             GameBase.black))

        self.hospitalHealButton = \
            MakeButton(self.screen,
                       callback=self.the_Player.set_player_health_max,
                       width=250, height=100,
                       desired_x=500, desired_y=250,
                       visibility=True,
                       standard_img=None, hover_img=None,
                       text=self.myfont.render(
                           "Heal Time!", True,
                           GameBase.black))

        self.leaveHospitalButton = \
            MakeButton(self.screen,
                       callback=self.leave_hospital,
                       width=250, height=100,
                       desired_x=100, desired_y=450,
                       visibility=True,
                       standard_img=None,
                       hover_img=None,
                       text=self.myfont.render(" Exit",
                                               True,
                                               GameBase.black))

    def show_main_buttons(self):
        """
        A function that calls all the "show" functions for each button on
        the main screen
        """
        self.battleButton.show()
        self.hospitalButton.show()

    def hide_main_buttons(self):
        """
         A function that calls all the "hide" functions for each button on
         the main screen
        """
        self.battleButton.hide()
        self.hospitalButton.hide()

    def show_hospital_buttons(self):
        """
        Shows all the buttons in the hospital screen
        """
        self.hospitalHealButton.show()
        self.leaveHospitalButton.show()

    def hide_hospital_buttons(self):
        """
        Hides all the buttons in the hospital screen
        """
        self.hospitalHealButton.hide()
        self.leaveHospitalButton.hide()

    def go_hospital(self):
        """
        Changes the screen to the hospital and also shows all the buttons
        """
        self.hide_main_buttons()
        self.display.blit(self.hospitalImg, (0, 0))
        self.show_hospital_buttons()

    def leave_hospital(self):
        """
        Changes the screen back to the main location screen and hides the
        hospital buttons while showing the main buttons
        """
        self.hide_hospital_buttons()
        self.display.blit(self.locationMap, (0, 0))
        self.show_main_buttons()

    def enter_battle(self):
        """
        Send the random enemy that is picked to the function battle_time
        which starts the battle and generates an enemy
        """
        self.enemies = self.screen.enemies.get_list(0, 2, 5)
        specific_enemy = self.enemies[random.randint(0, 2)]
        self.hide_main_buttons()
        self.screen.battle_time(specific_enemy)
