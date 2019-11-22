import pygame

class EnemyBase:

    enemy_name = ""
    enemy_description = ""
    enemy_icon = None
    enemy_health = 0
    enemy_max_health = 0
    healthpercentage = 0.0
    enemy_exp = 0
    enemy_damage = 0
    enemy_level = 0

    def __init__(self, name, desc, level, hp, exp, damage, icon):
        self.enemy_name = name
        self.enemy_description = desc
        self.enemy_icon = pygame.image.load(icon)
        self.enemy_health = hp
        self.enemy_max_health = hp
        self.enemy_exp = exp
        self.enemy_damage = damage
        self.enemy_level = level

    # Name getter and setters
    def setName(self, name):
        self.enemy_name = name

    def getName(self):
        return self.enemy_name

    # Sets and Gets enemy description
    def setDesc(self, desc):
        self.enemy_description = desc

    def getDesc(self):
        return self.enemy_description

    # Enemy exp getter and setter
    def setExp(self, exp):
        self.enemy_exp = exp

    def getExp(self):
        return self.enemy_exp

    # Hp getter and setters
    def setHp(self, hp):
        self.enemy_health = hp

    def getHp(self):
        return self.enemy_health

    def getMaxHp(self):
        return self.enemy_max_health

    def set_enemy_health_max(self):
        self.enemy_health = self.getMaxHp()

    def getEnemyHealthPercentage(self):
        self.healthpercentage = self.enemy_health / self.getMaxHp()
        return self.healthpercentage

    def enemyTakeDamage(self, taken):
        self.enemy_health = self.getHp() - taken
        if self.getHp() < 0:
            self.setHp(0)
            self.isAlive()

    # Enemy damage getter and setter
    def setDamage(self, damage):
        self.enemy_damage = damage

    def getDamage(self):
        return self.enemy_damage

    # Enemy level getter and setter
    def setLevel(self, level):
        self.enemy_level = level

    def getLevel(self):
        return self.enemy_level

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

    # Function to determine if the enemy is dead or not
    def isAlive(self):
        if self.getHp() == 0:
            return False
        else:
            return True
