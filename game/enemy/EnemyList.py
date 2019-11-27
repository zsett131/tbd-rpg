"""
This class creates a list of every enemy within the game based on the
players level.
__author__ = Jairo Garciga
"""
from game.enemy.EnemyBasic import EnemyBasic
from game.inventory import ConsumableItemsList


class EnemyList:
    """
    The creation of the enemy list in regards to the player level.
    Works closely with the location to create the location's enemy list.
    """
    def __init__(self):
        self.list_of_enemies = []
        self.returnList = []
        # Chad enemy loot table and enemy is created. Enemy 0.

        # Chad Family: 0-1
        chads_loot = [ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0],
                      ConsumableItemsList.consumables[0]]
        chad_stats = [1, 30, 2, 1, 1, 1, 2, 20]
        Chad = EnemyBasic("Chad", "Boring", chad_stats, chads_loot,
                          'chad')
        self.list_of_enemies.append(Chad)

        super_chad_stats = [7, 55, 4, 2, 1, 2, 4, 35]
        Super_Chad = EnemyBasic("Super Chad", "Alpha", super_chad_stats,
                                chads_loot, 'mega_chad.png')
        self.list_of_enemies.append(Super_Chad)

        # Sheldon Family: 2-4
        young_sheldon_loot = [ConsumableItemsList.consumables[0],
                              ConsumableItemsList.consumables[0],
                              ConsumableItemsList.consumables[0],
                              ConsumableItemsList.consumables[1],
                              ConsumableItemsList.consumables[1]]
        young_sheldon_stats = [2, 25, 1, 2, 2, 0, 1, 15]
        young_sheldon = EnemyBasic("Young Sheldon", "Prezinga.",
                                   young_sheldon_stats, young_sheldon_loot,
                                   'baby_sheldon.png')
        self.list_of_enemies.append(young_sheldon)

        normal_sheldon_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[1],
                               ConsumableItemsList.consumables[2]]
        normal_sheldon_stats = [6, 40, 2, 2, 5, 1, 2, 25]
        normal_sheldon = EnemyBasic("Sheldon", "Beware of the bazinga.",
                                    normal_sheldon_stats, normal_sheldon_loot,
                                    'sheldon.png')
        self.list_of_enemies.append(normal_sheldon)

        enraged_sheldon_loot = [ConsumableItemsList.consumables[0],
                                ConsumableItemsList.consumables[0],
                                ConsumableItemsList.consumables[1],
                                ConsumableItemsList.consumables[2],
                                ConsumableItemsList.consumables[2]]
        enraged_sheldon_stats = [13, 60, 2, 3, 8, 2, 2, 40]
        enraged_sheldon = EnemyBasic("Enranged_Sheldon",
                                     "Beware of the bazinga.",
                                     enraged_sheldon_stats,
                                     normal_sheldon_loot,
                                     'enraged_sheldon.png')
        self.list_of_enemies.append(enraged_sheldon)

        # Shaggy Family 5-9
        regular_shaggy_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[1],
                               ConsumableItemsList.consumables[1]]
        regular_shaggy_stats = [1, 20, 2, 2, 1, 1, 1, 20]
        regular_shaggy = EnemyBasic("Shaggy", "Zoinks", regular_shaggy_stats,
                                    regular_shaggy_loot, 'regular_shaggy.png')
        self.list_of_enemies.append(regular_shaggy)

        enraged_shaggy_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[2],
                               ConsumableItemsList.consumables[2]]
        enraged_shaggy_stats = [5, 35, 4, 2, 1, 2, 2, 35]
        enraged_shaggy = EnemyBasic("Angered Shaggy", "ZoinksX2",
                                    enraged_shaggy_stats,
                                    regular_shaggy_loot, 'enraged_shaggy.png')
        self.list_of_enemies.append(enraged_shaggy)

        SSJ_shaggy_loot = [ConsumableItemsList.consumables[0],
                           ConsumableItemsList.consumables[0],
                           ConsumableItemsList.consumables[0],
                           ConsumableItemsList.consumables[1],
                           ConsumableItemsList.consumables[1]]
        SSJ_shaggy_stats = [12, 80, 6, 3, 2, 3, 4, 48]
        SSJ_shaggy = EnemyBasic("SSJ Shaggy", "Mega Zoinks",
                                SSJ_shaggy_stats, SSJ_shaggy_loot,
                                'ssj_shaggy.png')
        self.list_of_enemies.append(SSJ_shaggy)

        SSJ_god_shaggy_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[1],
                               ConsumableItemsList.consumables[1]]
        SSJ_god_shaggy_stats = [20, 150, 10, 5, 3, 6, 7, 100]
        SSJ_god_shaggy = EnemyBasic("SSJSSJ Shaggy", "MonkaS",
                                    SSJ_god_shaggy_stats, SSJ_god_shaggy_loot,
                                    'ssjgod_shaggy.png')
        self.list_of_enemies.append(SSJ_god_shaggy)

        ultra_shaggy_blanco_loot = [ConsumableItemsList.consumables[0],
                                    ConsumableItemsList.consumables[0],
                                    ConsumableItemsList.consumables[0],
                                    ConsumableItemsList.consumables[1],
                                    ConsumableItemsList.consumables[1]]
        ultra_shaggy_blanco_stats = [50, 2500, 75, 100, 25, 40, 80, 1000]
        ultra_shaggy_blanco = EnemyBasic("Shaggy Blanco", "....",
                                         ultra_shaggy_blanco_stats,
                                         ultra_shaggy_blanco_loot,
                                         'ultra_shaggy_blanco.png')
        self.list_of_enemies.append(ultra_shaggy_blanco)

    def get_list(self, *args):
        """
        Returns the list of specific enemies
        :param args: The enemies
        :return: The enemy list which gets sent back to the location.
        """
        for arg in args:
            self.returnList.append(self.list_of_enemies[arg])
        return self.returnList
