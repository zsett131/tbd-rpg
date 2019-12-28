"""
This class creates a list of every enemy within the game based on the
players level.
__author__ = Jairo Garciga
"""
from game.characters.enemy.EnemyBasic import EnemyBasic
from game.inventory import ConsumableItemsList


class EnemyList:
    """
    The creation of the enemy list in regards to the player level.
    Works closely with the location to create the location's enemy list.
    """

    def __init__(self, location):
        self.current_location = location
        self.list_of_enemies = []
        self.returnList = []
        # chad enemy loot table and enemy is created. Enemy 0.

        # chad Family: 0-1
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

        chad = EnemyBasic("chad", "Boring", chads_loot, 'chad',
                          self.current_location.base_enemy_level, 20, 25, 2,
                          .70,
                          .15, 1)
        self.list_of_enemies.append(chad)

        super_chad = EnemyBasic("Super chad", "Alpha",
                                chads_loot, 'mega_chad.png',
                                self.current_location.base_enemy_level, 40,
                                50,
                                3, .70, .15, 1)
        self.list_of_enemies.append(super_chad)

        # Sheldon Family: 2-4
        young_sheldon_loot = [ConsumableItemsList.consumables[0],
                              ConsumableItemsList.consumables[0],
                              ConsumableItemsList.consumables[0],
                              ConsumableItemsList.consumables[1],
                              ConsumableItemsList.consumables[1]]

        young_sheldon = EnemyBasic("Young Sheldon", "Prezinga.",
                                   young_sheldon_loot, 'baby_sheldon.png',
                                   self.current_location.base_enemy_level,
                                   18, 15,
                                   1, .10, .30, 1)
        self.list_of_enemies.append(young_sheldon)

        normal_sheldon_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[1],
                               ConsumableItemsList.consumables[2]]

        normal_sheldon = EnemyBasic("Sheldon", "Beware of the bazinga.",
                                    normal_sheldon_loot, 'sheldon.png',
                                    self.current_location.base_enemy_level,
                                    36, 35, 2, .10, .30, 1)
        self.list_of_enemies.append(normal_sheldon)

        enraged_sheldon_loot = [ConsumableItemsList.consumables[0],
                                ConsumableItemsList.consumables[0],
                                ConsumableItemsList.consumables[1],
                                ConsumableItemsList.consumables[2],
                                ConsumableItemsList.consumables[2]]

        enraged_sheldon = EnemyBasic("Enranged_Sheldon",
                                     "Beware of the bazinga.",
                                     enraged_sheldon_loot,
                                     'enraged_sheldon.png',
                                     self.current_location.base_enemy_level,
                                     67, 75, 4, .10, .25, 2)
        self.list_of_enemies.append(enraged_sheldon)

        # Shaggy Family 5-9
        regular_shaggy_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[1],
                               ConsumableItemsList.consumables[1]]

        regular_shaggy = EnemyBasic("Shaggy", "Zoinks",
                                    regular_shaggy_loot,
                                    'regular_shaggy.png',
                                    self.current_location.base_enemy_level,
                                    21, 17, 1, .25, .60, 1)
        self.list_of_enemies.append(regular_shaggy)

        enraged_shaggy_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[2],
                               ConsumableItemsList.consumables[2]]

        enraged_shaggy = EnemyBasic("Angered Shaggy", "ZoinksX2",
                                    regular_shaggy_loot,
                                    'enraged_shaggy.png',
                                    self.current_location.base_enemy_level,
                                    40, 36, 2, .20, .60, 1)
        self.list_of_enemies.append(enraged_shaggy)

        ssj_shaggy_loot = [ConsumableItemsList.consumables[0],
                           ConsumableItemsList.consumables[0],
                           ConsumableItemsList.consumables[0],
                           ConsumableItemsList.consumables[1],
                           ConsumableItemsList.consumables[1]]

        ssj_shaggy = EnemyBasic("SSJ Shaggy", "Mega Zoinks", ssj_shaggy_loot,
                                'ssj_shaggy.png',
                                self.current_location.base_enemy_level,
                                75, 80, 5, .45, .45, 1)
        self.list_of_enemies.append(ssj_shaggy)

        ssj_god_shaggy_loot = [ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[0],
                               ConsumableItemsList.consumables[1],
                               ConsumableItemsList.consumables[1]]

        ssj_god_shaggy = EnemyBasic("SSJSSJ Shaggy", "MonkaS",
                                    ssj_god_shaggy_loot, 'ssjgod_shaggy.png',
                                    self.current_location.base_enemy_level,
                                    150, 100, 10, .46, .46, 2)
        self.list_of_enemies.append(ssj_god_shaggy)

        ultra_shaggy_blanco_loot = [ConsumableItemsList.consumables[0],
                                    ConsumableItemsList.consumables[0],
                                    ConsumableItemsList.consumables[0],
                                    ConsumableItemsList.consumables[1],
                                    ConsumableItemsList.consumables[1]]

        ultra_shaggy_blanco = \
            EnemyBasic("Shaggy Blanco", "....",
                       ultra_shaggy_blanco_loot,
                       'ultra_shaggy_blanco.png',
                       self.current_location.base_enemy_level,
                       500, 250, 20, .3, .64, 3)
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
