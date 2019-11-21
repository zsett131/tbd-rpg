from game.enemy.EnemyBasic import EnemyBasic
from game.inventory import ConsumableItemsList

"""
This class creates a list of every enemy within the game based on the 
players level.
__author__ = Jairo Garciga
"""
class EnemyList():

    ListofEnemies = []
    returnList = []
    player_level = None

    def __init__(self, level):
        self.player_level = level

    def getList(self, *args):
        for arg in args:
            self.returnList.append(self.ListofEnemies[arg])
        return self.returnList
    # -----------------------------------------Chad enemy loot table and enemy is created. Enemy 0.
    # Enemy Class template (Name, Description, level, playerlevel, hp, exp, damage, lootTables, icon).

    # Chad Family: 0-1
    ChadsLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0]]
    Chad = EnemyBasic("Chad", "Boring", 1, player_level, 16, 50, 2, ChadsLoot, 'chad')
    ListofEnemies.append(Chad)

    ChadsLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0]]
    Super_Chad = EnemyBasic("Super Chad", "Alpha", 3,  player_level, 20, 50, 2, ChadsLoot, 'mega_chad.png')
    ListofEnemies.append(Super_Chad)

    # Sheldon Family: 2-4
    BazingaLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
    Bazinga = EnemyBasic("Young Sheldon", "Prezinga.", 1,  player_level, 15, 50, 1, BazingaLoot, 'baby_sheldon.png')
    ListofEnemies.append(Bazinga)

    BazingaLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[2]]
    Old_Bazinga = EnemyBasic("Sheldon", "Beware of the Bazinga.", 4,  player_level, 25, 50, 3, BazingaLoot, 'sheldon.png')
    ListofEnemies.append(Old_Bazinga)

    BazingaLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
    Enranged_Bazinga = EnemyBasic("Enranged_Sheldon", "Beware of the Bazinga.", 8,  player_level, 40, 50, 5, BazingaLoot, 'enraged_sheldon.png')
    ListofEnemies.append(Enranged_Bazinga)

    # Shaggy Family 5-9
    ShaggyLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
    regular_shaggy = EnemyBasic("Shaggy", "Zoinks", 2,  player_level, 10, 40, 1, ShaggyLoot, 'regular_shaggy.png')
    ListofEnemies.append(regular_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[2], ConsumableItemsList.consumables[2]]
    enraged_shaggy = EnemyBasic("Angered Shaggy", "ZoinksX2", 7,  player_level, 38, 200, 5, ShaggyLoot, 'enraged_shaggy.png')
    ListofEnemies.append(enraged_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
    SSJ_shaggy = EnemyBasic("SSJ Shaggy", "Mega Zoinks", 15,  player_level, 80, 450, 10, ShaggyLoot, 'ssj_shaggy.png')
    ListofEnemies.append(SSJ_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
    SSJ_god_shaggy = EnemyBasic("SSJSSJ Shaggy", "MonkaS", 30,  player_level, 200, 1000, 25, ShaggyLoot, 'ssjgod_shaggy.png')
    ListofEnemies.append(SSJ_god_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
    ultra_shaggy_blanco = EnemyBasic("Shaggy Blanco", "....", 55,  player_level, 690, 2785, 69, ShaggyLoot, 'ultra_shaggy_blanco.png')
    ListofEnemies.append(ultra_shaggy_blanco)


