from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
import ConsumableItemsList
import time

class Battle:

    thePlayer = PlayerBase
    theEnemy = EnemyBasic

    def __init__(self, Player, Enemy):
        thePlayer = Player
        theEnemy = Enemy

    def damagePlayer(self):
        return self.thePlayer.playerTakeDamage(self.Enemy.enemyAttack)

    def damageEnemy(self):
        return self.theEnemy.enemyTakeDamage(self.thePlayer.playerAttack())

    def battleComplete(self):
        if self.thePlayer.isPlayerAlive() and not self.theEnemy.isAlive():
            self.thePlayer.getBattleDrops(self.theEnemy.died())
            return self.thePlayer
        else:
            return self.thePlayer
