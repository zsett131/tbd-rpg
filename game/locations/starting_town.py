from game.base import GameBase
from game.battle import Battle
from game.enemy import EnemyList
from game.base import MakeButton
from game.locations import location

class starting_town(location):

 ##    def __init__(self, player, base):
 ##        location(player, base)

    def addButtons(self):
        self.battleButton = MakeButton(self.mainGame, callback=lambda: print(self.battle, '4'), width=250, height=100,
                                       desired_x=600, desired_y=525, visibility=False, standard_img=None, hover_img=None)

    def showMainButtons(self):
        None

    def hideMainButtons(self):
        None