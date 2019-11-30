"""
This class is the parent class for all attacks that the player and enemies
have.
__author__: Jairo Garciga
"""

import random
import math


class Attacks:
    """
    This class is the parent class for all attacks that the player and enemies
    have.
    """

    def __init__(self, name, desc, attack_type, attack_accuracy):
        self.name = name
        self.desc = desc
        self.attack_type = attack_type
        self.attack_base_accuracy = attack_accuracy
        self.attack_accuracy = self.attack_base_accuracy
        self.character = None

    def set_attack_name(self, new_name):
        """
        Sets the attack name. Not sure what this will be used for later on,
        perhaps evolving attack names?
        :param new_name: The new name
        """
        self.name = new_name

    def get_attack_name(self):
        """
        Gets the attack name
        :return: attack name
        """
        return self.name

    def set_attack_desc(self, new_desc):
        """
        Sets the description to a new description. This would be useful for
        evolved attacks.
        :param new_desc: new description
        """
        self.desc = new_desc

    def get_attack_desc(self):
        """
        Returns the attack description
        :return:
        """
        return self.desc

    def get_attack_type(self):
        """
        No setter because the attack type should remain the same regardless
        of evolution.
        :return: attack type
        """
        return self.attack_type

    def set_attack_accuracy(self, accuracy):
        """
        Sets the accuracy of an attack, either increasing it or decreasing it.
        :param accuracy: The new accuracy
        """
        self.attack_accuracy = accuracy

    def get_attack_accuracy(self):
        """
        Gets the attack accuracy, not the base accuracy.
        :return: attack_accuracy
        """
        return self.attack_accuracy

    def set_character(self, character):
        """
        Sets the character using the attack
        :param character: the character
        """
        self.character = character

    def get_character(self):
        """
        Gets the user of this attack
        :return: character
        """
        return self.character


class BasicAttack(Attacks):
    """
    Attacks that have no side effects
    """

    def __init__(self, name, desc, attack_type, attack_accuracy,
                 base_damage, variance):
        Attacks.__init__(self, name, desc, attack_type, attack_accuracy)
        self.base_damage = base_damage
        self.damage = self.base_damage
        self.damage_range = None
        self.variance = variance
        self.modifiers = []

    def set_base_damage(self, new_base_damage):
        """
        Sets the new base damage for the attack
        :param new_base_damage: new base damage
        """
        self.base_damage = new_base_damage

    def get_base_damage(self):
        """
        Gets the base damage
        :return: base damage
        """
        return self.base_damage

    def calculate_damage(self):
        """
        Calculates the damage to be done based on the damage range, damage,
        and modifiers.
        :return:
        """
        damage_range = random.random() * (2 * self.variance) - self.variance
        self.get_modifiers()
        damage_to_be_done = self.damage + damage_range
        print("Damage:", damage_to_be_done)
        return damage_to_be_done

    # Format: ([type_one, type_one_percentage, modifier_type])
    def get_modifiers(self):
        """
        Creates the modifiers from the saved modifiers that were set
        """
        self.damage = self.base_damage
        for argument in self.modifiers:
            if argument[2] == "+":
                self.damage += math.floor(self.character.get_stat_xyz(
                    argument[0]) * argument[1])
                print(math.floor(self.character.get_stat_xyz(
                    argument[0]) * argument[1]))
                print("New Damage:", self.damage)
            elif argument[2] == "*":
                self.damage *= math.floor(self.character.get_stat_xyz(
                    argument[0]) * argument[1])

    def set_modifiers(self, *args):
        """
        THIS MUST ALWAYS BE CALLED BEFORE DAMAGE IS DONE IN THE CHARACTER
        CLASSES THAT USE AN ATTACK. EVEN IF THERE ARE NO UPDATE TO THE STATS.
        Sets the modifiers for the attack
        :param args: list of modifiers
        """
        self.modifiers = []
        for argument in args:
            self.modifiers.append(argument)
