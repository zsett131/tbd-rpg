"""
This is the object for the player and stores hp, exp, items, and stats.
__author__: Jairo Garciga and Zachary Setterquist
"""

import pygame
import math
from game.inventory import Item


class PlayerBase:
    """
    This class sets up the player object which is used throughout the program.
    """

    def __init__(self, name):
        """
        :param name: place holder for the name
        All the other variables are being called for initialization.
        """
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

    def exp_algorithm(self):
        """
        Creates the logistical function for percent increase in exp.
        :return: percentage increase for the exp cap.
        """
        expLogistic = 1 / (
                3 + math.exp(-(3 / 4) * (self.playerLevel / 16) - 4))
        return expLogistic

    def set_player_name(self, input_name):
        """
        Sets the player's name to the input
        :param input_name: Takes input for the name
        """
        self.playerName = input_name

    def get_player_name(self):
        """
        Outputs player's name
        :return: the player's name
        """
        return self.playerName

    def get_player_level(self):
        """
        Gets player's level
        :return: player level
        """
        return self.playerLevel

    def player_level_up(self):
        """
        Levels up the player WIP
        """
        while self.get_player_exp() >= self.get_player_exp_cap():
            self.playerLevel += 1
            self.increment_skill_points()
            self.set_player_exp(
                self.get_player_exp() - self.get_player_exp_cap())
            self.set_player_exp_cap()

    # Player Exp Setter and Getter.

    def add_player_exp(self, exp_gained):
        """
        Adds exp to the player's exp and levels up if necessary
        :param exp_gained: exp increase amount
        """
        self.playerExp += exp_gained
        self.player_level_up()

    def set_player_exp(self, amount):
        """
        Sets the Player's exp
        :param amount: the amount of exp
        """
        self.playerExp = amount

    def get_player_exp(self):
        """
        Returns the Player's exp
        :return: player exp
        """
        return self.playerExp

    def set_player_exp_cap(self):
        """
        Sets the exp cap each time in relation to player level
        """
        self.playerExpCap = int(self.playerExpCap * self.exp_algorithm())

    def get_player_exp_cap(self):
        """
        Returns player exp cap
        :return: the player exp cap
        """
        return self.playerExpCap

    def set_player_current_health(self, incoming):
        """
        Sets the current health of the player to the incoming number,
        either adding or subtracting
        :param incoming: number health changing by
        """
        self.playerCurrentHealth = incoming

    def get_player_current_health(self):
        """
        Outputs player's current health and checks if player is alive
        :return: player's current health
        """
        return self.playerCurrentHealth

    def player_heal(self, amount):
        """
        Heals the player's health by adding the current health and the
        health amount together.
        At most it can be the max health.
        :param amount: Amount of health the player is healed
        """
        if amount + self.get_player_current_health() <= \
                self.get_player_max_health():
            self.set_player_current_health(self.get_player_current_health() +
                                           amount)
        else:
            self.set_player_current_health(self.get_player_max_health())

    def set_player_health_max(self):
        """
        Automatically sets the player's current health to max.
        """
        self.set_player_current_health(self.get_player_max_health())

    def player_take_damage(self, damage):
        """
        Reduces the health of the player based on incoming damage.
        :param damage: The amount of damage the player is taking
        """
        if self.playerCurrentHealth - damage > 0:
            self.playerCurrentHealth = self.get_player_current_health() - \
                                       damage
        elif self.playerCurrentHealth - damage <= 0:
            self.playerCurrentHealth = 0

    def is_player_alive(self):
        """
        Determines if the player is alive
        :return: Boolean depending on player hp being 0 or not
        """
        if self.get_player_current_health() == 0:
            self.playerAlive = False
            return False
        else:
            return True

    def set_player_max_health(self):
        """
        Sets the maximum health of the player
        """
        self.playerMaxHealth = (
            self.get_player_max_health())

    def get_player_max_health(self):
        """
        Returns the player's maximum health
        :return: The player's maximum health value
        """
        return self.playerMaxHealth

    def set_player_health_percentage(self):
        """
        Creates a percentage of the current player health divided by the
        maximum player health.
        """
        self.playerHealthPercentage = (self.get_player_current_health()
                                       / self.get_player_max_health())

    def get_player_health_percentage(self):
        """
        Returns the health percentage
        :return: percentage of health the player has
        """
        self.set_player_health_percentage()
        return self.playerHealthPercentage

    # Sets and Gets the players equipped item
    def set_player_equipped(self, weapon):
        """
        Sets the item that the player has equipped
        :param weapon: The item
        """
        if self.get_player_equipped():
            self.set_player_damage(
                weapon.getDamage())  # * (1 + (self.get_player_strength() //
            # 10)))
        else:
            self.set_player_damage(1)  # + (self.get_player_strength() // 10))

    def get_player_equipped(self):
        """
        Returns the item the player has equipped
        :return: player weapon
        """
        return self.playerWeapon

    # Player damage Setter and Getter.

    def set_player_damage(self, damage):
        """
        Assigns the player's damage to the parameter damage
        :param damage: the amount of damage
        """
        self.playerDamage = damage

    def get_player_damage(self):
        """
        Returns the player's damage
        :return: player's damage
        """
        return self.playerDamage

    def increment_skill_points(self):
        """
        Increases the player's skill points by one
        """
        self.skillPoints += 1
        print("You have accrued one more skill point.")

    def set_skill_points(self, allocation):
        """
        Sets the player's skill points to the parameter allocation
        :param allocation: The amount of skill points
        """
        self.skillPoints += allocation

    def allocate_skill_points(self, allocation):
        """
        Subtracts skill points from the total skill points to "allocate"
        :param allocation: Skill points being allocated
        """
        self.skillPoints -= allocation

    def get_skill_points(self):
        """
        Returns the amount of skill points
        :return: the player's skill points
        """
        return self.skillPoints

    # The mythical land of player inventory. Appends to list and also
    # removes based on function.

    def add_to_player_inventory(self, item):
        """

        :param item:
        """
        self.playerInventory.append(item)

    def get_from_player_inventory(self, position):
        """

        :param position:
        :return:
        """
        return self.playerInventory[position]

    def remove_from_player_inventory(self, removal_point):
        """

        :param removal_point:
        """
        self.playerInventory.remove(removal_point)

    def get_player_inventory(self):
        """

        :return:
        """
        return self.playerInventory
