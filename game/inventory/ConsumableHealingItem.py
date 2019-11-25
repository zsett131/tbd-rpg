"""
Module containing class for healing items.
__author__: Jairo Garciga
"""
from game.inventory.Item import Item


class ConsumableHealingItem(Item):
    """
    This is the class for items that heal the player upon usage.
    """
    heal_amount = 0
    Affect = 1

    def __init__(self, name, desc, stack_cap, stack, heal, drop_rate):
        Item.__init__(self, name, desc, stack_cap, stack, drop_rate)

    # Getter and setter for the amount healed
    def set_heal_amount(self, heal):
        """
        Sets the amount that the item will heal the player by.
        :param heal: health amount
        """
        self.heal_amount = heal

    def get_heal_amount(self):
        """
        Returns the amount of health the item will heal the player by.
        :return: health amount
        """
        return self.heal_amount

    # Getter for Affect
    def get_affect(self):
        """
        Returns the effect of the item.
        :return: item effect
        """
        return self.Affect
