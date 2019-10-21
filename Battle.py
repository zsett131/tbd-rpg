from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic

class Battle:
    def __init__ (self, Player, Enemy):

        while not(Player.isPlayerAlive()) and not(Enemy.isAlive()):
            pass
