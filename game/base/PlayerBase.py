import pygame
import math
from game.inventory import Item


class PlayerBase:
    def __init__(self, name):
        # Player stats and attributes
        self.playerName = name
        self.playerAlive = True
        self.playerIcon = pygame.image.load('Jotaro.jpg')
        self.playerLevel = 1
        self.playerExp = 0
        self.playerExpCap = 100
        self.playerHealthPercentage = 0.0
        self.expLogistic = 0
        self.playerCurrentHealth = 20
        self.playerMaxHealth = 20
        self.playerWeapon = Item
        self.playerDamage = 2
        self.playerInventory = []

        # The stats, strength, wisdom, and agility.

        self.strength = 0
        self.wisdom = 0
        self.agility = 0
        self.skillPoints = 0

    def expAlgorithm(self):
        expLogistic = 1/(3+math.exp(-(3/4)*(self.playerLevel/16)-4))
        print(expLogistic)

    # Player name Setter & Getter

    def setPlayerName(self, inputName):
        self.playerName = inputName

    def getPlayerName(self):
        return self.playerName

    # Player Level getter.

    def getPlayerLevel(self):
        return self.playerLevel

    def playerLevelUp(self):
        while self.getPlayerExp() >= self.getPlayerExpCap():
            self.playerLevel += 1
            self.incrementSkillPoints()
            self.setPlayerExp(self.getplayerExp()-self.getplayerExpCap())
            self.setPlayerExpCap()

    # Player Exp Setter and Getter.

    def addPlayerExp(self, expGained):
        self.playerExp += expGained
        self.playerLevelUp()

    def setPlayerExp(self, amount):
        self.playerExp = amount

    def getPlayerExp(self):
        return self.playerExp

    # Player ExpCap Setter, Getter, & Algorithm.

    # Multiplies the current exp cap by the multiplier from the exp algorithm to produce the new exp cap.
    def setPlayerExpCap(self):
        self.playerExpCap = int(self.playerExpCap*self.expAlgorithm())

    def getPlayerExpCap(self):
        return self.playerExpCap

    def expAlgorithm(self):
        self.expLogistic = 1+(1 / (3 + math.exp(-(3 / 4) * (self.playerLevel / 16) - 4)))
        multiplier = 1 + self.expLogistic
        return self.expLogistic

    # Player health Setter, Getter, and Health calculation.

    def setPlayerCurrentHealth(self, incoming):
        self.playerCurrentHealth = incoming

    def checkPlayerCurrentHealth(self):
        return self.playerCurrentHealth

    def getPlayerCurrentHealth(self):
        if self.checkPlayerCurrentHealth() <= 0:
            self.playerAlive = False
        return self.playerCurrentHealth

    def playerHeal(self, amount):
        if amount+self.getPlayerCurrentHealth() <= self.getPlayerMaxHealth():
            self.setPlayerCurrenthealth(self.getPlayerCurrentHealth()+amount)
        else:
            self.setPlayerCurrentHealth(self.getPlayerMaxHealth())

    def playerHospitalHeal(self):
        self.setPlayerCurrentHealth(self.getPlayerMaxHealth())

    def playerTakeDamage(self, damage):
        if self.playerCurrentHealth - damage > 0:
            self.playerCurrentHealth = self.getPlayerCurrentHealth() - damage
        elif self.playerCurrentHealth - damage <= 0:
            self.playerCurrentHealth = 0


    def isPlayerAlive(self):
        if self.getPlayerCurrentHealth() == 0:
            return False
        else:
            return True

    def setPlayerMaxHealth(self):
        self.playerMaxHealth = (self.getPlayerMaxHealth() + self.getPlayerStrength())

    def getPlayerMaxHealth(self):
        return self.playerMaxHealth

    def setPlayerHealthPercentage(self):
        self.playerHealthPercentage = self.getPlayerCurrentHealth()/self.getPlayerMaxHealth()

    def getPlayerHealthPercentage(self):
        self.setPlayerHealthPercentage()
        return self.playerHealthPercentage

    # Sets and Gets the players equipped item
    def setPlayerEquiped(self, weapon):
        if self.getPlayerEquiped():
            self.setPlayerDamage(weapon.getDamage()*(1+(self.getPlayerStrength()//10)))
        else:
            self.setPlayerDamage(1+(self.getPlayerStrength()//10))

    def getPlayerEquiped(self):
        return self.playerWeapon

    # Player damage Setter and Getter.

    def setPlayerDamage(self, damage):
        self.playerDamage = damage

    def getPlayerDamage(self):
        self.getPlayerEquiped()
        return self.playerDamage

    def playerAttack(self):
        return self.getPlayerDamage()

    # Attributes: strength, wisdom, agility

    # Skill point Stuff.
    def incrementSkillPoints(self):
        self.skillPoints += 1
        print("You have accrued one more skill point.")

    def setSkillPoints(self, allocation):
        self.skillPoints += allocation

    def allocateSkillPoints(self, allocation):
        self.skillPoints -= allocation

    def getSkillPoints(self):
        return self.skillPoints

    # Player strength Setter and Getter.

    def setPlayerStrength(self, allocation):
        if self.skillPoints >= allocation:
            self.strength += allocation
            self.allocateSkillPoints(allocation)
            playerStrength = self.getPlayerStrength()
            print("Your strength is now {}".format(playerStrength))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerStrength(self):
        return self.strength

    # Player wisdom Setter and Getter

    def setPlayerWisdom(self, allocation):
        if self.skillPoints >= allocation:
            self.wisdom += allocation
            self.allocateSkillPoints(allocation)
            playerwisdom = self.getPlayerWisdom()
            print("Your wisdom is now {}".format(playerwisdom))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerWisdom(self):
        return self.wisdom

    # Player agility Setter and Getter

    def setPlayerAgility(self, allocation):
        if self.skillPoints >= allocation:
            self.agility += allocation
            self.allocateSkillPoints(allocation)
            playeragility = self.getPlayerAgility()
            print("Your agility is now {}".format(playeragility))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerAgility(self):
        return self.agility

    # The mythical land of player inventory. Appends to list and also removes based on function.
    def addToPlayerInventory(self, item):
        self.playerInventory.append(item)

    def getFromPlayerInventory(self, position):
        return self.playerInventory[position]

    def removeFromPlayerInventory(self, removalpoint):
        self.playerInventory.remove(removalpoint)

    def getPlayerInventory(self):
        return self.playerInventory

    # Get battle drops
    def getBattleDrops(self, drops):
        self.addPlayerExp(drops[0])
        for x in drops[1:]:
            self.addToPlayerInventory(x)

    # Item affects and what to do with them
    def itemAffects(self, item):
        if item.getAffect() == 1:
            self.setPlayerCurrentHealth(item.gethealAmount())

    # Item getters
    def getItem(self, position):
        if self.getPlayerInventory():
            return self.playerInventory[position].getItemName()
        else:
            print("Bruh the inventory is empty.")

