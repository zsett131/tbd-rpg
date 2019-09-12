

class EnemyBase:

    name = ""
    desc = ""
    hp = 0
    exp = 0
    damage = 0
    level = 0

    def __init__(self, name, desc, level, hp, exp, damage):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.exp = exp
        self.damage = damage
        self.level = level

    # Name getter and setters
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    # Sets and Gets enemy description
    def setDesc(self, desc):
        self.desc = desc

    def getDesc(self):
        return self.desc

    # Enemy exp getter and setter
    def setExp(self, exp):
        self.exp = exp

    def getExp(self):
        return self.exp

    # Hp getter and setters
    def setHp(self, hp):
        self.hp = hp

    def getHp(self, hp):
        return self.hp

    # Enemy damage getter and setter
    def setDamage(self, damage):
        self.damage = damage

    def getDamage(self):
        return self.damage

    # Enemy level getter and setter
    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    # Lever generator based on monster level and player level
    def levelGenerator(self, level, playerlevel):
        if playerlevel < level:
            self.setLevel(level + (level % playerlevel)//3)
        if playerlevel > level:
            self.setlevel(level - (playerlevel % level)//3)

    # Exp, hp, and damage generator based on monster's level in comparison to input level.
    def expGenerator(self, originalExp, originalHp, originalDamage, originalLevel, currentLevel):

        levelDifference = originalLevel % currentLevel

        if originalLevel > currentLevel:
            percentMultiplier = 1-(levelDifference*2)/100

        if currentLevel > originalLevel:
            percentMultiplier = 1+(levelDifference*2)/100

        self.setExp(int(originalExp * percentMultiplier))
        self.setHp(int(originalHp * percentMultiplier))
        self.setDamage(int(originalDamage * percentMultiplier))


    def died(self, *args): # TODO: xp calculation, loot generation, etc.
        pass
