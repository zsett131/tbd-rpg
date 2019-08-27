import pygame
import math

class PlayerBase:
    # All the player variables are kept within this area.
    # Exp, health, weapons, damage, and stats will all be here.

    playerName = ""
    playerLevel = 1
    playerExp = 0
    playerExpCap = 100
    ExpLogistic = 0
    playercurrentHealth = 20
    playermaxHealth = 20
    playerWeapon = 0
    playerDamage = 0

    # The stats, Strength, Wisdom, and Agility.

    Strength = 0
    Wisdom = 0
    Agility = 0
    Skillpoints = 0

    # The constructor (place holder for now)
    def __init__(self):
        print("I exist")
        self.expalgorithm()

    def expAlgorithm(self):
        expLogistic = 1/(3+math.exp(-(3/4)*(self.playerLevel/16)-4))
        print (expLogistic)

    # Player name Setter & Getter

    def setplayername(self, inputName):
        self.playerName = inputName

    def getplayername(self):
        return self.playerName


    # Player Level getter.

    def getplayerLevel(self):
        return self.playerLevel

    def playerLevelUp(self):
        if self.playerExp >= self.playerExpCap:
            self.playerLevel += 1
            self.incrementSkillPoints()


    # Player Exp Setter and Getter.

    def setplayerExp(self, expGained):
        self.playerExp += expGained

    def getplayerExp(self):
        return self.playerExp


    # Player ExpCap Setter, Getter, & Algorithm.

    # Multiplies the current exp cap by the multiplier from the exp algorithm to produce the new exp cap.
    def setplayerExpCap(self):
        self.playerExpCap = self.playerExpCap*self.expalgorithm()

    def getplayerExpCap(self):
        return self.playerExpCap

    def expalgorithm(self):
        self.ExpLogistic = 1 / (3 + math.exp(-(3 / 4) * (self.playerLevel / 16) - 4))
        Multiplier = 1 + self.ExpLogistic
        return self.ExpLogistic

    # Player health Setter, Getter, and Health calculation.

    def setplayercurrenthealth(self, incoming):
        if (self.playercurrentHealth + incoming) <= self.playemaxHealth:
            self.playercurrentHealth += incoming
        else:
            self.playercurrentHealth = self.playerDamage

    def getplayercurrenthealth(self):
        return self.playerhealth

    def setplayermaxHealth(self):
        playermaxHealth = self.getplayermaxHealth()
        playerStrength = self.getplayerStrength()
        HealthCalculation = playermaxHealth + playerStrength

    def getplayermaxHealth(self):
        return self.playermaxHealth


    # Player damage Setter and Getter.

    def setplayerDamage(self, damage):
        self.playerDamage = damage

    def getplayerDamage(self):
        return self.playerDamage


    # Attributes: Strength, Wisdom, Agility

    # Skill point Stuff.
    def incrementSkillPoints(self):
        self.Skillpoints += 1

    def setSkillPoints(self, allocation):
        self.Skillpoints += allocation

    def allocateSkillPoints(self, allocation):
        self.Skillpoints -= allocation

    def getSkillPoints(self):
        return self.Skillpoints

    # Player Strength Setter and Getter.

    def setplayerStrength(self, allocation):
        if self.Skillpoints >= allocation:
            self.Strength += allocation
            self.allocateSkillPoints(allocation)
            playerstrength = self.getplayerStrength()
            print("Your strength is now {}".format(playerstrength))
        else:
            print("You only have {} to allocate, not {}".format(self.Skillpoints, allocation))

    def getplayerStrength(self):
        return self.Strength

    # Player Wisdom Setter and Getter

    def setplayerWisdom(self, allocation):
        if self.Skillpoints >= allocation:
            self.Wisdom += allocation
            self.allocateSkillPoints(self, allocation)
            playerwisdom = self.getplayerWisdom()
            print("Your strength is now {}".format(playerwisdom))
        else:
            print("You only have {} to allocate, not {}".format(self.Skillpoints, allocation))

    def getplayerWisdom(self):
        return self.Wisdom()

    # Player Agility Setter and Getter

    def setplayerAgility(self, allocation):
        if self.Skillpoints >= allocation:
            self.Agility += allocation
            self.allocateSkillPoints(self, allocation)
            playeragility = self.getplayerAgility()
            print("Your strength is now {}".format(playeragility))
        else:
            print("You only have {} to allocate, not {}".format(self.Skillpoints, allocation))

    def getplayerAgility(self):
        return self.Agility()

PlayerBase()
