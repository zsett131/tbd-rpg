"""
This class is the parent classes for all the enemies
__author__: Jairo Garciga
"""
import pygame
import random


class EnemyBase:
    """
    The base template for enemies
    """
    enemy_name = ""
    enemy_description = ""
    enemy_icon = None
    enemy_health = 0
    enemy_max_health = 0
    health_percentage = 0.0
    enemy_exp = 0
    enemy_damage = 0
    enemy_level = 0

    def __init__(self, name, desc, icon, stats):
        self.enemy_name = name
        self.enemy_description = desc
        self.enemy_icon = pygame.image.load("Images/" + icon)

        # For Clarification on what stats is.
        # Stats is all the stats of the specific enemy
        # Order: Level, exp,
        # strength, agility, wisdom, defense,
        # damage, health

        self.enemy_level = stats[0]
        self.enemy_exp = stats[1]
        self.enemy_strength = stats[2]
        self.enemy_agility = stats[3]
        self.enemy_wisdom = stats[4]
        self.enemy_defense = stats[5]
        self.enemy_damage = stats[6]
        self.enemy_max_health = stats[7]
        self.enemy_health = self.enemy_max_health

    # Name getter and setters
    def set_name(self, name):
        """
        Sets the name of the enemy
        :param name: name of enemy
        """
        self.enemy_name = name

    def get_name(self):
        """
        :return: enemy name
        """
        return self.enemy_name

    # Sets and Gets enemy description
    def set_desc(self, desc):
        """
        Sets the description of each enemy TODO
        :param desc: the description
        """
        self.enemy_description = desc

    def get_desc(self):
        """
        Returns the enemy's description
        :return: enemy's description
        """
        return self.enemy_description

    # Enemy exp getter and setter
    def set_exp(self, exp):
        """
        Sets the exp, which is given to the player upon death.
        :param exp: amount of exp
        """
        self.enemy_exp = exp

    def get_exp(self):
        """
        Returns the amount of exp,
        this is useful for giving the player the exp.
        :return: enemy's exp
        """
        return self.enemy_exp

    # Hp getter and setters
    def set_hp(self, hp):
        """
        Sets the health of the enemy
        :param hp: enemy health
        """
        self.enemy_health = hp

    def get_hp(self):
        """
        Returns the health of the enemy, this helps in reassigning
        the enemies health when it takes damage.
        :return: enemy's health
        """
        return self.enemy_health

    def set_max_hp(self, max_hp):
        """
        Sets the maximum hp for the enemy
        :param max_hp: the max hp
        """
        self.enemy_max_health = max_hp

    def get_max_hp(self):
        """
        Sets the maximum hp of the enemy.
        This function helps draw the health bars
        of the enemy as the bar length depends
        on the percentage of the current hp to maximum hp.
        :return: max enemy health
        """
        return self.enemy_max_health

    def set_enemy_health_to_max(self):
        """
        Sets the current health of the enemy to the maximum health.
        This function is used to regen the enemies before every battle.
        """
        self.enemy_health = self.get_max_hp()

    def get_enemy_health_percentage(self):
        """
        Calculates the enemies health percentage by dividing
        health by the maximum hp, then returns it.
        :return: health percentage
        """
        self.health_percentage = self.enemy_health / self.get_max_hp()
        return self.health_percentage

    def enemy_take_damage(self, taken):
        """
        Damages the enemy by reducing the enemy's hp by the parameter taken
        :param taken: the amount of hp taken from the enemy
        """
        self.enemy_health = self.get_hp() - taken
        if self.get_hp() < 0:
            self.set_hp(0)
            self.is_alive()

    # Enemy damage getter and setter
    def set_damage(self, damage):
        """
        Sets the damage for the enemy
        :param damage: Amount of damage
        """
        self.enemy_damage = damage

    def get_damage(self):
        """
        Gets the damage of the enemy
        :return: enemy's damage
        """
        return self.enemy_damage

    # Enemy level getter and setter
    def set_level(self, level):
        """
        Sets the level of the enemy. Helps in reducing
        or increasing enemy's level for normal enemies.
        :param level: The level
        """
        self.enemy_level = level

    def get_level(self):
        """
        Gets the enemies level for number crunching and
        also visual output in the battle screen.
        :return: enemy's level
        """
        return self.enemy_level

    def exp_generator(self, original_exp, original_hp, original_damage,
                      original_level, current_level):
        """
        This generates the exp of the enemy based on the level differences
        between the player and the enemy.
        Basically updates the level, exp, and health.
        :param original_exp: the enemy's original exp
        :param original_hp:  the enemy's original hp
        :param original_damage: the enemy's original damage
        :param original_level:  the enemy's original level
        :param current_level: the enemy's current level
        """

        level_difference = original_level % current_level

        if original_level > current_level:
            percent_multiplier = 1 - (level_difference * 2) / 100

        elif current_level > original_level:
            percent_multiplier = 1 + (level_difference * 2) / 100

        else:
            percent_multiplier = 1
        self.set_exp(int(original_exp * percent_multiplier))
        self.set_hp(int(original_hp * percent_multiplier))
        self.set_damage(int(original_damage * percent_multiplier))

    def died(self):  # TODO: xp calculation, loot generation, etc.
        """
        Will return the exp, and items of the enemy to the player.
        :return: The exp, then then the items of the enemy
        """
        pass

    # Function to determine if the enemy is dead or not
    def is_alive(self):
        """
        Checks to see if the enemy is alive
        :return: Boolean value based on live or not
        """
        if self.get_hp() == 0:
            return False
        else:
            return True
