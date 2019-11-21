from game.base import GameBase
from game.battle import Battle
from game.base.MakeButton import MakeButton
from game.locations.Location import Location
import pygame
import random


class starting_town(Location):

 ##    def __init__(self, player, base):
 ##        location(player, base)

    def __init__(self, player, base, mapp):
        Location.__init__(self, player, base, mapp)
        pygame.init()
        self.enemies = self.screen.enemies.getList(0, 2, 5)
        self.hospitalImg = pygame.image.load('hospital.png')
        self.myfont = pygame.font.SysFont('comicsansms', 26)

    def addButtons(self):
        self.battleButton = MakeButton(self.screen, callback=self.enterBattle, width=250, height=100,
                                    desired_x=100, desired_y=450, visibility=False, standard_img=None, hover_img=None)
        self.hospitalButton = MakeButton(self.screen, callback=self.goHospital, width=250, height=100,
                                    desired_x=500, desired_y=200, visibility=True, standard_img=None, hover_img=None,
                                    text=self.myfont.render("Hospital UWU", True, GameBase.black))
        self.hospitalHealButton = MakeButton(self.screen,
                                    callback=self.the_Player.playerHospitalHeal,
                                    width=250, height=100,
                                    desired_x=500, desired_y=250, visibility=True, standard_img=None, hover_img=None,
                                    text=self.myfont.render("Heal Time!", True, GameBase.black))
        self.leaveHospitalButton = MakeButton(self.screen, callback=self.leaveHospital, width=250, height=100,
                                    desired_x=100, desired_y=450, visibility=True, standard_img=None, hover_img=None,
                                    text=self.myfont.render(" Exit", True, GameBase.black))

    def showMainButtons(self):
        self.battleButton.show()
        self.hospitalButton.show()

    def hideMainButtons(self):
        self.battleButton.hide()
        self.hospitalButton.hide()

    def showHospitalButtons(self):
        self.hospitalHealButton.show()
        self.leaveHospitalButton.show()

    def hideHospitalButtons(self):
        self.hospitalHealButton.hide()
        self.leaveHospitalButton.hide()

    def goHospital(self):
        self.hideMainButtons()
        self.display.blit(self.hospitalImg, (0, 0))
        self.showHospitalButtons()

    def leaveHospital(self):
        self.hideHospitalButtons()
        self.display.blit(self.locationMap, (0, 0))
        self.showMainButtons()

    def enterBattle(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        specific_enemy = self.enemies[random.randint(0,2)]
        self.hideMainButtons()
        self.screen.battleTime(specific_enemy)