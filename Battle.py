from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
from GameBase import GameBase
from Frame import Frame
import ConsumableItemsList
import time

class Battle:

    thePlayer = PlayerBase
    theEnemy = EnemyBasic
    battleFrame = 0

    def __init__(self, Player, Enemy, mainGame):
        thePlayer = Player
        theEnemy = Enemy
        self.battleFrame = Frame(100,100, mainGame)

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
