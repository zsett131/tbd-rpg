import pygame
import math
import Item

class PlayerBase:
    # All the player variables are kept within this area.
    # Exp, health, weapons, damage, and stats will all be here.

    playerName = ""
    playerLevel = 1
    playerExp = 0
    playerExpCap = 100
    playerHealthPercentage = 0.0
    expLogistic = 0
    playerCurrentHealth = 20
    playerMaxHealth = 20
    playerWeapon = Item
    playerDamage = 1
    playerInventory = []

    # The stats, Strength, Wisdom, and Agility.

    Strength = 0
    Wisdom = 0
    Agility = 0
    SkillPoints = 0

    # The constructor (place holder for now)
    def __init__(self, name):
        self.setPlayerName(name)

    def expAlgorithm(self):
        expLogistic = 1/(3+math.exp(-(3/4)*(self.playerLevel/16)-4))
        print (expLogistic)

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
        self.ExpLogistic = 1+(1 / (3 + math.exp(-(3 / 4) * (self.playerLevel / 16) - 4)))
        Multiplier = 1 + self.ExpLogistic
        return self.ExpLogistic

    # Player health Setter, Getter, and Health calculation.

    def setPlayerCurrentHealth(self, incoming):
        self.playerCurrentHealth = incoming

    def getPlayerCurrentHealth(self):
        return self.playerCurrentHealth

    def playerHeal(self, amount):
        if amount+self.getPlayerCurrentHealth() <= self.getPlayerMaxHealth():
            self.setPlayerCurrenthealth(self.getPlayerCurrentHealth()+amount)
        else:
            self.setPlayerCurrentHealth(self.getPlayerMaxHealth())

    def playerTakeDamage(self, damage):
        self.playerCurrentHealth = self.getPlayerCurrentHealth() - damage

    def isPlayerAlive(self):
        if self.getPlayerCurrentHealth() == 0:
            return False
        else:
            return True

    def setPlayerMaxHealth(self):
        self.setPlayerMaxHealth(self.getplayerMaxHealth() + self.getPlayerStrength())

    def getPlayerMaxHealth(self):
        return self.playerMaxHealth

    def setPlayerHealthPercentage(self):
        self.playerHealthPercentage = self.getPlayerCurrentHealth()//self.getPlayerMaxHealth()

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

    # Attributes: Strength, Wisdom, Agility

    # Skill point Stuff.
    def incrementSkillPoints(self):
        self.SkillPoints += 1
        print("You have accrued one more skill point.")

    def setSkillPoints(self, allocation):
        self.SkillPoints += allocation

    def allocateSkillPoints(self, allocation):
        self.SkillPoints -= allocation

    def getSkillPoints(self):
        return self.SkillPoints

    # Player Strength Setter and Getter.

    def setPlayerStrength(self, allocation):
        if self.SkillPoints >= allocation:
            self.Strength += allocation
            self.allocateSkillPoints(allocation)
            playerStrength = self.getPlayerStrength()
            print("Your strength is now {}".format(playerStrength))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerStrength(self):
        return self.Strength

    # Player Wisdom Setter and Getter

    def setPlayerWisdom(self, allocation):
        if self.SkillPoints >= allocation:
            self.Wisdom += allocation
            self.allocateSkillPoints(allocation)
            playerwisdom = self.getPlayerWisdom()
            print("Your wisdom is now {}".format(playerwisdom))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerWisdom(self):
        return self.Wisdom

    # Player Agility Setter and Getter

    def setPlayerAgility(self, allocation):
        if self.SkillPoints >= allocation:
            self.Agility += allocation
            self.allocateSkillPoints(allocation)
            playeragility = self.getPlayerAgility()
            print("Your agility is now {}".format(playeragility))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerAgility(self):
        return self.Agility

    # The mythical land of player inventory. Appends to list and also removes based on function.
    def addtoPlayerInventory(self, item):
        self.playerInventory.append(item)

    def getfromPlayerInventory(self, position):
        return self.playerInventory(position)

    def removefromPlayerInventory(self, removalpoint):
        self.playerInventory.remove(removalpoint)

    def getPlayerInventory(self):
        return self.playerInventory

    # Get battle drops
    def getBattleDrops(self, drops):
        self.addPlayerExp(drops[0])
        for x in drops[1:]:
            self.addtoPlayerInventory(x)

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

