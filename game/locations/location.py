from game.base import GameBase
from game.battle import Battle
from game.enemy import EnemyList

class Location:

    the_Player = None
    enemies = None
    battle = None

    def __init__(self, player, base):
        self.the_Player = player
        self.enemies = EnemyList(self.the_Player)

    def addButtons(self):
        None

    def showMainButtons(self):
        None
    
    def hideMainButtons(self):
        None