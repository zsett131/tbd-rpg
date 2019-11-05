from game.base import GameBase
from game.battle import Battle
from game.enemy import EnemyList
from game.base.MakeButton import MakeButton
from game.locations.Location import Location

class starting_town(Location):

 ##    def __init__(self, player, base):
 ##        location(player, base)

    def addButtons(self):
        self.battleButton = MakeButton(self.screen, callback=lambda: print(self.battle, 'Button Pressed'), width=250, height=100,
                                       desired_x=600, desired_y=525, visibility=False, standard_img=None, hover_img=None)


    def showMainButtons(self):
        self.battleButton.show()

    def hideMainButtons(self):
        None