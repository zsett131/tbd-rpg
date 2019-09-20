from EnemyBase import EnemyBase
from random import random
from lootTableMaker import lootTableMaker

class EnemyBasic(EnemyBase):

    lootDrop = []

    def __init__(self, name, desc, level, playerlevel, hp, exp, damage, lootTable):
        EnemyBase.__init__(self, name, desc, level, hp, exp, damage)
        self.levelGenerator(self.level, playerlevel)
        self.statsGenerator(self.exp, self.hp, self.damage, level, self.level)
        self.lootDrop = lootTable

    # Level generator based on monster level and player level
    def levelGenerator(self, level, playerlevel):
        if playerlevel < level:
            self.setLevel(self.getLevel()-(level - playerlevel)//4)

        if playerlevel > level:
            self.setLevel(self.getLevel()+(playerlevel - level)//3)

    # Exp, hp, and damage generator based on monster's level in comparison to input level.
    def statsGenerator(self, originalExp, originalHp, originalDamage, originalLevel, currentLevel):

        levelDifference = originalLevel % currentLevel


        if originalLevel > currentLevel:
            percentMultiplier = 1-(levelDifference*5)/100
        if currentLevel > originalLevel:
            percentMultiplier = 1+(levelDifference*5)/100

        self.setExp(int(originalExp * percentMultiplier))
        self.setHp(int(originalHp * percentMultiplier))
        self.setDamage(int(originalDamage * percentMultiplier))

    # First a list called drops is created. Next, the exp amount of the enemy is put in followed by each item that is successfully dropped from the enemy.

    def died(self): # TODO: xp calculation, loot generation, etc.
        drops = [self.getExp()]
        for x in self.lootDrop:
            if self.lootDrop[x] <= random():
                drops.append(self.lootDrop[x])
        return drops