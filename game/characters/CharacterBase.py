"""
This is the parent class to all characters that have stats.
__author__: Jairo Gariga
"""


class CharacterBase:
    """
    The main character class.
    """

    def __init__(self):
        self.name = None
        self.icon = None
        self.level = None
        self.strength = None
        self.agility = None
        self.wisdom = None
        self.defense = None
        self.max_health = None
        self.current_health = self.max_health

    def get_name(self):
        """
        Gets the name of the character.
        :return: character name
        """

    def get_level(self):
        """
        Gets the level of the character.
        :return: character level
        """
        return self.level

    def get_strength(self):
        """
        Gets the strength of the character.
        :return: character strength
        """
        return self.strength

    def get_agility(self):
        """
        Gets the agility of the character.
        :return: character agility
        """
        return self.agility

    def get_wisdom(self):
        """
        Gets the wisdom of the character.
        :return: character wisdom
        """
        return self.wisdom

    def get_defense(self):
        """
        Gets the defense of the character.
        :return: character defense
        """
        return self.defense

    def get_max_health(self):
        """
        Gets the maximum health of the character.
        :return: character maximum health
        """
        return self.max_health

    def get_current_health(self):
        """
        Gets the current health of the character.
        :return: character current health
        """
        return self.current_health
