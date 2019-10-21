class EnemyBase:
    def __init__(self, *args): # TODO
        self.name = ''
        self.hp = 0
        self.level = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setHp(self, hp):
        self.hp = hp

    def getHp(self, hp):
        return self.hp

    def died(self, *args): # TODO: xp calculation, loot generation, etc.
        pass

