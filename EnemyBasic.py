from EnemyBase import EnemyBase

class EnemyBasic(EnemyBase):

    def __init__(self, name, desc, level, playerlevel, hp, exp, damage):
        EnemyBase.__init__(self, name, desc, level, hp, exp, damage)
        self.levelGenerator(self.level, playerlevel)
        self.statsGenerator(self.exp, self.hp, self.damage, level, self.level)
        print(self.getExp())

    # Level generator based on monster level and player level
    def levelGenerator(self, level, playerlevel):
        if playerlevel < level:
            self.setLevel(self.getLevel()-(level % playerlevel)//2)

        if playerlevel > level:
            self.setLevel(self.getLevel()+(playerlevel % level)//2)

    # Exp, hp, and damage generator based on monster's level in comparison to input level.
    def statsGenerator(self, originalExp, originalHp, originalDamage, originalLevel, currentLevel):
        print("The originalLevel: ", originalLevel)
        print("The current level: ", currentLevel)
        levelDifference = originalLevel % currentLevel
        print(levelDifference)

        if originalLevel > currentLevel:
            percentMultiplier = 1-(levelDifference*5)/100
        if currentLevel > originalLevel:
            percentMultiplier = 1+(levelDifference*5)/100

        print(percentMultiplier)
        self.setExp(int(originalExp * percentMultiplier))
        self.setHp(int(originalHp * percentMultiplier))
        self.setDamage(int(originalDamage * percentMultiplier))


    def died(self, *args): # TODO: xp calculation, loot generation, etc.
        pass