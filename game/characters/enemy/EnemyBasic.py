"""
This is the non-boss enemies. They are more generic and not event specific.
__author__: Jairo Garciga
"""
from game.characters.enemy.EnemyBase import EnemyBase
from random import random
import math


class EnemyBasic(EnemyBase):
    """
    Generates the basic enemy, scales them too.
    """
    lootDrop = []
    player_level = None

    def __init__(self, name, desc, stats, loot_table, icon):
        EnemyBase.__init__(self, name, desc, icon, stats)
        self.rand_level_amount = int((random() * 4) - 2)
        self.enemy_level = abs(self.enemy_level + self.rand_level_amount)
        if self.enemy_level < 1:
            self.enemy_level = 1
        self.lootDrop = loot_table
        self.rand_level_modifier()

    def rand_level_modifier(self):
        """
        Randomizes the stats based on the level difference
        """
        strength_random = random()
        if strength_random * 100 > 50 and self.rand_level_amount > 0:
            self.enemy_strength += 1
        elif strength_random * 100 < 50 and self.rand_level_amount >= 0:
            self.enemy_strength += 0
        else:
            self.enemy_strength -= 1

        agility_random = random()
        if agility_random * 100 > 50 and self.rand_level_amount > 0:
            self.enemy_agility += 1
        elif agility_random * 100 < 50 and self.rand_level_amount >= 0:
            self.enemy_agility += 0
        else:
            self.enemy_agility -= 1

        wisdom_random = random()
        if wisdom_random * 100 > 50 and self.rand_level_amount > 0:
            self.enemy_wisdom += 1
        elif wisdom_random * 100 < 50 and self.rand_level_amount >= 0:
            self.enemy_wisdom += 0
        else:
            self.enemy_wisdom -= 1
        randomized_health_modifier = 1 + ((random() / 10) - .10)
        self.enemy_max_health = int(
            (self.enemy_max_health + self.enemy_strength*2) *
            (1 + self.rand_level_amount / 20))
        self.enemy_max_health *= randomized_health_modifier
        self.enemy_max_health = math.ceil(self.enemy_max_health)

        self.enemy_health = self.enemy_max_health

        self.enemy_exp *= 1 + self.rand_level_amount / 20

    # First a list called drops is created.
    # Next, the exp amount of the enemy is put in followed
    # by each item that is successfully dropped from the enemy.

    def died(self):  # TODO: xp calculation, loot generation, etc.
        """
        Outputs the exp and loot, TO BE DECIDED
        :return: The exp and the items
        """
        drops = [self.get_exp()]
        for x in self.lootDrop:
            if x.get_item_drop_rate() >= random():
                drops.append(x)
        return drops
