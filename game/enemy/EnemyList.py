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
    list_of_enemies = []
    returnList = []
    player_level = None

    def __init__(self, level):
        self.player_level = level

    def get_list(self, *args):
        """
        Returns the list of specific enemies
        :param args: The enemies
        :return: The enemy list which gets sent back to the location.
        """
        for arg in args:
            self.returnList.append(self.list_of_enemies[arg])
        return self.returnList

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
    Chad = EnemyBasic("Chad", "Boring", 1, player_level, 16, 50, 2, chads_loot,
                      'chad')
    list_of_enemies.append(Chad)

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
    Super_Chad = EnemyBasic("Super Chad", "Alpha", 3, player_level, 20, 50, 2,
                            chads_loot, 'mega_chad.png')
    list_of_enemies.append(Super_Chad)

    # Sheldon Family: 2-4
    bazinga_loot = [ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[1],
                    ConsumableItemsList.consumables[1]]
    bazinga = EnemyBasic("Young Sheldon", "Prezinga.", 1, player_level, 15, 50,
                         1, bazinga_loot, 'baby_sheldon.png')
    list_of_enemies.append(bazinga)

    bazinga_loot = [ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[1],
                    ConsumableItemsList.consumables[2]]
    Old_Bazinga = EnemyBasic("Sheldon", "Beware of the bazinga.", 4,
                             player_level, 25, 50, 3, bazinga_loot,
                             'sheldon.png')
    list_of_enemies.append(Old_Bazinga)

    bazinga_loot = [ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[0],
                    ConsumableItemsList.consumables[1],
                    ConsumableItemsList.consumables[1]]
    enranged_bazinga = EnemyBasic("Enranged_Sheldon", "Beware of the bazinga.",
                                  8, player_level, 40, 50, 5, bazinga_loot,
                                  'enraged_sheldon.png')
    list_of_enemies.append(enranged_bazinga)

    # Shaggy Family 5-9
    ShaggyLoot = [ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[1],
                  ConsumableItemsList.consumables[1]]
    regular_shaggy = EnemyBasic("Shaggy", "Zoinks", 2, player_level, 10, 40, 1,
                                ShaggyLoot, 'regular_shaggy.png')
    list_of_enemies.append(regular_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[2],
                  ConsumableItemsList.consumables[2]]
    enraged_shaggy = EnemyBasic("Angered Shaggy", "ZoinksX2", 7, player_level,
                                38, 200, 5, ShaggyLoot, 'enraged_shaggy.png')
    list_of_enemies.append(enraged_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[1],
                  ConsumableItemsList.consumables[1]]
    SSJ_shaggy = EnemyBasic("SSJ Shaggy", "Mega Zoinks", 15, player_level, 80,
                            450, 10, ShaggyLoot, 'ssj_shaggy.png')
    list_of_enemies.append(SSJ_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[1],
                  ConsumableItemsList.consumables[1]]
    SSJ_god_shaggy = EnemyBasic("SSJSSJ Shaggy", "MonkaS", 30, player_level,
                                200, 1000, 25, ShaggyLoot, 'ssjgod_shaggy.png')
    list_of_enemies.append(SSJ_god_shaggy)

    ShaggyLoot = [ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[0],
                  ConsumableItemsList.consumables[1],
                  ConsumableItemsList.consumables[1]]
    ultra_shaggy_blanco = EnemyBasic("Shaggy Blanco", "....", 55, player_level,
                                     690, 2785, 69, ShaggyLoot,
                                     'ultra_shaggy_blanco.png')
    list_of_enemies.append(ultra_shaggy_blanco)
