from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
import time

class Battle:
    Player = PlayerBase
    Enemy = EnemyBasic
    def __init__(self, Player, Enemy):
        self.Player = Player
        self.Player.setPlayerDamage(5)
        self.Enemy = Enemy

        while Player.isPlayerAlive() and Enemy.isAlive():
            print(Player.getPlayerName(), "has", Player.getPlayerCurrentHealth(), "current health.")
            time.sleep(1)
            print(Enemy.getName(), "has", Enemy.getHp(), "current health.")
            time.sleep(1)
            Enemy.enemyTakeDamage(Player.playerAttack())
            print(Enemy.getName(), "took", Player.playerAttack(), "damage.")
            time.sleep(1)
            Player.playerTakeDamage(Enemy.enemyAttack())
            print(Player.getPlayerName(), "took", Enemy.enemyAttack(), "damage.")
            time.sleep(1)
        print(Enemy.getName(), "has been Euthanized")
        print("Player Exp: ", Player.getPlayerExp())

A = PlayerBase("Jairo")
B = EnemyBasic("Chad", "Boring", 5, A.getPlayerLevel(), 20, 50, 2, [])
Battle(A, B)