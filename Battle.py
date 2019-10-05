from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
from Frame import Frame
import GameBase
import time

class Battle:

    thePlayer = PlayerBase
    theEnemy = EnemyBasic
    bottomFrame = 0
    topFrame = 0

    def __init__(self, Player, Enemy, mainGame):
        thePlayer = Player
        theEnemy = Enemy
        self.bottomBattleFrame(mainGame)
        self.topBattleFrame(mainGame)

    def bottomBattleFrame(self,mainGame):
        self.bottomFrame = Frame(300, 0, mainGame)
        self.bottomFrame.makeRect(GameBase.blue, 800, 300)

    def topBattleFrame(self, mainGame):
        self.topFrame = Frame(0, 0, mainGame)
        self.topFrame.makeRect(GameBase.lightblue, 800, 300)
        self.topFrame.uniqueRect(GameBase.red, 50, 25, 275, 75)
        self.topFrame.uniqueRect(GameBase.red, GameBase.DISPLAY_WIDTH-50-275, GameBase.DISPLAY_HEIGHT-25-75-300, 275, 75)


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

