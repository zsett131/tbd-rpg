from game.enemy.EnemyBase import EnemyBase
from random import random


class EnemyBasic(EnemyBase):

    lootDrop = []
    playerlevel = None

    def __init__(self, name, desc, level, playerlevel, hp, exp, damage, lootTable, icon):
        EnemyBase.__init__(self, name, desc, level, hp, exp, damage, icon)
        self.playerlevel = playerlevel
        self.lootDrop = lootTable

    def setPlayerLevel(self, level):
        self.playerlevel = level
        self.level_generator(self.enemy_level, self.playerlevel)
        self.statsGenerator(self.enemy_exp, self.enemy_health, self.enemy_damage, level, self.enemy_level)

    # Level generator based on monster level and player level
    def level_generator(self, level, player_level):
        if player_level < level:
            self.set_level(self.get_level() - (level - player_level) // 4)

        if player_level > level:
            self.set_level(self.get_level() + (player_level - level) // 3)

    # Exp, hp, and damage generator based on monster's level in comparison to input level.
    def statsGenerator(self, originalExp, originalHp, originalDamage, originalLevel, currentLevel):

        levelDifference = abs(originalLevel - currentLevel)

        if originalLevel > currentLevel:
            percentMultiplier = 1-(levelDifference*5)/100
        elif currentLevel > originalLevel:
            percentMultiplier = 1+(levelDifference*5)/100
        else:
            percentMultiplier = 1

        self.set_exp(int(originalExp * percentMultiplier))
        self.set_hp(int(originalHp * percentMultiplier))
        self.set_damage(int(originalDamage * percentMultiplier))
        self.maxhp = self.enemy_health

    # First a list called drops is created. Next, the exp amount of the enemy is put in followed by each item that is successfully dropped from the enemy.

    def died(self): # TODO: xp calculation, loot generation, etc.
        drops = [self.get_exp()]
        for x in self.lootDrop:
            if x.getItemDropRate() >= random():
                drops.append(x)
        return drops