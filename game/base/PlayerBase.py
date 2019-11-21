import pygame
import math
from game.inventory import Item

"""
This is the object for the player and stores hp, exp, items, and stats.
__author__: Jairo Garciga and Zachary Setterquist
"""


class PlayerBase:
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
        self.playerExp = amount

    def get_player_exp(self):
        return self.playerExp

    def set_player_exp_cap(self):
        self.playerExpCap = int(self.playerExpCap * self.exp_algorithm())

    def get_player_exp_cap(self):
        return self.playerExpCap

    def set_player_current_health(self, incoming):
        self.playerCurrentHealth = incoming

    def check_player_current_health(self):
        return self.playerCurrentHealth

    def get_player_current_health(self):
        if self.check_player_current_health() <= 0:
            self.playerAlive = False
        return self.playerCurrentHealth

    def player_heal(self, amount):
        if amount + self.get_player_current_health() <= \
                self.get_player_max_health():
            self.set_player_current_health(self.get_player_current_health() +
                                           amount)
        else:
            self.set_player_current_health(self.get_player_max_health())

    def player_hospital_heal(self):
        self.set_player_current_health(self.get_player_max_health())

    def player_take_damage(self, damage):
        if self.playerCurrentHealth - damage > 0:
            self.playerCurrentHealth = self.get_player_current_health() - \
                                        damage
        elif self.playerCurrentHealth - damage <= 0:
            self.playerCurrentHealth = 0

    def is_player_alive(self):
        if self.get_player_current_health() == 0:
            return False
        else:
            return True

    def set_player_max_health(self):
        self.playerMaxHealth = (
                self.get_player_max_health() + self.get_player_strength())

    def get_player_max_health(self):
        return self.playerMaxHealth

    def set_player_health_percentage(self):
        self.playerHealthPercentage = self.get_player_current_health() / \
                                      self.get_player_max_health()

    def get_player_health_percentage(self):
        self.set_player_health_percentage()
        return self.playerHealthPercentage

    # Sets and Gets the players equipped item
    def set_player_equipped(self, weapon):
        if self.get_player_equipped():
            self.set_player_damage(
                weapon.getDamage() * (1 + (self.get_player_strength() // 10)))
        else:
            self.set_player_damage(1 + (self.get_player_strength() // 10))

    def get_player_equipped(self):
        return self.playerWeapon

    # Player damage Setter and Getter.

    def set_player_damage(self, damage):
        self.playerDamage = damage

    def get_player_damage(self):
        self.get_player_equipped()
        return self.playerDamage

    def player_attack(self):
        return self.get_player_damage()

    def increment_skill_points(self):
        self.skillPoints += 1
        print("You have accrued one more skill point.")

    def set_skill_points(self, allocation):
        self.skillPoints += allocation

    def allocate_skill_points(self, allocation):
        self.skillPoints -= allocation

    def get_skill_points(self):
        return self.skillPoints

    # Player strength Setter and Getter.

    def set_player_strength(self, allocation):
        if self.skillPoints >= allocation:
            self.strength += allocation
            self.allocate_skill_points(allocation)
            playerStrength = self.get_player_strength()
            print("Your strength is now {}".format(playerStrength))
        else:
            print("You only have {} to allocate, not {}.".format(
                self.skillPoints, allocation))

    def get_player_strength(self):
        return self.strength

    # Player wisdom Setter and Getter

    def set_player_wisdom(self, allocation):
        if self.skillPoints >= allocation:
            self.wisdom += allocation
            self.allocate_skill_points(allocation)
            player_wisdom = self.get_player_wisdom()
            print("Your wisdom is now {}".format(player_wisdom))
        else:
            print("You only have {} to allocate, not {}.".format(
                self.skillPoints, allocation))

    def get_player_wisdom(self):
        return self.wisdom

    # Player agility Setter and Getter

    def set_player_agility(self, allocation):
        if self.skillPoints >= allocation:
            self.agility += allocation
            self.allocate_skill_points(allocation)
            player_agility = self.get_player_agility()
            print("Your agility is now {}".format(player_agility))
        else:
            print("You only have {} to allocate, not {}.".format(
                self.skillPoints, allocation))

    def get_player_agility(self):
        return self.agility

    # The mythical land of player inventory. Appends to list and also
    # removes based on function.

    def add_to_player_inventory(self, item):
        self.playerInventory.append(item)

    def get_from_player_inventory(self, position):
        return self.playerInventory[position]

    def remove_from_player_inventory(self, removal_point):
        self.playerInventory.remove(removal_point)

    def get_player_inventory(self):
        return self.playerInventory

    # Get battle drops
    def get_battle_drops(self, drops):
        self.add_player_exp(drops[0])
        for x in drops[1:]:
            self.add_to_player_inventory(x)

    # Item affects and what to do with them
    def item_affects(self, item):
        if item.getAffect() == 1:
            self.set_player_current_health(item.gethealAmount())

    # Item getters
    def get_item(self, position):
        if self.get_player_inventory():
            return self.playerInventory[position].getItemName()
        else:
            print("Bruh the inventory is empty.")
