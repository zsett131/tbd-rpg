from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
import ConsumableItemsList
import time

class Battle:
    Player = PlayerBase
    Enemy = EnemyBasic
    def __init__(self, Player, Enemy):
        self.Player = Player
        self.Player.setPlayerDamage(15)
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
        Player.getBattleDrops(Enemy.died())
        print(Player.getPlayerExp())
        print(Player.getItem(0))
        print(Player.getPlayerInventory())
ChadsLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0]]

A = PlayerBase("Jairo")
B = EnemyBasic("Chad", "Boring", 5, A.getPlayerLevel(), 20, 50, 2, ChadsLoot)
Battle(A, B)