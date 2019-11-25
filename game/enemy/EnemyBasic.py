"""
This is the non-boss enemies. They are more generic and not event specific.
__author__: Jairo Garciga
"""
from game.enemy.EnemyBase import EnemyBase
from random import random


class EnemyBasic(EnemyBase):
    """
    Generates the basic enemy, scales them too.
    """
    lootDrop = []
    player_level = None

    def __init__(self, name, desc, level, player_level, hp, exp, damage,
                 loot_table, icon):
        EnemyBase.__init__(self, name, desc, level, hp, exp, damage, icon)
        self.player_level = player_level
        self.lootDrop = loot_table

    def set_player_level(self, level):
        """
        Receives the player's level and sets it for the object.
        :param level: The player's level
        """
        self.player_level = level
        self.level_generator(self.enemy_level, self.player_level)
        self.stats_generator(self.enemy_exp, self.enemy_health,
                             self.enemy_damage, level, self.enemy_level)

    # Level generator based on monster level and player level
    def level_generator(self, level, player_level):
        """
        Establishes the level for the enemy based on the player's level
        :param level: The enemy's level
        :param player_level: The player's level
        """
        if player_level < level:
            self.set_level(self.get_level() - (level - player_level) // 4)

        if player_level > level:
            self.set_level(self.get_level() + (player_level - level) // 3)

    # Exp, hp, and damage generator based
    # on monster's level in comparison to input level.
    def stats_generator(self, original_exp, original_hp, original_damage,
                        original_level, current_level):
        """
        Generates the stats(exp and health) based on level
        :param original_exp: The enemy's original exp
        :param original_hp: The enemy's health
        :param original_damage: The enemy's original damage
        :param original_level: The enemy's original level
        :param current_level: The enemy's new level
        :return:
        """

        level_difference = abs(original_level - current_level)

        if original_level > current_level:
            percent_multiplier = 1 - (level_difference * 5) / 100
        elif current_level > original_level:
            percent_multiplier = 1 + (level_difference * 5) / 100
        else:
            percent_multiplier = 1

        self.set_exp(int(original_exp * percent_multiplier))
        self.set_hp(int(original_hp * percent_multiplier))
        self.set_damage(int(original_damage * percent_multiplier))
        self.enemy_max_health = self.enemy_health

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
