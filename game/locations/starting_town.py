from game.base import GameBase
from game.battle import Battle
from game.base.MakeButton import MakeButton
from game.locations.Location import Location
import random


class starting_town(Location):

 ##    def __init__(self, player, base):
 ##        location(player, base

    def addButtons(self):
        self.battleButton = MakeButton(self.screen, callback=self.enterBattle, width=250, height=100,
                                       desired_x=100, desired_y=450, visibility=False, standard_img=None, hover_img=None)
        self.enemies = self.screen.enemies.getList(0, 2, 5)


    def showMainButtons(self):
        self.battleButton.show()

    def hideMainButtons(self):
        self.battleButton.hide()

    def enterBattle(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        specific_enemy = self.enemies[random.randint(0,2)]
        self.hideMainButtons()
        self.screen.battleTime(specific_enemy)