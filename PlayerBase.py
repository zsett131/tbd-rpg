import pygame
import math

class PlayerBase:
    # All the player variables are kept within this area.
    # Exp, health, weapons, damage, and stats will all be here.

    playerName = ""
    playerLevel = 20
    playerExp = 0
    playerExpCap = 100
    playerHealth = 20
    playerWeapon = 0
    playerDamage = 0

    # The stats, Strength, Wisdom, and Agility.

    Strength = 0
    Wisdom = 0
    Agility = 0

    # The constructor (place holder for now)
    def _init_(self):
        print("I exist")
        self.expAlgorithm()

    def expAlgorithm(self):
        expLogistic = 1/(3+math.exp(-(3/4)*(self.playerLevel/16)-4))
        print (expLogistic)
